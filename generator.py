import datetime
import json
import logging
import os
from functools import partialmethod

import coloredlogs
from github import Github

from lib.config import *
from lib.diff import *
from lib.graphql import *
from lib.io import *
from lib.js_parser.js_parser import *
from lib.legacy import *
from lib.md import *
from lib.md_generator.i18n import *
from lib.md_generator.md_generator import *
from lib.twitter import *

# === Confing ===
DEBUG = os.environ.get("DEBUG", "False") == "True"
ENV = os.environ.get("ENV", "Develop")
CLIENT_TYPE = os.environ.get("CLIENT_TYPE", "Responsive")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "docs")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)
REPOSITORY = os.environ.get("REPOSITORY", None)
BASE_BRANCH = os.environ.get("BASE_BRANCH", None)
REF_BRANCH = os.environ.get("REF_BRANCH", None)
SCAN_TYPE = os.environ.get("SCAN_TYPE", "Full")
TQDM_DISABLE = os.environ.get("TQDM_DISABLE", "False") == "True"
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "Into").upper()
CACHE = os.environ.get("CACHE", "False") == "True"
GRAPHQL_CACHE = os.environ.get("GRAPHQL_CACHE", "False") == "True"
READ_SCRIPT_JSON = os.environ.get("READ_SCRIPT_JSON", "False") == "True"
TIMEOUT = 30

coloredlogs.install(
    level=logging.getLevelName(LOGGING_LEVEL),
    fmt="[%(levelname)s] %(relativeCreated)dms %(message)s",
)
dumps_args = {"ensure_ascii": False, "indent": 2}
if TQDM_DISABLE:
    tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)

logging.info("init is completed")

# === Requests ===

if CLIENT_TYPE == "Responsive":
    twitter = TwitterHome()
elif CLIENT_TYPE == "Deck":
    twitter = TwitterDeck()

if TwitterHome.TWITTER_FRONTEND_FLOW and os.path.isfile("cookie.json"):
    twitter.load("cookie.json")
    logging.info("cookie load is completed")
twitter.get_home()


script = "".join(twitter.get_script_res())
parsed_script_list = Js(script).parser()
src = twitter.get_script_url()
i18n_src = {}
logging.info("src: " + json.dumps(src, **dumps_args))

# === Initial decode ===

initial_state = search_js_reg(parsed_script_list, "window.__INITIAL_STATE__=")[0].after
initial_output = json.loads(json_parser(initial_state))

meta_data = search_js(parsed_script_list, ";window.__META_DATA__=")[0].after
meta_output = json.loads(json_parser(meta_data))

script_load_data = search_js_reg(parsed_script_list, "Promise.all")[0].after
script_load_json = json.loads(json_parser(script_load_data))
script_load_output = {}
base_url = "https://abs.twimg.com/{0}/client-web/".format(twitter.CLIENT)

if READ_SCRIPT_JSON:
    output_dir = OUTPUT_DIR if OUTPUT_DIR[-1] == "/" else f"{OUTPUT_DIR}/"
    script_load_url = json.loads(read(f"{output_dir}{FileConf.SCRIPT_LOAD_JSON}"))
else:
    script_load_url = {
        k: "{0}{1}.{2}a.js".format(base_url, k, script_load_json[k])
        for k in script_load_json
    }

for k, url in script_load_url.items():
    script_load_output[k] = url
    if k.startswith("i18n"):
        i18n_src[k] = url
    elif SCAN_TYPE == "Full":
        src.append(url)
    elif SCAN_TYPE == "Api":
        if k.startswith("api"):
            src.append(url)
    elif k.startswith("endpoints"):
        src.append(url)
    elif k.startswith("shared~endpoints"):
        src.append(url)
    elif k.startswith("shared~loader"):
        src.append(url)


logging.info("script decode is completed")

# === x-client-transaction-id ===

ondemand = script_load_output["ondemand.s"]
ondemand_response = twitter.session.get(
    ondemand, headers=twitter.get_header(), timeout=twitter.TIMEOUT
).text
INDICES_REGEX = re.compile(
    r"""(\(\w{1}\[(\d{1,2})\],\s*16\))+""", flags=(re.VERBOSE | re.MULTILINE)
)
ondemand_index = INDICES_REGEX.findall(ondemand_response)
transaction_output = {"index": [int(i[1]) for i in ondemand_index]}

# === Road ===

