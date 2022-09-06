import requests
import re
import json
import os

os.makedirs("doc/json", exist_ok=True)

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
