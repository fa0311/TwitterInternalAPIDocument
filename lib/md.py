import logging

from lib.md_generator.md_generator import md_generator


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
    md.p(
        "Please do not take what is written for granted, especially since static analysis of `variables` is very difficult. Most likely it is wrong."
    )
    md.h2("Usage")
    md.p("If the parameter is an array type, encode it in json format.")
    md.p("Body example:")
    md.code(
        """json.dumps({
        "queryId": "oPHs3ydu7ZOOy2f02soaPA",
        "variables": json.dumps({
            "userId": "900282258736545792",
            "count": 40,
            "includePromotedContent": True,
            "withQuickPromoteEligibilityTweetFields": True,
            "withSuperFollowsUserFields": True,
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": True,
            "withVoice": True,
            "withV2Timeline": True,
        }),
        "variables": json.dumps({
            "responsive_web_twitter_blue_verified_badge_is_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": False,
            "verified_phone_label_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "longform_notetweets_consumption_enabled": True,
            "tweetypie_unmention_optimization_enabled": True,
            "vibe_api_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "freedom_of_speech_not_reach_appeal_label_enabled": False,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
            "interactive_text_enabled": True,
            "responsive_web_text_conversations_enabled": False,
            "responsive_web_enhance_cards_enabled": False,
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
            "https://x.com/i/api/graphql/{queryId}/{operationName}".format(
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
                switch = exports["metadata"]["featureSwitch"].get(key, None)
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


def gen_md_dispatch(dispatch_output: list) -> md_generator:
    md = md_generator()
    for d in dispatch_output:
        md.h2(d["queryId"])
        md.p("Request URL", end=": ")
        md.inline(d["dispatch"][2].format(queryId=d["queryId"]))
        md.p("Request Method", end=": ")
        md.inline(d["dispatch"][0].upper())
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
