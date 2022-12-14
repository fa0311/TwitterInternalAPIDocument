# Twitter Internal GraphQL API Document<br>
This document is entirely auto-generated and may contain errors.<br>
## Usage<br>
If the parameter is an array type, encode it in json format.<br>
Body example:<br>
```Python
json.dumps({
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
    })
```
`json.dumps` is equivalent to `JSON.stringify` in javaScript<br>
## AudioSpaceById<br>
Request URL: `https://twitter.com/i/api/graphql/JG6QN6rBEJU0Hxz2XDixqA/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable    |
|:----------------|:-------|:------------|
| id              | Future | n           |
| isMetatagsQuery | Future | o           |
| ...()(0,r.d)    | Future | _           |
| withReplays     | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| spaces_2022_h2_clipping                                                 | boolean | True      |
| spaces_2022_h2_spaces_communities                                       | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## SubscribeToScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| id    | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnsubscribeFromScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Zevhh76Msw574ZSs2NQHGQ/UnsubscribeFromScheduledSpace`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| id    | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AudioSpaceSearch<br>
Request URL: `https://twitter.com/i/api/graphql/NTq79TuSz6fHj8lQaferJw/AudioSpaceSearch`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| query  | Future | t          |
| filter | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/_CFT9CUyP5SQ23iEHhayaw/Followers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| userId                 | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,l.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/Vhc3r1d1sYcdHvnK7vw5gA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| userId                 | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,l.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/lBDN55B4BQFzW3j9II2Bkg/Following`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| userId                 | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,l.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/tVXT_bnZB6czWhKjG5R7wQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,l.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ugBJ68SNxBlSsts6juIAEw/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| rootTweetId            | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,l.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/FL7Ow0tfZgz8POupSccO5Q/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,l.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/r_uGpRxsKF86cJ8G0qKCxg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable   |
|:---------------------------------------|:-------|:-----------|
| timelineId                             | Future | r          |
| count                                  | Future | n          |
| cursor                                 | Future | i          |
| withQuickPromoteEligibilityTweetFields | Future | True       |
| ...()(0,l.d)                           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/HtSXz4lDHANsgSZx_SoPKw/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable                                                 |
|:--------------------------|:-------|:---------------------------------------------------------|
| tweetId                   | Future | a                                                        |
| includePromotedContent    | Future | True                                                     |
| withBirdwatchNotes        | Future | t.isTrue()                                               |
| withVoice                 | Future | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | Future | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,c.d) | Future | _                                                        |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## FavoriteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable      |
|:---------|:-------|:--------------|
| tweet_id | Future | a             |
| ...()&&  | Future | {'...o': '_'} |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnfavoriteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable      |
|:---------|:-------|:--------------|
| tweet_id | Future | a             |
| ...()&&  | Future | {'...o': '_'} |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTweetDownvote<br>
Request URL: `https://twitter.com/i/api/graphql/Eo65jl-gww30avDgrXvhUA/CreateTweetDownvote`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweetDownvote<br>
Request URL: `https://twitter.com/i/api/graphql/VNEvEGXaUAMfiExP8Tbezw/DeleteTweetDownvote`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTweetReaction<br>
Request URL: `https://twitter.com/i/api/graphql/D7M6X3h4-mJE8UB1Ap3_dQ/CreateTweetReaction`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable      |
|:--------------|:-------|:--------------|
| tweet_id      | Future | i             |
| reaction_type | Future | a             |
| ...()&&       | Future | {'...t': '_'} |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweetReaction<br>
Request URL: `https://twitter.com/i/api/graphql/GKwK0Rj4EdkfwdHQMZTpuw/DeleteTweetReaction`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable      |
|:---------|:-------|:--------------|
| tweet_id | Future | r             |
| ...()&&  | Future | {'...o': '_'} |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| tweet_id     | Future | s             |
| ...()&&      | Future | {'...t': '_'} |
| dark_request | Future | False         |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable      |
|:--------------|:-------|:--------------|
| tweet_id      | Future | s             |
| comparison_id | Future | t             |
| ...()&&       | Future | {'...n': '_'} |
| dark_request  | Future | True          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable   |
|:----------------|:-------|:-----------|
| source_tweet_id | Future | r          |
| comparison_id   | Future | t          |
| dark_request    | Future | True       |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable   |
|:----------------|:-------|:-----------|
| source_tweet_id | Future | r          |
| dark_request    | Future | False      |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateBookmark<br>
Request URL: `https://twitter.com/i/api/graphql/aoDbu3RHznuiSkQ9aNM67Q/CreateBookmark`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmark<br>
Request URL: `https://twitter.com/i/api/graphql/Wlmlj2-xzyS1GN3a6cj-mQ/DeleteBookmark`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ModerateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/pjFnHGVqCjTcZol0xcBJjw/ModerateTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| tweetId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnmoderateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/pVSyu6PA57TLvIE4nN2tsA/UnmoderateTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| tweetId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/vG6RO31HxvpGl9JY79lCxg/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| ...r         | Future | _             |
| dark_request | Future | !!n.preview   |
| ...()&&      | Future | {'...l': '_'} |
| ...()(0,c.d) | Future | _             |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CreateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/vG6RO31HxvpGl9JY79lCxg/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable      |
|:--------------|:-------|:--------------|
| ...o          | Future | _             |
| comparison_id | Future | s             |
| dark_request  | Future | True          |
| ...()&&       | Future | {'...l': '_'} |
| ...()(0,c.d)  | Future | _             |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## DeleteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | s          |
| dark_request | Future | False      |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable   |
|:--------------|:-------|:-----------|
| tweet_id      | Future | s          |
| comparison_id | Future | r          |
| dark_request  | Future | True       |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConversationControlChange<br>
Request URL: `https://twitter.com/i/api/graphql/hb1elGcj6769uT8qVYqtjw/ConversationControlChange`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | n          |
| mode     | Future | r          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConversationControlDelete<br>
Request URL: `https://twitter.com/i/api/graphql/OoMO_aSZ1ZXjegeamF9QmA/ConversationControlDelete`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnmentionUserFromConversation<br>
Request URL: `https://twitter.com/i/api/graphql/xVW9j3OqoBRY9d6_2OONEg/UnmentionUserFromConversation`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mHjPNFFphzuYJRPGd4i0Ow/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| tweetText | Future | r          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_enhance_cards_enabled                  | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/IuBygwNJorVBfJGTrEtPGg/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| includePromotedContent | Future | True       |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## timelinesFeedback<br>
Request URL: `https://twitter.com/i/api/graphql/vfVbgvTPTQ-dF_PQ5lD1WQ/timelinesFeedback`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConnectTabTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/u8fJxYzeq2j-f9geieaY1w/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | i          |
| cursor       | Future | r          |
| context      | Future | n          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J912WAYzbDa7kWhc34_hWg/GetTweetReactionTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable   |
|:---------------------------|:-------|:-----------|
| tweetId                    | Future | n          |
| withSuperFollowsUserFields | Future | t.isTrue() |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/evFSxb_pfw8vn_LHQIlgNQ/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| tweetId                | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | True       |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://twitter.com/i/api/graphql/3fODegwhTIkaB9ZujUu2Uw/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| tweetId                | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | True       |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://twitter.com/i/api/graphql/43vwj05eUlKDUmf6ck8IYQ/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable   |
|:---------------------------------------|:-------|:-----------|
| tweetId                                | Future | n          |
| ...()(0,P.d)                           | Future | _          |
| withQuickPromoteEligibilityTweetFields | Future | True       |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## articleNudgeDomains<br>
Request URL: `https://twitter.com/i/api/graphql/88Bu08U2ddaVVjKmmXjVYg/articleNudgeDomains`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UsersVerifiedAvatars<br>
Request URL: `https://twitter.com/i/api/graphql/2GG0in75SNCqtCn6xyyf7w/UsersVerifiedAvatars`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| userIds | Future | r          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| blue_business_consumption_api_enabled                 | boolean | True      |

