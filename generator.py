import requests
import re
import json
import os
import pandas as pd


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
        self.after = None
        self.before = None


class js_search_data:
    def __init__(self):
        self.children: list = []
        self.parent: js_data = None
        self.after = None
        self.before = None
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
            if len(js.children) > key + 1:
                output[-1].after = js.children[key + 1]
            if len(js.children) > 0:
                output[-1].before = js.children[key - 1]
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
            for _ in range(len(find)):
                output.append(js_search_data())
                output[-1].children = js.children[key]
                output[-1].parent = js
                if len(js.children) > key + 1:
                    output[-1].after = js.children[key + 1]
                if len(js.children) > 0:
                    output[-1].before = js.children[key - 1]
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


def get_graphql(parsed_list: list) -> list:
    reg_graphql = "e\.graphQL\({func}\(\),$".format(func="([a-zA-Z_\$]{1,2})")
    graphql_list = search_js_reg(parsed_list, reg_graphql)
    graphql_output = []

    for graphql in graphql_list:
        reg_func = "{func}=n.n\({arg}\)".format(
            func=re.escape(graphql.data[0]),
            arg="([a-zA-Z_\$]{1,2})",
        )

        graphql_parent = graphql.parent
        match_func = search_js_reg(graphql_parent, reg_func)
        while match_func == []:
            graphql_parent = graphql_parent.parent
            match_func = search_js_reg(graphql_parent, reg_func)

        reg_func_init = "{func}=n\({arg}\)".format(
            func=re.escape(match_func[0].data[0]),
            arg="([0-9]{1,5})",
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
    return graphql_output


def marge_exports(parsed_list: list, graphql_output: list) -> list:
    exports = search_js(parsed_list, "e.exports=")
    reg_exports = ",{int}:e=>".format(int="([0-9]{1,5})")
    for export in exports:
        n = re.findall(reg_exports, export.parent.before)[0]
        for key in range(len(graphql_output)):
            if graphql_output[key]["n"] == n:
                graphql_output[key].update(
                    {"exports": json.loads(json_parser(export.parent.children[1]))}
                )
    return graphql_output


def get_freeze_object(parsed_list: list) -> list:

    reg_freeze_object = "Object\.freeze\($"
    freeze_object_list = search_js_reg(parsed_list, reg_freeze_object)
    freeze_object_output = []

    for freeze_object in freeze_object_list:
        if len(freeze_object.after.children) > 0:
            obj = json_parser(freeze_object.after)
            try:
                obj = json.loads(obj)
            except:
                pass
            freeze_object_output.append(obj)
    return freeze_object_output


def get_feature_switches(parsed_list: list) -> list:
    reg_exports = "e\.exports={var}$".format(var="([a-zA-Z]{1,2})")
    exports_list = search_js_reg(parsed_list, reg_exports)
    for exports in exports_list:
        feature_switches = get_freeze_object(exports.parent)
        if len(feature_switches) > 0:
            return feature_switches[0]


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

    def table_escape(self, text: str):
        if type(text) is str:
            return text.replace("|", "\|")
        else:
            return text

    def save(self, file_name: str):
        with open(file_name, "w") as f:
            f.write(self.output)


def gen_md_graphql(graphql_output: list, feature_switches_output: list) -> md_generator:
    md = md_generator()
    md.h1("Twitter Internal GraphQL API Document")
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
            "https://twitter.com/i/api/graphql/{queryId}/{operationName}".format(
                **exports
            )
        )

        md.p("Request Method", end=": ")
        if exports["operationType"] == "mutation":
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
                value = query[key]
                if type(value) is str:
                    value = {"!0": True, "!1": False}.get(value, value)
                datafram.append({"key": key, "type": "Future", "variable": value})
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
                default = {"!0": True, "!1": False}.get(
                    feature_switches_output.get(switch)
                )
                datafram.append({"key": switch, "type": "boolean", "default": default})
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
    return md


def gen_md_freeze_object(freeze_object_output: list) -> md_generator:
    md = md_generator()
    md.h1("Twitter Internal Constants Document")
    md.p("This document is entirely auto-generated and may contain errors.")

    for freeze_object in freeze_object_output:
        if type(freeze_object) is dict:
            datafram = []
            for key in freeze_object.keys():
                value = freeze_object[key]
                if type(value) is str:
                    value = {"!0": True, "!1": False}.get(value, value)
                datafram.append({"constant": key, "value": md.table_escape(value)})
            md.table(datafram)
        else:
            md.code("# Error\n" + freeze_object, title="internal process")
    return md


os.makedirs("docs/json", exist_ok=True)
os.makedirs("docs/markdown", exist_ok=True)
legacy = False

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36".format(v = "100" if legacy else "104")
}

response_home = requests.get("https://twitter.com/home", headers=headers)
reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
    nonce="([a-zA-Z0-9]{48})", src="(https://abs\.twimg\.com\/responsive\-web/[a-zA-Z0-9\-/]*?/main\.[a-z0-9]{8}\.js)"
)

src = re.findall(reg_script, response_home.text)[0][1]
response = requests.get(src, headers=headers)
print(f"src: {src}")

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
