import re


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
