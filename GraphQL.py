import requests
import re
import json
import os
import sys

sys.setrecursionlimit(999999)


class js:
    def __init__(self, script):
        self.script = script
        self.length = len(self.script)
        self.key = 0
    
    def parser(self):
        print(self.script[self.key:self.key+30])
        char = self.script[self.key]
        if char == "{":
            self.key += 1
            return self.array_parser()
        elif char == "[":
            self.key += 1
            return self.list_parser()
        elif char in ["\"","'"]:
            self.key += 1
            return self.text_parser()
        elif self.is_value():
            return self.value_parser()
        else:
            return self.syntax_parser()

    def is_array(self):
        key = self.key
        while self.length > key:
            char = self.script[key]
            key += 1
            if char == ":":
                return True
            if char == ";":
                return False
        return False

    def is_value(self):
        key = self.key
        value = ""
        while self.length > key:
            char = self.script[key]
            key += 1
            if char in [",","}","]"]:
                break
            else:
                value += char
        if value in ["true","false","null","!0","!1"]:
            return True
        try:
            float(value)
        except ValueError:
            return False
        return True

    def syntax_parser(self):
        output = []
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            if char == "{" and not self.is_array():
                self.key += 1
                value += char
            elif char in ["{","["]:
                output.append(value)
                value = ""
                output.append(self.parser())
            elif char in ["="]:
                self.key += 1
                output.append(value)
                value = ""
                output.append(self.parser())
            elif char in ["}"]:
                self.key += 1
                if value != "":
                    output.append(value)
                    value = ""
                return output
            else:
                self.key += 1
                value += char
        return output

    def array_parser(self):
        output = {}
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            self.key += 1
            if char == ":":
                output[value] = self.parser()
                value = ""
            elif char == "}":
                return output
            else:
                value += char
        return output

    def list_parser(self):
        output = []
        while self.length > self.key:
            char = self.script[self.key]
            if char not in [",", "]"]:
                output.append(self.parser())
            elif char == "]":
                self.key += 1
                return output
            else:
                self.key += 1
        return output

    def text_parser(self):
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            self.key += 1
            if char in ["\"", "'"]:
                return value
            else:
                value += char
        return value

    def value_parser(self):
        value = ""
        while self.length > self.key:
            char = self.script[self.key]
            self.key += 1
            if char in [",", "}", "]"]:
                return value
            else:
                value += char
        return value

def recursive_search(parsed_list):
    for parsed in parsed_list:
        pass

os.makedirs('doc/json',  exist_ok=True)

response = requests.get(
    "https://abs.twimg.com/responsive-web/client-web/main.811341e8.js"
)


parsed_list = js(response.text[:10000]).parser()
print("aaaaaaaaaaaaaa")
with open("doc/json/kkk.json", "w", encoding="utf-8") as f:
    json.dump(parsed_list, f, ensure_ascii=False, indent=2)

exit()

reg_exports = '{key}:e=>{{e.exports={{queryId:{text},operationName:{text},operationType:{text},metadata:{{featureSwitches:{text}}}}}}},'.format(
    key='([0-9]{1,5})', text='"?(.*?)"?',
)


match_exports = re.findall(reg_exports, response.text)
output = []

for data in match_exports:
    try:
        reg_func_init = '{func}=n\({arg}\)'.format(
            func='([a-zA-Z_\$]{1,2})',
            arg=re.escape(data[0]),
        )
        match_func_init = re.findall(reg_func_init, response.text)[0]
        reg_func = '{func}=n.n\({arg}\)'.format(
            func='([a-zA-Z_\$]{1,2})',
            arg=re.escape(match_func_init),
        )
        match_func = re.findall(reg_func, response.text)[0]
    except:
        match_func = None

    try:
        reg_graphql_func = '{func}:{text}=>e\.graphQL\({arg}\(\),'.format(
            func='([a-zA-Z_\$]*)',
            arg=re.escape(match_func),
            text='[a-zA-Z\(\)]*?',
        )
        match_graphql_func = re.findall(reg_graphql_func, response.text)[0]
    except:
        try:
            reg_graphql_func = '{func}\({func_arg}\){text}return e\.graphQL\({arg}\(\),'.format(
                func='([a-zA-Z_\$]*)',
                func_arg='(|[a-zA-Z]*|[a-zA-Z]*\:[a-zA-Z]*)',
                arg=re.escape(match_func),
                text='.{0,100}',
            )
            match_graphql_func = re.findall(reg_graphql_func, response.text)[0]
        except:
            match_graphql_func = None

    output.append(
        {
            "n": data[0],
            "match_func": match_func,
            "match_graphql_func": match_graphql_func,
            "queryId": data[1],
            "operationName": data[2],
            "operationType": data[3],
            "metadata": {"featureSwitches": json.loads(data[4])},
        }
    )
    
    print(data[0])
    if data[0] == "0":
        break


    with open("doc/json/GraphQL.json", "w") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
with open("doc/json/aaa.js", "w", encoding="utf-8") as f:
    f.write(response.text)
    
    

