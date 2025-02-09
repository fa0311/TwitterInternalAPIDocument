from lib.js_parser.js_parser import *

# this.dispatch


def get_dispatch_list():
    method_list = ["get", "post", "delete", "put"]
    url_list = [
        ("", "https://api.x.com/1.1/{queryId}.json"),
        ("I", "https://x.com/i/api/1.1/{queryId}.json"),
        ("URT", "https://x.com/i/api/2/{queryId}.json"),
        ("Unversioned", "Unversioned"),
    ]

    output = {}
    for m in method_list:
        for u in url_list:
            output.update({m + u[0]: (m, u[0], u[1])})
    return output


def get_dispatch(parsed_list: js_data) -> dict:
    reg_graphql = 'e.{method}\("{queryId}",'.format(
        method="({0})".format("|".join(get_dispatch_list().keys())),
        queryId="([a-z_/]*?)",
    )
    dispatch_list = search_js_reg(parsed_list, reg_graphql)
    dispatch_list_unique: list[js_search_data] = []

    for i in dispatch_list:
        for ii in dispatch_list_unique:
            if "".join(i.data[0]) == "".join(ii.data[0]):
                break
        else:
            dispatch_list_unique.append(i)

    return [
        {"queryId": d.data[0][1], "dispatch_key": d.data[0][0]}
        for d in dispatch_list_unique
    ]


def split_dispatch(dispatch_list: list[dict]) -> dict:
    dispatch = get_dispatch_list()

    dispatch_key = (
        [d for d in dispatch.keys() if dispatch[d][1] in ["", "I"]],
        [d for d in dispatch.keys() if dispatch[d][1] in ["URT"]],
        [d for d in dispatch.keys() if dispatch[d][1] in ["Unversioned"]],
    )

    [d.update({"dispatch": dispatch[d["dispatch_key"]]}) for d in dispatch_list]

    return (
        [d for d in dispatch_list if d["dispatch_key"] in dispatch_key[0]],
        [d for d in dispatch_list if d["dispatch_key"] in dispatch_key[1]],
        [d for d in dispatch_list if d["dispatch_key"] in dispatch_key[2]],
    )
