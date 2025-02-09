import json

import requests
from TwitterFrontendFlow.TwitterFrontendFlow.TwitterFrontendFlow import *

api = requests.get(
    "https://raw.githubusercontent.com/fa0311/TwitterInternalAPIDocument/v1.2/docs/json/API.json"
).json()

# Always use new APIs
# api = requests.get("https://github.com/fa0311/TwitterInternalAPIDocument/blob/master/docs/json/API.json").json()

headers = api["header"]
session = requests.session()
session.get(
    "https://developer.x.com", headers={"User-Agent": headers["User-Agent"]}
)
x_guest_token = session.post(
    "https://api.x.com/1.1/guest/activate.json", headers=headers
).json()["guest_token"]

# <Recommendation> You can also use TwitterFrontendFlow
# flow = TwitterFrontendFlow()
# session = flow.session
# x_guest_token = flow.x_guest_token

headers.update(
    {
        "Content-type": "application/json",
        "x-guest-token": x_guest_token,
        "x-csrf-token": session.cookies.get("ct0"),
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "en",
    }
)

# API you want to use
operationName = "UserTweets"

# variables must be entered by yourself
variables = {
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
}

data = api["graphql"][operationName]
parameters = {
    "queryId": data["queryId"],
    "variables": json.dumps(variables),
    "features": json.dumps(data["features"]),
}

data["url"] = "https://x.com/i/api/graphql/oPHs3ydu7ZOOy2f02soaPA/UserTweets"


if data["method"] == "GET":
    response = session.get(data["url"], headers=headers, params=parameters).json()
elif data["method"] == "POST":
    response = session.post(data["url"], headers=headers, json=parameters).json()

for instructions in response["data"]["user"]["result"]["timeline_v2"]["timeline"][
    "instructions"
]:
    try:
        for entries in instructions["entries"]:
            try:
                print(
                    entries["content"]["itemContent"]["tweet_results"]["result"][
                        "legacy"
                    ]["full_text"]
                )
            except:
                pass
    except:
        pass
