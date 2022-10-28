import requests
import json
import os
from github import Github
from lib.md_generator.md_generator import md_generator
from lib.diff import diff
from lib.twitter import twitter_home
from lib.js_parser.js_parser import js

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


twitter = twitter_home()
src = twitter.get_main_script_url()
print(f"src: {src}")
response = requests.get(src, headers=twitter.headers)

parsed_list = js(response.text).parser()
graphql_output = get_graphql(parsed_list)
graphql_output = marge_exports(parsed_list, graphql_output)

freeze_object_output = get_freeze_object(parsed_list)
feature_switches_output = get_feature_switches(parsed_list)

if os.environ.get("ENV", "Develop") != "GithubAction":
    os.makedirs("docs/json", exist_ok=True)
    os.makedirs("docs/markdown", exist_ok=True)

    with open("docs/json/GraphQL.json", "w") as f:
        json.dump(graphql_output, f, ensure_ascii=False, indent=2)
    # with open("docs/json/FreezeObject.json", "w") as f:
    #     json.dump(freeze_object_output, f, ensure_ascii=False, indent=2)
    gen_md_graphql(graphql_output, feature_switches_output).save(
        "docs/markdown/GraphQL.md"
    )
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
            graphql_output, feature_switches_output
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
    for file_name, data in file.items():
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                old_data = f.read()
        else:
            old_data = ""

        if file_name.endswith("GraphQL.json"):
            old_graphql_data = json.loads(old_data)
            diff_data = diff(graphql_output, old_graphql_data,lambda x: x["exports"]["operationName"])
            for title, items in diff_data.items():
                body.h3(title)
                if len(items) > 0:
                    for item in items:
                        body.p(item)
                else:
                    body.p("None")

        if old_data == data:
            print(f"No change to {file_name}")
        else:
            print(f"Commit to {file_name}")
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
                print("Not Found")

    if send_pull_request:
        try:
            repo.create_pull(
                title="Update Document", body=body.output, head=branch, base="master"
            )
        except:
            print("A pull request already exists")
