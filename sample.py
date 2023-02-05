import requests
import json

api = requests.get(
    "https://raw.githubusercontent.com/fa0311/TwitterInternalAPIDocument/develop/docs/json/API.json"
).json()

# Always use new APIs
# api = requests.get("https://github.com/fa0311/TwitterInternalAPIDocument/blob/master/docs/json/API.json").json()

headers=api["header"]
session = requests.session()
session.get("https://twitter.com/", headers={"User-Agent": headers["User-Agent"]})
x_guest_token  = session.post("https://api.twitter.com/1.1/guest/activate.json",headers=headers).json()["guest_token"]
headers.update({
            "Content-type": "application/json",
            "x-guest-token": x_guest_token,
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "en",
})

# <Recommendation> You can also use TwitterFrontendFlow
# flow = TwitterFrontendFlow()
# session = flow.session
# x_guest_token = flow.x_guest_token

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

data["url"] = "https://api.twitter.com/graphql/oPHs3ydu7ZOOy2f02soaPA/UserTweets"


if data["method"] == "GET":
    response = session.get(data["url"],headers=headers, params=parameters).json()
elif data["method"] == "POST":
    response = session.post(data["url"],headers=headers, json=parameters).json()


print(response)