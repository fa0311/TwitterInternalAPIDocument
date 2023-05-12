# Twitter Internal GraphQL API Document<br>
This document is entirely auto-generated and may contain errors.<br>
Please do not take what is written for granted, especially since static analysis of `variables` is very difficult. Most likely it is wrong.<br>
## Usage<br>
If the parameter is an array type, encode it in json format.<br>
Body example:<br>
```Python
json.dumps({
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
    })
```
`json.dumps` is equivalent to `JSON.stringify` in javaScript<br>
## BakeryQuery<br>
Request URL: `https://twitter.com/i/api/graphql/pROR-yRiBVsEjJyHt3fvhg/BakeryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CheckTweetForNudge<br>
Request URL: `https://twitter.com/i/api/graphql/C2dcvh7H69JALtomErxWlA/CheckTweetForNudge`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                          | type    | variable   |
|:-----------------------------|:--------|:-----------|
| standardized_nudges_toxicity | boolean | False      |

#### queryId<br>
`None`<br>
## ConversationControlChange<br>
Request URL: `https://twitter.com/i/api/graphql/hb1elGcj6769uT8qVYqtjw/ConversationControlChange`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConversationControlDelete<br>
Request URL: `https://twitter.com/i/api/graphql/OoMO_aSZ1ZXjegeamF9QmA/ConversationControlDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateBookmark<br>
Request URL: `https://twitter.com/i/api/graphql/aoDbu3RHznuiSkQ9aNM67Q/CreateBookmark`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateHighlight<br>
Request URL: `https://twitter.com/i/api/graphql/7jEc7ECTTDcNaqsMhjTxXg/CreateHighlight`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateNoteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/pwQhmvJv6I58pPtbjMzs2Q/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/-tr9gsjcukmYZRN4dpYN8g/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DeleteBookmark<br>
Request URL: `https://twitter.com/i/api/graphql/Wlmlj2-xzyS1GN3a6cj-mQ/DeleteBookmark`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteHighlight<br>
Request URL: `https://twitter.com/i/api/graphql/ea-VVDSLIEYNY2_2aPg3Uw/DeleteHighlight`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteRetweet<br>
Request URL: `https://twitter.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FavoriteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ModerateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/pjFnHGVqCjTcZol0xcBJjw/ModerateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/0kc0a_7TTr3dvweZlMslsQ/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnfavoriteTweet<br>
Request URL: `https://twitter.com/i/api/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnmentionUserFromConversation<br>
Request URL: `https://twitter.com/i/api/graphql/xVW9j3OqoBRY9d6_2OONEg/UnmentionUserFromConversation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnmoderateTweet<br>
Request URL: `https://twitter.com/i/api/graphql/pVSyu6PA57TLvIE4nN2tsA/UnmoderateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UsersVerifiedAvatars<br>
Request URL: `https://twitter.com/i/api/graphql/r44_3RKP3wHOF-nvFQmjZw/UsersVerifiedAvatars`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled          | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DisableUserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/_ckHEj05gan2VfNHG6thBA/DisableUserAccountLabel`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## articleNudgeDomains<br>
Request URL: `https://twitter.com/i/api/graphql/88Bu08U2ddaVVjKmmXjVYg/articleNudgeDomains`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://twitter.com/i/api/graphql/fYAuJHiY3TmYdBmrRtIKhA/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| spaces_2022_h2_clipping                                                 | boolean | True       |
| spaces_2022_h2_spaces_communities                                       | boolean | True       |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceSearch<br>
Request URL: `https://twitter.com/i/api/graphql/NTq79TuSz6fHj8lQaferJw/AudioSpaceSearch`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscribeToScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnsubscribeFromScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Zevhh76Msw574ZSs2NQHGQ/UnsubscribeFromScheduledSpace`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/1fFrEaBu3jDDMm6xp6UbMw/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateAppeal<br>
Request URL: `https://twitter.com/i/api/graphql/TKdL0YFsX4DMOpMKeneLvA/BirdwatchCreateAppeal`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchCreateNote<br>
Request URL: `https://twitter.com/i/api/graphql/36EUZZyaciVmNrq4CRZcmw/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateRating<br>
Request URL: `https://twitter.com/i/api/graphql/bD3AEK9BMCSpRods_ng2fA/BirdwatchCreateRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchDeleteNote<br>
Request URL: `https://twitter.com/i/api/graphql/IKS_qrShkDyor6Ri1ahd9g/BirdwatchDeleteNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchDeleteRating<br>
Request URL: `https://twitter.com/i/api/graphql/OpvCOyOoQClUND66zDzrnA/BirdwatchDeleteRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchEditNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/FLgLReVIssXjB_ui3wcrRQ/BirdwatchEditNotificationSettings`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAliasSelfSelectOptions<br>
Request URL: `https://twitter.com/i/api/graphql/szoXMke8AZOErso908iglw/BirdwatchFetchAliasSelfSelectOptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAuthenticatedUserProfile<br>
Request URL: `https://twitter.com/i/api/graphql/wPAWxQMAlJP7SpkwiQnn9w/BirdwatchFetchAuthenticatedUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                         | type    | variable   |
|:--------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_note_limit_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://twitter.com/i/api/graphql/btgGtchypc3D491MJ7XXWA/BirdwatchFetchBirdwatchProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchCanTweetBeMediaNote<br>
Request URL: `https://twitter.com/i/api/graphql/GAjIlojf2Zsrl2dmwUzETg/BirdwatchFetchCanTweetBeMediaNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchGlobalTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/O4fpV98JJW_WOwqTyIA76Q/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://twitter.com/i/api/graphql/ZGMhf1M7kPKMOhEk1nz0Yw/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/GO8BR2MM2WZB63cdOoC7lw/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://twitter.com/i/api/graphql/9bDdJ6AL26RLkcUShEcF-A/BirdwatchFetchPublicData`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchProfileAcknowledgeEarnOut<br>
Request URL: `https://twitter.com/i/api/graphql/cED9wJy8Nd1kZCCYuIq9zQ/BirdwatchProfileAcknowledgeEarnOut`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BizProfileFetchUser<br>
Request URL: `https://twitter.com/i/api/graphql/6OFpJ3TH3p8JpwOSgfgyhg/BizProfileFetchUser`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/dUKOljanJMEn7LuotOghkg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| bookmark_collection_id | ...     | t          |
| cursor                 | ...     | r          |
| includePromotedContent | boolean | True       |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://twitter.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://twitter.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...o  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/4YRsCe5AE-Noi5F_Aqz4mA/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | r          |
| includePromotedContent | boolean | True       |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...o  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarksAllDelete<br>
Request URL: `https://twitter.com/i/api/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | ...    | _          |
| isListMemberTargetUserId | ...    | r          |
| count                    | ...    | l          |
| cursor                   | ...    | a          |
| ...()(0,s.d)             | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RemoveTweetFromBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |
| tweet_id               | ...    | r          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## LiveCommerceItemsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/-lnNX56S2YrZYrLzbccFAQ/LiveCommerceItemsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/TDRNGiQQxVFGCcilLh308Q/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/phhbnHy1AdkZxl4JNxU_pQ/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/s8-oxdVsoJ3w2CFD0nFt9g/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/O1c7DuSqSyYZY8kXBv2LIQ/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/-IQY85xCTZNveiDNMluNGQ/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/lRjZKTRcWuqwtYwCWGy9_w/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/omWyDTyKyqgfVyx51ZhLLg/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/bCVwRBDPi15jrdJQ7NCENQ/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ZDfOWAKpMQbbDRACq_aMRw/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/PXO-mA1KfmLqB9I6R-lOng/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/AtiTdhEyRN8ruNFW069ewQ/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/f_YqrHSCc1mPlG-aB7pFRw/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/qH1YfcZnSJgQO-7XtKICgg/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/6G66cW5zuxPXmHOeBOjF2w/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/1aPIVZJZGp6WwwOQxI-VOQ/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/9nnDM-yum8Te--T2REfgkg/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/5eq76kkUqfdCzInCtcxQOA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://twitter.com/i/api/graphql/x8hUNaBCOV2tSalqB9cwWQ/CommunityUserInvite`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/dShPoN6voXRusgxC1uvGog/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/KVkZwp8Q6xy6iyhlQE5d7Q/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/SKToKhvm3Z4Rir8ENCJ3YQ/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/eMat-u2kx6KocreGTAt-hA/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/9nEl5bNcdteuPGbGCdvEFA/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/4OhW6gWJwiu-JTAgBPsU1w/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/lSdK1v30qVhm37rDTgHq0Q/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/EI_g43Ss_Ixg0EC4K7nzlQ/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/VwluNMGnl5uaNZ3LnlCQ_A/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/miKSMGb2R1SewIJv2-ablQ/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/9qd2xqJkMURKSyXVJ33xBw/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                                                                                                             |
|:--------------------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| count                           | ...    | (optional) t.count                                                                                                                                                                   |
| query                           | ...    | t.query                                                                                                                                                                              |
| withAttachments                 | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_message_attachment_previews_enabled")&&i.isTrue("dm_inbox_search_message_results_enabled")                                                     |
| withConversationQueryHighlights | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled")                                                 |
| withMessageQueryHighlights      | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")&&i.isTrue("dm_inbox_search_query_highlighting_message_results_enabled")&&i.isTrue("dm_inbox_search_message_results_enabled") |
| withMessages                    | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")&&i.isTrue("dm_inbox_search_message_results_enabled")                                                                         |
| withSafetyModeUserFields        | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")                                                                                                                              |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/5zpY1dCR-8NyxQJS_CFJoQ/DmGroupSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...t                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/f_uQNTGwH90odWoXBQNivQ/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,_.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...t                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DismissRitoSuggestedAction<br>
Request URL: `https://twitter.com/i/api/graphql/jYvwa61cv3NwNP24iUru6g/DismissRitoSuggestedAction`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/JIeXE-I6BZXHfxsgOkyHYQ/EditDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteEmailNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/2qKKYFQift8p5-J1k6kqxQ/WriteEmailNotificationSettings`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ViewerEmailSettings<br>
Request URL: `https://twitter.com/i/api/graphql/JpjlNgn4sLGvS6tgpTzYBg/ViewerEmailSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/g2Zc9GpoWRm5KempHyv3qw/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GraphQLError<br>
Request URL: `https://twitter.com/i/api/graphql/2V2W3HIBuMW83vEMtfo_Rg/GraphQLError`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/AT3bQwrWSsbAbMgy_5C8CQ/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/WGbQHjliog_TsbB16fwZsA/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Yw1pKqHDSlwP4RIHPVA1gg/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/jnwTSDR-Eo_HWlSkXPcMGA/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/MDxKOwd-vjXr0hxuJaxKgw/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://twitter.com/i/api/graphql/Vupsa0nLEL7N6gmmQhnJlA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/YUAPFZrj8hpFG9SMLbxLRw/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/7OyDpqeNFY2VVw5f4YkO1g/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/m8nDdGpQPNiVXBAMoRQopQ/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/FVPxhgu-rifOsznYw6n_xw/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/9k8Hk6aphKPwGq1V74Jwhg/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DeleteList<br>
Request URL: `https://twitter.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListEditRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/-cQg57zstd92TFv9zGR8jQ/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/rFvb5VowTcZnu8XkYcTJdQ/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/WNPuPcdHeWhLeXNHQawDKA/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/7lZI8Asl_8Rw2agp9mkd8g/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MuteList<br>
Request URL: `https://twitter.com/i/api/graphql/ZYyanJsskNUcltu9bliMLA/MuteList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/ppQKGtSUBDAMsrkC__XE1Q/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://twitter.com/i/api/graphql/d18zaIOhoeOldj7wijgjTg/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://twitter.com/i/api/graphql/LpbU9IVW-sPBeGs6pmRqrg/ListPins`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/PSmgvSQYduHFYeaz6-39OQ/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/q0etZpaZHJDkmpmheOdHpQ/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/L66MbjfIJx7ttuQOwCnD-Q/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/YIn-NH9ZGXkH-bT3i9829w/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/DW7rr-jTRPrRYYGXdqn4zw/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnmuteList<br>
Request URL: `https://twitter.com/i/api/graphql/pMZrHRNsmEkXgbn3tOyr7Q/UnmuteList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/Mt3NY2sx-n8Pyns4oxw1uw/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/wV8r3YkbuL_9QTbY9If5Pg/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/-3t-fHm2tHafdEpOqqzesA/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/YZLrEvmtbvwHr7aUjkP1Xw/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/5HGqOQG51gkkrNzL0W1G9Q/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://twitter.com/i/api/graphql/uXPC2DKHcG5WJjiiln0w2w/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## EnableLoggedOutWebNotifications<br>
Request URL: `https://twitter.com/i/api/graphql/BqIHKmwZKtiUBPi07jKctg/EnableLoggedOutWebNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## PinReply<br>
Request URL: `https://twitter.com/i/api/graphql/GA2_1uKP9b_GyR4MVAQXAw/PinReply`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnpinReply<br>
Request URL: `https://twitter.com/i/api/graphql/iRe6ig5OV1EzOtldNIuGDQ/UnpinReply`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://twitter.com/i/api/graphql/FenMZDRGyp6gG3Wx8vHvkg/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | i                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | n                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/werXDifnSJtcWUSjVjTXIQ/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rest_id                | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/N1T22GLYezfp2cpnS-Nivg/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | r           |
| count                  | ...     | t           |
| cursor                 | ...     | n           |
| teamName               | ...     | i           |
| includePromotedContent | boolean | False       |
| ...()(0,a.d)           | ...     | _           |
| withClientEventToken   | boolean | False       |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://twitter.com/i/api/graphql/D2WyxrKOtYzYj6_XO-kfXw/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | i           |
| count                  | ...     | t           |
| cursor                 | ...     | n           |
| includePromotedContent | boolean | True        |
| ...()(0,a.d)           | ...     | _           |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://twitter.com/i/api/graphql/qQoeS7szGavsi8-ehD2AWg/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | i                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | n                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://twitter.com/i/api/graphql/etQ2Ovt6XpT7amDgVSbXvA/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"n","count":"_","cursor":"string"==typeof t?t:"void 0","includePromotedContent":"!1","withVoice":"!1"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserSuperFollowTweets<br>
Request URL: `https://twitter.com/i/api/graphql/I2gzL9TB_2IWa5pqqWRddg/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | i           |
| count                  | ...     | t           |
| cursor                 | ...     | n           |
| includePromotedContent | boolean | True        |
| ...()(0,a.d)           | ...     | _           |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://twitter.com/i/api/graphql/WzJjibAcDa-oCjCcLOotcg/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable                              |
|:---------------------------------------|:--------|:--------------------------------------|
| userId                                 | ...     | r                                     |
| count                                  | ...     | t                                     |
| cursor                                 | ...     | n                                     |
| includePromotedContent                 | boolean | True                                  |
| withQuickPromoteEligibilityTweetFields | boolean | True                                  |
| ...()(0,a.d)                           | ...     | _                                     |
| withVoice                              | ...     | _.isTrue(_)                           |
| withV2Timeline                         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://twitter.com/i/api/graphql/fn9oRltM1N4thkh5CVusPg/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## SetDefault<br>
Request URL: `https://twitter.com/i/api/graphql/QEMLEzEMzoPNbeauKCCLbg/SetDefault`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeletePaymentMethod<br>
Request URL: `https://twitter.com/i/api/graphql/VaaLGwK5KNLoc7wsOmp4uw/DeletePaymentMethod`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PaymentMethods<br>
Request URL: `https://twitter.com/i/api/graphql/mPF_G9okpbZuLcD6mN8K9g/PaymentMethods`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AdAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/a8KxGfFQAmm3WxqemuqSRA/AdAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AudienceEstimate<br>
Request URL: `https://twitter.com/i/api/graphql/1LYVUabJBYkPlUAWRabB3g/AudienceEstimate`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Budgets<br>
Request URL: `https://twitter.com/i/api/graphql/mbK3oSQotwcJXyQIBE3uYw/Budgets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Coupons<br>
Request URL: `https://twitter.com/i/api/graphql/R1h43jnAl2bsDoUkgZb7NQ/Coupons`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateQuickPromotion<br>
Request URL: `https://twitter.com/i/api/graphql/oDSoVgHhJxnd5IkckgPZdg/CreateQuickPromotion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## QuickPromoteEligibility<br>
Request URL: `https://twitter.com/i/api/graphql/LtpCXh66W-uXh7u7XSRA8Q/QuickPromoteEligibility`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EnrollCoupon<br>
Request URL: `https://twitter.com/i/api/graphql/SOyGmNGaEXcvk15s5bqDrA/EnrollCoupon`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RitoActionedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/DYW85A1ptzjpQtwjz9S1wA/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/glyzt5THcCSlzyQkEpWwGw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | ...    | t           |
| ...()(0,a.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/lx7ESTXeykLWNL-5cMh_jA/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | ...    | t           |
| rest_id                  | ...    | i           |
| ...()(0,r.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoSuggestedActionsFacePile<br>
Request URL: `https://twitter.com/i/api/graphql/GnQKeEdL1LyeK3dTQCS1yw/RitoSuggestedActionsFacePile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/CTOVqej0JBXAZSwkp1US0g/DeleteScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## getAltTextPromptPreference<br>
Request URL: `https://twitter.com/i/api/graphql/PFIxTk8owMoZgiMccP0r4g/getAltTextPromptPreference`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## updateCaptionsAlwaysDisplayPreference<br>
Request URL: `https://twitter.com/i/api/graphql/uCUQhvZ5sJ9qHinRp6CFlQ/updateCaptionsAlwaysDisplayPreference`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteDataSaverPreferences<br>
Request URL: `https://twitter.com/i/api/graphql/H03etWvZGz41YASxAU2YPg/WriteDataSaverPreferences`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmNsfwMediaFilterUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/of_N6O33zfyD4qsFJMYFxA/DmNsfwMediaFilterUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GetSafetyModeSettings<br>
Request URL: `https://twitter.com/i/api/graphql/AhxTX0lkbIos4WG53xwzSA/GetSafetyModeSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SharingAudiospacesListeningDataWithFollowersUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/5h0kNbk3ii97rmfY6CdgAA/SharingAudiospacesListeningDataWithFollowersUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateCustomerPortalSession<br>
Request URL: `https://twitter.com/i/api/graphql/2LHXrd1uYeaMWhciZgPZFw/CreateCustomerPortalSession`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListProductSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/wwdBYgScze0_Jnan79jEUw/ListProductSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscriptionCheckoutUrlWithEligibility<br>
Request URL: `https://twitter.com/i/api/graphql/hKfOOObQr5JmfmxW0YtPvg/SubscriptionCheckoutUrlWithEligibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscriptionProductDetails<br>
Request URL: `https://twitter.com/i/api/graphql/f0dExZDmFWFSWMCPQSAemQ/SubscriptionProductDetails`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FeatureSettingsUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/-btar_vkBwWA7s3YWfp_9g/FeatureSettingsUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/99h7-v-l3eaWRVnyFh15HA/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/yhwV4UX520Fi4Mj218k8SA/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://twitter.com/i/api/graphql/ATMi_eKiFwe2LOvsFM7Bzg/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | ...    | a          |
| cursor       | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicFollow<br>
Request URL: `https://twitter.com/i/api/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://twitter.com/i/api/graphql/21aU5RuVUAEo8eyLcuLlQA/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"l","cursor":"i","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","r.d_"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/4OUZZOonV2h60I0wdlQb_w/TopicByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://twitter.com/i/api/graphql/FkZb_xYbhsnQhMPq3CDGGg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicUnfollow<br>
Request URL: `https://twitter.com/i/api/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://twitter.com/i/api/graphql/gFH7AVHEhX9BWYXNOlza9w/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://twitter.com/i/api/graphql/JB8_oLN8iYxktCd9khCfxA/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://twitter.com/i/api/graphql/1arWZxkF8Fm-GVjAwAm6pw/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/LGaCKIHvsu2lZGS1j4Qz2A/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | l          |
| cursor       | ...    | a          |
| context      | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AuthenticatedUserTFLists<br>
Request URL: `https://twitter.com/i/api/graphql/QjN8ZdavFDqxUjNn3r9cig/AuthenticatedUserTFLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/mDc_nU8xGv0cLRWtTaIEug/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| tweetId                | ...     | a          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | True       |
| ...()(0,i.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://twitter.com/i/api/graphql/RCR9gqwYD1NEgi9FWzA50A/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| tweetId                | ...     | r          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | True       |
| ...()(0,i.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://twitter.com/i/api/graphql/mS6ZtqH3zVlEb2ScJiPcyQ/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | t          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://twitter.com/i/api/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | ...    | _          |

#### features<br>
| key                                             | type    | variable   |
|:------------------------------------------------|:--------|:-----------|
| profile_foundations_tweet_stats_enabled         | boolean | False      |
| profile_foundations_tweet_stats_tweet_frequency | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://twitter.com/i/api/graphql/lALYIusKEhpB5ITaPf_HVw/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleDelete<br>
Request URL: `https://twitter.com/i/api/graphql/6st-stMDc7KBqLT8KvWhHg/TwitterArticleDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterArticleByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/ELP96kRZ4gk3PdB28Y7KyA/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://twitter.com/i/api/graphql/e9WBiF8PPzZMoOL5ZbTBOA/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://twitter.com/i/api/graphql/aOqnvY8L7wK9wE6fxMcHVw/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://twitter.com/i/api/graphql/NFaDtPkZpUzWoPFTPPPjwQ/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/70lCUHih7EFIVwlqJatEvQ/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://twitter.com/i/api/graphql/eR-8ziKPVcCZUXi5p-o1YA/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/sSArbwPuRYTz2F_bvESDqg/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/NEwac2-8ONgf0756ne8oXA/CommunityMemberRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityUserRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/gi_UGcUurYp6N6p2BaLJqQ/CommunityUserRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/RRnOwHttRGscWKC1zY9VRA/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled          | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## ConnectTabTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/kZPmN4NTaf3W_aQMGyNawA/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ExplorePage<br>
Request URL: `https://twitter.com/i/api/graphql/d7LX_k8g7E-Z69wZas28Zw/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/7jT5GT59P8IFjgxwqnEdQw/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## timelinesFeedback<br>
Request URL: `https://twitter.com/i/api/graphql/vfVbgvTPTQ-dF_PQ5lD1WQ/timelinesFeedback`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/1zyNXoj8NfltDsKRdDAjGw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RemoveFollower<br>
Request URL: `https://twitter.com/i/api/graphql/QpNfg0kpPRfjROQ_9eOLXA/RemoveFollower`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/1YAM811Q8Ry4XyPpJclURQ/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/pVrmNaXcxPjisIvKtLDMEA/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/OJBgJQIrij6e3cjqQ3Zu1Q/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/zC51NksbixfctE9X0ITB-Q/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## articleNudgeDomains<br>
Request URL: `https://twitter.com/i/api/graphql/88Bu08U2ddaVVjKmmXjVYg/articleNudgeDomains`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/99h7-v-l3eaWRVnyFh15HA/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/yhwV4UX520Fi4Mj218k8SA/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://twitter.com/i/api/graphql/fYAuJHiY3TmYdBmrRtIKhA/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| spaces_2022_h2_clipping                                                 | boolean | True       |
| spaces_2022_h2_spaces_communities                                       | boolean | True       |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceSearch<br>
Request URL: `https://twitter.com/i/api/graphql/NTq79TuSz6fHj8lQaferJw/AudioSpaceSearch`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## getAltTextPromptPreference<br>
Request URL: `https://twitter.com/i/api/graphql/PFIxTk8owMoZgiMccP0r4g/getAltTextPromptPreference`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## updateCaptionsAlwaysDisplayPreference<br>
Request URL: `https://twitter.com/i/api/graphql/uCUQhvZ5sJ9qHinRp6CFlQ/updateCaptionsAlwaysDisplayPreference`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AuthenticatedUserTFLists<br>
Request URL: `https://twitter.com/i/api/graphql/QjN8ZdavFDqxUjNn3r9cig/AuthenticatedUserTFLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/1fFrEaBu3jDDMm6xp6UbMw/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateAppeal<br>
Request URL: `https://twitter.com/i/api/graphql/TKdL0YFsX4DMOpMKeneLvA/BirdwatchCreateAppeal`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchCreateNote<br>
Request URL: `https://twitter.com/i/api/graphql/36EUZZyaciVmNrq4CRZcmw/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateRating<br>
Request URL: `https://twitter.com/i/api/graphql/bD3AEK9BMCSpRods_ng2fA/BirdwatchCreateRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchDeleteNote<br>
Request URL: `https://twitter.com/i/api/graphql/IKS_qrShkDyor6Ri1ahd9g/BirdwatchDeleteNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchDeleteRating<br>
Request URL: `https://twitter.com/i/api/graphql/OpvCOyOoQClUND66zDzrnA/BirdwatchDeleteRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchEditNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/FLgLReVIssXjB_ui3wcrRQ/BirdwatchEditNotificationSettings`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAliasSelfSelectOptions<br>
Request URL: `https://twitter.com/i/api/graphql/szoXMke8AZOErso908iglw/BirdwatchFetchAliasSelfSelectOptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAuthenticatedUserProfile<br>
Request URL: `https://twitter.com/i/api/graphql/wPAWxQMAlJP7SpkwiQnn9w/BirdwatchFetchAuthenticatedUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                         | type    | variable   |
|:--------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_note_limit_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://twitter.com/i/api/graphql/btgGtchypc3D491MJ7XXWA/BirdwatchFetchBirdwatchProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchCanTweetBeMediaNote<br>
Request URL: `https://twitter.com/i/api/graphql/GAjIlojf2Zsrl2dmwUzETg/BirdwatchFetchCanTweetBeMediaNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchGlobalTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/O4fpV98JJW_WOwqTyIA76Q/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://twitter.com/i/api/graphql/ZGMhf1M7kPKMOhEk1nz0Yw/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/GO8BR2MM2WZB63cdOoC7lw/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://twitter.com/i/api/graphql/9bDdJ6AL26RLkcUShEcF-A/BirdwatchFetchPublicData`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchProfileAcknowledgeEarnOut<br>
Request URL: `https://twitter.com/i/api/graphql/cED9wJy8Nd1kZCCYuIq9zQ/BirdwatchProfileAcknowledgeEarnOut`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BizProfileFetchUser<br>
Request URL: `https://twitter.com/i/api/graphql/6OFpJ3TH3p8JpwOSgfgyhg/BizProfileFetchUser`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/3Jf98hrBD9_-WJtg8w4jKA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/nJUeL1KIaR2idom9FBNIoQ/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/XYOfeB7PjUyRlIqEOix-oA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/dUKOljanJMEn7LuotOghkg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| bookmark_collection_id | ...     | t          |
| cursor                 | ...     | r          |
| includePromotedContent | boolean | True       |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://twitter.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://twitter.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...o  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/4YRsCe5AE-Noi5F_Aqz4mA/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | r          |
| includePromotedContent | boolean | True       |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/jnwTSDR-Eo_HWlSkXPcMGA/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/MDxKOwd-vjXr0hxuJaxKgw/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/TDRNGiQQxVFGCcilLh308Q/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/phhbnHy1AdkZxl4JNxU_pQ/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/s8-oxdVsoJ3w2CFD0nFt9g/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/O1c7DuSqSyYZY8kXBv2LIQ/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/-IQY85xCTZNveiDNMluNGQ/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/lRjZKTRcWuqwtYwCWGy9_w/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/dShPoN6voXRusgxC1uvGog/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/omWyDTyKyqgfVyx51ZhLLg/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/KVkZwp8Q6xy6iyhlQE5d7Q/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/SKToKhvm3Z4Rir8ENCJ3YQ/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/eMat-u2kx6KocreGTAt-hA/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/9nEl5bNcdteuPGbGCdvEFA/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/4OhW6gWJwiu-JTAgBPsU1w/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/bCVwRBDPi15jrdJQ7NCENQ/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ZDfOWAKpMQbbDRACq_aMRw/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/PXO-mA1KfmLqB9I6R-lOng/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/AtiTdhEyRN8ruNFW069ewQ/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/NEwac2-8ONgf0756ne8oXA/CommunityMemberRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/f_YqrHSCc1mPlG-aB7pFRw/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/qH1YfcZnSJgQO-7XtKICgg/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/lSdK1v30qVhm37rDTgHq0Q/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/EI_g43Ss_Ixg0EC4K7nzlQ/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/VwluNMGnl5uaNZ3LnlCQ_A/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/6G66cW5zuxPXmHOeBOjF2w/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/1aPIVZJZGp6WwwOQxI-VOQ/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/9nnDM-yum8Te--T2REfgkg/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/5eq76kkUqfdCzInCtcxQOA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://twitter.com/i/api/graphql/x8hUNaBCOV2tSalqB9cwWQ/CommunityUserInvite`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityUserRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/gi_UGcUurYp6N6p2BaLJqQ/CommunityUserRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ConnectTabTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/kZPmN4NTaf3W_aQMGyNawA/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ConvertRitoSuggestedActions<br>
Request URL: `https://twitter.com/i/api/graphql/2njnYoE69O2jdUM7KMEnDw/ConvertRitoSuggestedActions`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...o  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateCustomerPortalSession<br>
Request URL: `https://twitter.com/i/api/graphql/2LHXrd1uYeaMWhciZgPZFw/CreateCustomerPortalSession`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/AT3bQwrWSsbAbMgy_5C8CQ/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DataSaverMode<br>
Request URL: `https://twitter.com/i/api/graphql/xF6sXnKJfS2AOylzxRjf6A/DataSaverMode`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteDataSaverPreferences<br>
Request URL: `https://twitter.com/i/api/graphql/H03etWvZGz41YASxAU2YPg/WriteDataSaverPreferences`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SetDefault<br>
Request URL: `https://twitter.com/i/api/graphql/QEMLEzEMzoPNbeauKCCLbg/SetDefault`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarksAllDelete<br>
Request URL: `https://twitter.com/i/api/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeletePaymentMethod<br>
Request URL: `https://twitter.com/i/api/graphql/VaaLGwK5KNLoc7wsOmp4uw/DeletePaymentMethod`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/CTOVqej0JBXAZSwkp1US0g/DeleteScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DisableUserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/_ckHEj05gan2VfNHG6thBA/DisableUserAccountLabel`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DismissRitoSuggestedAction<br>
Request URL: `https://twitter.com/i/api/graphql/jYvwa61cv3NwNP24iUru6g/DismissRitoSuggestedAction`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/9qd2xqJkMURKSyXVJ33xBw/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                                                                                                             |
|:--------------------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| count                           | ...    | (optional) t.count                                                                                                                                                                   |
| query                           | ...    | t.query                                                                                                                                                                              |
| withAttachments                 | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_message_attachment_previews_enabled")&&i.isTrue("dm_inbox_search_message_results_enabled")                                                     |
| withConversationQueryHighlights | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled")                                                 |
| withMessageQueryHighlights      | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")&&i.isTrue("dm_inbox_search_query_highlighting_message_results_enabled")&&i.isTrue("dm_inbox_search_message_results_enabled") |
| withMessages                    | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")&&i.isTrue("dm_inbox_search_message_results_enabled")                                                                         |
| withSafetyModeUserFields        | ...    | i.isTrue("direct_messages_incremental_holdback_2022h1")                                                                                                                              |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/5zpY1dCR-8NyxQJS_CFJoQ/DmGroupSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...t                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/f_uQNTGwH90odWoXBQNivQ/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,_.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmNsfwMediaFilterUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/of_N6O33zfyD4qsFJMYFxA/DmNsfwMediaFilterUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...t                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | ...    | _          |
| isListMemberTargetUserId | ...    | r          |
| count                    | ...    | l          |
| cursor                   | ...    | a          |
| ...()(0,s.d)             | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/JIeXE-I6BZXHfxsgOkyHYQ/EditDraftTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditScheduledTweet<br>
Request URL: `https://twitter.com/i/api/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WriteEmailNotificationSettings<br>
Request URL: `https://twitter.com/i/api/graphql/2qKKYFQift8p5-J1k6kqxQ/WriteEmailNotificationSettings`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EnableLoggedOutWebNotifications<br>
Request URL: `https://twitter.com/i/api/graphql/BqIHKmwZKtiUBPi07jKctg/EnableLoggedOutWebNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ExplorePage<br>
Request URL: `https://twitter.com/i/api/graphql/d7LX_k8g7E-Z69wZas28Zw/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/mDc_nU8xGv0cLRWtTaIEug/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| tweetId                | ...     | a          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | True       |
| ...()(0,i.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FeatureSettingsUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/-btar_vkBwWA7s3YWfp_9g/FeatureSettingsUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/fmp6rQCkeM5p0tJQOMSBag/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/kM8S6MKw7NmKX2yZNWWVqQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,s.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/q4cKckK0lNxWkHfAXXXzJQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                          | type   | variable   |
|:---------------------------------------------|:-------|:-----------|
| userId                                       | ...    | n          |
| sharingAudiospacesListeningDataWithFollowers | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/Ah2K7ACCzCkqSyjJb3lJNg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| count        | ...    | i          |
| cursor       | ...    | l          |
| context      | ...    | n          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GraphQLError<br>
Request URL: `https://twitter.com/i/api/graphql/2V2W3HIBuMW83vEMtfo_Rg/GraphQLError`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/WGbQHjliog_TsbB16fwZsA/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Yw1pKqHDSlwP4RIHPVA1gg/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/g2Zc9GpoWRm5KempHyv3qw/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://twitter.com/i/api/graphql/FenMZDRGyp6gG3Wx8vHvkg/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | i                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | n                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://twitter.com/i/api/graphql/Vupsa0nLEL7N6gmmQhnJlA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/YUAPFZrj8hpFG9SMLbxLRw/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/7OyDpqeNFY2VVw5f4YkO1g/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/m8nDdGpQPNiVXBAMoRQopQ/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/FVPxhgu-rifOsznYw6n_xw/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/9k8Hk6aphKPwGq1V74Jwhg/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DeleteList<br>
Request URL: `https://twitter.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListEditRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/-cQg57zstd92TFv9zGR8jQ/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/rFvb5VowTcZnu8XkYcTJdQ/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/WNPuPcdHeWhLeXNHQawDKA/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/7lZI8Asl_8Rw2agp9mkd8g/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MuteList<br>
Request URL: `https://twitter.com/i/api/graphql/ZYyanJsskNUcltu9bliMLA/MuteList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/ppQKGtSUBDAMsrkC__XE1Q/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://twitter.com/i/api/graphql/d18zaIOhoeOldj7wijgjTg/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://twitter.com/i/api/graphql/LpbU9IVW-sPBeGs6pmRqrg/ListPins`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListProductSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/wwdBYgScze0_Jnan79jEUw/ListProductSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/PSmgvSQYduHFYeaz6-39OQ/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/q0etZpaZHJDkmpmheOdHpQ/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/L66MbjfIJx7ttuQOwCnD-Q/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/YIn-NH9ZGXkH-bT3i9829w/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/DW7rr-jTRPrRYYGXdqn4zw/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnmuteList<br>
Request URL: `https://twitter.com/i/api/graphql/pMZrHRNsmEkXgbn3tOyr7Q/UnmuteList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/Mt3NY2sx-n8Pyns4oxw1uw/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/wV8r3YkbuL_9QTbY9If5Pg/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/-3t-fHm2tHafdEpOqqzesA/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/YZLrEvmtbvwHr7aUjkP1Xw/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/5HGqOQG51gkkrNzL0W1G9Q/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://twitter.com/i/api/graphql/uXPC2DKHcG5WJjiiln0w2w/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | False      |
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LiveCommerceItemsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/-lnNX56S2YrZYrLzbccFAQ/LiveCommerceItemsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/e5tzuf-cuGRqyGguK8WA1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | s          |
| cursor       | ...    | a          |
| context      | ...    | l          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/r0J0DrnXptImeiaYBVp5vQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| visibility       | ...    | s          |
| ...()(0,a.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://twitter.com/i/api/graphql/ATMi_eKiFwe2LOvsFM7Bzg/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | ...    | a          |
| cursor       | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## PaymentMethods<br>
Request URL: `https://twitter.com/i/api/graphql/mPF_G9okpbZuLcD6mN8K9g/PaymentMethods`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PinReply<br>
Request URL: `https://twitter.com/i/api/graphql/GA2_1uKP9b_GyR4MVAQXAw/PinReply`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnpinReply<br>
Request URL: `https://twitter.com/i/api/graphql/iRe6ig5OV1EzOtldNIuGDQ/UnpinReply`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PutClientEducationFlag<br>
Request URL: `https://twitter.com/i/api/graphql/IjQ-egg0uPkY11NyPMfRMQ/PutClientEducationFlag`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AdAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/a8KxGfFQAmm3WxqemuqSRA/AdAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AudienceEstimate<br>
Request URL: `https://twitter.com/i/api/graphql/1LYVUabJBYkPlUAWRabB3g/AudienceEstimate`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Budgets<br>
Request URL: `https://twitter.com/i/api/graphql/mbK3oSQotwcJXyQIBE3uYw/Budgets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Coupons<br>
Request URL: `https://twitter.com/i/api/graphql/R1h43jnAl2bsDoUkgZb7NQ/Coupons`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateQuickPromotion<br>
Request URL: `https://twitter.com/i/api/graphql/oDSoVgHhJxnd5IkckgPZdg/CreateQuickPromotion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## QuickPromoteEligibility<br>
Request URL: `https://twitter.com/i/api/graphql/LtpCXh66W-uXh7u7XSRA8Q/QuickPromoteEligibility`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EnrollCoupon<br>
Request URL: `https://twitter.com/i/api/graphql/SOyGmNGaEXcvk15s5bqDrA/EnrollCoupon`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RemoveFollower<br>
Request URL: `https://twitter.com/i/api/graphql/QpNfg0kpPRfjROQ_9eOLXA/RemoveFollower`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RemoveTweetFromBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |
| tweet_id               | ...    | r          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://twitter.com/i/api/graphql/RCR9gqwYD1NEgi9FWzA50A/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| tweetId                | ...     | r          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | True       |
| ...()(0,i.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoActionedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/DYW85A1ptzjpQtwjz9S1wA/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/glyzt5THcCSlzyQkEpWwGw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | ...    | t           |
| ...()(0,a.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/lx7ESTXeykLWNL-5cMh_jA/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | ...    | t           |
| rest_id                  | ...    | i           |
| ...()(0,r.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoSuggestedActionsFacePile<br>
Request URL: `https://twitter.com/i/api/graphql/GnQKeEdL1LyeK3dTQCS1yw/RitoSuggestedActionsFacePile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GetSafetyModeSettings<br>
Request URL: `https://twitter.com/i/api/graphql/AhxTX0lkbIos4WG53xwzSA/GetSafetyModeSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/7jT5GT59P8IFjgxwqnEdQw/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SharingAudiospacesListeningDataWithFollowersUpdate<br>
Request URL: `https://twitter.com/i/api/graphql/5h0kNbk3ii97rmfY6CdgAA/SharingAudiospacesListeningDataWithFollowersUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscribeToScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscriptionCheckoutUrlWithEligibility<br>
Request URL: `https://twitter.com/i/api/graphql/hKfOOObQr5JmfmxW0YtPvg/SubscriptionCheckoutUrlWithEligibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SubscriptionProductDetails<br>
Request URL: `https://twitter.com/i/api/graphql/f0dExZDmFWFSWMCPQSAemQ/SubscriptionProductDetails`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/okr7pnpLkcFiZb8L4s19LQ/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable          |
|:---------|:-------|:------------------|
| userId   | ...    | n                 |
| enabled  | ...    | none!==t          |
| duration | ...    | none===t?void 0:t |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## timelinesFeedback<br>
Request URL: `https://twitter.com/i/api/graphql/vfVbgvTPTQ-dF_PQ5lD1WQ/timelinesFeedback`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicFollow<br>
Request URL: `https://twitter.com/i/api/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://twitter.com/i/api/graphql/21aU5RuVUAEo8eyLcuLlQA/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"l","cursor":"i","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","r.d_"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/4OUZZOonV2h60I0wdlQb_w/TopicByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://twitter.com/i/api/graphql/FkZb_xYbhsnQhMPq3CDGGg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicUnfollow<br>
Request URL: `https://twitter.com/i/api/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://twitter.com/i/api/graphql/gFH7AVHEhX9BWYXNOlza9w/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://twitter.com/i/api/graphql/JB8_oLN8iYxktCd9khCfxA/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://twitter.com/i/api/graphql/1arWZxkF8Fm-GVjAwAm6pw/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/RRnOwHttRGscWKC1zY9VRA/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled          | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/miKSMGb2R1SewIJv2-ablQ/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://twitter.com/i/api/graphql/mS6ZtqH3zVlEb2ScJiPcyQ/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | t          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://twitter.com/i/api/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | ...    | _          |

#### features<br>
| key                                             | type    | variable   |
|:------------------------------------------------|:--------|:-----------|
| profile_foundations_tweet_stats_enabled         | boolean | False      |
| profile_foundations_tweet_stats_tweet_frequency | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://twitter.com/i/api/graphql/lALYIusKEhpB5ITaPf_HVw/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleDelete<br>
Request URL: `https://twitter.com/i/api/graphql/6st-stMDc7KBqLT8KvWhHg/TwitterArticleDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterArticleByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/ELP96kRZ4gk3PdB28Y7KyA/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://twitter.com/i/api/graphql/e9WBiF8PPzZMoOL5ZbTBOA/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://twitter.com/i/api/graphql/aOqnvY8L7wK9wE6fxMcHVw/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://twitter.com/i/api/graphql/NFaDtPkZpUzWoPFTPPPjwQ/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/70lCUHih7EFIVwlqJatEvQ/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://twitter.com/i/api/graphql/eR-8ziKPVcCZUXi5p-o1YA/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/sSArbwPuRYTz2F_bvESDqg/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnsubscribeFromScheduledSpace<br>
Request URL: `https://twitter.com/i/api/graphql/Zevhh76Msw574ZSs2NQHGQ/UnsubscribeFromScheduledSpace`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/1zyNXoj8NfltDsKRdDAjGw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/werXDifnSJtcWUSjVjTXIQ/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rest_id                | ...     | i          |
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| rest_id | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/N1T22GLYezfp2cpnS-Nivg/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | r           |
| count                  | ...     | t           |
| cursor                 | ...     | n           |
| teamName               | ...     | i           |
| includePromotedContent | boolean | False       |
| ...()(0,a.d)           | ...     | _           |
| withClientEventToken   | boolean | False       |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/1YAM811Q8Ry4XyPpJclURQ/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/pVrmNaXcxPjisIvKtLDMEA/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## GetUserClaims<br>
Request URL: `https://twitter.com/i/api/graphql/lFi3xnx0auUUnyG4YwpCNw/GetUserClaims`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://twitter.com/i/api/graphql/D2WyxrKOtYzYj6_XO-kfXw/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | i           |
| count                  | ...     | t           |
| cursor                 | ...     | n           |
| includePromotedContent | boolean | True        |
| ...()(0,a.d)           | ...     | _           |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://twitter.com/i/api/graphql/qQoeS7szGavsi8-ehD2AWg/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | i                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | n                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://twitter.com/i/api/graphql/etQ2Ovt6XpT7amDgVSbXvA/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"n","count":"_","cursor":"string"==typeof t?t:"void 0","includePromotedContent":"!1","withVoice":"!1"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserSessionsList<br>
Request URL: `https://twitter.com/i/api/graphql/vJ-XatpmQSG8bDch8-t9Jw/UserSessionsList`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserSuperFollowTweets<br>
Request URL: `https://twitter.com/i/api/graphql/I2gzL9TB_2IWa5pqqWRddg/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | i           |
| count                  | ...     | t           |
| cursor                 | ...     | n           |
| includePromotedContent | boolean | True        |
| ...()(0,a.d)           | ...     | _           |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://twitter.com/i/api/graphql/WzJjibAcDa-oCjCcLOotcg/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable                              |
|:---------------------------------------|:--------|:--------------------------------------|
| userId                                 | ...     | r                                     |
| count                                  | ...     | t                                     |
| cursor                                 | ...     | n                                     |
| includePromotedContent                 | boolean | True                                  |
| withQuickPromoteEligibilityTweetFields | boolean | True                                  |
| ...()(0,a.d)                           | ...     | _                                     |
| withVoice                              | ...     | _.isTrue(_)                           |
| withV2Timeline                         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://twitter.com/i/api/graphql/fn9oRltM1N4thkh5CVusPg/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/OJBgJQIrij6e3cjqQ3Zu1Q/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewerEmailSettings<br>
Request URL: `https://twitter.com/i/api/graphql/JpjlNgn4sLGvS6tgpTzYBg/ViewerEmailSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/zC51NksbixfctE9X0ITB-Q/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/D8mVcJSVv66_3NcR7fOf6g/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/LGaCKIHvsu2lZGS1j4Qz2A/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | l          |
| cursor       | ...    | a          |
| context      | ...    | i          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## VerifiedRouteQuery<br>
Request URL: `https://twitter.com/i/api/graphql/inQHR9aa8pXO9Jqy4swaJw/VerifiedRouteQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## urtModuleOperationsInjectEntryQuery<br>
Request URL: `https://twitter.com/i/api/graphql/null/urtModuleOperationsInjectEntryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## urtModuleOperationsUpdateEntryQuery<br>
Request URL: `https://twitter.com/i/api/graphql/null/urtModuleOperationsUpdateEntryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useRelayDelegateDataQuery<br>
Request URL: `https://twitter.com/i/api/graphql/BAMss4qXZvxtUJdCn__AnA/useRelayDelegateDataQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## usersModuleProtectedQuery<br>
Request URL: `https://twitter.com/i/api/graphql//usersModuleProtectedQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesDashMenuItemQuery<br>
Request URL: `https://twitter.com/i/api/graphql/cFC8pqLWsfzTUOY674C6OA/CommunitiesDashMenuItemQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## managementListsPageTimelineQuery<br>
Request URL: `https://twitter.com/i/api/graphql/P5eX9gk6uk074s4L4G1X6A/managementListsPageTimelineQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| vibe_api_enabled                                                        | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |

#### queryId<br>
`None`<br>
## AccountSwitcherDelegateQuery<br>
Request URL: `https://twitter.com/i/api/graphql/1gowCMPzY09WyApNQM68kA/AccountSwitcherDelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DelegatedAccountListQuery<br>
Request URL: `https://twitter.com/i/api/graphql/b0NSGdpcMo6KAYbeYpIXRA/DelegatedAccountListQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DelegateAlertBannerContainerQuery<br>
Request URL: `https://twitter.com/i/api/graphql/zuUTzlnI-XomL9lfWFqSKg/DelegateAlertBannerContainerQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMMessageDeleteMutation<br>
Request URL: `https://twitter.com/i/api/graphql/BJ6DtxA2llfjnRoRjaiIiw/DMMessageDeleteMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useDMReactionMutationAddMutation<br>
Request URL: `https://twitter.com/i/api/graphql/VyDyV9pC2oZEj6g52hgnhA/useDMReactionMutationAddMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useDMReactionMutationRemoveMutation<br>
Request URL: `https://twitter.com/i/api/graphql/bV_Nim3RYHsaJwMkTXJ6ew/useDMReactionMutationRemoveMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useTypingNotifierMutation<br>
Request URL: `https://twitter.com/i/api/graphql/HL96-xZ3Y81IEzAdczDokg/useTypingNotifierMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMConversationSearchTabGroupsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/8D8KoSq5q9d5Su3emu2dwg/DMConversationSearchTabGroupsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMConversationSearchTabPeopleQuery<br>
Request URL: `https://twitter.com/i/api/graphql/qno3lU4_eSHtSFoWQUhEag/DMConversationSearchTabPeopleQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMMessageSearchTabQuery<br>
Request URL: `https://twitter.com/i/api/graphql/Ts3aYOhbDlDxVrS9Dw62rA/DMMessageSearchTabQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## DMPinnedInboxAppend_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/o0aymgGiJY-53Y52YSUGVA/DMPinnedInboxAppend_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMPinnedInboxDelete_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/_TQxP2Rb0expwVP9ktGrTQ/DMPinnedInboxDelete_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMPinnedInboxQuery<br>
Request URL: `https://twitter.com/i/api/graphql/_gBQBgClVuMQb8efxWkbbQ/DMPinnedInboxQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesFetchOneQuery<br>
Request URL: `https://twitter.com/i/api/graphql/bC3Saf4niY6YuzJWV2oUGg/CommunitiesFetchOneQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsRecentQuery<br>
Request URL: `https://twitter.com/i/api/graphql/bTZFMvlXj45yFKlQVU8e1Q/CommunitiesMembershipsRecentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## UsersGraphQLFetchByScreenNameQuery<br>
Request URL: `https://twitter.com/i/api/graphql/yGtWhat0rodvNPZ-AlYdnA/UsersGraphQLFetchByScreenNameQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesFetchOneQuery<br>
Request URL: `https://twitter.com/i/api/graphql/bC3Saf4niY6YuzJWV2oUGg/CommunitiesFetchOneQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsRecentQuery<br>
Request URL: `https://twitter.com/i/api/graphql/bTZFMvlXj45yFKlQVU8e1Q/CommunitiesMembershipsRecentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## UsersGraphQLFetchByScreenNameQuery<br>
Request URL: `https://twitter.com/i/api/graphql/yGtWhat0rodvNPZ-AlYdnA/UsersGraphQLFetchByScreenNameQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## useDMReactionMutationAddMutation<br>
Request URL: `https://twitter.com/i/api/graphql/VyDyV9pC2oZEj6g52hgnhA/useDMReactionMutationAddMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useDMReactionMutationRemoveMutation<br>
Request URL: `https://twitter.com/i/api/graphql/bV_Nim3RYHsaJwMkTXJ6ew/useDMReactionMutationRemoveMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CarouselQuery<br>
Request URL: `https://twitter.com/i/api/graphql/A9Lt_vHgiD1zkiB2fdU9Zw/CarouselQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesCreateButtonQuery<br>
Request URL: `https://twitter.com/i/api/graphql/8daJzV6tGCTssiKBRFpXtQ/CommunitiesCreateButtonQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesListActivityQuery<br>
Request URL: `https://twitter.com/i/api/graphql/ZnEsP44ZDzRe9aId7SVoZg/CommunitiesListActivityQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesSearchQuery<br>
Request URL: `https://twitter.com/i/api/graphql/JLnMuCshIrWkJlp7LRvWFw/CommunitiesSearchQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityAppBarButtonQuery<br>
Request URL: `https://twitter.com/i/api/graphql/hNQLWhD2pxRBtp7mg6hWEQ/CommunityAppBarButtonQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityInviteButtonQuery<br>
Request URL: `https://twitter.com/i/api/graphql/8s4H3Tf6VXViIQuaHMJE1Q/CommunityInviteButtonQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityToolsScreenContainerQuery<br>
Request URL: `https://twitter.com/i/api/graphql/c7MAOYAoh0dfh_06YrxSpg/CommunityToolsScreenContainerQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteCommunityMutation<br>
Request URL: `https://twitter.com/i/api/graphql/zHWYNyObppV8ZXY0o3oHTw/DeleteCommunityMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditMembershipTypeQuery<br>
Request URL: `https://twitter.com/i/api/graphql/ruZM8GnBs_0uuSjWLF6nkw/EditMembershipTypeQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HashtagResultsCommunity_Query<br>
Request URL: `https://twitter.com/i/api/graphql/IqDv9dN3LO-GORp6lRMyoA/HashtagResultsCommunity_Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MemberRequests_Query<br>
Request URL: `https://twitter.com/i/api/graphql/WZkL3cX8Ht0d8TQO20Bk6w/MemberRequests_Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NotificationSettingsModalQuery<br>
Request URL: `https://twitter.com/i/api/graphql/d86C1tsqqQ-_2b7xStjYJQ/NotificationSettingsModalQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NotificationSettingsSaveButtonMutation<br>
Request URL: `https://twitter.com/i/api/graphql/GhfS-OCV4WH5I4aT2_i8jg/NotificationSettingsSaveButtonMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PeopleCommunity_Query<br>
Request URL: `https://twitter.com/i/api/graphql/t7j24Zrx2IjCj13ndCU2hA/PeopleCommunity_Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PrimaryContentQuery<br>
Request URL: `https://twitter.com/i/api/graphql/DPcSNOtovRKeAwtHAqwUlg/PrimaryContentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                 | type    |   variable | default   |
|:------------------------------------|:--------|-----------:|:----------|
| c9s_list_members_action_api_enabled | boolean |          0 | nan       |
| c9s_superc9s_indication_enabled     | ...     |        nan | error     |

#### queryId<br>
`None`<br>
## actions_approveMemberRequest_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/LVHUDWQ4jsU9iixwJUbT4Q/actions_approveMemberRequest_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## actions_denyMemberRequest_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/5AncQiBia2eEnbL_0_jYAA/actions_denyMemberRequest_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## communityPeopleActionMenu_roleUpdate_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/-z7ecfy5Y04vSJHD3xQ1aA/communityPeopleActionMenu_roleUpdate_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## edit_membershipSettings_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/YiJSKw8k6Mpy-pkVOwuQ7w/edit_membershipSettings_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## membersSliceTimeline_Query<br>
Request URL: `https://twitter.com/i/api/graphql/hLcguL_F3iWKoGbYxhlb4g/membersSliceTimeline_Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## moderatorsSliceTimeline_Query<br>
Request URL: `https://twitter.com/i/api/graphql/0MgU66yLfLlhaNQDFfQwzA/moderatorsSliceTimeline_Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## QuickPromoteLiteRecommendedKeywordsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/WQ2-bNb5RVhDy2g1Dc3DtA/QuickPromoteLiteRecommendedKeywordsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DelegateAlertBannerContainerQuery<br>
Request URL: `https://twitter.com/i/api/graphql/zuUTzlnI-XomL9lfWFqSKg/DelegateAlertBannerContainerQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DelegateQuery<br>
Request URL: `https://twitter.com/i/api/graphql/GhQlWgEZ8wKf_JimVEG-Yw/DelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GroupDetailDelegateQuery<br>
Request URL: `https://twitter.com/i/api/graphql/wukK4h-BcKgSGlEU-hAtng/GroupDetailDelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## GroupMenuMutation<br>
Request URL: `https://twitter.com/i/api/graphql/35IlHo3PPoKCgjGN9PyBEQ/GroupMenuMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GroupsDelegateQuery<br>
Request URL: `https://twitter.com/i/api/graphql/n1GJpi0gdaioyoc_xAocsA/GroupsDelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GroupsModalQuery<br>
Request URL: `https://twitter.com/i/api/graphql/p8Xg0Q4L4E08_SwyD-o8cg/GroupsModalQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## InviteMenu_accept_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/DpdMDix7rAjl6SVAs3SNSQ/InviteMenu_accept_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## InviteMenu_reject_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/QLNN5GVLRMe93lHnX3Um2w/InviteMenu_reject_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MembersDelegateQuery<br>
Request URL: `https://twitter.com/i/api/graphql/rbxOB044qx_iXNsD5vR1xQ/MembersDelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## useAddMemberModalMutation_add_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/SFV2FWbGnq-s473RcXrDsg/useAddMemberModalMutation_add_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useChangeMemberRoleModalMutation_change_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/bt_mUik7_sqXKofZmEBzAw/useChangeMemberRoleModalMutation_change_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useDelegateMutation_settings_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/2HD9lnvauHCbl4wRw2P_QQ/useDelegateMutation_settings_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useMemberMenuMutation_cancel_invite_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/QSkmmm7WG94DG9AfV2QHkg/useMemberMenuMutation_cancel_invite_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useMemberMenuMutation_remove_Mutation<br>
Request URL: `https://twitter.com/i/api/graphql/R8K9DRNeWen33po2wpZhZw/useMemberMenuMutation_remove_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AdsCategoriesMutation<br>
Request URL: `https://twitter.com/i/api/graphql/eRWyTnzFgPgv9D4W8ujf6A/AdsCategoriesMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AdsCategoriesQuery<br>
Request URL: `https://twitter.com/i/api/graphql/FO_KX1o77E3vYL14rATn9Q/AdsCategoriesQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/669l97INfasuMJpzgAZckA/MonetizationSettingsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RepliesGetUserToxicReplyFilterSettingQuery<br>
Request URL: `https://twitter.com/i/api/graphql/kmAhocLFK1cbzXxGq5Boow/RepliesGetUserToxicReplyFilterSettingQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useToggleToxicReplyFilterSettingMutation<br>
Request URL: `https://twitter.com/i/api/graphql/2DSpolLNDpVL7KDJ-UWHSg/useToggleToxicReplyFilterSettingMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BlueVerifiedProfileEditCalloutQuery<br>
Request URL: `https://twitter.com/i/api/graphql/myAwUDICwB5gFdJhNB7xsg/BlueVerifiedProfileEditCalloutQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SensitiveMediaSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/ft92vAsha0RhDxwgq_ojWQ/SensitiveMediaSettingsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useEditSensitiveMediaSettingsMutation<br>
Request URL: `https://twitter.com/i/api/graphql/YWGRWrle16Fb6JvAjvjoTQ/useEditSensitiveMediaSettingsMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSuperFollowsDeactivateMutation<br>
Request URL: `https://twitter.com/i/api/graphql/K5_KjMpjdtjQXzKGLqyFXw/useSuperFollowsDeactivateMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSuperFollowsSaveOnboardingMutation<br>
Request URL: `https://twitter.com/i/api/graphql/tYYBdo8fCA4AHLbLpVCjSg/useSuperFollowsSaveOnboardingMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationAwardsRevenueQuery<br>
Request URL: `https://twitter.com/i/api/graphql/kXcc0Edof6svF-lk2byuyg/MonetizationAwardsRevenueQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationAwardsSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/9aX5g4DnUZtOROAY-c4zxg/MonetizationAwardsSettingsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationAwardsTransactionsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/8S_of9efbNK7t-CL-jSZuQ/MonetizationAwardsTransactionsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationEarningsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/8ILEvKmsRdSCvMq03hkyjQ/MonetizationEarningsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationPayoutHistoryQuery<br>
Request URL: `https://twitter.com/i/api/graphql/7p0HY_Hd7ZcK3uXqAmAoSg/MonetizationPayoutHistoryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSuperFollowsNewSubscriptionsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/oDwDolKDS4GwnN9hXMk4mQ/MonetizationSuperFollowsNewSubscriptionsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSuperFollowsPerksQuery<br>
Request URL: `https://twitter.com/i/api/graphql/OBJmA_N_-QlXqicPhXWs3A/MonetizationSuperFollowsPerksQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSuperFollowsRenewalsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/hu8-2WbJu3mnli9ReDDA6A/MonetizationSuperFollowsRenewalsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSuperFollowsRevenueQuery<br>
Request URL: `https://twitter.com/i/api/graphql/lQxEoln7Xul4ElAtFi1qAQ/MonetizationSuperFollowsRevenueQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSuperFollowsSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/aFWWcodXU_NhvBbfkXjleQ/MonetizationSuperFollowsSettingsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSuperFollowsTransactionDetailsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/4VdTCYsekUxY02wIhS_cnw/MonetizationSuperFollowsTransactionDetailsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useAwardsDeactivateMutation<br>
Request URL: `https://twitter.com/i/api/graphql/01C9DqWmpi6YUNYaIWMBwA/useAwardsDeactivateMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SuperFollowsApplicationSubmitScreenMutation<br>
Request URL: `https://twitter.com/i/api/graphql/0cMDdco5hsmp1NHhuOtJtg/SuperFollowsApplicationSubmitScreenMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SuperFollowsOnboardingPricingConfirmScreenMutation<br>
Request URL: `https://twitter.com/i/api/graphql/_97mdj3S3wU106zmC8Wy3A/SuperFollowsOnboardingPricingConfirmScreenMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SuperFollowsSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/OvkCmdYEuNjNgFzGJOaiSw/SuperFollowsSettingsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSuperFollowsCreateStripeOnboardingUrlMutation<br>
Request URL: `https://twitter.com/i/api/graphql/KCzv96qeUky_-C22g3lZSw/useSuperFollowsCreateStripeOnboardingUrlMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AwardsSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/c_ww6XqjHvIqQAZWzaRR2g/AwardsSettingsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useAwardsActivateMutation<br>
Request URL: `https://twitter.com/i/api/graphql/ql0nbxLYZcgEQyw5Z0PlWw/useAwardsActivateMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AddParticipantsMutation<br>
Request URL: `https://twitter.com/i/api/graphql/oBwyQ0_xVbAQ8FAyG0pCRA/AddParticipantsMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DMReportMessageListQuery<br>
Request URL: `https://twitter.com/i/api/graphql/l-DPVCAJvDQio7Q1iZyapQ/DMReportMessageListQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## DelegateAlertBannerContainerQuery<br>
Request URL: `https://twitter.com/i/api/graphql/zuUTzlnI-XomL9lfWFqSKg/DelegateAlertBannerContainerQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileSpotlights_EditableProfileSpotlightsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/r3pgxpnbcR10hKon3pxNEg/ProfileSpotlights_EditableProfileSpotlightsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateProfileSpotlightVisibilityMutation<br>
Request URL: `https://twitter.com/i/api/graphql/mDq5tCOsuuDzxezaI30d3A/UpdateProfileSpotlightVisibilityMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## LocationSpotlightQuery<br>
Request URL: `https://twitter.com/i/api/graphql/PtT7DMn9eI8yFh-jkG-fGg/LocationSpotlightQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useDeleteLocationSpotlightMutation<br>
Request URL: `https://twitter.com/i/api/graphql/2ohYQLw6z3bqaCjSqs_LBQ/useDeleteLocationSpotlightMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useMapImageLoaderQuery<br>
Request URL: `https://twitter.com/i/api/graphql/1fFcufgOXV2EXGD578RpQw/useMapImageLoaderQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfessionalHomeQuery<br>
Request URL: `https://twitter.com/i/api/graphql/632WUqDqccL3BXgIjSn4aw/ProfessionalHomeQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ReportDetailQuery<br>
Request URL: `https://twitter.com/i/api/graphql/iDoo9-T00DI2oypZ0YmRNQ/ReportDetailQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ReportDetailSafetyCenterQuery<br>
Request URL: `https://twitter.com/i/api/graphql/1wRoskRvcqMJ66YJuIJVJA/ReportDetailSafetyCenterQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## LoggedOutSearchHomeTrendsListQuery<br>
Request URL: `https://twitter.com/i/api/graphql/jFSVxO6XekDkqa9LhEqxug/LoggedOutSearchHomeTrendsListQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TweetActivityQuery<br>
Request URL: `https://twitter.com/i/api/graphql/vnwexpl0q33_Bky-SROVww/TweetActivityQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                       | type    | variable   |
|:------------------------------------------|:--------|:-----------|
| responsive_web_tweet_analytics_m3_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## TweetCoinDetailsScreenQuery<br>
Request URL: `https://twitter.com/i/api/graphql/PkaL35ppw8P48oNr3vAU7g/TweetCoinDetailsScreenQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterBlueSignUpV2Query<br>
Request URL: `https://twitter.com/i/api/graphql/B7I5HPN6jm5Mgv9N8fgFPg/TwitterBlueSignUpV2Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterCoinsManagementCoinBalanceQuery<br>
Request URL: `https://twitter.com/i/api/graphql/7UIOQwnGlrNqaLd16fTwYg/TwitterCoinsManagementCoinBalanceQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TwitterCoinsManagementCoinPackQuery<br>
Request URL: `https://twitter.com/i/api/graphql/TtPtRW7yaLbnwCFJANYNFQ/TwitterCoinsManagementCoinPackQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useCoinPurchaseSessionUrlMutation<br>
Request URL: `https://twitter.com/i/api/graphql/QP5WVTrpvWikhlKybPX5jQ/useCoinPurchaseSessionUrlMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TrustedFriendsAddRemoveButtonAddMutation<br>
Request URL: `https://twitter.com/i/api/graphql/kz2e24ykUcLEssPne7Df-Q/TrustedFriendsAddRemoveButtonAddMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsAddRemoveButtonRemoveMutation<br>
Request URL: `https://twitter.com/i/api/graphql/Zv06okw7DQo4_O7nWyV-9g/TrustedFriendsAddRemoveButtonRemoveMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsMembersQuery<br>
Request URL: `https://twitter.com/i/api/graphql/xvgZLwKHLR_oc_PCZIeOTg/TrustedFriendsMembersQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsRecommendedQuery<br>
Request URL: `https://twitter.com/i/api/graphql/7iALzu_vGU0ELUrZR5mlwg/TrustedFriendsRecommendedQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## combinedListsPageTimelineQuery<br>
Request URL: `https://twitter.com/i/api/graphql/NghAx8ZgL1H3FSsc40AQ-A/combinedListsPageTimelineQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| blue_business_profile_image_shape_enabled                               | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| rweb_lists_timeline_redesign_enabled                                    | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| vibe_api_enabled                                                        | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |

#### queryId<br>
`None`<br>
## userNftContainer_Query<br>
Request URL: `https://twitter.com/i/api/graphql/z-_uxIiYELU35OzocPdDIw/userNftContainer_Query`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SuperFollowsManageQuery<br>
Request URL: `https://twitter.com/i/api/graphql/9wSLGuGXeq_zKNUZYEAF6Q/SuperFollowsManageQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSuperFollowsChangeBadgePrivacyAddMutation<br>
Request URL: `https://twitter.com/i/api/graphql/X6X4JiyQHfLz0SdTaZPixw/useSuperFollowsChangeBadgePrivacyAddMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSuperFollowsChangeBadgePrivacyRemoveMutation<br>
Request URL: `https://twitter.com/i/api/graphql/Mg-0dMrg-__WGhnWqj4nfQ/useSuperFollowsChangeBadgePrivacyRemoveMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSuperFollowsCreateStripePortalUrlMutation<br>
Request URL: `https://twitter.com/i/api/graphql/cot9fAsCQIQGNYu9Rica6w/useSuperFollowsCreateStripePortalUrlMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SuperFollowsSubscribeQuery<br>
Request URL: `https://twitter.com/i/api/graphql/RM_GpjWsezBynXW4N7VJWQ/SuperFollowsSubscribeQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                | type    | variable   |
|:---------------------------------------------------|:--------|:-----------|
| super_follow_subscriptions_tax_calculation_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## useSuperFollowsCreateStripeSubscriptionUrlMutation<br>
Request URL: `https://twitter.com/i/api/graphql/1nNykZ_aQohdxHKoykBVmg/useSuperFollowsCreateStripeSubscriptionUrlMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileSpotlightsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/9zwVLJ48lmVUk8u_Gh9DmA/ProfileSpotlightsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AffiliateListItemMutation<br>
Request URL: `https://twitter.com/i/api/graphql/QSueyUwwWLaV6s50Z8Ct4Q/AffiliateListItemMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AffiliateListItemUpdateAffiliateTypeMutation<br>
Request URL: `https://twitter.com/i/api/graphql/v5rNoNo7tAvWpUn6pIdo9A/AffiliateListItemUpdateAffiliateTypeMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AffiliatesScreenAffiliatesQuery<br>
Request URL: `https://twitter.com/i/api/graphql/TKK1gU40yLQfYj892YEu9g/AffiliatesScreenAffiliatesQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CancelModalMutation<br>
Request URL: `https://twitter.com/i/api/graphql/KZeNJv26eQ1JCIMbcwMXng/CancelModalMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PriceQuery<br>
Request URL: `https://twitter.com/i/api/graphql/X8Nj2SgEktmjI5dAiJnsIw/PriceQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TabBarCreateStripePortalUrlMutation<br>
Request URL: `https://twitter.com/i/api/graphql/Ro4_N0mgeE5CyS6oD_Y13w/TabBarCreateStripePortalUrlMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WelcomeScreenMutation<br>
Request URL: `https://twitter.com/i/api/graphql/vmeQkOLp4CLZ2zG0AgIe3A/WelcomeScreenMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WelcomeScreenQuery<br>
Request URL: `https://twitter.com/i/api/graphql/pjK2GUBF-ZmPvgo9qqBD-A/WelcomeScreenQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useAffiliatesAndInvitesQuery<br>
Request URL: `https://twitter.com/i/api/graphql/R23fc4rldc6jOdcv8u_nRw/useAffiliatesAndInvitesQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useCreateInvitationMutation<br>
Request URL: `https://twitter.com/i/api/graphql/1SlsDAsmE-7LDHGQf9KTcA/useCreateInvitationMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useDeleteInvitationMutation<br>
Request URL: `https://twitter.com/i/api/graphql/crOZy3iUFNLxqbq41GQ7pg/useDeleteInvitationMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FollowHostButtonQuery<br>
Request URL: `https://twitter.com/i/api/graphql/kURURMFUKw2d-eHgilgSzA/FollowHostButtonQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HighlightTweetSheetQuery<br>
Request URL: `https://twitter.com/i/api/graphql/j5-kjpQseTlPnVtfck8i_Q/HighlightTweetSheetQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PinTweetToCommunityMutation<br>
Request URL: `https://twitter.com/i/api/graphql/5jpFuDdu111UuWpne0_ajg/PinTweetToCommunityMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UnpinTweetFromCommunityMutation<br>
Request URL: `https://twitter.com/i/api/graphql/GJ-aDJmAPMnisHg-52fI3g/UnpinTweetFromCommunityMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
