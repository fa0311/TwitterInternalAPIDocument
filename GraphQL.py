import requests
import re
import json
import os
import pandas as pd

os.makedirs("doc/json", exist_ok=True)
os.makedirs("doc/markdown", exist_ok=True)

response = requests.get(
    "https://abs.twimg.com/responsive-web/client-web/main.811341e8.js"
)


class js:
    def __init__(self, script):
        self.script = script
        self.length = len(self.script)
        self.key = 0

    def parser(self) -> list:
        output = js_data()
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            self.key += 1
            if char == "{":
                output.children.append(value)
                value = ""
                output.children.append(self.parser())
                output.children[-1].parent = output
                output.children[-1].before = output.children[-2]
            elif char == "}":
                if value != "":
                    output.children.append(value)
                return output
            else:
                value += char
        return output


class js_data:
    def __init__(self):
        self.children: list = []
        self.parent: js_data = None
        self.before = None


class js_search_data:
    def __init__(self):
        self.children: list = []
        self.parent: js_data = None
        self.after = None
        self.data = None


def search_js(js: js_data, search: str) -> list[js_search_data]:
    output = []
    for data in js.children:
        if type(data) is js_data:
            output.extend(search_js(data, search))
    for key in range(len(js.children)):
        data = js.children[key]
        if data == search:
            output.append(js_search_data())
            output[-1].children = js.children
            output[-1].parent = js
            output[-1].after = js.children[key + 1]
            output[-1].data = search
            break
    return output


def search_js_reg(js: js_data, search: str) -> list[js_search_data]:
    output = []
    for data in js.children:
        if type(data) is js_data:
            output.extend(search_js_reg(data, search))
    for key in range(len(js.children)):
        data = js.children[key]
        if type(data) is str:
            find = re.findall(search, data)
            if len(find) > 0:
                output.append(js_search_data())
                output[-1].children = js.children[key]
                output[-1].parent = js
                output[-1].after = js.children[key + 1]
                output[-1].data = find
                break
    return output


def json_parser(js: js_data):
    output = ""
    for data in js.children:
        if type(data) is js_data:
            output += json_parser(data)
        else:
            re_sub = re.sub("(,|^)([0-9a-zA-Z!$_]+?)(:|$)", r'\1"\2"\3', data)
            output += re.sub("(:|^)([0-9a-zA-Z!$_]+?)(,|$)", r'\1"\2"\3', re_sub)
    return "{" + output + "}"


parsed_list = js(response.text).parser()

reg_graphql = "e\.graphQL\({func}\(\),$".format(func="([a-zA-Z_\$]{1,2})",)
graphql_list = search_js_reg(parsed_list, reg_graphql)
graphql_output = []

for graphql in graphql_list:
    reg_func = "{func}=n.n\({arg}\)".format(
        func=re.escape(graphql.data[0]), arg="([a-zA-Z_\$]{1,2})",
    )

    graphql_parent = graphql.parent
    match_func = search_js_reg(graphql_parent, reg_func)
    while match_func == []:
        graphql_parent = graphql_parent.parent
        match_func = search_js_reg(graphql_parent, reg_func)

    reg_func_init = "{func}=n\({arg}\)".format(
        func=re.escape(match_func[0].data[0]), arg="([0-9]{1,5})",
    )
    match_func_init = search_js_reg(graphql_parent, reg_func_init)
    n = match_func_init[0].data[0]

    query = json_parser(graphql.after)
    try:
        query = json.loads(query)
    except:
        pass
    graphql_output.append(
        {
            "n": n,
            "func_name": graphql.data[0],
            "func_name_init": match_func[0].data[0],
            "query": query,
        }
    )


exports = search_js(parsed_list, "e.exports=")
reg_exports = ",{int}:e=>".format(int="([0-9]{1,5})")
for export in exports:
    n = re.findall(reg_exports, export.parent.before)[0]
    for key in range(len(graphql_output)):
        if graphql_output[key]["n"] == n:
            graphql_output[key].update(
                {"exports": json.loads(json_parser(export.parent.children[1]))}
            )

with open("doc/json/GraphQL.json", "w") as f:
    json.dump(graphql_output, f, ensure_ascii=False, indent=2)

# Markdown


class md_generator:
    def __init__(self):
        self.output = ""

    def h1(self, text: str, end: str = "<br>\n"):
        self.output += f"# {text}{end}"

    def h2(self, text: str, end: str = "<br>\n"):
        self.output += f"## {text}{end}"

    def h3(self, text: str, end: str = "<br>\n"):
        self.output += f"### {text}{end}"

    def h4(self, text: str, end: str = "<br>\n"):
        self.output += f"#### {text}{end}"

    def p(self, text: str, end: str = "<br>\n"):
        self.output += f"{text}{end}"

    def inline(self, text: str, end: str = "<br>\n"):
        self.output += f"`{text}`{end}"

    def code(self, text: str, title: str = "", end: str = "\n"):
        self.output += f"```{title}\n{text}\n```{end}"

    def table(self, data: dict, end: str = "\n\n"):
        datafram = pd.DataFrame(data)
        self.output += f"{datafram.to_markdown(index=False)}{end}"

    def save(self, file_name: str):

        with open(file_name, "w") as f:
            f.write(self.output)


md = md_generator()
md.h1("Twitter Unofficial GraphQL API Document")
md.p("This document is entirely auto-generated and may contain errors.")
md.h2("Usage")
md.p("If the parameter is an array type, encode it in json format.")
md.p("Body example:")
md.code(
    """json.dumps({
    "queryId": "kV0jgNRI3ofhHK_G5yhlZg",
    "variables": json.dumps({
        "tweet_text": "Hello, world!",
        "media": {"media_entities": [], "possibly_sensitive": False},
        "withDownvotePerspective": False,
        "withReactionsMetadata": False,
        "withReactionsPerspective": False,
        "withSuperFollowsTweetFields": True,
        "withSuperFollowsUserFields": False,
        "semantic_annotation_ids": [],
        "dark_request": False,
        "withBirdwatchPivots": False,
    }),
})""",
    title="Python",
)
md.p("`json.dumps` is equivalent to `JSON.stringify` in javaScript")

for graphql in graphql_output:
    exports = graphql["exports"]
    query = graphql["query"]
    switches = exports["metadata"]["featureSwitches"]

    md.h2(exports["operationName"])
    md.p("Request URL", end=": ")
    md.inline(
        "https://twitter.com/i/api/graphql/{queryId}/{operationName}".format(**exports)
    )

    md.p("Request Method", end=": ")
    if query == "mutation":
        md.inline("POST")
    else:
        md.inline("GET")
    md.p("Login Required", end=": ")
    md.inline("Future")

    md.h3("Param")
    md.h4("variables")
    if type(query) is dict and len(query) > 0:
        datafram = []
        for key in query.keys():
            datafram.append(
                {"key": key, "type": "Future", "variable": query[key],}
            )
        md.table(datafram)
    elif type(query) is list and len(query) == 0:
        md.inline("None")
    elif type(query) is str:
        md.code("# Error\n" + query, title="internal process")
    else:
        md.inline("None")

    md.h4("features")
    if type(switches) is list and len(switches) > 0:
        datafram = []
        for switch in exports["metadata"]["featureSwitches"]:
            datafram.append({"key": switch, "type": "boolean", "variable": "Future"})
        md.table(datafram)
    elif type(switches) is list and len(switches) == 0:
        md.inline("None")
    else:
        md.inline("Error")

    md.h4("queryId")
    if query == "mutation":
        md.inline(exports["queryId"])
    else:
        md.inline("None")


md.save("doc/markdown/GraphQL.md")
