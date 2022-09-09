import json
import re


class js:
    def __init__(self, script:str,start_char:str="{",end_char:str="}"):
        self.script = script
        self.length = len(self.script)
        self.key = 0
        self.start_char = start_char
        self.end_char = end_char

    def parser(self) -> list:
        output = js_data()
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            self.key += 1
            if char == self.start_char:
                output.children.append(value)
                value = ""
                output.children.append(self.parser())
                output.children[-1].parent = output
                output.children[-1].before = output.children[-2]
            elif char == self.end_char:
                if value != "":
                    output.children.append(value)
                return output
            else:
                value += char
        if value != "":
            output.children.append(value)
        return output


class js_data:
    def __init__(self):
        self.children: list = []
        self.parent: js_data = None
        self.after = None
        self.before = None

    def __repr__(self):
        return json.dumps(self.children)


class js_search_data:
    def __init__(self):
        self.children: list = []
        self.parent: js_data = None
        self.after = None
        self.before = None
        self.data = None

    def __repr__(self):
        return json.dumps(self.children)


def search_js(text: js_data, search: str) -> list[js_search_data]:
    output = []
    for data in text.children:
        if type(data) is js_data:
            output.extend(search_js(data, search))
    for key in range(len(text.children)):
        data = text.children[key]
        if data == search:
            output.append(js_search_data())
            output[-1].children = text.children
            output[-1].parent = text
            if len(text.children) > key + 1:
                output[-1].after = text.children[key + 1]
            if len(text.children) > 0:
                output[-1].before = text.children[key - 1]
            output[-1].data = search
            break
    return output


def search_js_reg(text: js_data, search: str) -> list[js_search_data]:
    output = []
    for data in text.children:
        if type(data) is js_data:
            output.extend(search_js_reg(data, search))
    for key in range(len(text.children)):
        data = text.children[key]
        if type(data) is str:
            find = re.findall(search, data)
            for _ in range(len(find)):
                output.append(js_search_data())
                output[-1].children = text.children[key]
                output[-1].parent = text
                if len(text.children) > key + 1:
                    output[-1].after = text.children[key + 1]
                if len(text.children) > 0:
                    output[-1].before = text.children[key - 1]
                output[-1].data = find
                break
    return output


def json_parser(text: js_data):
    output = ""
    reg_other = "[0-9a-zA-Z\s" + re.escape("!?$_.{}&=") + "]"
    for data in text.children:
        if type(data) is js_data:
            json = json_parser(data)
        else:
            parsed_list = js(data, start_char="(", end_char=")").parser()
            json_child = ""
            js_data_list = []
            for parsed in parsed_list.children:

                if type(parsed) is js_data:
                    json_child += f"{{{len(js_data_list)}}}"
                    js_data_list.append(parsed)
                else:
                    json_child += parsed

            json = re.sub(f"(,|^)(\.\.\.{reg_other}+?)(,|$)", r'\1"\2":"_"\3', json_child)
            while json_child != json:
                json_child = json
                json = re.sub(f"(,|^)(\.\.\.{reg_other}+?)(,|$)", r'\1"\2":"_"\3', json_child)
            json = re.sub(f"(,|^)({reg_other}+?)(:|$)", r'\1"\2"\3', json)
            json = re.sub(f"(:|^)({reg_other}+?)(,|$)", r'\1"\2"\3', json)
            
            args = [json_parser_child(parsed,start_char="(",end_char=")") for parsed in js_data_list]
            json = json.format(*args)

        output += json
    return "{" + output + "}"



def json_parser_child(text: js_data,start_char:str="{",end_char:str="}"):
    output = ""
    for data in text.children:
        if type(data) is js_data:
            output += json_parser_child(data,start_char=start_char,end_char=end_char)
        else:
            output += data
    return start_char + output.replace("\"","\\\"") + end_char
