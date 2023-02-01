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
## TweetResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/bSa1023OVguTmp92unNwrQ/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable                                                 |
|:--------------------------|:-------|:---------------------------------------------------------|
| tweetId                   | Future | r                                                        |
| includePromotedContent    | Future | True                                                     |
| withBirdwatchNotes        | Future | n.isTrue()                                               |
| withVoice                 | Future | n.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | Future | n.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,c.d) | Future | _                                                        |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| tweet_id | Future | r             |
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
| tweet_id | Future | r             |
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
| tweet_id | Future | d          |

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
| tweet_id | Future | d          |

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
| tweet_id      | Future | d             |
| reaction_type | Future | r             |
| ...()&&       | Future | {'...n': '_'} |

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
| tweet_id | Future | a             |
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
| tweet_id     | Future | l             |
| ...()&&      | Future | {'...n': '_'} |
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
| tweet_id      | Future | l             |
| comparison_id | Future | n             |
| ...()&&       | Future | {'...t': '_'} |
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
| source_tweet_id | Future | a          |
| comparison_id   | Future | n          |
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
| source_tweet_id | Future | a          |
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
| tweet_id | Future | d          |

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
| tweet_id | Future | d          |

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
| tweetId | Future | t          |

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
| tweetId | Future | t          |

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
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | l          |
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
| tweet_id      | Future | l          |
| comparison_id | Future | a          |
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
| tweet_id | Future | t          |
| mode     | Future | a          |

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
| tweet_id | Future | t          |

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
| tweet_id | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://twitter.com/i/api/graphql/xm_O-zSjwIQZl1gcHK1VVw/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable    |
|:----------------|:-------|:------------|
| id              | Future | t           |
| isMetatagsQuery | Future | r           |
| ...()(0,w.d)    | Future | _           |
| withReplays     | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| spaces_2022_h2_clipping                                                 | boolean | False     |
| spaces_2022_h2_spaces_communities                                       | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| id    | Future | n          |

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
| id    | Future | n          |

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
| query  | Future | n          |
| filter | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| tweetText | Future | a          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_enhance_cards_enabled                  | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/eVhHH2-zqwLkx5HLrYX2Ww/GetTweetReactionTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable   |
|:---------------------------|:-------|:-----------|
| tweetId                    | Future | t          |
| withSuperFollowsUserFields | Future | n.isTrue() |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/Hz3U-HJitmBGNUoCqBZ6eQ/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| tweetId                | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | True       |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://twitter.com/i/api/graphql/9HxeKO3iCsRe8apdkjECjQ/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| tweetId                | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | True       |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://twitter.com/i/api/graphql/fLWI2k7Z6EK1s2lIvNll7g/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable   |
|:---------------------------------------|:-------|:-----------|
| tweetId                                | Future | t          |
| ...()(0,w.d)                           | Future | _          |
| withQuickPromoteEligibilityTweetFields | Future | True       |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/iF-NT7oBU1rBNTurpeFG_A/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| includePromotedContent | Future | True       |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| ...n  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConnectTabTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/YoHW74HhBjNsDOPAaMOYdQ/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | d          |
| cursor       | Future | a          |
| context      | Future | t          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DisableUserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/_ckHEj05gan2VfNHG6thBA/DisableUserAccountLabel`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## adFreeArticleDomains<br>
Request URL: `https://twitter.com/i/api/graphql/zwTrX9CtnMvWlBXjsx95RQ/adFreeArticleDomains`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
Request URL: `https://twitter.com/i/api/graphql/Bjbv9tA3kxsmhHDy_4yImw/UsersVerifiedAvatars`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| userIds | Future | a          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| blue_business_consumption_api_enabled                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://twitter.com/i/api/graphql/Lx6O5UuGKcC6s6d6n6HKcw/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | d          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |

