import requests
import json
import os
import datetime
from github import Github
from lib.md_generator.md_generator import md_generator
from lib.diff import diff
from lib.twitter import twitter_home
from lib.js_parser.js_parser import js
import logging
import coloredlogs
from tqdm import tqdm

from lib.graphql import (
    get_graphql,
    marge_exports,
    get_freeze_object,
    get_feature_switches,
)
from lib.md import (
    gen_md_graphql,
    gen_md_freeze_object,
)

coloredlogs.install(
    level=logging.DEBUG,
    fmt="[%(levelname)s] %(relativeCreated)dms %(message)s",
)
logging.getLogger("urllib3").setLevel(logging.WARNING)

twitter = twitter_home()
src = twitter.get_main_script_url()
logging.log(f"src: {src}")
response = requests.get(src, headers=twitter.headers)

parsed_list = js(response.text).parser()

# with open("parsed_list.json", "w", encoding="utf-8") as f:
#     json.dump(parsed_list.to_list(), f, ensure_ascii=False, indent=2)

graphql_output = get_graphql(parsed_list)
logging.debug("get_graphql is completed")
graphql_output = marge_exports(parsed_list, graphql_output)
logging.debug("marge_exports is completed")
freeze_object_output = get_freeze_object(parsed_list)
logging.debug("get_freeze_object is completed")
# feature_switches_output = get_feature_switches(parsed_list)
# logging.debug("get_feature_switches is completed")

if os.environ.get("ENV", "Develop") != "GithubAction":
    os.makedirs("docs/json", exist_ok=True)
    os.makedirs("docs/markdown", exist_ok=True)

    with open("docs/json/GraphQL.json", "w") as f:
        json.dump(graphql_output, f, ensure_ascii=False, indent=2)
    # with open("docs/json/FreezeObject.json", "w") as f:
    #     json.dump(freeze_object_output, f, ensure_ascii=False, indent=2)
    gen_md_graphql(graphql_output, response.text).save("docs/markdown/GraphQL.md")
    gen_md_freeze_object(freeze_object_output).save("docs/markdown/FreezeObject.md")

else:

    file = {
        "docs/json/GraphQL.json": json.dumps(
            graphql_output, ensure_ascii=False, indent=2
        ),
        # "docs/json/FreezeObject.json": json.dumps(
        #     freeze_object_output, ensure_ascii=False, indent=2
        # ),
        "docs/markdown/GraphQL.md": gen_md_graphql(
            graphql_output, response.text
        ).output,
        "docs/markdown/FreezeObject.md": gen_md_freeze_object(
            freeze_object_output
        ).output,
    }

    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["REPOSITORY"])
    branch = "develop"
    send_pull_request = False

    body = md_generator()
    for file_name, data in tqdm(file.items()):
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                old_data = f.read()
        else:
            old_data = ""

        if file_name.endswith("GraphQL.json"):
            old_graphql_data = json.loads(old_data)
            diff_data = diff(
                graphql_output,
                old_graphql_data,
                lambda x: x["exports"]["operationName"],
            )
            change_len = 0
            for title, items in diff_data.items():
                body.h3(title)
                if len(items) > 0:
                    for item in items:
                        body.li(item)
                        change_len += 1
                else:
                    body.li("None")

        if old_data == data:
            logging.debug(f"No change to {file_name}")
        else:
            logging.debug(f"Commit to {file_name}")
            send_pull_request = True
            try:
                f = repo.get_contents(file_name, ref=branch)
                repo.update_file(
                    f.path,
                    message=f"Update {file_name} on {branch} branch",
                    content=data,
                    sha=f.sha,
                    branch=branch,
                )
            except:
                logging.warning("Not Found")

    if send_pull_request:
        if change_len > 0:
            file_name = "docs/markdown/ChangeLog.md"
            if os.path.exists(file_name):
                with open(file_name, "r") as f:
                    change_log = f.read()
            else:
                change_log = ""
            change_log += "## {time}{br}{new}".format(
                br="<br>\n",
                time=datetime.datetime.now().strftime("%Y/%m/%d"),
                new=body.output,
            )

            f = repo.get_contents(file_name, ref=branch)
            repo.update_file(
                f.path,
                message=f"Update {file_name} on {branch} branch",
                content=change_log,
                sha=f.sha,
                branch=branch,
            )
        try:
            repo.create_pull(
                title="Update Document", body=body.output, head=branch, base="master"
            )
        except:
            logging.warning("A pull request already exists")

logging.debug("All completed")
