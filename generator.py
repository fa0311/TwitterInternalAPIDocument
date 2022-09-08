import requests
import json
import os
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


os.makedirs("docs/json", exist_ok=True)
os.makedirs("docs/markdown", exist_ok=True)

twitter = twitter_home()
src = twitter.get_main_script_url()
print(f"src: {src}")
response = requests.get(src, headers=twitter.headers)

parsed_list = js(response.text).parser()
graphql_output = get_graphql(parsed_list)
graphql_output = marge_exports(parsed_list, graphql_output)

freeze_object_output = get_freeze_object(parsed_list)
feature_switches_output = get_feature_switches(parsed_list)


with open("docs/json/GraphQL.json", "w") as f:
    json.dump(graphql_output, f, ensure_ascii=False, indent=2)
with open("docs/json/FreezeObject.json", "w") as f:
    json.dump(freeze_object_output, f, ensure_ascii=False, indent=2)

gen_md_graphql(graphql_output, feature_switches_output).save("docs/markdown/GraphQL.md")
gen_md_freeze_object(freeze_object_output).save("docs/markdown/FreezeObject.md")