#### queryId<br>
`None`<br>
## BirdwatchProfileAcknowledgeEarnOut<br>
Request URL: `https://twitter.com/i/api/graphql/cED9wJy8Nd1kZCCYuIq9zQ/BirdwatchProfileAcknowledgeEarnOut`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchCreateAppeal<br>
Request URL: `https://twitter.com/i/api/graphql/TKdL0YFsX4DMOpMKeneLvA/BirdwatchCreateAppeal`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| note_id | Future | n.note_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchCreateNote<br>
Request URL: `https://twitter.com/i/api/graphql/ao8QMqwVuZmCGbh9biIj1g/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | t.tweet_id |
| data_v1      | Future | t.data     |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |

#### queryId<br>
`None`<br>
## BirdwatchDeleteNote<br>
Request URL: `https://twitter.com/i/api/graphql/IKS_qrShkDyor6Ri1ahd9g/BirdwatchDeleteNote`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| note_id | Future | n.note_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchDeleteRating<br>
Request URL: `https://twitter.com/i/api/graphql/OpvCOyOoQClUND66zDzrnA/BirdwatchDeleteRating`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| note_id | Future | n.note_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchEditNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/FLgLReVIssXjB_ui3wcrRQ/BirdwatchEditNotificationSettings`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| settings | Future | n.settings |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/MihoHX2vr2E8wC-7ZrylEQ/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| note_id      | Future | t.note_id  |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |

#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://twitter.com/i/api/graphql/btgGtchypc3D491MJ7XXWA/BirdwatchFetchBirdwatchProfile`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| alias | Future | n.alias    |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/THk_XXiF29ZNM8UXU1K9uQ/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | 10         |
| ...t         | Future | _          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/THk_XXiF29ZNM8UXU1K9uQ/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | 10         |
| ...t         | Future | _          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## BirdwatchFetchAuthenticatedUserProfile<br>
Request URL: `https://twitter.com/i/api/graphql/pMbW6Y4LuS5MzlSOEqERJQ/BirdwatchFetchAuthenticatedUserProfile`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAliasSelfSelectStatus<br>
Request URL: `https://twitter.com/i/api/graphql/LUEdtkcpBlGktUtms4BvwA/BirdwatchFetchAliasSelfSelectStatus`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchAliasSelect<br>
Request URL: `https://twitter.com/i/api/graphql/3ss48WFwGokBH_gj8t_8aQ/BirdwatchAliasSelect`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| alias | Future | n.alias    |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://twitter.com/i/api/graphql/9bDdJ6AL26RLkcUShEcF-A/BirdwatchFetchPublicData`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchGlobalTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/jPc9fYvHES4F7E3xhJKxlw/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## BizProfileFetchUser<br>
Request URL: `https://twitter.com/i/api/graphql/6OFpJ3TH3p8JpwOSgfgyhg/BizProfileFetchUser`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | Future | n.rest_id  |

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
| bookmark_collection_id | Future | t          |

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
| bookmark_collection_id | Future | t          |
| name                   | Future | d          |

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
| bookmark_collection_id | Future | t          |
| tweet_id               | Future | d          |

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
| ...n  | Future | _          |

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
| ...n  | Future | _          |

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
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | True       |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | True       |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| flag  | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/NmdlGqz39V_ORG8zeYKRpA/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable   |
|:--------------|:-------|:-----------|
| name          | Future | o          |
| description   | Future | d          |
| joinPolicy    | Future | r          |
| invitesPolicy | Future | a          |
| ...()(0,w.S)  | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/lD9GCXcGwOoNBm16-EBqEQ/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/3DuFMQT7Eq3vgmEY41k1Vg/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...t                      | Future | _          |
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/5Z-ePbY0QvAXWGyfcRu61w/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...t                      | Future | _          |
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/WNgLHZxRLvt9D2c8vCYOZA/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...t                      | Future | _          |
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/UNQ9rdMef1DvlJp60JNZvg/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...t                      | Future | _          |
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/9AH2Fcrph5OyEV6i7ZvmMA/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,w.S) | Future | _          |
| ...t         | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/FyG-u17Ur6i1OVAWu7iHiQ/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...t                      | Future | _          |
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/WacTyrmlyouLPgK9hb4ubw/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable   |
|:--------------|:-------|:-----------|
| ...t          | Future | _          |
| withCommunity | Future | True       |
| ...()(0,w.d)  | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/xk08n_JXQA5ssE7vptiYWA/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...t                      | Future | _          |
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/u34qfsEJskB9-1EPqTGp9A/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |
| ...t                      | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/1mMOP0xPsf7z8iWlL1Sgjg/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| withCommunity             | Future | n.isTrue() |
| ...("c9s_enabled")(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/ZbGoPZDBv5XtBDXAGDCJSQ/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweetId      | Future | t.tweetId  |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/XMRgjnjQHcysDNza9nNsaw/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/PPuIemauUaw6RBSn3D6crQ/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/f1aUxc3y7d0Yij4Lua1G6A/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ...()(0,w.S) | Future | _             |

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
| communityId | Future | n.communityId |
| userId      | Future | n.userId      |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/Xes3AZRC6u_BFX-PXEubeA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...t         | Future | _          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/ZisEomXBhpw7ChFL94YUTA/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| name         | Future | t.name        |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/VNhZH-ZvJtmeGjcswYwWBw/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| description  | Future | t.purpose     |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/pmVRkaO_ZFB2WNUUrQpCWw/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| theme        | Future | t.theme       |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/g-O0_-icMSObaQr30HPz3g/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ruleId       | Future | t.ruleId      |
| name         | Future | t.name        |
| description  | Future | t.description |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/kQ8ho2sItJgyh_f9q_h0Aw/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| name         | Future | t.name        |
| description  | Future | t.description |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/lBpBFpy7p-Szg35lTZvOpA/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ruleId       | Future | t.ruleId      |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/SZG-l_czgL_bxPtojHnqiA/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ruleIds      | Future | t.ruleIds     |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/ti6XJRdfObJMlbHrBImLTg/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| mediaId      | Future | t.mediaId     |
| ...()(0,w.S) | Future | _             |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/fIt_0icLCp5mj5S0T7DnLw/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | t.communityId |
| ...()(0,w.S) | Future | _             |

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
| toolId | Future | t          |

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
| toolId | Future | t          |

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
| toolId | Future | t          |

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
Request URL: `https://twitter.com/i/api/graphql/6lWNh96EXDJCXl05SAtn_g/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                                        | type   | variable                              |
|:-----------------------------------------------------------|:-------|:--------------------------------------|
| focalTweetId                                               | Future | a                                     |
| cursor                                                     | Future | d                                     |
| referrer                                                   | Future | o                                     |
| controller_data                                            | Future | t                                     |
| rux_context                                                | Future | l                                     |
| with_rux_injections                                        | Future | i                                     |
| includePromotedContent                                     | Future | True                                  |
| withCommunity                                              | Future | n.isTrue()                            |
| withQuickPromoteEligibilityTweetFields                     | Future | True                                  |
| withBirdwatchNotes                                         | Future | n.isTrue("c9s_enabled")               |
| ...("responsive_web_birdwatch_consumption_enabled")(0,w.d) | Future | _                                     |
| withVoice                                                  | Future | n.isTrue(n)                           |
| withV2Timeline                                             | Future | n.isTrue("voice_consumption_enabled") |
| isReaderMode                                               | Future | r                                     |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| ...n  | Future | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/_vfykx0gciwejfyzQyd9Ag/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                                                                                                             |
|:--------------------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| count                           | Future | null==t?void 0:t.count                                                                                                                                                               |
| query                           | Future | t.query                                                                                                                                                                              |
| withAttachments                 | Future | n.isTrue()&&n.isTrue("dm_inbox_search_message_attachment_previews_enabled")&&n.isTrue("dm_inbox_search_message_results_enabled")                                                     |
| withConversationQueryHighlights | Future | n.isTrue("direct_messages_incremental_holdback_2022h1")&&n.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled")                                                 |
| withMessageQueryHighlights      | Future | n.isTrue("direct_messages_incremental_holdback_2022h1")&&n.isTrue("dm_inbox_search_query_highlighting_message_results_enabled")&&n.isTrue("dm_inbox_search_message_results_enabled") |
| withMessages                    | Future | n.isTrue("direct_messages_incremental_holdback_2022h1")&&n.isTrue("dm_inbox_search_message_results_enabled")                                                                         |
| withSafetyModeUserFields        | Future | n.isTrue("direct_messages_incremental_holdback_2022h1")                                                                                                                              |
| withSuperFollowsUserFields      | Future | n.isTrue("rito_safety_mode_blocked_profile_enabled")                                                                                                                                 |

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
| ...t                            | Future | _                                                                                       |
| withConversationQueryHighlights | Future | n.isTrue()&&n.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

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
| ...t                            | Future | _                                                                                       |
| withConversationQueryHighlights | Future | n.isTrue()&&n.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/iOmsg5RhylE_TGjw-RHMKg/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| draft_tweet_id | Future | t          |

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
| draft_tweet_id     | Future | t          |
| post_tweet_request | Future | lr()       |

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
| ...t  | Future | _          |
| ...n  | Future | _          |

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
| post_tweet_request | Future | lr()       |

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
| userId   | Future | d          |
| settings | Future | t          |

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
Request URL: `https://twitter.com/i/api/graphql/ggw0DFpYRNeR2pmEQ3r3GQ/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                |
|:-------------|:-------|:------------------------|
| count        | Future | null==t?void 0:t.count  |
| cursor       | Future | null==t?void 0:t.cursor |
| ...()(0,w.d) | Future | _                       |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/5hFzRHD3y8LtZu8GpkI30A/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable                         |
|:----------------|:-------|:---------------------------------|
| pinned_tweet_id | Future | null==t?void 0:t.pinned_tweet_id |
| page_name       | Future | null==t?void 0:t.page_name       |
| ...()(0,w.d)    | Future | _                                |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/6AB4F2ntV7x0Oad-FvRHbw/Followers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| userId                 | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/y4amXqI3qOlqCmxLhv-G9w/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| userId                 | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/n1HqDGhrfjoOv2VUOtjbtg/Following`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| userId                 | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/K6cyVdGKIS5rhCxZJnZUcQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/B16oZCHYM_mneeUxcXV7TA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| rootTweetId            | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/hffn3Qz90fD_Txm3GaCqDA/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/PtCwMEeOe2Em1Mtvim32jQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable   |
|:---------------------------------------|:-------|:-----------|
| timelineId                             | Future | a          |
| count                                  | Future | t          |
| cursor                                 | Future | d          |
| withQuickPromoteEligibilityTweetFields | Future | True       |
| ...()(0,w.d)                           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
Request URL: `https://twitter.com/i/api/graphql/JEdqM-soumaq1QH8qoLWYA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | a          |
| userId       | Future | r          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/8WmfiEcyX_PZPgcbTAigbA/CreateList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| isPrivate    | Future | private===r.toLowerCase() |
| name         | Future | o                         |
| description  | Future | a                         |
| ...()(0,w.S) | Future | _                         |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/rTDrkKvKYd8ipKCYs8Nx1A/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | a          |
| mediaId      | Future | r          |
| ...()(0,w.S) | Future | _          |

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
| listId | Future | d          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/6uODT6Psdb46LorXqHVUtQ/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | a          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/-RN8LbOq_33uKwZ-ODFUAA/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| screenName   | Future | d          |
| listSlug     | Future | a          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/aJY9qPNhvwMBE3AQuVMuoA/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | t.list_id  |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/v8S-c_QbR2S3O-zCIRAl7w/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| listId                   | Future | o           |
| count                    | Future | a           |
| cursor                   | Future | r           |
| ...()(0,w.d)             | Future | _           |
| withSafetyModeUserFields | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/tXeBUhmSO7TbNdieskzmWA/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | o          |
| count        | Future | a          |
| cursor       | Future | r          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/Tf-yKHvRC_LX-ckBawLuog/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | Future | l          |
| isListMemberTargetUserId | Future | o          |
| count                    | Future | a          |
| cursor                   | Future | r          |
| ...()(0,w.d)             | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/ehLICs2w16MNIYbWIW3hRQ/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | o          |
| count        | Future | a          |
| cursor       | Future | r          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/p8usjxnSYIFXEJXWAFAiLA/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | a          |
| userId       | Future | r          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/BDwbCk3arXsnkPxcG9uImA/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | a          |
| ...r   | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://twitter.com/i/api/graphql/ScLNPIgax0cf-A9NeB3tAw/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | a          |
| ...r   | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://twitter.com/i/api/graphql/16ErGbUQRBempTsOFRhmxA/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listIds      | Future | d          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/b0A9GUlGZuhOtau-ZqZ-cg/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | a          |
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/NGRv0RHZvA15KsDb-ZC6aA/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | a          |
| ...()(0,w.S) | Future | _          |

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
| listId | Future | d          |

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
| listId | Future | d          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/rp2ASdW_g98DDB3dmb-81A/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| listId       | Future | r                         |
| isPrivate    | Future | private===o.toLowerCase() |
| description  | Future | a                         |
| name         | Future | l                         |
| ...()(0,w.S) | Future | _                         |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/NpvWu0QrCoxt11Kc2FQG7Q/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | a          |
| count        | Future | t          |
| cursor       | Future | d          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/jvjy6oomkvbvNRLu-ZJp7w/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | t          |
| cursor       | Future | d          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://twitter.com/i/api/graphql/_6GxHNTU27FScIEI_mvD-w/ListPins`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,w.S) | Future | _          |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/9B_nNbmFNpgVc43883rWrg/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | t          |
| cursor       | Future | d          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/5yUN5-dO-oTZSl0h9KyHbA/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| rest_id                | Future | a          |
| count                  | Future | t          |
| cursor                 | Future | d          |
| includePromotedContent | Future | False      |
| ...()(0,w.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://twitter.com/i/api/graphql/sj-BEQ0Jq5AwrydqFstdvg/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable                              |
|:---------------------------------------|:-------|:--------------------------------------|
| userId                                 | Future | a                                     |
| count                                  | Future | t                                     |
| cursor                                 | Future | d                                     |
| includePromotedContent                 | Future | True                                  |
| withQuickPromoteEligibilityTweetFields | Future | True                                  |
| ...()(0,w.d)                           | Future | _                                     |
| withVoice                              | Future | n.isTrue(n)                           |
| withV2Timeline                         | Future | n.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://twitter.com/i/api/graphql/8kng9osBW4CYEw-hlGGHeQ/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable                              |
|:--------------------------|:-------|:--------------------------------------|
| userId                    | Future | a                                     |
| count                     | Future | t                                     |
| cursor                    | Future | d                                     |
| includePromotedContent    | Future | True                                  |
| withCommunity             | Future | n.isTrue()                            |
| ...("c9s_enabled")(0,w.d) | Future | _                                     |
| withVoice                 | Future | n.isTrue(n)                           |
| withV2Timeline            | Future | n.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserSuperFollowTweets<br>
Request URL: `https://twitter.com/i/api/graphql/Yu9jVDqmyaqJjyD-1l_FOg/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable    |
|:-----------------------|:-------|:------------|
| userId                 | Future | a           |
| count                  | Future | t           |
| cursor                 | Future | d           |
| includePromotedContent | Future | True        |
| ...()(0,w.d)           | Future | _           |
| withVoice              | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://twitter.com/i/api/graphql/4qbGcQEBF731A4580bEzzw/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"d","count":"n","cursor":"string"==typeof t?t:"void 0","includePromotedContent":"!1","withDownvotePerspective":"!1","withReactionsMetadata":"!1","withReactionsPerspective":"!1","withSuperFollowsTweetFields":"!1","withSuperFollowsUserFields":"!1","withVoice":"!1"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://twitter.com/i/api/graphql/p3ELQstq2ZEbEID4yu9R1A/Likes`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable                              |
|:-----------------------|:-------|:--------------------------------------|
| userId                 | Future | a                                     |
| count                  | Future | t                                     |
| cursor                 | Future | d                                     |
| includePromotedContent | Future | False                                 |
| ...()(0,w.d)           | Future | _                                     |
| withClientEventToken   | Future | False                                 |
| withBirdwatchNotes     | Future | False                                 |
| withVoice              | Future | n.isTrue(n)                           |
| withV2Timeline         | Future | n.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://twitter.com/i/api/graphql/LsL6YcDRR1EWy6Ojp9zeMA/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable                              |
|:-----------------------|:-------|:--------------------------------------|
| userId                 | Future | a                                     |
| count                  | Future | t                                     |
| cursor                 | Future | d                                     |
| includePromotedContent | Future | False                                 |
| ...()(0,w.d)           | Future | _                                     |
| withClientEventToken   | Future | False                                 |
| withBirdwatchNotes     | Future | False                                 |
| withVoice              | Future | n.isTrue(n)                           |
| withV2Timeline         | Future | n.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/6n6AxbUdJbcq_pXMLCHUMw/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable    |
|:-----------------------|:-------|:------------|
| userId                 | Future | r           |
| count                  | Future | t           |
| cursor                 | Future | d           |
| teamName               | Future | a           |
| includePromotedContent | Future | False       |
| ...()(0,w.d)           | Future | _           |
| withClientEventToken   | Future | False       |
| withVoice              | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## RitoActionedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/NILd6PjeSql80d9YgLvJeQ/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | t           |
| rest_id                  | Future | d           |
| ...()(0,w.d)             | Future | _           |
| withSafetyModeUserFields | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| userId | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Ave1sXtEXo3lUgle9ueWbQ/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | t           |
| ...()(0,w.d)             | Future | _           |
| withSafetyModeUserFields | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/DaeRLM2KuS6eXCgt_8lOpg/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | t           |
| rest_id                  | Future | d           |
| ...()(0,w.d)             | Future | _           |
| withSafetyModeUserFields | Future | n.isTrue(n) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| ...n  | Future | _          |

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
| post_tweet_request | Future | a          |
| execute_at         | Future | Qi()       |

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
| ...t  | Future | _          |
| ...n  | Future | _          |

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
| scheduled_tweet_id | Future | d          |
| post_tweet_request | Future | r          |
| execute_at         | Future | Qi()       |

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
| promptType | Future | t          |

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
| displayPreference | Future | t          |

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
| device_id | Future | n          |

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
| dataSaverEnabled | Future | n          |
| deviceId         | Future | t          |
| videoAutoplay    | Future | d          |

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
| userId            | Future | t          |
| dmNsfwMediaFilter | Future | n          |

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
| userId                                       | Future | t          |
| sharingAudiospacesListeningDataWithFollowers | Future | n          |

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
| userId   | Future | t                 |
| enabled  | Future | none!==n          |
| duration | Future | none===n?void 0:n |

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
Request URL: `https://twitter.com/i/api/graphql/rvC1orOh3vabuEq3gEQD4w/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...t                | Future | _          |
| ...()(0,w.d)        | Future | _          |
| articleListSeedType | Future | d          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/_S2Cdk40cEGNF0J13dBj9Q/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...t                | Future | _          |
| ...()(0,w.d)        | Future | _          |
| articleListSeedType | Future | d          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://twitter.com/i/api/graphql/MF-Q9nIwLizOEIHAyL9ktw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"a","context":"JSON.stringify()"{"data_lookup_id":"r"}"0","w.dn"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://twitter.com/i/api/graphql/RS509hY2TKqxxT0acAH1DQ/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | Future | a          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| topicId | Future | d          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://twitter.com/i/api/graphql/PFaDAYTT6b_sV4Sgk3HlCQ/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | Future | a          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://twitter.com/i/api/graphql/6K-Pg6znrfQk3aVKekW3zQ/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/_nXjsDh65E9ZKav6L8Y7hA/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | o          |
| cursor       | Future | r          |
| context      | Future | a          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://twitter.com/i/api/graphql/-wt00yzvTYhGFkegc9mA9w/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | Future | r          |
| cursor       | Future | a          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| topicId | Future | d          |

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
| topicId | Future | d          |

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
| topicId | Future | d          |

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
| topicId | Future | d          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://twitter.com/i/api/graphql/cyeptFGCY-6SLbFtQ1Btmg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | a          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| rest_id | Future | n          |

#### features<br>
| key                                             | type    | default   |
|:------------------------------------------------|:--------|:----------|
| profile_foundations_tweet_stats_enabled         | boolean | False     |
| profile_foundations_tweet_stats_tweet_frequency | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticleByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/YyD5ButWvOHuvJAIXdxIlg/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | d          |
| ...()(0,w.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://twitter.com/i/api/graphql/QTJkWgKoGgOtx1GE6iGI-w/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                    |
|:-------------|:-------|:----------------------------|
| data         | Future | {'content_state_json': 'd'} |
| ...()(0,w.d) | Future | _                           |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

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
| twitterArticleId | Future | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://twitter.com/i/api/graphql/jzp4Yxr1zsbH23Da-2WIoA/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | a          |
| mediaId          | Future | d          |
| ...()(0,w.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://twitter.com/i/api/graphql/G4hVzDpei5XcLvCaahWQaw/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable                                                         |
|:-----------------|:-------|:-----------------------------------------------------------------|
| twitterArticleId | Future | r                                                                |
| data             | Future | {'content_state_json': 'd', 'plaintext': 'a', 'word_count': 'o'} |
| ...()(0,w.d)     | Future | _                                                                |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://twitter.com/i/api/graphql/H3OhLGsJ6NL22mBf0KMV-w/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | a          |
| mediaKeys        | Future | d          |
| ...()(0,w.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/Mx3m40paC1ilutSbysOIEw/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | a          |
| title            | Future | d          |
| ...()(0,w.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://twitter.com/i/api/graphql/J_dNIothGTmzBXn_24DTVg/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | d          |
| visibility       | Future | a          |
| ...()(0,w.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/sXpjgTSGH-aYZqAHGrZuXQ/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...t         | Future | _          |
| ...()(0,w.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False     |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True      |
| verified_phone_label_enabled                                            | boolean | True      |
| longform_notetweets_consumption_enabled                                 | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| tweetypie_unmention_optimization_enabled                                | boolean | False     |
| vibe_api_enabled                                                        | boolean | True      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | False     |
| view_counts_everywhere_api_enabled                                      | boolean | False     |
| standardized_nudges_misinfo                                             | boolean | False     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_enhance_cards_enabled                                    | boolean | False     |

#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/_vUIWq3vpyL0amiNTjrM-w/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable           |
|:-----------------|:-------|:-------------------|
| trustedFriendsId | Future | n.trustedFriendsId |
| prefix           | Future | n.prefix           |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

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
| communityId | Future | n.communityId |
| prefix      | Future | n.prefix      |

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
| communityId | Future | n.communityId |
| prefix      | Future | n.prefix      |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |

#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/E1y4CwfVcatdt8uaixkB0g/Viewer`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                   |
|:---------------------------|:-------|:-------------------------------------------|
| withCommunitiesMemberships | Future | n.isTrue()                                 |
| withCommunitiesCreation    | Future | n.isTrue("c9s_enabled")                    |
| withSuperFollowsUserFields | Future | n.isTrue("c9s_community_creation_enabled") |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/hVhfo_TquFTmgL7gYwf91Q/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| screen_name                | Future | t                                                    |
| withSafetyModeUserFields   | Future | n.isTrue()                                           |
| withSuperFollowsUserFields | Future | n.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/mi_IjXgFyr41N9zkszPz9w/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | Future | t                                                    |
| withSafetyModeUserFields   | Future | n.isTrue()                                           |
| withSuperFollowsUserFields | Future | n.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                   | type    | default   |
|:------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True      |
| verified_phone_label_enabled                          | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | False     |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/vcl5Tp6rs_SV-to6g4_IAQ/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable      |
|:---------------------------|:-------|:--------------|
| userIds                    | Future | t.split()     |
| withSuperFollowsUserFields | Future | n.isTrue(",") |

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
| target_user_id | Future | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAliasSelfSelectOptions<br>
Request URL: `https://twitter.com/i/api/graphql/szoXMke8AZOErso908iglw/BirdwatchFetchAliasSelfSelectOptions`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
