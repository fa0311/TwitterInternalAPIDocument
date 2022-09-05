import requests
import re
import json
import os

os.makedirs('doc/json',  exist_ok=True)

response = requests.get(
    "https://abs.twimg.com/responsive-web/client-web/main.811341e8.js"
)

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
    