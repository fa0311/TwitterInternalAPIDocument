import requests
import re
import json
import os

os.makedirs('doc/json')

response = requests.get(
    "https://abs.twimg.com/responsive-web/client-web/main.811341e8.js"
)

reg_graphql = '{key}:e=>{{e.exports={{queryId:{text},operationName:{text},operationType:{text},metadata:{{featureSwitches:{text}}}}}}},'.format(
    key='[0-9]{1,5}', text='"?(.*?)"?',
)

match = re.findall(reg_graphql, response.text)
output = []
for data in match:
    output.append(
        {
            "queryId": data[0],
            "operationName": data[1],
            "operationType": data[2],
            "metadata": {"featureSwitches": json.loads(data[3])},
        }
    )


with open("doc/json/GraphQL.json", "w") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
