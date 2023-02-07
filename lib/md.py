from lib.md_generator.md_generator import md_generator
import logging


def gen_md_graphql(graphql_output: list) -> md_generator:
    type_converter = {
        "!0": "boolean",
        "!1": "boolean",
        "true": "boolean",
        "false": "boolean",
    }
    variable_converter = {
        "!0": True,
        "!1": False,
        "true": True,
        "false": False,
    }
    md = md_generator()
    md.h1("Twitter Internal GraphQL API Document")
    md.p("This document is entirely auto-generated and may contain errors.")
    md.h2("Usage")
    md.p("If the parameter is an array type, encode it in json format.")
    md.p("Body example:")
    md.code(
        """json.dumps({
        "queryId": "kV0jgNRI3ofhHK_G5yhlZg",
        "variables": json.dumps({
            "tweet_text": "Hello, world!",
            "media": {"media_entities": [], "possibly_sensitive": False},
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": True,
            "withSuperFollowsUserFields": False,
            "semantic_annotation_ids": [],
            "dark_request": False,
            "withBirdwatchPivots": False,
        }),
    })""",
        title="Python",
    )
    md.p("`json.dumps` is equivalent to `JSON.stringify` in javaScript")

    for graphql in graphql_output:
        try:
            exports = graphql["exports"]
            query = graphql.get("query", {})
            switches = exports["metadata"]["featureSwitches"]
        except KeyError:
            logging.warning("KeyError: " + str(graphql))
            continue

        md.h2(exports["operationName"])
        md.p("Request URL", end=": ")
        md.inline(
            "https://api.twitter.com/graphql/{queryId}/{operationName}".format(
                **exports
            )
        )

        md.p("Request Method", end=": ")
        if exports["operationType"] == "mutation":
            md.inline("POST")
        else:
            md.inline("GET")
        md.p("Login Required", end=": ")
        md.inline("...")

        md.h3("Param")
        md.h4("variables")
        if type(query) is dict and len(query) > 0:
            datafram = []
            for key in query.keys():
                value = query[key]
                if type(value) is str:
                    datafram.append(
                        {
                            "key": key,
                            "type": type_converter.get(value, "..."),
                            "variable": variable_converter.get(value, value),
                        }
                    )
                else:
                    datafram.append(
                        {
                            "key": key,
                            "type": "...",
                            "variable": value,
                        }
                    )
            md.table(datafram)
        elif type(query) is list and len(query) == 0:
            md.inline("None")
        elif type(query) is str:
            if len(query) > 300:
                query = query[:300] + "..."
            md.code(
                "# Error\n" + query,
                title="internal process",
            )
        else:
            md.inline("None")

        md.h4("features")
        if type(switches) is list and len(switches) > 0:
            datafram = []
            for key in exports["metadata"]["featureSwitches"]:
                switch = exports["metadata"]["featureSwitch"][key]
                if switch == None:
                    datafram.append(
                        {
                            "key": key,
                            "type": "...",
                            "default": "error",
                        }
                    )
                elif type(switch["value"]) is str:
                    datafram.append(
                        {
                            "key": key,
                            "type": type_converter.get(switch["value"], "..."),
                            "variable": variable_converter.get(switch["value"], "..."),
                        }
                    )
                else:
                    datafram.append(
                        {
                            "key": key,
                            "type": "...",
                            "default": switch["value"],
                        }
                    )
            md.table(datafram)
        elif type(switches) is list and len(switches) == 0:
            md.inline("None")
        else:
            md.inline("Error")

        md.h4("queryId")
        if query == "mutation":
            md.inline(exports["queryId"])
        else:
            md.inline("None")
    return md


def gen_md_v11(v11_output: list) -> md_generator:
    md = md_generator()
    for v11 in v11_output:
        md.h2(v11["queryId"])
        md.p("Request URL", end=": ")
        md.inline(
            "https://api.twitter.com/1.1/{queryId}.json".format(queryId=v11["queryId"])
        )

        md.p("Request Method", end=": ")
        md.inline(v11["method"].upper())
    return md


def gen_md_freeze_object(
    freeze_object_output: list,
) -> md_generator:
    md = md_generator()
    md.h1("Twitter Internal Constants Document")
    md.p("This document is entirely auto-generated and may contain errors.")

    for freeze_object in freeze_object_output:
        if type(freeze_object) is dict:
            datafram = []
            for key in freeze_object.keys():
                value = freeze_object[key]
                if type(value) is str:
                    value = {"!0": True, "!1": False}.get(value, value)
                datafram.append(
                    {
                        "constant": key,
                        "value": md.table_escape(value),
                    }
                )
            md.table(datafram)
        else:
            if len(freeze_object) > 300:
                freeze_object = freeze_object[:300] + "..."
            md.code(
                "# Error\n" + freeze_object,
                title="internal process",
            )
    return md
