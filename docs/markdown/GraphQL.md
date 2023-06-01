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
Request URL: `https://twitter.com/i/api/graphql/kcSC9DHDn8HImtYJCNLKnA/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
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
Request URL: `https://twitter.com/i/api/graphql/rKfRn_Qf3U79SMqGQ01s8A/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
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
Request URL: `https://twitter.com/i/api/graphql/qjxeunghOe7iRZQexNKZJw/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/P_Sp84IvEnCcfSlWDT7gMw/UsersVerifiedAvatars`<br>
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
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/KhvtrL1jfFK8fBym-whPDg/AudioSpaceById`<br>
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
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/cwhkg8kJlwFnAjVYoyyoxg/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/I5CLEkpNgGuIk0EoCGOzCg/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/q1oSUQEvoj18GdNkAotkEg/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/mweOMx9L55AZh2EMRH6veQ/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/Alw3vX9Xovg8Y5RlC5Nn2A/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/njO7h1NI2M3zE5yAE4fONA/BookmarkFolderTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/YNtYqNuki6_oiVwx0uP8mQ/Bookmarks`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |
| name                   | ...    | r          |

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
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/aFpS88_7jvnavdPVfHjUvQ/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/Pdpy2jIwNCqlcltorHszdw/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/1AHHi4xXA1jRMDNP3gX3DA/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/WSXkKig0PBiDBDTkJEEnVQ/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/5KG16XY88UO24eo_XME3dQ/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/80LepAaYM01f1_R_ysilwQ/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/x-UJnGLR4TkCPInvh66ryw/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/oWCWp-ZncUC9g0c3KJpaFw/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Xtj7OpiEDfzzCQ0E7qvX0g/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/yPahVR8oiEBB693uYK0-Jg/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/pv7GK3ICrUc9wddFPPHytw/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/10OLl9WxisO5Nf7y7MEU9A/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/9aKBNbBs_d2CE-VK_d-4cg/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/pB4E_vxw9QVd8ZWOd0bjvw/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/vRPaH8zDseJo0DR9ti75Wg/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/C_Zg8WWmUrOO-rt2cfYknA/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/A8gmwEIp7u0xwaZvDGMiMA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/4AzBLPMXjrB78z-7vY3sbg/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/DlKMwUaeLeFnL1Q96NGcdQ/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/Llx-gO8mDNUYti9FYlF0tA/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/C_BhKDystUBehagYAL7JHw/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/1rX09kfAcdABqyAfyVeSEg/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/yOIa2wr4jG8gXy7qoveK-g/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/UgX9mwVwNVWUlCNlPiLf1w/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/x7ZO9T3hxLo1o7da77rsmw/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/iz7ctjmKSd9pimwDEW3iBg/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/JlLZj42Ltr2qwjasw-l5lQ/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/U-QXVRZ6iddb1QuZweh5DQ/DmAllSearchSlice`<br>
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
Request URL: `https://twitter.com/i/api/graphql/SERzgce4BvXHB4J65f90Nw/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/fMp3izG_gCZKVk3Aa1vVKw/FetchDraftTweets`<br>
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
Request URL: `https://twitter.com/i/api/graphql/3EH_bBwETOB-daPmw6imFg/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/F_JKpQNE4br7h5x6zMniuQ/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ZJ6XSVn-ensPalXcfwCHZA/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ZqqafEXWWY8MdTOfNJmNGg/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/e_3T7eUhzCpZrb4BT8hVBA/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                              | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/MihMM6riIpCWMuSxKoLSwQ/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | n          |
| count        | ...    | t          |
| cursor       | ...    | i          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/27lfFOrDygiZs382QLttKA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| userId       | ...    | a          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/FDbUAQJgu0N4hekhvX7rgg/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/pSDf0Ki8JBv3v_hXkyE4wA/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| mediaId      | ...    | a          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/cvZq4Qw3Q47PXI4ShbZX4g/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| screenName   | ...    | n          |
| listSlug     | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/mti1h_AfzjbIeJLtKo-BXQ/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| isPrivate    | ...    | private===a.toLowerCase() |
| name         | ...    | o                         |
| description  | ...    | r                         |
| ...()(0,s.S) | ...    | _                         |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/bLw4CaM17YXCR0caQuQr6Q/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListEditRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/kWzfixCDBCmD3Q4b6p9Tjg/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ZBbXrl37E6za5ml-DIpmgg/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/a_ZQomd3MMk1crWkeiQBPg/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| listId                   | ...    | a           |
| count                    | ...    | n           |
| cursor                   | ...    | r           |
| ...()(0,s.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/b7y1-7qC0ATzhRQNpjG7kA/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | a          |
| count        | ...    | n          |
| cursor       | ...    | r          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/c2dFrAzxY-4C7EUK5s5gpQ/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | ...    | l          |
| isListMemberTargetUserId | ...    | a          |
| count                    | ...    | n          |
| cursor                   | ...    | r          |
| ...()(0,s.d)             | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/negrmqSqbhkDWZ1nldVDnQ/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | n          |
| ...r   | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://twitter.com/i/api/graphql/Fhd55uRVi2Vn0gBaEZi1zQ/ListPins`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/AmCdeFUvlrKAO96yHr-GCg/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | t.list_id  |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/USnBSpDYEaSz_SHzQG1uow/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | r          |
| count        | ...    | l          |
| cursor       | ...    | a          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/54V1srlLYeTs06l95sllWQ/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/kdLSflVgHzDZCzawpZ9KdA/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/HBZnb6By-HN2-dRmvqXlvA/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| count        | ...    | n          |
| cursor       | ...    | r          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| count        | ...    | l          |
| cursor       | ...    | a          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/pAcI57f2nvwn2V14rKBOMw/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | n          |
| ...r   | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/jC0GenNTH_xFYvkq4OMErQ/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/BjSP4hEJQ9ag9BCBTZJTKA/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| listId       | ...    | r                         |
| isPrivate    | ...    | private===_.toLowerCase() |
| description  | ...    | a                         |
| name         | ...    | d                         |
| ...()(0,s.S) | ...    | _                         |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/tCz50npFjE5qdUtx0oTE6A/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | n.communityId |
| ...()(0,a.S) | ...    | _             |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/8dSfkjFfJF9rHZ5QF1uVbA/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...n         | ...    | _          |
| ...()(0,a.S) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/mrQiqP_sYUwmQRYiLFUKtg/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | ...    | t.communityId |
| userId      | ...    | t.userId      |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/6JET1d0iHsIzW0Zjs3OOwQ/Likes`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/Hksg1U21aseTyyLTEHLGVg/UserAboutTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FV0kZL--JNrouJrvhsxz1A/UserBusinessProfileTeamTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/P_Bem6KC1MHpejV4rrcLLA/UserHighlightsTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/lo965xQZdN2-eSM1Jc-W_A/UserMedia`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/cLNqqXIgeRcVXRJw6w3ZtA/UserPromotableTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/INd_WXR4OAg0GuejVF61Tg/UserSuperFollowTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/-AY51QoFpVf-w7TxjQ6lpw/UserTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/urrCZMyyIh1FkSFi2cdPUA/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                              |
|:--------------------------|:--------|:--------------------------------------|
| userId                    | ...     | i                                     |
| count                     | ...     | t                                     |
| cursor                    | ...     | n                                     |
| includePromotedContent    | boolean | True                                  |
| withCommunity             | ...     | _.isTrue()                            |
| ...("c9s_enabled")(0,a.d) | ...     | _                                     |
| withVoice                 | ...     | _.isTrue(_)                           |
| withV2Timeline            | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
## BoostAudienceEstimate<br>
Request URL: `https://twitter.com/i/api/graphql/hiAXpFX4zFb6vOvGctGYyQ/BoostAudienceEstimate`<br>
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
Request URL: `https://twitter.com/i/api/graphql/3rmiAds7omMF--GeBb0mXA/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/wmMncHgLN-IQDsTIm-bimQ/RitoFlaggedAccountsTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qoU7UkTCwIEZPxCvEK_jAQ/RitoFlaggedTweetsTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/-6V0v8iYfMoJupVU_-NsLg/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ROpPuVpzI6SxUiKXTWb28w/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ALnoqeD9X5xuIvRvkIaCBQ/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | ...    | r          |
| cursor       | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/A_O1qU6E-Q__cKjIk9WTVw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"i","context":"JSON.stringify()"{"data_lookup_id":"r"}"0","a.d_"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/BGxEfw6QQ4ead2tKHP2ZfQ/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/vLzEJZqfuheKa98bG9slmw/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/Qw6jG80lSKzL3KeYyIf9og/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/6zcsC3P4gU4sGf62mhCz6w/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/nqSLPurFSIAiUR9ISUZewQ/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | o          |
| cursor       | ...    | r          |
| context      | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/leEkJQ6KH6dPJZgVJlA_YQ/Favoriters`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/1WUjEBo67tk9mDbj938yVQ/Retweeters`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/T8AhOGYPdl-zw79vVGbOJA/TweetEditHistory`<br>
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
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://twitter.com/i/api/graphql/qXufHbgVrj1zgudEgkf2sA/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/PnV3gU3RCu0t9lQvxgjSxQ/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/uObzwPvFeXgTSr1KStZD0Q/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/RIbWChxtc6BW9c9-XovHGQ/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/PkTko_5c0m1z6EyFOEAjFA/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/tpV-lOAuCrBRat_MVQPPlw/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/uhpI6D-NQdm6hrvXrouldw/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/HrqXlSuZFYbaXPCKzORs_Q/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/RcwJTxY-HoqYpgdHVBjCOA/TrustedFriendsTypeahead`<br>
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
## ConnectTabTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/0bvf3qBp4ur9RHHhZYTZEQ/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/IbdrLgj5b3HYrlhRUh25UA/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## ListSearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/oFeB5CR7z-LzgAHK-zl7CA/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/g18tCF-SH4HkOsP7_IL48w/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/UMmLW9HjT7jbPKgqMUjvsw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/C7l7QZTjKN5D1oaGMrqSyw/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_likes_enabled                                      | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/XA6F1nJELYg65hxOC2Ekmg/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_likes_enabled                                      | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| subscriptions_verification_info_verified_since_enabled            | boolean | True       |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/GD4q8bBE2i6cqWw2iT74Gg/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/k3027HdkVqbuDPpdoniLKA/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/-6V0v8iYfMoJupVU_-NsLg/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ROpPuVpzI6SxUiKXTWb28w/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/KhvtrL1jfFK8fBym-whPDg/AudioSpaceById`<br>
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
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/cwhkg8kJlwFnAjVYoyyoxg/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/I5CLEkpNgGuIk0EoCGOzCg/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/q1oSUQEvoj18GdNkAotkEg/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/mweOMx9L55AZh2EMRH6veQ/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/Alw3vX9Xovg8Y5RlC5Nn2A/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ol-H7n5CvkG8ua3aOmJWyA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/eGK0uOAEsAwI5LXhO_AwOw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/xjlfbSY0Lsz2sWbA4u0pQA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/njO7h1NI2M3zE5yAE4fONA/BookmarkFolderTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/YNtYqNuki6_oiVwx0uP8mQ/Bookmarks`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/e_3T7eUhzCpZrb4BT8hVBA/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                              | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/MihMM6riIpCWMuSxKoLSwQ/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | n          |
| count        | ...    | t          |
| cursor       | ...    | i          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/aFpS88_7jvnavdPVfHjUvQ/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/Pdpy2jIwNCqlcltorHszdw/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/1AHHi4xXA1jRMDNP3gX3DA/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/WSXkKig0PBiDBDTkJEEnVQ/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/5KG16XY88UO24eo_XME3dQ/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/80LepAaYM01f1_R_ysilwQ/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/4AzBLPMXjrB78z-7vY3sbg/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/x-UJnGLR4TkCPInvh66ryw/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/DlKMwUaeLeFnL1Q96NGcdQ/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/Llx-gO8mDNUYti9FYlF0tA/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/C_BhKDystUBehagYAL7JHw/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/1rX09kfAcdABqyAfyVeSEg/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://twitter.com/i/api/graphql/yOIa2wr4jG8gXy7qoveK-g/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/oWCWp-ZncUC9g0c3KJpaFw/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Xtj7OpiEDfzzCQ0E7qvX0g/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/yPahVR8oiEBB693uYK0-Jg/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/pv7GK3ICrUc9wddFPPHytw/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/10OLl9WxisO5Nf7y7MEU9A/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/9aKBNbBs_d2CE-VK_d-4cg/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/UgX9mwVwNVWUlCNlPiLf1w/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/x7ZO9T3hxLo1o7da77rsmw/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/iz7ctjmKSd9pimwDEW3iBg/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/pB4E_vxw9QVd8ZWOd0bjvw/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/vRPaH8zDseJo0DR9ti75Wg/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/C_Zg8WWmUrOO-rt2cfYknA/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/A8gmwEIp7u0xwaZvDGMiMA/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/0bvf3qBp4ur9RHHhZYTZEQ/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/F_JKpQNE4br7h5x6zMniuQ/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/U-QXVRZ6iddb1QuZweh5DQ/DmAllSearchSlice`<br>
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
Request URL: `https://twitter.com/i/api/graphql/SERzgce4BvXHB4J65f90Nw/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | False      |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |
| name                   | ...    | r          |

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
Request URL: `https://twitter.com/i/api/graphql/IbdrLgj5b3HYrlhRUh25UA/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/leEkJQ6KH6dPJZgVJlA_YQ/Favoriters`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/EAqBhgcGr_qPOzhS4Q3scQ/Followers`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FlqX2X2i-Ha4qQ7XiqCV0Q/FollowersYouKnow`<br>
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
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/JPZiqKjET7_M1r5Tlr8pyA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rootTweetId            | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/0_BVYO3k5ciXGCizGIvzXQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ZJ6XSVn-ensPalXcfwCHZA/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ZqqafEXWWY8MdTOfNJmNGg/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/3EH_bBwETOB-daPmw6imFg/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/6JET1d0iHsIzW0Zjs3OOwQ/Likes`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/27lfFOrDygiZs382QLttKA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| userId       | ...    | a          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/FDbUAQJgu0N4hekhvX7rgg/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/pSDf0Ki8JBv3v_hXkyE4wA/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| mediaId      | ...    | a          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/cvZq4Qw3Q47PXI4ShbZX4g/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| screenName   | ...    | n          |
| listSlug     | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/mti1h_AfzjbIeJLtKo-BXQ/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| isPrivate    | ...    | private===a.toLowerCase() |
| name         | ...    | o                         |
| description  | ...    | r                         |
| ...()(0,s.S) | ...    | _                         |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/bLw4CaM17YXCR0caQuQr6Q/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://twitter.com/i/api/graphql/fMp3izG_gCZKVk3Aa1vVKw/FetchDraftTweets`<br>
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
Request URL: `https://twitter.com/i/api/graphql/kWzfixCDBCmD3Q4b6p9Tjg/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ZBbXrl37E6za5ml-DIpmgg/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/a_ZQomd3MMk1crWkeiQBPg/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| listId                   | ...    | a           |
| count                    | ...    | n           |
| cursor                   | ...    | r           |
| ...()(0,s.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | _.isTrue(_) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/b7y1-7qC0ATzhRQNpjG7kA/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | a          |
| count        | ...    | n          |
| cursor       | ...    | r          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListOwnerships<br>
Request URL: `https://twitter.com/i/api/graphql/c2dFrAzxY-4C7EUK5s5gpQ/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | ...    | l          |
| isListMemberTargetUserId | ...    | a          |
| count                    | ...    | n          |
| cursor                   | ...    | r          |
| ...()(0,s.d)             | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/negrmqSqbhkDWZ1nldVDnQ/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | n          |
| ...r   | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://twitter.com/i/api/graphql/Fhd55uRVi2Vn0gBaEZi1zQ/ListPins`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AmCdeFUvlrKAO96yHr-GCg/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | t.list_id  |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/USnBSpDYEaSz_SHzQG1uow/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | r          |
| count        | ...    | l          |
| cursor       | ...    | a          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/54V1srlLYeTs06l95sllWQ/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/oFeB5CR7z-LzgAHK-zl7CA/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/kdLSflVgHzDZCzawpZ9KdA/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/HBZnb6By-HN2-dRmvqXlvA/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| count        | ...    | n          |
| cursor       | ...    | r          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| count        | ...    | l          |
| cursor       | ...    | a          |
| ...()(0,s.d) | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListUnpinOne<br>
Request URL: `https://twitter.com/i/api/graphql/pAcI57f2nvwn2V14rKBOMw/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | n          |
| ...r   | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/jC0GenNTH_xFYvkq4OMErQ/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/BjSP4hEJQ9ag9BCBTZJTKA/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| listId       | ...    | r                         |
| isPrivate    | ...    | private===_.toLowerCase() |
| description  | ...    | a                         |
| name         | ...    | d                         |
| ...()(0,s.S) | ...    | _                         |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/tCz50npFjE5qdUtx0oTE6A/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | n.communityId |
| ...()(0,a.S) | ...    | _             |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/8dSfkjFfJF9rHZ5QF1uVbA/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...n         | ...    | _          |
| ...()(0,a.S) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/mrQiqP_sYUwmQRYiLFUKtg/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | ...    | t.communityId |
| userId      | ...    | t.userId      |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                              | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/NHdnOGiiu2gRdgg-W77rdA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | n          |
| ...()(0,i.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/AzYwo5H3Ol9wTuxES3LIhg/MutedAccounts`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/ALnoqeD9X5xuIvRvkIaCBQ/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | ...    | r          |
| cursor       | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## BoostAudienceEstimate<br>
Request URL: `https://twitter.com/i/api/graphql/hiAXpFX4zFb6vOvGctGYyQ/BoostAudienceEstimate`<br>
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
Request URL: `https://twitter.com/i/api/graphql/1WUjEBo67tk9mDbj938yVQ/Retweeters`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/3rmiAds7omMF--GeBb0mXA/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/wmMncHgLN-IQDsTIm-bimQ/RitoFlaggedAccountsTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qoU7UkTCwIEZPxCvEK_jAQ/RitoFlaggedTweetsTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/g18tCF-SH4HkOsP7_IL48w/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qp7LqM_Ix2iKNKHy4gf3-Q/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                                         |
|:---------------------------|:-------|:-----------------------------------------------------------------|
| withCommunitiesMemberships | ...    | t.isTrue()                                                       |
| withSubscribedTab          | ...    | t.isTrue("c9s_enabled")                                          |
| withCommunitiesCreation    | ...    | t.isTrue("super_follow_subscriptions_home_timeline_tab_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/A_O1qU6E-Q__cKjIk9WTVw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"i","context":"JSON.stringify()"{"data_lookup_id":"r"}"0","a.d_"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/BGxEfw6QQ4ead2tKHP2ZfQ/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/vLzEJZqfuheKa98bG9slmw/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/Qw6jG80lSKzL3KeYyIf9og/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/6zcsC3P4gU4sGf62mhCz6w/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/RcwJTxY-HoqYpgdHVBjCOA/TrustedFriendsTypeahead`<br>
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
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/JlLZj42Ltr2qwjasw-l5lQ/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/T8AhOGYPdl-zw79vVGbOJA/TweetEditHistory`<br>
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
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/qXufHbgVrj1zgudEgkf2sA/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/PnV3gU3RCu0t9lQvxgjSxQ/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/uObzwPvFeXgTSr1KStZD0Q/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/RIbWChxtc6BW9c9-XovHGQ/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/PkTko_5c0m1z6EyFOEAjFA/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/tpV-lOAuCrBRat_MVQPPlw/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/uhpI6D-NQdm6hrvXrouldw/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/HrqXlSuZFYbaXPCKzORs_Q/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/UMmLW9HjT7jbPKgqMUjvsw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/Hksg1U21aseTyyLTEHLGVg/UserAboutTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/FV0kZL--JNrouJrvhsxz1A/UserBusinessProfileTeamTimeline`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/C7l7QZTjKN5D1oaGMrqSyw/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_likes_enabled                                      | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/XA6F1nJELYg65hxOC2Ekmg/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_likes_enabled                                      | boolean | False      |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| subscriptions_verification_info_verified_since_enabled            | boolean | True       |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
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
## UserCreatorSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/hq4IiNy2V-Bt9WSZOuYQBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | l          |
| count                  | ...     | n          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,o.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/nvdL4-mc_83rX7j9KlTlSQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | i          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/P_Bem6KC1MHpejV4rrcLLA/UserHighlightsTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/lo965xQZdN2-eSM1Jc-W_A/UserMedia`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/cLNqqXIgeRcVXRJw6w3ZtA/UserPromotableTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/INd_WXR4OAg0GuejVF61Tg/UserSuperFollowTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/-AY51QoFpVf-w7TxjQ6lpw/UserTweets`<br>
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/urrCZMyyIh1FkSFi2cdPUA/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                              |
|:--------------------------|:--------|:--------------------------------------|
| userId                    | ...     | i                                     |
| count                     | ...     | t                                     |
| cursor                    | ...     | n                                     |
| includePromotedContent    | boolean | True                                  |
| withCommunity             | ...     | _.isTrue()                            |
| ...("c9s_enabled")(0,a.d) | ...     | _                                     |
| withVoice                 | ...     | _.isTrue(_)                           |
| withV2Timeline            | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/GD4q8bBE2i6cqWw2iT74Gg/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/k3027HdkVqbuDPpdoniLKA/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/S4icxY2BbBgyUPd_soBLng/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/nqSLPurFSIAiUR9ISUZewQ/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | o          |
| cursor       | ...    | r          |
| context      | ...    | i          |
| ...()(0,a.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/zxG-O9zRtbFLf2q2JDzzSQ/managementListsPageTimelineQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| view_counts_everywhere_api_enabled                                      | boolean | True       |

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
Request URL: `https://twitter.com/i/api/graphql/gmCQ4dGVEts-aUSUENQWdQ/CommunitiesFetchOneQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsRecentQuery<br>
Request URL: `https://twitter.com/i/api/graphql/Xka10709FHpbHWqJFVZoeg/CommunitiesMembershipsRecentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## UsersGraphQLFetchByScreenNameQuery<br>
Request URL: `https://twitter.com/i/api/graphql/EjTjgF4MfoBg7pEmhIAmHg/UsersGraphQLFetchByScreenNameQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesFetchOneQuery<br>
Request URL: `https://twitter.com/i/api/graphql/gmCQ4dGVEts-aUSUENQWdQ/CommunitiesFetchOneQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsRecentQuery<br>
Request URL: `https://twitter.com/i/api/graphql/Xka10709FHpbHWqJFVZoeg/CommunitiesMembershipsRecentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## UsersGraphQLFetchByScreenNameQuery<br>
Request URL: `https://twitter.com/i/api/graphql/EjTjgF4MfoBg7pEmhIAmHg/UsersGraphQLFetchByScreenNameQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
## TargetingKeywordsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/8Sm_SjESFOaQfO9tUJHB2A/TargetingKeywordsQuery`<br>
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
## HiddenLikesTabSettingsMutation<br>
Request URL: `https://twitter.com/i/api/graphql/VKbNUE3NwVCyM1vVHhyLPQ/HiddenLikesTabSettingsMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HiddenLikesTabSettingsQuery<br>
Request URL: `https://twitter.com/i/api/graphql/J9In7cq0qeok1s5Rvlnwug/HiddenLikesTabSettingsQuery`<br>
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
Request URL: `https://twitter.com/i/api/graphql/GyO1NLi_48MlLDhWq-iIfg/DMReportMessageListQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
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
Request URL: `https://twitter.com/i/api/graphql/6Pd1nMGg7tVGqe-83LGSTA/combinedListsPageTimelineQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
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
| rweb_lists_timeline_redesign_enabled                                    | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
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
Request URL: `https://twitter.com/i/api/graphql/cwNDNtLO0yfGhoXuZM4_sA/SuperFollowsSubscribeQuery`<br>
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
## useAffiliatesPriceQuery<br>
Request URL: `https://twitter.com/i/api/graphql/kJbxZev65xXg-ADhCUhw1w/useAffiliatesPriceQuery`<br>
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
