import json
import os
import datetime
from github import Github
import logging
import coloredlogs

from lib.md_generator.md_generator import *
from lib.diff import *
from lib.twitter import *
from lib.js_parser.js_parser import *
from lib.graphql import *
from lib.md import *
from lib.config import *
from lib.io import *
from lib.config import *
from lib.md_generator.i18n import *

# === Confing ===

coloredlogs.install(
    level=logging.INFO,
    fmt="[%(levelname)s] %(relativeCreated)dms %(message)s",
)
DEBUG = False
dumps_args = {"ensure_ascii": False, "indent": 2}
logging.info("init is completed")


# === Requests ===

twitter = twitter_home()

if twitter_home.TWITTER_FRONTEND_FLOW and os.path.isfile("cookie.json"):
    twitter.load("cookie.json")
    logging.info("cookie load is completed")
twitter.get_home()


script = "".join(twitter.get_script())
parsed_script_list = js(script).parser()
src = twitter.get_script_url()
i18n_src = {}
logging.info("src: " + json.dumps(src, **dumps_args))

# === Initial decode ===

initial_state = search_js(parsed_script_list, "window.__INITIAL_STATE__=")[0].after
initial_output = json.loads(json_parser(initial_state))

meta_data = search_js(parsed_script_list, ";window.__META_DATA__=")[0].after
meta_output = json.loads(json_parser(meta_data))

script_load_data = search_js_reg(parsed_script_list, "Promise.all")[0].after
script_load_json = json.loads(json_parser(script_load_data))
script_load_output = {}
base_url = "https://abs.twimg.com/responsive-web/client-web/"
for k in script_load_json:
    url = "{0}{1}.{2}a.js".format(base_url, k, script_load_json[k])
    script_load_output[k] = url
    if k.startswith("i18n"):
        i18n_src[k] = url
    elif k.startswith("endpoints"):
        src.append(url)
    elif k.startswith("shared~endpoints"):
        src.append(url)


logging.info("script decode is completed")

# === Road ===

response = "".join(
    [twitter.session.get(s, headers=twitter.get_header()).text for s in tqdm(src)]
)
parsed_list = js(response).parser()
logging.info("script loading is completed")

i18n_response = {
    k: twitter.session.get(s, headers=twitter.get_header()).text
    for k, s in tqdm(i18n_src.items())
}
logging.info("i18n loading is completed")

# === Parse ===

graphql_output = get_graphql(parsed_list)
logging.info("get_graphql is completed")
graphql_output = marge_exports(parsed_list, graphql_output)
logging.info("marge_exports is completed")
graphql_output = marge_metadata(graphql_output, initial_output)
logging.info("marge_metadata is completed")
freeze_object_output = get_freeze_object(parsed_list)
logging.info("get_freeze_object is completed")


# feature_switches_output = get_feature_switches(parsed_list)
# logging.info("get_feature_switches is completed")

i18n_output = {k: get_i18n(r) for k, r in i18n_response.items()}
logging.info("get_i18n is completed")

if DEBUG:
    os.makedirs("debug", exist_ok=True)
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

# === OUTPUT ===
items = {
    FileConf.GRAPH_QL_JSON: json.dumps(graphql_output, **dumps_args),
    FileConf.GRAPH_QL_MD: gen_md_graphql(graphql_output).output,
    FileConf.FREEZE_OBJECT_MD: gen_md_freeze_object(freeze_object_output).output,
    FileConf.FREEZE_OBJECT_JSON: json.dumps(freeze_object_output, **dumps_args),
    FileConf.INITIAL_STATE_JSON: json.dumps(initial_output, **dumps_args),
    FileConf.META_DATA_JSON: json.dumps(meta_output, **dumps_args),
    FileConf.SCRIPT_LOAD_JSON: json.dumps(script_load_output, **dumps_args),
    FileConf.CHANGE_LOG_MD: "",
}

for k, o in i18n_output.items():
    items.update({f"docs/json/{k}.arb": json.dumps(o, **dumps_args)})


# === Backup and File Check===
[os.makedirs("/".join(f.split("/")[:-1]), exist_ok=True) for f in items.keys()]
[open(f, "a+").close() for f in items.keys()]
[os.remove(f"{f}.backup") for f in items.keys() if os.path.isfile(f"{f}.backup")]
[os.rename(f, f"{f}.backup") for f in items.keys()]
logging.info("backup is completed")


# === READ ===
items_backup = {k: read(f"{k}.backup") for k in items.keys()}


# === DIFF ===


body = md_generator()
try:
    backup_graphql_data = json.loads(items_backup[FileConf.GRAPH_QL_JSON])
except:
    backup_graphql_data = {}

diff_data = diff(
    graphql_output,
    backup_graphql_data,
    lambda x: x["exports"]["operationName"],
)
change_len = 0
for title, data in diff_data.items():
    body.h3(title)
    if len(data) > 0:
        for li in data:
            body.li(li)
            change_len += 1
    else:
        body.li("None")

items.update({FileConf.CHANGE_LOG_MD: items_backup[FileConf.CHANGE_LOG_MD]})

if change_len > 0:
    items[FileConf.CHANGE_LOG_MD] += "## {time}{br}{new}".format(
        br="<br>\n",
        time=datetime.datetime.now().strftime("%Y/%m/%d"),
        new=body.output,
    )


# === WRITE ===
[write(k, items[k]) for k in items.keys()]

# === GITHUB ===

if os.environ.get("ENV", "Develop") == "GithubAction":

    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["REPOSITORY"])
    branch = "develop"
    send_pull_request = False

    for file_name in items.keys():

        if items[file_name] == items_backup[file_name]:
            logging.info(f"No change to {file_name}")
        else:
            logging.info(f"Commit to {file_name}")
            send_pull_request = True
            try:
                f = repo.get_contents(file_name, ref=branch)
                repo.update_file(
                    f.path,
                    message=f"Update {file_name} on {branch} branch",
                    content=items[file_name],
                    sha=f.sha,
                    branch=branch,
                )
            except:
                logging.warning(f"Not Found {file_name} on {branch} branch")

    if send_pull_request:
        try:
            repo.create_pull(
                title="Update Document",
                body=body.output,
                head=branch,
                base="master",
            )
        except:
            logging.warning("A pull request already exists")
else:
    for file_name in items.keys():
        if items[file_name] == items_backup[file_name]:
            logging.info(f"No change to {file_name}")
        else:
            logging.info(f"Commit to {file_name}")

[os.remove(f"{f}.backup") for f in items.keys() if os.path.isfile(f"{f}.backup")]
logging.info("All completed")