#### queryId<br>
`None`<br>
## BizProfileFetchUser<br>
Request URL: `https://twitter.com/i/api/graphql/Rp94IhO-2f4Gqi7MSwBquA/BizProfileFetchUser`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | Future | t.rest_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubcribeToRevueNewsletter<br>
Request URL: `https://twitter.com/i/api/graphql/yUpmLojxsGPk0Sh3JHfEcQ/SubcribeToRevueNewsletter`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key            | type   | variable         |
|:---------------|:-------|:-----------------|
| revueAccountId | Future | t.revueAccountId |
| doubleOptIn    | Future | t.doubleOptIn    |
| via            | Future | t.via            |
| client         | Future | t.client         |
| element        | Future | t.element        |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | Future | n          |
| name                   | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RemoveTweetFromBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | Future | n          |
| tweet_id               | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://twitter.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarksAllDelete<br>
Request URL: `https://twitter.com/i/api/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/nYcJT7I2QL7l7UFL7JL3Hg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | True       |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/r3qZG8mhPyx7ArOk-Unplw/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | True       |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## PutClientEducationFlag<br>
Request URL: `https://twitter.com/i/api/graphql/IjQ-egg0uPkY11NyPMfRMQ/PutClientEducationFlag`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| flag  | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/td7lxRy7ebrYrSOTXujvKQ/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable   |
|:--------------|:-------|:-----------|
| name          | Future | o          |
| description   | Future | i          |
| joinPolicy    | Future | a          |
| invitesPolicy | Future | r          |
| ...()(0,P.S)  | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/SJbkSoB-KVWdhOictF3dkA/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/A8jO9OaEYcOkJZRQ-XYDlg/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/1toGhsa3iXuwAVtAAro_FA/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/bySN2Br1MSz9Qixyo1gbUw/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fB3UYualPq5lqvBH7gxHWg/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/v5et0cshlQ6em991kwtw6Q/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,P.S) | Future | _          |
| ...n         | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/q0WKkjb70_5Qz9ClYtM3Gg/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/NlJkjcxDqgE2TvWSOlnsMQ/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable   |
|:--------------|:-------|:-----------|
| ...n          | Future | _          |
| withCommunity | Future | True       |
| ...()(0,P.d)  | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/2jNfqKit0o2fNDT4Ykyk2Q/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/vWCNSlC57v9fwq42MzxaiA/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |
| ...n                      | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/7qOEAwz6o5FF8OiPu78NAQ/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/gSvBr8bps-XJKnZeSfGrdA/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweetId      | Future | n.tweetId  |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/wkz0R6LZ3r5wEQogvikKIw/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/WqyE1Danfz1FA7ilHmIefA/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/gssPziA-p-__2P0kVXzmnw/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://twitter.com/i/api/graphql/el2xSrgrXBxyWvbz193qaA/CommunityUserInvite`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |
| userId      | Future | t.userId      |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/WxsIKHo8ZlvCdyTbBNjNQA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...n         | Future | _          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/RuLDnIZExnVv6kY30--INg/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| name         | Future | n.name        |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/tCtE03uRpnjJ07PLEZQnIw/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| description  | Future | n.purpose     |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/ctQ9ueodvTRbyWSR-Tximg/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| theme        | Future | n.theme       |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/3dF-qqCrcWGUAvR1PvmwRg/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ruleId       | Future | n.ruleId      |
| name         | Future | n.name        |
| description  | Future | n.description |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/FpHrdQqMXSxdU5GvAA-gsQ/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| name         | Future | n.name        |
| description  | Future | n.description |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/A3_8wiyS_qQv1mfbdYjS7w/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ruleId       | Future | n.ruleId      |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/-p2z4fQWCnVWkwWkRqJ23A/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ruleIds      | Future | n.ruleIds     |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/UemodwVHn_43HJkmAbEhVQ/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| mediaId      | Future | n.mediaId     |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/NHIWPrJLpzz1jdXUB4X8PA/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,P.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ContentControlToolFetchOne<br>
Request URL: `https://twitter.com/i/api/graphql/JD2EtsNFZ3uvvTP_lfn9Bg/ContentControlToolFetchOne`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| toolId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolEnable<br>
Request URL: `https://twitter.com/i/api/graphql/4dMgLjwMMTqp33sMQ6IrJA/ContentControlToolEnable`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| toolId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolDisable<br>
Request URL: `https://twitter.com/i/api/graphql/N6oDUH0bX-7w9Cj4Wd6zXA/ContentControlToolDisable`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| toolId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolFetchAll<br>
Request URL: `https://twitter.com/i/api/graphql/nMDl1pqwn1QotVzqPAjjOw/ContentControlToolFetchAll`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key        | type   | variable     |
|:-----------|:-------|:-------------|
| visibility | Future | Discoverable |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolFetchAllUserEnabled<br>
Request URL: `https://twitter.com/i/api/graphql/kOKEPqQB769u1TI5FJt-tw/ContentControlToolFetchAllUserEnabled`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/Npe3vpgBkJAjor90HATuCQ/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                                        | type   | variable                              |
|:-----------------------------------------------------------|:-------|:--------------------------------------|
| focalTweetId                                               | Future | r                                     |
| cursor                                                     | Future | i                                     |
| referrer                                                   | Future | o                                     |
| controller_data                                            | Future | n                                     |
| rux_context                                                | Future | s                                     |
| with_rux_injections                                        | Future | l                                     |
| includePromotedContent                                     | Future | True                                  |
| withCommunity                                              | Future | t.isTrue()                            |
| withQuickPromoteEligibilityTweetFields                     | Future | True                                  |
| withBirdwatchNotes                                         | Future | t.isTrue("c9s_enabled")               |
| ...("responsive_web_birdwatch_consumption_enabled")(0,P.d) | Future | _                                     |
| withVoice                                                  | Future | t.isTrue(t)                           |
| withV2Timeline                                             | Future | t.isTrue("voice_consumption_enabled") |
| isReaderMode                                               | Future | a                                     |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ConvertRitoSuggestedActions<br>
Request URL: `https://twitter.com/i/api/graphql/2njnYoE69O2jdUM7KMEnDw/ConvertRitoSuggestedActions`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/SkUL3NxTXU5bZMS6GynSBw/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                                                                                                             |
|:--------------------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| count                           | Future | null==n?void 0:n.count                                                                                                                                                               |
| query                           | Future | n.query                                                                                                                                                                              |
| withAttachments                 | Future | t.isTrue()&&t.isTrue("dm_inbox_search_message_attachment_previews_enabled")&&t.isTrue("dm_inbox_search_message_results_enabled")                                                     |
| withConversationQueryHighlights | Future | t.isTrue("direct_messages_incremental_holdback_2022h1")&&t.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled")                                                 |
| withMessageQueryHighlights      | Future | t.isTrue("direct_messages_incremental_holdback_2022h1")&&t.isTrue("dm_inbox_search_query_highlighting_message_results_enabled")&&t.isTrue("dm_inbox_search_message_results_enabled") |
| withMessages                    | Future | t.isTrue("direct_messages_incremental_holdback_2022h1")&&t.isTrue("dm_inbox_search_message_results_enabled")                                                                         |
| withSafetyModeUserFields        | Future | t.isTrue("direct_messages_incremental_holdback_2022h1")                                                                                                                              |
| withSuperFollowsUserFields      | Future | t.isTrue("rito_safety_mode_blocked_profile_enabled")                                                                                                                                 |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/5zpY1dCR-8NyxQJS_CFJoQ/DmGroupSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...n                            | Future | _                                                                                       |
| withConversationQueryHighlights | Future | t.isTrue()&&t.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...n                            | Future | _                                                                                       |
| withConversationQueryHighlights | Future | t.isTrue()&&t.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/soQ-SmPkdz_22T9bi1tZ_Q/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## DeleteDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key            | type   | variable   |
|:---------------|:-------|:-----------|
| draft_tweet_id | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/JIeXE-I6BZXHfxsgOkyHYQ/EditDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                | type   | variable   |
|:-------------------|:-------|:-----------|
| draft_tweet_id     | Future | n          |
| post_tweet_request | Future | ii()       |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://twitter.com/i/api/graphql/ZkqIq_xRhiUme0PBJNpRtg/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...n  | Future | _          |
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                | type   | variable   |
|:-------------------|:-------|:-----------|
| post_tweet_request | Future | ii()       |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteEmailNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/2qKKYFQift8p5-J1k6kqxQ/WriteEmailNotificationSettings`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| userId   | Future | i          |
| settings | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ViewerEmailSettings<br>
Request URL: `https://twitter.com/i/api/graphql/JpjlNgn4sLGvS6tgpTzYBg/ViewerEmailSettings`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ForYouExplore<br>
Request URL: `https://twitter.com/i/api/graphql/ceWUF_fRUKCPm_mX7VFUfQ/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                |
|:-------------|:-------|:------------------------|
| count        | Future | null==n?void 0:n.count  |
| cursor       | Future | null==n?void 0:n.cursor |
| ...()(0,P.d) | Future | _                       |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/6DbO9ORz0MqSO4mrfRMAFw/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable                         |
|:----------------|:-------|:---------------------------------|
| pinned_tweet_id | Future | null==n?void 0:n.pinned_tweet_id |
| page_name       | Future | null==n?void 0:n.page_name       |
| ...()(0,P.d)    | Future | _                                |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## GraphQLError<br>
Request URL: `https://twitter.com/i/api/graphql/2V2W3HIBuMW83vEMtfo_Rg/GraphQLError`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://twitter.com/i/api/graphql/4C65-E4-H9y2bmtJSyxCjQ/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| userId       | Future | a          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/hLYmQkMzr-63PH4iuzCE4w/CreateList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| isPrivate    | Future | private===a.toLowerCase() |
| name         | Future | o                         |
| description  | Future | r                         |
| ...()(0,P.S) | Future | _                         |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/KdXKwcw_ppXURRqgSe17gA/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| mediaId      | Future | a          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## DeleteList<br>
Request URL: `https://twitter.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/gXkdRiysF0d03ronFIEjlQ/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/cWJrtl1F1u_M5KNf-n9jZQ/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| screenName   | Future | i          |
| listSlug     | Future | r          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/Jw7DBqqmkrXglizvULXuFQ/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | n.list_id  |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/-LEqmBRQIEfuElicDt5owg/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| listId                   | Future | o           |
| count                    | Future | r           |
| cursor                   | Future | a           |
| ...()(0,P.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/lMy5gOfWTRL5rdMjknmvDg/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | o          |
| count        | Future | r          |
| cursor       | Future | a          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/sTCwCSH0JWSqw-p2B5zzeQ/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | Future | s          |
| isListMemberTargetUserId | Future | o          |
| count                    | Future | r          |
| cursor                   | Future | a          |
| ...()(0,P.d)             | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/grsLBCABkl2nu83CSjYSCQ/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | o          |
| count        | Future | r          |
| cursor       | Future | a          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/dXNE3eAXlM80OOBlvAv1oQ/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| userId       | Future | a          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/3tGx2fYMpb4ZenkHb8Cktw/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | r          |
| ...a   | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://twitter.com/i/api/graphql/HbdapRIyeqveMw4UrisXbw/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | r          |
| ...a   | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://twitter.com/i/api/graphql/5tWZRNw92Ml9ceGJJ5EEBA/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listIds      | Future | i          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/RYl7h8zLdch8lFNVEwI63g/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/xm_4ggQUlaOeaVnUJtuM-Q/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## MuteList<br>
Request URL: `https://twitter.com/i/api/graphql/ZYyanJsskNUcltu9bliMLA/MuteList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnmuteList<br>
Request URL: `https://twitter.com/i/api/graphql/pMZrHRNsmEkXgbn3tOyr7Q/UnmuteList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/jtLihBHG_ljMImm_5-8whA/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| listId       | Future | a                         |
| isPrivate    | Future | private===o.toLowerCase() |
| description  | Future | r                         |
| name         | Future | s                         |
| ...()(0,P.S) | Future | _                         |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/JFrA4V8HzSYn13SjsOKfeA/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | r          |
| count        | Future | n          |
| cursor       | Future | i          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ZIFR9IFSFi1VwNSiPGBpDw/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | n          |
| cursor       | Future | i          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://twitter.com/i/api/graphql/fOHcMbtKWopvL2ZYZ5Arvw/ListPins`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,P.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/kplBCO34s0o5ghx5B4bh3w/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | n          |
| cursor       | Future | i          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/xlcvrM-RNHWSUoNsnqab4Q/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| rest_id                | Future | r          |
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,P.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://twitter.com/i/api/graphql/zEAmYdYUvRuhrr9zjc5Vvg/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable                              |
|:---------------------------------------|:-------|:--------------------------------------|
| userId                                 | Future | r                                     |
| count                                  | Future | n                                     |
| cursor                                 | Future | i                                     |
| includePromotedContent                 | Future | True                                  |
| withQuickPromoteEligibilityTweetFields | Future | True                                  |
| ...()(0,P.d)                           | Future | _                                     |
| withVoice                              | Future | t.isTrue(t)                           |
| withV2Timeline                         | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://twitter.com/i/api/graphql/HMDNer3bNC9hzw6-bq89HQ/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable                              |
|:--------------------------|:-------|:--------------------------------------|
| userId                    | Future | r                                     |
| count                     | Future | n                                     |
| cursor                    | Future | i                                     |
| includePromotedContent    | Future | True                                  |
| withCommunity             | Future | t.isTrue()                            |
| ...("c9s_enabled")(0,P.d) | Future | _                                     |
| withVoice                 | Future | t.isTrue(t)                           |
| withV2Timeline            | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## UserSuperFollowTweets<br>
Request URL: `https://twitter.com/i/api/graphql/lSdL_CH3uxP6vglVmJcDYg/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable    |
|:-----------------------|:-------|:------------|
| userId                 | Future | r           |
| count                  | Future | n           |
| cursor                 | Future | i           |
| includePromotedContent | Future | True        |
| ...()(0,P.d)           | Future | _           |
| withVoice              | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://twitter.com/i/api/graphql/PJdFpt65UlB7qW9bFsEwlQ/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"i","count":"t","cursor":"string"==typeof n?n:"void 0","includePromotedContent":"!1","withDownvotePerspective":"!1","withReactionsMetadata":"!1","withReactionsPerspective":"!1","withSuperFollowsTweetFields":"!1","withSuperFollowsUserFields":"!1","withVoice":"!1"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://twitter.com/i/api/graphql/nfvMXIYTK6YQmXZ6OnM8FA/Likes`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable                              |
|:-----------------------|:-------|:--------------------------------------|
| userId                 | Future | r                                     |
| count                  | Future | n                                     |
| cursor                 | Future | i                                     |
| includePromotedContent | Future | False                                 |
| ...()(0,P.d)           | Future | _                                     |
| withClientEventToken   | Future | False                                 |
| withBirdwatchNotes     | Future | False                                 |
| withVoice              | Future | t.isTrue(t)                           |
| withV2Timeline         | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://twitter.com/i/api/graphql/IMtUJRC4tlzBN1stVnQbzw/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable                              |
|:-----------------------|:-------|:--------------------------------------|
| userId                 | Future | r                                     |
| count                  | Future | n                                     |
| cursor                 | Future | i                                     |
| includePromotedContent | Future | False                                 |
| ...()(0,P.d)           | Future | _                                     |
| withClientEventToken   | Future | False                                 |
| withBirdwatchNotes     | Future | False                                 |
| withVoice              | Future | t.isTrue(t)                           |
| withV2Timeline         | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## RevueAccountByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/NFARV9iE-FIK7FOsO_d23Q/RevueAccountByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | Future | t.rest_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RitoActionedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/4zqHQUo54w66n5uv7cn8nQ/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | n           |
| rest_id                  | Future | i           |
| ...()(0,P.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## DismissRitoSuggestedAction<br>
Request URL: `https://twitter.com/i/api/graphql/jYvwa61cv3NwNP24iUru6g/DismissRitoSuggestedAction`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| userId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/_EmBHAMY8qLDxeBa6KhGBg/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | n           |
| ...()(0,P.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/gIiZbG3vsqWI-pSg89yhyg/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | n           |
| rest_id                  | Future | i           |
| ...()(0,P.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## RitoSuggestedActionsFacePile<br>
Request URL: `https://twitter.com/i/api/graphql/GnQKeEdL1LyeK3dTQCS1yw/RitoSuggestedActionsFacePile`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                | type   | variable   |
|:-------------------|:-------|:-----------|
| post_tweet_request | Future | r          |
| execute_at         | Future | Ho()       |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchScheduledTweets<br>
Request URL: `https://twitter.com/i/api/graphql/ITtjAzvlZni2wWXwf295Qg/FetchScheduledTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...n  | Future | _          |
| ...t  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                | type   | variable   |
|:-------------------|:-------|:-----------|
| scheduled_tweet_id | Future | i          |
| post_tweet_request | Future | a          |
| execute_at         | Future | Ho()       |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserSessionsList<br>
Request URL: `https://twitter.com/i/api/graphql/vJ-XatpmQSG8bDch8-t9Jw/UserSessionsList`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EnableVerifiedPhoneLabel<br>
Request URL: `https://twitter.com/i/api/graphql/C3RJFfMsb_KcEytpKmRRkw/EnableVerifiedPhoneLabel`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DisableVerifiedPhoneLabel<br>
Request URL: `https://twitter.com/i/api/graphql/g2m0pAOamawNtVIfjXNMJg/DisableVerifiedPhoneLabel`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileUserPhoneState<br>
Request URL: `https://twitter.com/i/api/graphql/5kUWP8C1hcd6omvg6HXXTQ/ProfileUserPhoneState`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## updateAltTextPromptPreference<br>
Request URL: `https://twitter.com/i/api/graphql/aQKrduk_DA46XfOQDkcEng/updateAltTextPromptPreference`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key        | type   | variable   |
|:-----------|:-------|:-----------|
| promptType | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## updateCaptionsAlwaysDisplayPreference<br>
Request URL: `https://twitter.com/i/api/graphql/uCUQhvZ5sJ9qHinRp6CFlQ/updateCaptionsAlwaysDisplayPreference`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key               | type   | variable   |
|:------------------|:-------|:-----------|
| displayPreference | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## getAltTextPromptPreference<br>
Request URL: `https://twitter.com/i/api/graphql/PFIxTk8owMoZgiMccP0r4g/getAltTextPromptPreference`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## getCaptionsAlwaysDisplayPreference<br>
Request URL: `https://twitter.com/i/api/graphql/BwgMOGpOViDS0ri7VUgglg/getCaptionsAlwaysDisplayPreference`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DataSaverMode<br>
Request URL: `https://twitter.com/i/api/graphql/xF6sXnKJfS2AOylzxRjf6A/DataSaverMode`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| device_id | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteDataSaverPreferences<br>
Request URL: `https://twitter.com/i/api/graphql/H03etWvZGz41YASxAU2YPg/WriteDataSaverPreferences`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| dataSaverEnabled | Future | t          |
| deviceId         | Future | n          |
| videoAutoplay    | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmNsfwMediaFilterUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/of_N6O33zfyD4qsFJMYFxA/DmNsfwMediaFilterUpdate`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key               | type   | variable   |
|:------------------|:-------|:-----------|
| userId            | Future | n          |
| dmNsfwMediaFilter | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SharingAudiospacesListeningDataWithFollowersUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/5h0kNbk3ii97rmfY6CdgAA/SharingAudiospacesListeningDataWithFollowersUpdate`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | Future | n          |
| sharingAudiospacesListeningDataWithFollowers | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GetSafetyModeSettings<br>
Request URL: `https://twitter.com/i/api/graphql/AhxTX0lkbIos4WG53xwzSA/GetSafetyModeSettings`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SetSafetyModeSettings<br>
Request URL: `https://twitter.com/i/api/graphql/qSJIPIpf4gA7Wn21bT3D4w/SetSafetyModeSettings`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | Future | n                 |
| enabled  | Future | none!==t          |
| duration | Future | none===t?void 0:t |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GetUserClaims<br>
Request URL: `https://twitter.com/i/api/graphql/lFi3xnx0auUUnyG4YwpCNw/GetUserClaims`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscriptionProductFeaturesFetch<br>
Request URL: `https://twitter.com/i/api/graphql/Me2CVcAXxvK2WMr-Nh_Qqg/SubscriptionProductFeaturesFetch`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ctTeCNEBzKyQVI9yOwfFSQ/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...n                | Future | _          |
| ...()(0,P.d)        | Future | _          |
| articleListSeedType | Future | i          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/1uLYTP66dtOsg_C5iulpDw/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...n                | Future | _          |
| ...()(0,P.d)        | Future | _          |
| articleListSeedType | Future | i          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TopicTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/6jrNAoBKZGetR6Jle3cxQg/TopicTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"r","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","P.dt"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://twitter.com/i/api/graphql/9mELAze6KN4AkDhYeOw_ng/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"r","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","P.dt"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://twitter.com/i/api/graphql/5x1bsZSlwks9kDr3OeNKRg/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | Future | r          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TopicByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/4OUZZOonV2h60I0wdlQb_w/TopicByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://twitter.com/i/api/graphql/-2K3sM0C6c_qNIWbwzQyeQ/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | Future | r          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://twitter.com/i/api/graphql/gf73mx0IQ5iUIJT8IGRqVQ/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/GS1zbaDE-QgECod_wkfBmA/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | o          |
| cursor       | Future | a          |
| context      | Future | r          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://twitter.com/i/api/graphql/DTe3H-nfK-wHsNtppziT9A/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | Future | a          |
| cursor       | Future | r          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TopicFollow<br>
Request URL: `https://twitter.com/i/api/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicUnfollow<br>
Request URL: `https://twitter.com/i/api/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | Future | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://twitter.com/i/api/graphql/BHmqi2k5qdtAGOvFTYU0zg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | r          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## AuthenticatedUserTFLists<br>
Request URL: `https://twitter.com/i/api/graphql/QjN8ZdavFDqxUjNn3r9cig/AuthenticatedUserTFLists`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTrustedFriendsList<br>
Request URL: `https://twitter.com/i/api/graphql/2tP8XUYeLHKjq5RHvuvpZw/CreateTrustedFriendsList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://twitter.com/i/api/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | Future | t          |

#### features<br>
| key                                             | type    | default   |
|:------------------------------------------------|:--------|:----------|
| profile_foundations_tweet_stats_enabled         | boolean | True      |
| profile_foundations_tweet_stats_tweet_frequency | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/vB4FItxO6WLbzTcwAqcBPQ/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| ...()(0,P.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://twitter.com/i/api/graphql/z3w6o7PABcB6MOP0RWYfKQ/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                    |
|:-------------|:-------|:----------------------------|
| data         | Future | {'content_state_json': 'i'} |
| ...()(0,P.d) | Future | _                           |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleDelete<br>
Request URL: `https://twitter.com/i/api/graphql/6st-stMDc7KBqLT8KvWhHg/TwitterArticleDelete`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://twitter.com/i/api/graphql/Hfvj0dep-4yi3e2O7myl8g/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | r          |
| mediaId          | Future | i          |
| ...()(0,P.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://twitter.com/i/api/graphql/Pbws1LGvVzaSB6luMlo93A/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable                                                         |
|:-----------------|:-------|:-----------------------------------------------------------------|
| twitterArticleId | Future | a                                                                |
| data             | Future | {'content_state_json': 'i', 'plaintext': 'r', 'word_count': 'o'} |
| ...()(0,P.d)     | Future | _                                                                |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://twitter.com/i/api/graphql/s28LoacvsKEC6LPGN_6QaQ/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | r          |
| mediaKeys        | Future | i          |
| ...()(0,P.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/WiFyREI2Vxg6HDvXpsSTyQ/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | r          |
| title            | Future | i          |
| ...()(0,P.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://twitter.com/i/api/graphql/BhkiIBT0KCpGBpjysPw2zQ/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| visibility       | Future | r          |
| ...()(0,P.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/mWiqSasO2juD50Lqe49rHg/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...n         | Future | _          |
| ...()(0,P.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| view_counts_public_visibility_enabled                                   | boolean | True      |
| view_counts_everywhere_api_enabled                                      | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/K68SNPXXT2pcSypG7eUmHQ/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable           |
|:-----------------|:-------|:-------------------|
| trustedFriendsId | Future | t.trustedFriendsId |
| prefix           | Future | t.prefix           |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityUserRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/C9CUCfAvlaMEhJBmM2hZkg/CommunityUserRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |
| prefix      | Future | t.prefix      |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/npEFiYc3sCX-YDHZ1B69nw/CommunityMemberRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |
| prefix      | Future | t.prefix      |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |

#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/3_rHKnFbEGn6AlZdNjf8hQ/Viewer`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                   |
|:---------------------------|:-------|:-------------------------------------------|
| withCommunitiesMemberships | Future | t.isTrue()                                 |
| withCommunitiesCreation    | Future | t.isTrue("c9s_enabled")                    |
| withSuperFollowsUserFields | Future | t.isTrue("c9s_community_creation_enabled") |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/0dbpv_sJc_YxCb-1RO2NFA/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| screen_name                | Future | n                                                    |
| withSafetyModeUserFields   | Future | t.isTrue()                                           |
| withSuperFollowsUserFields | Future | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                          | type    | default   |
|:-------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled        | boolean | True      |
| verified_phone_label_enabled                                 | boolean | True      |
| responsive_web_twitter_blue_new_verification_copy_is_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled           | boolean | False     |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/3uv4-34w15chv3dW9DoVhQ/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | Future | n                                                    |
| withSafetyModeUserFields   | Future | t.isTrue()                                           |
| withSuperFollowsUserFields | Future | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/JTB-JEmY-GvEgyUXTYo3ZA/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable      |
|:---------------------------|:-------|:--------------|
| userIds                    | Future | n.split()     |
| withSuperFollowsUserFields | Future | t.isTrue(",") |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## RemoveFollower<br>
Request URL: `https://twitter.com/i/api/graphql/QpNfg0kpPRfjROQ_9eOLXA/RemoveFollower`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key            | type   | variable   |
|:---------------|:-------|:-----------|
| target_user_id | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
