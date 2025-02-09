import json
import logging
import re

from tqdm import tqdm

from lib.js_parser.js_parser import *


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
        if match_func_init == []:
            continue
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
    exports_output = []
    exports = search_js(parsed_list, "e.exports=")
    reg_exports = "{comma}{int}:{var}=>".format(
        comma=",?",
        int="([0-9]{1,5})",
        var="(e|\([a-z,]*?\))",
    )
    for export in exports:
        n = re.findall(reg_exports, export.parent.before)[0][0]
        try:
            data = json.loads(json_parser(export.parent.children[1]))
            if data["metadata"] is not None:
                exports_output.append({"n": n, "exports": data})
        except:
            pass

    reg_exports_ext = ';{var}.hash="{hash}",e.exports={var}'.format(
        hash="[a-z0-9]{32}", var="[a-zA-Z0-9]{1,2}"
    )
    exports = search_js_reg(parsed_list, reg_exports_ext)
    for export in exports:
        params = search_js(export.before, ",params:")
        if len(params) > 0:
            n = re.findall(reg_exports, export.parent.before)[0][0]
            data = json.loads(json_parser(params[0].after))
            exports_output.append(
                {
                    "n": n,
                    "exports": {
                        "queryId": data["id"],
                        "operationName": data["name"],
                        "operationType": data["operationKind"],
                        "metadata": {
                            "featureSwitches": data["metadata"].get("features", [])
                        },
                    },
                }
            )

    for key in range(len(exports_output)):
        for graphql in graphql_output:
            if exports_output[key]["n"] == graphql["n"]:
                exports_output[key].update(graphql)
    return exports_output


def marge_feature_switch(initial_output: dict) -> dict:
    featureSwitches = {}
    for k in initial_output["featureSwitch"].keys():
        if k == "debug":
            for k in initial_output["featureSwitch"]["debug"].keys():
                featureSwitches[k] = initial_output["featureSwitch"]["debug"][k]
        if k == "defaultConfig":
            for k in initial_output["featureSwitch"]["defaultConfig"].keys():
                featureSwitches[k] = initial_output["featureSwitch"]["defaultConfig"][k]
        if k == "user":
            for k in initial_output["featureSwitch"]["user"]["config"].keys():
                featureSwitches[k] = initial_output["featureSwitch"]["user"]["config"][k]
    return featureSwitches


def marge_metadata(graphql_output: list, feature_switch: dict) -> list:
    for i in range(len(graphql_output)):
        graphql_output[i]["exports"]["metadata"]["featureSwitch"] = {}
        for switch in graphql_output[i]["exports"]["metadata"]["featureSwitches"]:
            for k in feature_switch:
                if switch == k:
                    graphql_output[i]["exports"]["metadata"]["featureSwitch"][
                        switch
                    ] = feature_switch[k]
                    break
            else:
                if "config" in feature_switch:
                    for config_k in feature_switch["config"]:
                        if switch == config_k:
                            graphql_output[i]["exports"]["metadata"]["featureSwitch"][
                                switch
                            ] = feature_switch["config"][config_k]
                            break
                    else:
                        logging.warning("NotFoundKey: " + switch)
                else:
                    logging.warning("NotFoundKey: " + switch)
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


def to_api(graphql_output: list, kwargs: dict) -> dict:
    variable_converter = {
        "!0": True,
        "!1": False,
        "true": True,
        "false": False,
    }
    api_output = {"graphql": {}}

    for graphql in graphql_output:
        features = {}
        exports = graphql["exports"]
        for key in exports["metadata"]["featureSwitches"]:
            switch = exports["metadata"]["featureSwitch"].get(key, None)
            if switch != None:
                features[key] = variable_converter.get(switch["value"])
            else:
                logging.warning("NotFoundKey: " + key)

        api_output["graphql"][exports["operationName"]] = {
            "url": "https://x.com/i/api/graphql/{queryId}/{operationName}".format(
                **exports
            ),
            "queryId": exports["queryId"],
            "method": "POST" if exports["operationType"] == "mutation" else "GET",
            "features": features,
        }

    api_output.update(kwargs)
    return api_output