if CACHE and os.path.isfile("debug/script_response.txt"):
    response = read("debug/script_response.txt")
    logging.info("script loading is completed")
    i18n_response = json.loads(read("debug/i18n_response.json"))
    logging.info("i18n loading is completed")

else:
    response = "".join(
        [
            twitter.session.get(
                s, headers=twitter.get_header(), timeout=twitter.TIMEOUT
            ).text
            for s in tqdm(src)
        ]
    )
    logging.info("script loading is completed")

    i18n_response = {
        k: twitter.session.get(
            s, headers=twitter.get_header(), timeout=twitter.TIMEOUT
        ).text
        for k, s in tqdm(i18n_src.items())
    }
    logging.info("i18n loading is completed")


parsed_list = Js(response).parser()
logging.info("script parser is completed")

# === Parse ===

header = twitter.get_header()
header.update(
    {
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    }
)
if GRAPHQL_CACHE:
    output_dir = OUTPUT_DIR if OUTPUT_DIR[-1] == "/" else f"{OUTPUT_DIR}/"
    graphql_output = json.loads(read(f"{output_dir}{FileConf.GRAPH_QL_JSON}"))
    logging.info("graphql loading is completed")
else:
    graphql_output = get_graphql(parsed_list)
    logging.info("get_graphql is completed")
    graphql_output = marge_exports(parsed_list, graphql_output)
    logging.info("marge_exports is completed")

feature_switch = marge_feature_switch(initial_output)
logging.info("marge_exports is completed")
graphql_output = marge_metadata(graphql_output, feature_switch)
logging.info("marge_metadata is completed")
freeze_object_output = get_freeze_object(parsed_list)
logging.info("get_freeze_object is completed")
api_output = to_api(graphql_output, {"header": header})
logging.info("to_api is completed")

dispatch_output = split_dispatch(get_dispatch(parsed_list))
logging.info("get_dispatch is completed")

# feature_switches_output = get_feature_switches(parsed_list)
# logging.info("get_feature_switches is completed")

i18n_output = {k: get_i18n(r) for k, r in i18n_response.items()}
logging.info("get_i18n is completed")

if DEBUG:
    os.makedirs("debug", exist_ok=True)
    write(
        "debug/script_response.txt",
        response,
    )
    write(
        "debug/parsed_list.json",
        json.dumps(parsed_list.to_list(), **dumps_args),
    )
    write(
        "debug/parsed_script_list.json",
        json.dumps(parsed_script_list.to_list(), **dumps_args),
    )
    write(
        "debug/i18n_response.json",
        json.dumps(i18n_response, **dumps_args),
    )
    logging.info("debug is completed")

# === OUTPUT ===
output_dir = OUTPUT_DIR if OUTPUT_DIR[-1] == "/" else f"{OUTPUT_DIR}/"
items = {
    FileConf.GRAPH_QL_JSON: json.dumps(graphql_output, **dumps_args),
    FileConf.GRAPH_QL_MD: gen_md_graphql(graphql_output).output,
    FileConf.V11_QL_JSON: json.dumps(dispatch_output[0], **dumps_args),
    FileConf.V11_QL_MD: gen_md_dispatch(dispatch_output[0]).output,
    FileConf.V2_QL_JSON: json.dumps(dispatch_output[1], **dumps_args),
    FileConf.V2_QL_MD: gen_md_dispatch(dispatch_output[1]).output,
    FileConf.UNVERSIONED_QL_JSON: json.dumps(dispatch_output[2], **dumps_args),
    FileConf.UNVERSIONED_QL_MD: gen_md_dispatch(dispatch_output[2]).output,
    FileConf.FREEZE_OBJECT_MD: gen_md_freeze_object(freeze_object_output).output,
    FileConf.FREEZE_OBJECT_JSON: json.dumps(freeze_object_output, **dumps_args),
    FileConf.INITIAL_STATE_JSON: json.dumps(initial_output, **dumps_args),
    FileConf.META_DATA_JSON: json.dumps(meta_output, **dumps_args),
    FileConf.SCRIPT_LOAD_JSON: json.dumps(script_load_output, **dumps_args),
    FileConf.API_JSON: json.dumps(api_output, **dumps_args),
    FileConf.CHANGE_LOG_MD: "",
    FileConf.TRANSLATION_JSON: json.dumps(transaction_output, **dumps_args),
}
for k, o in i18n_output.items():
    items.update({f"json/{k}.json": json.dumps(o, **dumps_args)})

