import logging
import re
import json
from lib.js_parser.js_parser import (
    search_js,
    search_js_reg,
    json_parser,
    js_data,
)
from tqdm import tqdm


def get_graphql(parsed_list: js_data) -> list:

    reg_graphql = "e\.graphQL\({func}\(\),$".format(func="([a-zA-Z_\$]{1,2})")
    graphql_list = search_js_reg(parsed_list, reg_graphql)
    graphql_output = []

    for graphql in tqdm(graphql_list):
        reg_func = "{func}=t.n\({arg}\)".format(
            func=re.escape(graphql.data[0]),
            arg="([a-zA-Z_\$]{1,2})",
        )

        graphql_parent = graphql.parent
        match_func = search_js_reg(graphql_parent, reg_func)
        while match_func == []:
            graphql_parent = graphql_parent.parent
            if graphql_parent == None:
                break
            match_func = search_js_reg(graphql_parent, reg_func)

        if match_func == []:
            continue
        reg_func_init = "{func}=t\({arg}\)".format(
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
    reg_exports = "{comma}{int}:{var}=>".format(
        comma=",?", int="([0-9]{1,5})", var="(e|\([a-z,]*?\))"
    )
    for export in exports:
        n = re.findall(reg_exports, export.parent.before)[0][0]
        for key in range(len(graphql_output)):
            if graphql_output[key]["n"] == n:
                graphql_output[key].update(
                    {"exports": json.loads(json_parser(export.parent.children[1]))}
                )

    reg_exports_ext = ';{var}.hash="{hash}",e.exports={var}'.format(
        hash="[a-z0-9]{32}", var="[a-zA-Z0-9]{1,2}"
    )
    exports = search_js_reg(parsed_list, reg_exports_ext)
    for export in exports:
        params = search_js(export.before, ",params:")
        if len(params) > 0:
            n = re.findall(reg_exports, export.parent.before)[0][0]
            for key in range(len(graphql_output)):
                if graphql_output[key]["n"] == n:
                    data = json.loads(json_parser(params[0].after))
                    graphql_output[key].update(
                        {
                            "exports": {
                                "queryId": data["id"],
                                "operationName": data["name"],
                                "operationType": data["operationKind"],
                                "metadata": {
                                    "featureSwitches": data["metadata"]["features"],
                                },
                            }
                        }
                    )
    return list(filter(lambda x: x.get("exports", False), graphql_output))


def marge_metadata(graphql_output: list, initial_output: dict) -> list:
    featureSwitches = {}
    for k in initial_output["featureSwitch"].keys():
        if k == "debug":
            for k in initial_output["featureSwitch"]["debug"].keys():
                featureSwitches[k] = initial_output["featureSwitch"]["debug"][k]
        if k == "defaultConfig":
            for k in initial_output["featureSwitch"]["defaultConfig"].keys():
                featureSwitches[k] = initial_output["featureSwitch"]["defaultConfig"][k]
        if k == "user":
            for k in initial_output["featureSwitch"]["user"].keys():
                featureSwitches[k] = initial_output["featureSwitch"]["user"][k]
    print(featureSwitches)
    for i in range(len(graphql_output)):
        graphql_output[i]["exports"]["metadata"]["featureSwitch"] = {}
        for switch in graphql_output[i]["exports"]["metadata"]["featureSwitches"]:
            for k in featureSwitches:
                if switch == k:
                    graphql_output[i]["exports"]["metadata"]["featureSwitch"][
                        switch
                    ] = featureSwitches[k]
    return graphql_output


def get_freeze_object(parsed_list: list, disable_tqdm=True) -> list:

    reg_freeze_object = "Object\.freeze\($"
    freeze_object_list = search_js_reg(parsed_list, reg_freeze_object)
    freeze_object_output = []

    for freeze_object in tqdm(freeze_object_list, disable=disable_tqdm):
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
        feature_switches = get_freeze_object(exports.parent, disable_tqdm=True)
        if len(feature_switches) > 0:
            return feature_switches[0]
