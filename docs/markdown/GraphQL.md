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
Request URL: `https://twitter.com/i/api/graphql/KHhrAKFmw0Sgy2TdQBQ29A/AudioSpaceById`<br>
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
## TweetResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/iP-uFmcTSH-vW1kjsxT9cw/TweetResultByRestId`<br>
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
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/3oCAhKqrb4PRuVPH59ySGQ/CreateTweet`<br>
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
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CreateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/3oCAhKqrb4PRuVPH59ySGQ/CreateTweet`<br>
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
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/FBucz2MB41mLVzFAlhRyZQ/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| tweetText | Future | r          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_enhance_cards_enabled               | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/JAFiENABXsz6YVOd39qafA/GetTweetReactionTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable   |
|:---------------------------|:-------|:-----------|
| tweetId                    | Future | n          |
| withSuperFollowsUserFields | Future | t.isTrue() |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/1CGpRHyEDO2Z9Tkzh0Uw_w/Favoriters`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/TrvaKd-Mhr-5Fe-W344cpA/Retweeters`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/5jODBaGdZives7qe9w4pZA/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                                    | type   | variable   |
|:---------------------------------------|:-------|:-----------|
| tweetId                                | Future | n          |
| ...()(0,g.d)                           | Future | _          |
| withQuickPromoteEligibilityTweetFields | Future | True       |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |

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
| rest_id | Future | t          |

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
Request URL: `https://twitter.com/i/api/graphql/_-551vdsE782ujbAhHfWvA/UsersVerifiedAvatars`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| userIds | Future | r          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://twitter.com/i/api/graphql/fGXSeSM3jcKzBNmt3Gux4w/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | i          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
| note_id | Future | t.note_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchCreateNote<br>
Request URL: `https://twitter.com/i/api/graphql/b5mjd5JvWAIP8s0eAdE6jg/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | n.tweet_id |
| data_v1      | Future | n.data     |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
| note_id | Future | t.note_id  |

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
| note_id | Future | t.note_id  |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/j8KhVoKy_P9WUPxdeyPkdA/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| note_id      | Future | n.note_id  |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
| alias | Future | t.alias    |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/WIhArUGR-8NA41rXS6fBQQ/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | 10         |
| ...n         | Future | _          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
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
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/WIhArUGR-8NA41rXS6fBQQ/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | 10         |
| ...n         | Future | _          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
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
## BirdwatchFetchAuthenticatedUserProfile<br>
Request URL: `https://twitter.com/i/api/graphql/1AdvbF0AMpC5QNcy2OLeag/BirdwatchFetchAuthenticatedUserProfile`<br>
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
| alias | Future | t.alias    |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://twitter.com/i/api/graphql/kd54IHJj7owgVY1WqHXhXQ/BirdwatchFetchPublicData`<br>
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
Request URL: `https://twitter.com/i/api/graphql/8MGx7LQWtKQKko6nHZjg1A/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/GwCrnd2nHVWjZP0jxJkkeQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | True       |
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/5w1a7oaTjbPGuRgkiWDXjg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | True       |
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/sM3RbdmQu3Wi_U7-ZlbQJQ/CreateCommunity`<br>
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
| ...()(0,g.S)  | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/w7HcuxrkAGFx9hDTBOou6g/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/6aYkkJh2GAeSTqyy-jDV9A/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/q7mJCUqKtHEUEoPZaJryTg/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/-yDez-QWmOTlIuGIepAavA/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/sn1-3K1LQ8_68oq-LpJkCQ/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,g.S) | Future | _          |
| ...n         | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/FLBxynFsyzGqlI7Neo4cnw/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.S) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean | True      |
| responsive_web_uc_gql_enabled                                           | boolean | True      |
| vibe_api_enabled                                                        | boolean | False     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True      |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True      |
| standardized_nudges_misinfo                                             | boolean | True      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True      |
| interactive_text_enabled                                                | boolean | True      |
| responsive_web_text_conversations_enabled                               | boolean | True      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| responsive_web_enhance_cards_enabled                                    | boolean | True      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/W3x66cl7H6ibsNZCcSX8Ow/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key           | type   | variable   |
|:--------------|:-------|:-----------|
| ...n          | Future | _          |
| withCommunity | Future | True       |
| ...()(0,g.d)  | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/O80KX5fF_aMzZnvMxa4Q5Q/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | Future | _          |
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/zfXV0hjXUJB33iMRdyOWmg/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |
| ...n                      | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/iNTR8LE9ETP2akDpBuCAZA/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| withCommunity             | Future | t.isTrue() |
| ...("c9s_enabled")(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
## CommunityModerationData<br>
Request URL: `https://twitter.com/i/api/graphql/qBQVFGy1Lij5iFkWSCcfwg/CommunityModerationData`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/SfyhF_QIZqNAumj475duMQ/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweetId      | Future | n.tweetId  |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/4M03kncpY8jm8pd3cj9sBA/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/D-nkU334NeSQln6afk_dxQ/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/ed3WWHhSLcUGhmgXzpF4aQ/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://twitter.com/i/api/graphql/TyBoUatRGhYWhUMPpC0IpA/CommunityUserInvite`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |
| userId      | Future | t.userId      |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/uUebGFZj8ZqEYUrdsTNhGA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...n         | Future | _          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/o9Xz-HGzPOULYydbnvE70g/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| name         | Future | n.name        |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/A1JlIq7qwu4ksU9aoDmpWA/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| description  | Future | n.purpose     |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/VZXTObS3bTMJNS8zSJowBQ/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| theme        | Future | n.theme       |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/oCMSvDKqNc7jwBR6lHICVQ/CommunityEditRule`<br>
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
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/0DbHvt6fN9M87vWsCYlL1Q/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| name         | Future | n.name        |
| description  | Future | n.description |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/H-Ydlr1pgUJiQY2n6ReI4g/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ruleId       | Future | n.ruleId      |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/Eik_acj-TY0rRGqnIL5F2w/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ruleIds      | Future | n.ruleIds     |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/NVzGOARxRUwiUGYvO76GdA/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| mediaId      | Future | n.mediaId     |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/eWmnow_05C5xLcTXSXJ-_w/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | Future | n.communityId |
| ...()(0,g.S) | Future | _             |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ContentControlToolFetchOne<br>
Request URL: `https://twitter.com/i/api/graphql/1SWzL143l7Q5qyZxfCwyWQ/ContentControlToolFetchOne`<br>
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
Request URL: `https://twitter.com/i/api/graphql/R81Cy35-Qp6oXuFxHo5Jlw/ContentControlToolFetchAll`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolFetchAllUserEnabled<br>
Request URL: `https://twitter.com/i/api/graphql/7drRDTt2JpU5eIuYi4JZig/ContentControlToolFetchAllUserEnabled`<br>
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
Request URL: `https://twitter.com/i/api/graphql/WpsPNC5QMhwzpczwbXfZJQ/TweetDetail`<br>
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
| ...("responsive_web_birdwatch_consumption_enabled")(0,g.d) | Future | _                                     |
| withVoice                                                  | Future | t.isTrue(t)                           |
| withV2Timeline                                             | Future | t.isTrue("voice_consumption_enabled") |
| isReaderMode                                               | Future | a                                     |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/IuNGv6WuEzSU0poCl6BH4A/DmAllSearchSlice`<br>
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
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
Request URL: `https://twitter.com/i/api/graphql/ctiotiMWm6Ed9UCiuimv7w/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
| post_tweet_request | Future | Mr()       |

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
| post_tweet_request | Future | Mr()       |

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
Request URL: `https://twitter.com/i/api/graphql/s-QrKIS9y07FB7ikHH6bmg/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                |
|:-------------|:-------|:------------------------|
| count        | Future | null==n?void 0:n.count  |
| cursor       | Future | null==n?void 0:n.cursor |
| ...()(0,g.d) | Future | _                       |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/RHm5L-77wfxKosi2B8hUAg/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable                         |
|:----------------|:-------|:---------------------------------|
| pinned_tweet_id | Future | null==n?void 0:n.pinned_tweet_id |
| page_name       | Future | null==n?void 0:n.page_name       |
| ...()(0,g.d)    | Future | _                                |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/88KouZmVV1TF3cpIZ2WzzA/Followers`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/VITz8quB-NnimxK_Goiyfw/FollowersYouKnow`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/Ge7x4NGuwJMAmHrKNtbawg/Following`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/AArNPw5lZyWQM_rmihhyVg/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/NvMErGXkZpqkAmQq0VGghQ/ModeratedTimeline`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/WObNCspIiGSq6PlWcHbhdQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| count                  | Future | n          |
| cursor                 | Future | i          |
| includePromotedContent | Future | False      |
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/uewep_tguLCBubuXZ8K9hQ/GenericTimelineById`<br>
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
| ...()(0,g.d)                           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/2AlTjyrPhFvb4s8cjmSEgA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| userId       | Future | a          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/eDiODdYxe1WEp4RbOandQA/CreateList`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| isPrivate    | Future | private===a.toLowerCase() |
| name         | Future | o                         |
| description  | Future | r                         |
| ...()(0,g.S) | Future | _                         |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/0gdIfoGytXyZuueV_Xx4rQ/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| mediaId      | Future | a          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
Request URL: `https://twitter.com/i/api/graphql/as9jIONTUVWFown9CsnoGQ/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/W7QX3vPtN5h9NDBh71WKzQ/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| screenName   | Future | i          |
| listSlug     | Future | r          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/S46EqK-mxgYYG_YFZlWj_w/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | n.list_id  |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/xrTqZgSLAh_-OY4tc-JLSw/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| listId                   | Future | o           |
| count                    | Future | r           |
| cursor                   | Future | a           |
| ...()(0,g.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/7-7Csk9E7sMRFWdpKUR3pA/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | o          |
| count        | Future | r          |
| cursor       | Future | a          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/JGkAIj-W0feglVaB7uBULw/ListOwnerships`<br>
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
| ...()(0,g.d)             | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/-ZKchvAtTabUlTPfh-AiNg/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | o          |
| count        | Future | r          |
| cursor       | Future | a          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/5u1B3MD68WwN6PE4bzpEyg/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| userId       | Future | a          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/7dd3QdFwCwPkjiKPcS4Qsg/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | r          |
| ...a   | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://twitter.com/i/api/graphql/GCnbz5VC661IG9appoS-2A/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | Future | r          |
| ...a   | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://twitter.com/i/api/graphql/e4Hcx59BZNGllWmXUsm85w/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listIds      | Future | i          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/B0xR3Q1xbm6bTNbNxuvJCg/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/t1XJuAOuGyAc3q5KCn9MhA/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | Future | r          |
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
Request URL: `https://twitter.com/i/api/graphql/AiOHLJvkMGl3muUaukvDqQ/UpdateList`<br>
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
| ...()(0,g.S) | Future | _                         |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/LWWoWtEsfB8_IkEoVl5zvQ/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | r          |
| count        | Future | n          |
| cursor       | Future | i          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/uX3HJkRBqNMu2vnJYRRh6g/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | n          |
| cursor       | Future | i          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/2TFmnToh9ZL0wowx_F_C3w/ListPins`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,g.S) | Future | _          |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/CVg63Z2cfuu7kEIF-YUWlw/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | n          |
| cursor       | Future | i          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/Rr4V1CFTK70s1j9Ae4Vb6A/UserAboutTimeline`<br>
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
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/YYrLjMmB9csfOiIt45jmzA/UserTweets`<br>
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
| ...()(0,g.d)                           | Future | _                                     |
| withVoice                              | Future | t.isTrue(t)                           |
| withV2Timeline                         | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/VFlv-Qzdjdl_d9cedjgfTw/UserTweetsAndReplies`<br>
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
| ...("c9s_enabled")(0,g.d) | Future | _                                     |
| withVoice                 | Future | t.isTrue(t)                           |
| withV2Timeline            | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/TWrB56gWN8kwYe4EZNNMgg/UserSuperFollowTweets`<br>
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
| ...()(0,g.d)           | Future | _           |
| withVoice              | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/dwNOm6TDj1f4oZ1rN3COgA/UserPromotableTweets`<br>
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
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/Iwc62s0EdM1tiAJBfvLHjw/Likes`<br>
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
| ...()(0,g.d)           | Future | _                                     |
| withClientEventToken   | Future | False                                 |
| withBirdwatchNotes     | Future | False                                 |
| withVoice              | Future | t.isTrue(t)                           |
| withV2Timeline         | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/FC1uXW_W-XgDuboJDRbDVA/UserMedia`<br>
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
| ...()(0,g.d)           | Future | _                                     |
| withClientEventToken   | Future | False                                 |
| withBirdwatchNotes     | Future | False                                 |
| withVoice              | Future | t.isTrue(t)                           |
| withV2Timeline         | Future | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/kpSGG5cbfhyiKWzaOYqOvg/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | n           |
| rest_id                  | Future | i           |
| ...()(0,g.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/CoalEccBaZVH7wvKQllLmQ/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | n           |
| ...()(0,g.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/AhHLWrc9C4whX3Erne1RfQ/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | Future | n           |
| rest_id                  | Future | i           |
| ...()(0,g.d)             | Future | _           |
| withSafetyModeUserFields | Future | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
| execute_at         | Future | vl()       |

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
| execute_at         | Future | vl()       |

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
Request URL: `https://twitter.com/i/api/graphql/CBlcR-buFR0PDip451IziA/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...n                | Future | _          |
| ...()(0,g.d)        | Future | _          |
| articleListSeedType | Future | i          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/HTdiqmDQqyPIRq0AlxLoVg/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...n                | Future | _          |
| ...()(0,g.d)        | Future | _          |
| articleListSeedType | Future | i          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/_Q8Skqtz7_0BBK6uZU8NSQ/TopicTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"r","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","g.dt"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/hELJfwasvppzCbeuUdM4MA/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"r","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","g.dt"}
```
#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/DM_ypcCTegNNE9Ry84vujw/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | Future | r          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/XkFHJ6UTpPXk2_K_HYHBKA/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | Future | r          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/9_LOE06A3RqftB-rZBIcpQ/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/xwHGeABJgpQobrcwzURzWg/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | o          |
| cursor       | Future | a          |
| context      | Future | r          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/JWkwz62uv6BMw5VtvoEuTA/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | Future | a          |
| cursor       | Future | r          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/vJ-WRR9EDSmcYbIm9YAkYw/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | Future | r          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/x6Rsdjciu3g-tAwfpJHDHQ/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| ...()(0,g.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/zESxEKSg0mLPxagXSXeVSA/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                    |
|:-------------|:-------|:----------------------------|
| data         | Future | {'content_state_json': 'i'} |
| ...()(0,g.d) | Future | _                           |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/x2pd4d9pe2pgqiJB7VGl6Q/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | r          |
| mediaId          | Future | i          |
| ...()(0,g.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/S1HtBaeZjcpF3TI8PrtKMA/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable                                                         |
|:-----------------|:-------|:-----------------------------------------------------------------|
| twitterArticleId | Future | a                                                                |
| data             | Future | {'content_state_json': 'i', 'plaintext': 'r', 'word_count': 'o'} |
| ...()(0,g.d)     | Future | _                                                                |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/C1S2QxYE-jbucZRn0Rosdg/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | r          |
| mediaKeys        | Future | i          |
| ...()(0,g.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/0lwr7IRUcpp1Q0-ceQiFEg/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | r          |
| title            | Future | i          |
| ...()(0,g.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/B-m23LvdlrXs5igNRuCLBw/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| visibility       | Future | r          |
| ...()(0,g.d)     | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/hXVJpFNna_1hCdZN6y7VUQ/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...n         | Future | _          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/4lk-D0Y8kfimSyPJjEocsA/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable           |
|:-----------------|:-------|:-------------------|
| trustedFriendsId | Future | t.trustedFriendsId |
| prefix           | Future | t.prefix           |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityUserRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/mHD64WE922Oa5EmHCgwOcg/CommunityUserRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |
| prefix      | Future | t.prefix      |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/EaCbT1bOCOFxrDbDapS-Dw/CommunityMemberRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | Future | t.communityId |
| prefix      | Future | t.prefix      |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/kJET8dNfqVkzserU4dWV6w/Viewer`<br>
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
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/YQP-xivhhgmh7pPlV2lQlg/UserByScreenName`<br>
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
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/F1t5FjrLwN4XsIC4WeKHMA/UserByRestId`<br>
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
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/sAHTL2Dur9kUJGSXMrBi8Q/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable      |
|:---------------------------|:-------|:--------------|
| userIds                    | Future | n.split()     |
| withSuperFollowsUserFields | Future | t.isTrue(",") |

#### features<br>
| key                                                | type    | default   |
|:---------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | False     |

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
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/s_nDeNKj7t9Mv7qsEne1Dg/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| includePromotedContent | Future | True       |
| ...()(0,g.d)           | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
Request URL: `https://twitter.com/i/api/graphql/IXs46sQX16fiQvWuDAl8GA/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | Future | i          |
| cursor       | Future | r          |
| context      | Future | n          |
| ...()(0,g.d) | Future | _          |

#### features<br>
| key                                                                     | type    | default   |
|:------------------------------------------------------------------------|:--------|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | False     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | True      |
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
