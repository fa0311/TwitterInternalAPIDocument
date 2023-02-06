import logging
import re
import json
from lib.js_parser.js_parser import *
from tqdm import tqdm


def get_v11(parsed_list: js_data) -> dict:
    reg_graphql = 'e.{method}\("{queryId}",'.format(
        method="(get|post)", queryId="([a-z_/]*?)"
    )
    v11_list = search_js_reg(parsed_list, reg_graphql)
    v11_list_unique:list[js_search_data] = []

    for i in v11_list:
        for ii in v11_list_unique:
            if "".join(i.data[0]) == "".join(ii.data[0]):
                break
        else:
            v11_list_unique.append(i)

    return [{"queryId": v11.data[0][1], "method": v11.data[0][0]} for v11 in v11_list_unique]
