# Twitter Unofficial GraphQL API Document<br>
This document is entirely auto-generated and may contain errors.<br>
## Usage<br>
If the parameter is an array type, it is encoded in json format.<br>
Body example:<br>
```Python
json.dumps({
    "queryId": "XyvN0Wv13eeu_gVIHDi10g",
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
Request URL: `https://twitter.com/i/api/graphql/gMM94mZD6vm7pgAmurx0gQ/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"id":"n","isMetatagsQuery":"a",...(0,r.d)(t),"withReplays":t.isTrue("voice_rooms_replay_consumption")}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| spaces_2022_h2_clipping                                                 | boolean | Future     |
| spaces_2022_h2_spaces_communities                                       | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## SubscribeToScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/HGmy5MWoSC4fCXAAvroOuw/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"tweetId":"o","includePromotedContent":"!0","withBirdwatchNotes":t.isTrue("responsive_web_birdwatch_consumption_enabled"),"withVoice":t.isTrue("voice_consumption_enabled"),"withCommunity":t.isTrue("c9s_enabled"),...(0,c.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## FavoriteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnfavoriteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTweetDownvote<br>
Request URL: `https://twitter.com/i/api/graphql/Eo65jl-gww30avDgrXvhUA/CreateTweetDownvote`<br>
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweetReaction<br>
Request URL: `https://twitter.com/i/api/graphql/GKwK0Rj4EdkfwdHQMZTpuw/DeleteTweetReaction`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable   |
|:----------------|:-------|:-----------|
| source_tweet_id | Future | r          |
| comparison_id   | Future | t          |
| dark_request    | Future | !0         |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key             | type   | variable   |
|:----------------|:-------|:-----------|
| source_tweet_id | Future | r          |
| dark_request    | Future | !1         |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateBookmark<br>
Request URL: `https://twitter.com/i/api/graphql/aoDbu3RHznuiSkQ9aNM67Q/CreateBookmark`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | r          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmark<br>
Request URL: `https://twitter.com/i/api/graphql/Wlmlj2-xzyS1GN3a6cj-mQ/DeleteBookmark`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | Future | r          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ModerateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/pjFnHGVqCjTcZol0xcBJjw/ModerateTweet`<br>
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/kV0jgNRI3ofhHK_G5yhlZg/CreateTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{...r,"dark_request":!!n.preview,...(null==l||null==(m=l.engagement_request)?void 0:m.impression_id)&&{...l},...(0,c.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## CreateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/kV0jgNRI3ofhHK_G5yhlZg/CreateTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{...a,"comparison_id":"s","dark_request":"!0",...(null==l||null==(h=l.engagement_request)?void 0:h.impression_id)&&{...l},...(0,c.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## DeleteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| tweet_id     | Future | s          |
| dark_request | Future | !1         |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConversationControlChange<br>
Request URL: `https://twitter.com/i/api/graphql/hb1elGcj6769uT8qVYqtjw/ConversationControlChange`<br>
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/ooxuguX0iqkLVf_r_WcDxA/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"tweetText":o.status}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled               | boolean | Future     |
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/JpO-6lRdee6mTVyWDz-RMw/GetTweetReactionTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"tweetId":"n","withSuperFollowsUserFields":t.isTrue("super_follow_user_api_enabled")}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

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
Request URL: `https://twitter.com/i/api/graphql/Cj2A9yMXkeYJiyYcIcivTw/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"tweet_id":"i",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## BirdwatchProfileAcknowledgeEarnOut<br>
Request URL: `https://twitter.com/i/api/graphql/cED9wJy8Nd1kZCCYuIq9zQ/BirdwatchProfileAcknowledgeEarnOut`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BizProfileFetchUser<br>
Request URL: `https://twitter.com/i/api/graphql/Rp94IhO-2f4Gqi7MSwBquA/BizProfileFetchUser`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request Method: `GET`<br>
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
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PutClientEducationFlag<br>
Request URL: `https://twitter.com/i/api/graphql/IjQ-egg0uPkY11NyPMfRMQ/PutClientEducationFlag`<br>
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/TQt5GP8tbFNhUrO0apYflw/CreateCommunity`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"name":"a","description":"i","joinPolicy":"o","invitesPolicy":"r",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/sGjJIWaQyCSuAhU-5MHiAg/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{...n,"withCommunity":t.isTrue("c9s_enabled"),...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/TVCdwH7_j8KROXqjCtCLbg/CommunityEditName`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"communityId":n.communityId,"name":n.name,...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

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
## ContentControlToolDisable<br>
Request URL: `https://twitter.com/i/api/graphql/N6oDUH0bX-7w9Cj4Wd6zXA/ContentControlToolDisable`<br>
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
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/Nze3idtpjn4wcl09GpmDRg/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"focalTweetId":"r","cursor":"i","referrer":"a","controller_data":"n","rux_context":"s","with_rux_injections":"l","includePromotedContent":"!0","withCommunity":t.isTrue("c9s_enabled"),"withQuickPromoteEligibilityTweetFields":"!0","withBirdwatchNotes":t.isTrue("responsive_web_birdwatch_consumption_enabled"),...(0,g.d)(t),"withVoice":t.isTrue("voice_consumption_enabled"),"withV2Timeline":t.isTrue("graphql_timeline_v2_query_threaded_conversation_with_injections"),"isReaderMode":"o"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ConvertRitoSuggestedActions<br>
Request URL: `https://twitter.com/i/api/graphql/2njnYoE69O2jdUM7KMEnDw/ConvertRitoSuggestedActions`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/N7MUEpMnkYqhNzBwu1EJdg/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"count":null==n?void 0:n.count,"query":n.query,"withAttachments":t.isTrue("dm_inbox_search_message_attachment_previews_enabled")&&t.isTrue("dm_inbox_search_message_results_enabled")&&t.isTrue("direct_messages_incremental_holdback_2022h1"),"withConversationQueryHighlights":t.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled")&&t.isTrue("direct_messages_incremental_holdback_2022h1"),"withMessageQueryHighlights":t.isTrue("dm_inbox_search_query_highlighting_message_results_enabled")&&t.isTrue("dm_inbox_search_message_results_enabled")&&t.isTrue("direct_messages_incremental_holdback_2022h1"),"withMessages":t.isTrue("dm_inbox_search_message_results_enabled")&&t.isTrue("direct_messages_incremental_holdback_2022h1"),"withSafetyModeUserFields":t.isTrue("rito_safety_mode_blocked_profile_enabled"),"withSuperFollowsUserFields":t.isTrue("super_follow_user_api_enabled")}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## DeleteDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
Request Method: `GET`<br>
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
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteEmailNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/2qKKYFQift8p5-J1k6kqxQ/WriteEmailNotificationSettings`<br>
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/4Yqsud8dtxrdSooSFb3jlQ/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"count":null==n?void 0:n.count,"cursor":null==n?void 0:n.cursor,...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/p6oAap7drmgt2ViNbhB62Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"r","count":"n","cursor":"i","includePromotedContent":"!1",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

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
Request URL: `https://twitter.com/i/api/graphql/RKtQuzpcy2gym71UorWg6g/ListAddMember`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r","userId":"o",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/x5aSMDodNU02VT1VRyW48A/CreateList`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"isPrivate":"private"===o.toLowerCase(),"name":"a","description":"r",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/dXRBGISGFHWBkK0LdUYCEg/EditListBanner`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r","mediaId":"o",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## DeleteList<br>
Request URL: `https://twitter.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList`<br>
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/5hkpoz-sCeMQQSHqeE-gMg/DeleteListBanner`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/dX9RR-iwiXqxTPTUzzsjHA/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"screenName":"i","listSlug":"r",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/vxx-Y8zadpAP64HHiw4hMQ/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":n.list_id,...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/sXFXEmtFr3nLyG1dmS81jw/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"a","count":"r","cursor":"o",...(0,g.d)(t),"withSafetyModeUserFields":t.isTrue("rito_safety_mode_blocked_profile_enabled")}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/LxXoouvfd5E8PXsdrQ0iMg/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"a","count":"r","cursor":"o",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/6E69fsenLDPDcprqtogzdw/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"s","isListMemberTargetUserId":"a","count":"r","cursor":"o",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/t3VvMv98F3U12lZv4Qkgmw/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"a","count":"r","cursor":"o",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/mDlp1UvnnALC_EzybKAMtA/ListRemoveMember`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r","userId":"o",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/fieeOPSAOCgC7FUhX6DmbQ/ListUnpinOne`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r",...o}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://twitter.com/i/api/graphql/J-U5JsCVrEiMA7Auxo96VQ/ListsPinMany`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listIds":"i",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/nymTz5ek0FQPC3kh63Tp1w/ListSubscribe`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/Wi5-aG4bvTmdjyRyRGkyhA/ListUnsubscribe`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"r",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## MuteList<br>
Request URL: `https://twitter.com/i/api/graphql/ZYyanJsskNUcltu9bliMLA/MuteList`<br>
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/P9YDuvCt6ogRf-kyr5E5xw/UpdateList`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"listId":"o","isPrivate":"private"===a.toLowerCase(),"description":"r","name":"s",...(0,g.S)(t)}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/mLKOzzVOWUycBiExBT1gjg/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"r","count":"n","cursor":"i",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/-QhX8r1nIYFqaFOM0eYyJA/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"r","count":"n","cursor":"i","includePromotedContent":"!1",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## RevueAccountByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/NFARV9iE-FIK7FOsO_d23Q/RevueAccountByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RitoActionedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/10vAW5KbNX5Wvcgr2GF4uw/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"cursor":"n","rest_id":"i",...(0,g.d)(t),"withSafetyModeUserFields":t.isTrue("rito_safety_mode_blocked_profile_enabled")}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## DismissRitoSuggestedAction<br>
Request URL: `https://twitter.com/i/api/graphql/jYvwa61cv3NwNP24iUru6g/DismissRitoSuggestedAction`<br>
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/RR7bcThNWYW5zAsi_LPklA/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"cursor":"n",...(0,g.d)(t),"withSafetyModeUserFields":t.isTrue("rito_safety_mode_blocked_profile_enabled")}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/_8ut4NdEiUbgdKJW0WHJeQ/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"cursor":"n","rest_id":"i",...(0,g.d)(t),"withSafetyModeUserFields":t.isTrue("rito_safety_mode_blocked_profile_enabled")}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## RitoSuggestedActionsFacePile<br>
Request URL: `https://twitter.com/i/api/graphql/GnQKeEdL1LyeK3dTQCS1yw/RitoSuggestedActionsFacePile`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
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
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/J-8Z-4VM-Jr9dl8A6Y4-Dg/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{...n,...(0,g.d)(t),"articleListSeedType":"i"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/eKrwrU5eRBL_R9t5sFXfIg/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{...n,...(0,g.d)(t),"articleListSeedType":"i"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## TopicTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/h1sIF7iIZNOxfim4_cS9JA/TopicTimeline`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"a","cursor":"r","context":JSON.stringify({"data_lookup_id":"o"}),...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://twitter.com/i/api/graphql/irYg0qxSCU-z6XhwhM1z1w/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"a","cursor":"r","context":JSON.stringify({"data_lookup_id":"o"}),...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://twitter.com/i/api/graphql/i06ljnVzu-Wu5RU1a3MK8Q/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"cursor":"r",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

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
Request URL: `https://twitter.com/i/api/graphql/nr2qOBmky1AM5W4u083y8g/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"topicId":"r",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/_YOj3ANPbZuporTfoUxhFQ/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"a","cursor":"o","context":"r",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://twitter.com/i/api/graphql/KTAbu7SNxjuOQPp0MEsZgg/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"r",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

#### queryId<br>
`None`<br>
## TopicFollow<br>
Request URL: `https://twitter.com/i/api/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
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
## TopicUnfollow<br>
Request URL: `https://twitter.com/i/api/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
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
## TopicNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
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
## TopicUndoNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
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
## TopicToFollowSidebar<br>
Request URL: `https://twitter.com/i/api/graphql/1lTmlc6V0Bzlwu75DzTnyg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"r",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

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
| key                                             | type    | variable   |
|:------------------------------------------------|:--------|:-----------|
| profile_foundations_tweet_stats_enabled         | boolean | Future     |
| profile_foundations_tweet_stats_tweet_frequency | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/qJcDMzHIAriWE-t7lMetRA/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | n          |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://twitter.com/i/api/graphql/pb3IOdFOl-Tr36FSlcldXA/TwitterArticleCreate`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key   | type   | variable                    |
|:------|:-------|:----------------------------|
| data  | Future | {'content_state_json': 'n'} |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleDelete<br>
Request URL: `https://twitter.com/i/api/graphql/6st-stMDc7KBqLT8KvWhHg/TwitterArticleDelete`<br>
Request Method: `GET`<br>
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
Request URL: `https://twitter.com/i/api/graphql/kD_hIBypsu2FUqDnizClmw/TwitterArticleUpdateCoverImage`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| mediaId          | Future | n          |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://twitter.com/i/api/graphql/eRP6I7aZT9r_uL3ejAxi8A/TwitterArticleUpdateData`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable                                                         |
|:-----------------|:-------|:-----------------------------------------------------------------|
| twitterArticleId | Future | r                                                                |
| data             | Future | {'content_state_json': 'n', 'plaintext': 'i', 'word_count': 'o'} |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://twitter.com/i/api/graphql/5bi7E0dsbmudoLY9W98tSg/TwitterArticleUpdateMedia`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| mediaKeys        | Future | n          |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/_9O13lsQHMbCJt6fuw0nQQ/TwitterArticleUpdateTitle`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | i          |
| title            | Future | n          |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://twitter.com/i/api/graphql/MhXaPMhemLjRZA0xwnd4XA/TwitterArticleUpdateVisibility`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | Future | n          |
| visibility       | Future | i          |

#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/4lk-D0Y8kfimSyPJjEocsA/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/4jeP7HyKpQUitFUTWedrqA/Viewer`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"withCommunitiesMemberships":t.isTrue("c9s_enabled"),"withCommunitiesCreation":t.isTrue("c9s_community_creation_enabled"),"withSuperFollowsUserFields":t.isTrue("super_follow_user_api_enabled")}
```
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | Future     |

#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/qNZkBA9QShKetdS6WHdsgQ/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `Future`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"includePromotedContent":"!0",...(0,g.d)(t)}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | Future     |
| unified_cards_ad_metadata_container_dynamic_card_content_query_enabled  | boolean | Future     |
| dont_mention_me_view_api_enabled                                        | boolean | Future     |
| responsive_web_uc_gql_enabled                                           | boolean | Future     |
| vibe_api_enabled                                                        | boolean | Future     |
| responsive_web_edit_tweet_api_enabled                                   | boolean | Future     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | Future     |
| standardized_nudges_misinfo                                             | boolean | Future     |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | Future     |
| interactive_text_enabled                                                | boolean | Future     |
| responsive_web_text_conversations_enabled                               | boolean | Future     |
| responsive_web_enhance_cards_enabled                                    | boolean | Future     |

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