items = {f"{output_dir}{k}": items[k] for k in items.keys()}

# === Backup and File Check===
[os.makedirs("/".join(f.split("/")[:-1]), exist_ok=True) for f in items.keys()]
[open(f, "a+").close() for f in items.keys()]
[os.remove(f"{f}.backup") for f in items.keys() if os.path.isfile(f"{f}.backup")]
[os.rename(f, f"{f}.backup") for f in items.keys()]
logging.info("backup is completed")


# === READ ===
items_backup = {k: read(f"{k}.backup") for k in items.keys()}
items_backup = {
    k: items_backup[k] for k in items_backup.keys() if items_backup[k] != ""
}

# === DIFF API ===


body = MdGenerator()
body.h3("API")
try:
    backup_graphql_data = json.loads(
        items_backup[f"{output_dir}{FileConf.GRAPH_QL_JSON}"]
    )
except:
    backup_graphql_data = {}

diff_data = diff_list(
    graphql_output,
    backup_graphql_data,
    lambda x: x["exports"]["operationName"],
)
change_len = 0
for title, data in diff_data.items():
    body.h4(title)
    if len(data) > 0:
        for li in data:
            body.li(li)
            change_len += 1
    else:
        body.li("None")

# === DIFF Feature Switch ===

body.h3("Feature Switch")

try:
    backup_initial_state = json.loads(
        items_backup[f"{output_dir}{FileConf.INITIAL_STATE_JSON}"]
    )
    backup_feature_switch = marge_feature_switch(backup_initial_state)
except:
    backup_initial_state = {}
    backup_feature_switch = {}

diff_data = diff_dict(
    feature_switch,
    backup_feature_switch,
)
change_len = 0
for title, data in diff_data.items():
    body.h4(title)
    if len(data) > 0:
        for li in data:
            body.li(li)
            change_len += 1
    else:
        body.li("None")

# === Gen Change Log ===

change_log = items_backup.get(f"{output_dir}{FileConf.CHANGE_LOG_MD}", "")
if change_len > 0:
    change_log += "## {time}{br}{new}".format(
        br="<br>\n",
        time=datetime.datetime.now().strftime("%Y/%m/%d"),
        new=body.output,
    )

# === File Check===

items.update({f"{output_dir}{FileConf.CHANGE_LOG_MD}": change_log})
[open(f, "a+").close() for f in items.keys()]

# === WRITE ===
[write(k, items[k]) for k in items.keys()]

# === GITHUB ===

if ENV == "GithubAction":
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPOSITORY)

    for file_name in set(list(items.keys()) + list(items_backup.keys())):
        try:
            if items.get(file_name, None) == items_backup.get(file_name, None):
                logging.info(f"No change to {file_name}")
            elif items_backup.get(file_name, None) == None:
                logging.info(f"Create to {file_name}")
                repo.create_file(
                    file_name,
                    message=f"Update {file_name} on {REF_BRANCH} branch",
                    content=items[file_name],
                    branch=REF_BRANCH,
                )
            elif items.get(file_name, None) == None:
                logging.info(f"Remove to {file_name}")
                repo.delete_file(
                    file_name,
                    message=f"Remove {file_name} on {REF_BRANCH} branch",
                    sha=repo.get_contents(file_name, ref=REF_BRANCH).sha,
                    branch=REF_BRANCH,
                )
            else:
                logging.info(f"Update to {file_name}")
                repo.update_file(
                    file_name,
                    message=f"Update {file_name} on {REF_BRANCH} branch",
                    content=items[file_name],
                    sha=repo.get_contents(file_name, ref=REF_BRANCH).sha,
                    branch=REF_BRANCH,
                )
        except:
            logging.warning(f"Error to {file_name}")

    if BASE_BRANCH:
        try:
            repo.create_pull(
                title="Update Document",
                body=body.output,
                head=REF_BRANCH,
                base=BASE_BRANCH,
            )
        except:
            logging.warning("A pull request already exists")
            head = "fa0311:{0}".format(REF_BRANCH)
            repo.get_pulls(state="open", head=head)[0].create_issue_comment(
                body=body.output,
            )
else:
    for file_name in items.keys():
        if items.get(file_name, "") == items_backup.get(file_name, ""):
            logging.info(f"No change to {file_name}")
        else:
            logging.info(f"Commit to {file_name}")

[os.remove(f"{f}.backup") for f in items.keys() if os.path.isfile(f"{f}.backup")]
logging.info("All completed")
