import json
import re


class Js:
    def __init__(self, script: str):
        self.script = script
        self.length = len(self.script)
        self.key = 0

    def parser(self, init=True):
        output = JsData()
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            self.key += 1
            if char == "{":
                output.children.append(value)
                value = ""
                output.children.append(self.parser(init=False))
                output.children[-1].parent = output
                output.children[-1].before = output.children[-2]
            elif char == "}":
                if value != "":
                    output.children.append(value)
                if init:
                    value = ""
                else:
                    return output
            else:
                value += char
        if value != "":
            output.children.append(value)
        return output


class JsData:
    def __init__(self):
        self.children: list = []
        self.parent: JsData = None
        self.after = None
        self.before = None

    def __repr__(self):
        return json.dumps(self.to_list())

    def to_list(self):
        output = []
        for child in self.children:
            if type(child) is JsData:
                output.append(child.to_list())
            else:
                output.append(child)
        return output


class JsSearchData:
    def __init__(self):
        self.children: list = []
        self.parent: JsData = None
        self.after = None
        self.before = None
        self.data = None

    def __repr__(self):
        return json.dumps(self.children)

    def to_list(self):
        output = []
        for child in self.children:
            if type(child) is js_data:
                output.append(child.to_list())
            else:
                output.append(child)
        return output


def search_js(text: JsData, search: str) -> list[JsSearchData]:
    output = []
    for data in text.children:
        if type(data) is JsData:
            output.extend(search_js(data, search))
    for key in range(len(text.children)):
        data = text.children[key]
        if data == search:
            output.append(JsSearchData())
            output[-1].children = text.children
            output[-1].parent = text
            if len(text.children) > key + 1:
                output[-1].after = text.children[key + 1]
            if len(text.children) > 0:
                output[-1].before = text.children[key - 1]
            output[-1].data = search
            break
    return output


def search_js_reg(text: JsData, search: str) -> list[JsSearchData]:
    output = []
    for data in text.children:
        if type(data) is JsData:
            output.extend(search_js_reg(data, search))
    for key in range(len(text.children)):
        data = text.children[key]
        if type(data) is str:
            find = re.findall(search, data)
            for _ in range(len(find)):
                output.append(JsSearchData())
                output[-1].children = text.children[key]
                output[-1].parent = text
                if len(text.children) > key + 1:
                    output[-1].after = text.children[key + 1]
                if len(text.children) > 0:
                    output[-1].before = text.children[key - 1]
                output[-1].data = find
                break
    return output


def json_parser(text: JsData):
    output = ""
    reg_other = "[0-9a-zA-Z\s" + re.escape("!?$_.{}&=") + "]"
    for data in text.children:
        if type(data) is JsData:
            json = json_parser(data)
        else:
            data = (
                data.replace("null==t?void 0:", "{optional}")
                .replace("?void 0:", "{void}")
                .replace('"private"', "{private}")
                .replace('"none"', "{none}")
            )
            placeholder = parentheses_placeholder(data)
            json_child = ""
            json = re.sub(
                f"(,|^)(\.\.\.{reg_other}+)(,|$)",
                r'\1"\2":"_"\3',
                placeholder.text,
            )
            while json_child != json:
                json_child = json
                json = re.sub(
                    f"(,|^)(\.\.\.{reg_other}+)(,|$)",
                    r'\1"\2":"_"\3',
                    json_child,
                )
            json = re.sub(
                f"(,|^)({reg_other}+)(:|$)",
                r'\1"\2"\3',
                json,
            )
            json = re.sub(
                f"(:|^)({reg_other}+)(,|$)",
                r'\1"\2"\3',
                json,
            )
            args = [
                "(" + parsed.replace('"', '\\"') + ")" for parsed in placeholder.list
            ]
            json = json.format(
                *args,
                optional="(optional) ",
                void="?void 0:",
                private="private",
                none="none",
            )
        output += json
    output = output.replace(':"_"{', ":{")
    return "{" + output + "}"


def parentheses_placeholder(text: str):
    length = len(text)
    key = 0
    placeholder = 0
    depth = 0
    output = ParenthesesPlaceholderData()
    output.list.append("")
    while length > key:
        char = text[key]
        key += 1
        if char == "(":
            depth += 1
            if depth == 1:
                output.text += f"{{{placeholder}}}"
                output.list.append("")
                placeholder += 1
        elif char == ")":
            depth -= 1
        elif depth == 0:
            output.text += char
        else:
            output.list[-1] += char
    return output


class ParenthesesPlaceholderData:
    def __init__(self):
        self.text = ""
        self.list = []
