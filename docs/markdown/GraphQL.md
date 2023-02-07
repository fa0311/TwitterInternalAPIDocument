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
Request URL: `https://api.twitter.com/graphql/pROR-yRiBVsEjJyHt3fvhg/BakeryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UsersVerifiedAvatars<br>
Request URL: `https://api.twitter.com/graphql/Bjbv9tA3kxsmhHDy_4yImw/UsersVerifiedAvatars`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| blue_business_consumption_api_enabled                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/wh2NGLu0MrP0pcmEC7NknA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/P8cwDQU_0LnMZDiH6E0_sw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | r          |
| mediaId      | ...    | s          |
| ...()(0,a.S) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/SPHShnVTjIQyYDlpHnlCVA/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable      |
|:---------------------------|:-------|:--------------|
| userIds                    | ...    | a.split()     |
| withSuperFollowsUserFields | ...    | l.isTrue(",") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://api.twitter.com/graphql/YvtGAR1HE3u53A1f5SNbTg/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable                                                         |
|:-----------------|:-------|:-----------------------------------------------------------------|
| twitterArticleId | ...    | s                                                                |
| data             | ...    | {'content_state_json': 'a', 'plaintext': 'l', 'word_count': 'd'} |
| ...()(0,n.d)     | ...    | _                                                                |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/quZ3LfJwtiIAsSIhk6cUNQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key            | type   | variable   |
|:---------------|:-------|:-----------|
| target_user_id | ...    | l          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/3TV0vBEpVhoknHxnUA5c9w/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| listId | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/IDoOeQV6wdTAEh85rYbkIg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| title            | ...    | a          |
| ...()(0,n.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/PHcyk8SMl8F8Nxgmakmd1A/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | a          |
| visibility       | ...    | l          |
| ...()(0,n.d)     | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/Ruenl2JMIfTqN6FYTEfc_Q/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| screen_name                | ...    | a                                                    |
| withSafetyModeUserFields   | ...    | l.isTrue()                                           |
| withSuperFollowsUserFields | ...    | l.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/SBRXnVA0KjOtv2XkCSuXVA/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable   |
|:-------------------------|:-------|:-----------|
| userId                   | ...    | l          |
| isListMemberTargetUserId | ...    | s          |
| count                    | ...    | n          |
| cursor                   | ...    | r          |
| ...()(0,a.d)             | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/fdeoKcRr0pMdo01JY-Vtiw/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type   | variable      |
|:--------------|:-------|:--------------|
| tweet_id      | ...    | r             |
| reaction_type | ...    | i             |
| ...()&&       | ...    | {'...t': '_'} |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DisableUserAccountLabel<br>
Request URL: `https://api.twitter.com/graphql/_ckHEj05gan2VfNHG6thBA/DisableUserAccountLabel`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserAccountLabel<br>
Request URL: `https://api.twitter.com/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## adFreeArticleDomains<br>
Request URL: `https://api.twitter.com/graphql/zwTrX9CtnMvWlBXjsx95RQ/adFreeArticleDomains`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## articleNudgeDomains<br>
Request URL: `https://api.twitter.com/graphql/88Bu08U2ddaVVjKmmXjVYg/articleNudgeDomains`<br>
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
Request URL: `https://api.twitter.com/graphql/h0y6YMZmsBvOAiXZRCwfag/AudioSpaceById`<br>
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
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceSearch<br>
Request URL: `https://api.twitter.com/graphql/NTq79TuSz6fHj8lQaferJw/AudioSpaceSearch`<br>
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
Request URL: `https://api.twitter.com/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
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
Request URL: `https://api.twitter.com/graphql/Zevhh76Msw574ZSs2NQHGQ/UnsubscribeFromScheduledSpace`<br>
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
Request URL: `https://api.twitter.com/graphql/3ss48WFwGokBH_gj8t_8aQ/BirdwatchAliasSelect`<br>
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
Request URL: `https://api.twitter.com/graphql/sLE-6pvzKFZ8NzB-IjS7OA/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateAppeal<br>
Request URL: `https://api.twitter.com/graphql/TKdL0YFsX4DMOpMKeneLvA/BirdwatchCreateAppeal`<br>
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
Request URL: `https://api.twitter.com/graphql/LHKIJ56KN4IIAaF4XXsdlA/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateRating<br>
Request URL: `https://api.twitter.com/graphql/xWLuzZoATvfEIEGxnsLt7w/BirdwatchCreateRating`<br>
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
Request URL: `https://api.twitter.com/graphql/IKS_qrShkDyor6Ri1ahd9g/BirdwatchDeleteNote`<br>
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
Request URL: `https://api.twitter.com/graphql/OpvCOyOoQClUND66zDzrnA/BirdwatchDeleteRating`<br>
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
Request URL: `https://api.twitter.com/graphql/FLgLReVIssXjB_ui3wcrRQ/BirdwatchEditNotificationSettings`<br>
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
Request URL: `https://api.twitter.com/graphql/szoXMke8AZOErso908iglw/BirdwatchFetchAliasSelfSelectOptions`<br>
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
Request URL: `https://api.twitter.com/graphql/LUEdtkcpBlGktUtms4BvwA/BirdwatchFetchAliasSelfSelectStatus`<br>
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
Request URL: `https://api.twitter.com/graphql/pMbW6Y4LuS5MzlSOEqERJQ/BirdwatchFetchAuthenticatedUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://api.twitter.com/graphql/btgGtchypc3D491MJ7XXWA/BirdwatchFetchBirdwatchProfile`<br>
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
Request URL: `https://api.twitter.com/graphql/jP51Qc9ntknUjTmSJOedcg/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://api.twitter.com/graphql/dzGQATA7a74xHfX7fEH0AA/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://api.twitter.com/graphql/DNVXaV7c8BnuXp3gBo_dqQ/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://api.twitter.com/graphql/9bDdJ6AL26RLkcUShEcF-A/BirdwatchFetchPublicData`<br>
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
Request URL: `https://api.twitter.com/graphql/cED9wJy8Nd1kZCCYuIq9zQ/BirdwatchProfileAcknowledgeEarnOut`<br>
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
Request URL: `https://api.twitter.com/graphql/6OFpJ3TH3p8JpwOSgfgyhg/BizProfileFetchUser`<br>
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
Request URL: `https://api.twitter.com/graphql/I0RlmftJieYXRCuAF3A0iw/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| bookmark_collection_id | ...     | t          |
| cursor                 | ...     | r          |
| includePromotedContent | boolean | True       |
| ...()(0,n.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://api.twitter.com/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                | type   | variable   |
|:-------------------|:-------|:-----------|
| post_tweet_request | ...    | i          |
| execute_at         | ...    | p()        |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://api.twitter.com/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
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
Request URL: `https://api.twitter.com/graphql/IUOUPtM9QEK2laNG2wwuyQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://api.twitter.com/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
Request URL: `https://api.twitter.com/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
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
Request URL: `https://api.twitter.com/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| mediaKeys        | ...    | a          |
| ...()(0,n.d)     | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EditBookmarkFolder<br>
Request URL: `https://api.twitter.com/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
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
Request URL: `https://api.twitter.com/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
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
## CheckTweetForNudge<br>
Request URL: `https://api.twitter.com/graphql/C2dcvh7H69JALtomErxWlA/CheckTweetForNudge`<br>
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
Request URL: `https://api.twitter.com/graphql/hb1elGcj6769uT8qVYqtjw/ConversationControlChange`<br>
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
Request URL: `https://api.twitter.com/graphql/OoMO_aSZ1ZXjegeamF9QmA/ConversationControlDelete`<br>
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
Request URL: `https://api.twitter.com/graphql/aoDbu3RHznuiSkQ9aNM67Q/CreateBookmark`<br>
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
Request URL: `https://api.twitter.com/graphql/eE18XrbyYsLkBwmXB6oO1Q/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://api.twitter.com/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
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
Request URL: `https://api.twitter.com/graphql/pTlmPgesqtCzLeWNTVORjA/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateTweetDownvote<br>
Request URL: `https://api.twitter.com/graphql/Eo65jl-gww30avDgrXvhUA/CreateTweetDownvote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateTweetReaction<br>
Request URL: `https://api.twitter.com/graphql/D7M6X3h4-mJE8UB1Ap3_dQ/CreateTweetReaction`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteBookmark<br>
Request URL: `https://api.twitter.com/graphql/Wlmlj2-xzyS1GN3a6cj-mQ/DeleteBookmark`<br>
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
Request URL: `https://api.twitter.com/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
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
Request URL: `https://api.twitter.com/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweetDownvote<br>
Request URL: `https://api.twitter.com/graphql/VNEvEGXaUAMfiExP8Tbezw/DeleteTweetDownvote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteTweetReaction<br>
Request URL: `https://api.twitter.com/graphql/GKwK0Rj4EdkfwdHQMZTpuw/DeleteTweetReaction`<br>
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
Request URL: `https://api.twitter.com/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/pjFnHGVqCjTcZol0xcBJjw/ModerateTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/AIVjXMOFBZDymOvIDuBk6Q/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnfavoriteTweet<br>
Request URL: `https://api.twitter.com/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/xVW9j3OqoBRY9d6_2OONEg/UnmentionUserFromConversation`<br>
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
Request URL: `https://api.twitter.com/graphql/pVSyu6PA57TLvIE4nN2tsA/UnmoderateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## LiveCommerceItemsSlice<br>
Request URL: `https://api.twitter.com/graphql/-lnNX56S2YrZYrLzbccFAQ/LiveCommerceItemsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://api.twitter.com/graphql/kicP8-K6i8KHv5v9WauS1Q/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://api.twitter.com/graphql/ZzQeju2gCfwtVXivFeIkaQ/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://api.twitter.com/graphql/tW8ifM7xeB_BjQ0F0D5FFg/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://api.twitter.com/graphql/PDPVXp70LISutwEfZongKw/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://api.twitter.com/graphql/1Liz5OFSKeoue-ojDrh2kQ/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://api.twitter.com/graphql/JFTE4IPoU0ANdKUWab2_cQ/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://api.twitter.com/graphql/-eCYLCo-souXl0DINdr8Yw/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://api.twitter.com/graphql/NTWQz2zvUeHO31bPYpEX0Q/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://api.twitter.com/graphql/k-w6wL43zMRDTneFh9ildA/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://api.twitter.com/graphql/hoJEVjoGqcfSkF4HFLRXeg/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://api.twitter.com/graphql/R3kU7B-EpeYMSOslGE88vw/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://api.twitter.com/graphql/GEjxvhhq7XNgbD4N8ovTmA/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://api.twitter.com/graphql/4kW8gwpk-4bnY9I_NZfwwA/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://api.twitter.com/graphql/UizTkXQ94XjzHBpifcGg9A/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedTimeline<br>
Request URL: `https://api.twitter.com/graphql/VuX0XrvJUtBOhzq0O9IlFA/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/FWtICXlK6GXhqHNVEyxRPA/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://api.twitter.com/graphql/HM2K9P2V92ZdqFP4AMT7jQ/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://api.twitter.com/graphql/el2xSrgrXBxyWvbz193qaA/CommunityUserInvite`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://api.twitter.com/graphql/dQsl5Q68YwUa8Ph9GwLaEw/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| name         | ...    | t.name        |
| description  | ...    | t.description |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://api.twitter.com/graphql/8tnhUj-wa7p7k2_QOC_BxA/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| mediaId      | ...    | t.mediaId     |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://api.twitter.com/graphql/Z0pp0d9vmrll0_ywwJIeqw/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| name         | ...    | t.name        |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://api.twitter.com/graphql/2g7EqJcObpAwSn3fkScXcQ/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| description  | ...    | t.purpose     |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://api.twitter.com/graphql/tZK8XZ7G9CPG8cZv27G4oA/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| ruleId       | ...    | t.ruleId      |
| name         | ...    | t.name        |
| description  | ...    | t.description |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditTheme<br>
Request URL: `https://api.twitter.com/graphql/1lNrl9dY-yJLG0Zw6NrHaA/CommunityEditTheme`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| theme        | ...    | t.theme       |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://api.twitter.com/graphql/pd1vTq0TJCPHsr0YQkSyZQ/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://api.twitter.com/graphql/-Ag6oWT6LKTCj6SZB1E8fw/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| ruleId       | ...    | t.ruleId      |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://api.twitter.com/graphql/vllQsJumMfQSePmGNExAGQ/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| ruleIds      | ...    | t.ruleIds     |
| ...()(0,r.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://api.twitter.com/graphql/9Urn0VM6X5qXUa0UdFPFlg/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/zW35Uw0TWaXEmoqC-N3ZKg/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/5zpY1dCR-8NyxQJS_CFJoQ/DmGroupSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://api.twitter.com/graphql/EiCgpMysjPFUo1xAIn-PSQ/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DismissRitoSuggestedAction<br>
Request URL: `https://api.twitter.com/graphql/jYvwa61cv3NwNP24iUru6g/DismissRitoSuggestedAction`<br>
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
Request URL: `https://api.twitter.com/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/JIeXE-I6BZXHfxsgOkyHYQ/EditDraftTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/ZkqIq_xRhiUme0PBJNpRtg/FetchDraftTweets`<br>
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
Request URL: `https://api.twitter.com/graphql/2qKKYFQift8p5-J1k6kqxQ/WriteEmailNotificationSettings`<br>
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
Request URL: `https://api.twitter.com/graphql/JpjlNgn4sLGvS6tgpTzYBg/ViewerEmailSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ForYouExplore<br>
Request URL: `https://api.twitter.com/graphql/HktnjY8qgjTDn22PwzbUQQ/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://api.twitter.com/graphql/KRmmYYpv909IZPAQpfwK_A/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GraphQLError<br>
Request URL: `https://api.twitter.com/graphql/2V2W3HIBuMW83vEMtfo_Rg/GraphQLError`<br>
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
Request URL: `https://api.twitter.com/graphql/uB6qU4XgrS0yKOOi-Jc4HA/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://api.twitter.com/graphql/S4iaTnJcz9D0okXNpp8UMQ/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://api.twitter.com/graphql/QtKsPe9RTZUXZasRycrtpQ/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| tweetText | ...    | s          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                              | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://api.twitter.com/graphql/tzTK9J9c_9Wby9f4c-sZcg/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://api.twitter.com/graphql/_Pt6770IB5l0EzHDQLl9Fg/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://api.twitter.com/graphql/YoKSVpBkQwzHECX8ourzXA/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://api.twitter.com/graphql/wcpjdM5IuK0VSn3ivPkcxg/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://api.twitter.com/graphql/_DWzU0badVARuVM1DYKzSw/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://api.twitter.com/graphql/KSSGXzhn5_gBcqRqzKJF1g/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://api.twitter.com/graphql/IQkfLawtVpXJE7VZ7HnhqA/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DeleteList<br>
Request URL: `https://api.twitter.com/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList`<br>
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
Request URL: `https://api.twitter.com/graphql/FMRJ75ByL0a0d2IoOFTN2Q/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/739-lYeTXXN3JzRHCTDQ0g/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://api.twitter.com/graphql/kofaAT0XHlnuefvuR4OC8A/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://api.twitter.com/graphql/e4dazW4ShhT6ogL8jknwQg/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MuteList<br>
Request URL: `https://api.twitter.com/graphql/ZYyanJsskNUcltu9bliMLA/MuteList`<br>
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
Request URL: `https://api.twitter.com/graphql/Ad9zP929OePgGxr4dJcUWg/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://api.twitter.com/graphql/rxurtlh9mCqJMnIp59xpiw/ListPinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListPins<br>
Request URL: `https://api.twitter.com/graphql/kwoti6srsk6bagtnybeqLg/ListPins`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://api.twitter.com/graphql/liQAJt9RifTEHURLplkqoA/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/GnfJpHEiV3O8-NzJXNdHdA/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://api.twitter.com/graphql/5p9ddA6v33r5_dYEgXJEEg/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://api.twitter.com/graphql/GwHRo2jedf4PfGDBGCdmvw/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://api.twitter.com/graphql/ng69mE5nrzbv7nFQfxgSgg/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnmuteList<br>
Request URL: `https://api.twitter.com/graphql/pMZrHRNsmEkXgbn3tOyr7Q/UnmuteList`<br>
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
Request URL: `https://api.twitter.com/graphql/utTr6yFFHtGKMDCihDNB8w/ListUnpinOne`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListUnsubscribe<br>
Request URL: `https://api.twitter.com/graphql/avVC2YTwi7Zc2qygTRRTfQ/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://api.twitter.com/graphql/0cCBb9Lyg9FJND02Z-arxQ/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://api.twitter.com/graphql/pm4CI79hwDzjMx7HFPwKzA/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://api.twitter.com/graphql/nobN-YSF4ipfXtYhQotATg/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://api.twitter.com/graphql/rSuFDOnU_-BLIO6G6KsQnA/ListsPinMany`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EnableLoggedOutWebNotifications<br>
Request URL: `https://api.twitter.com/graphql/BqIHKmwZKtiUBPi07jKctg/EnableLoggedOutWebNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PinReply<br>
Request URL: `https://api.twitter.com/graphql/GA2_1uKP9b_GyR4MVAQXAw/PinReply`<br>
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
Request URL: `https://api.twitter.com/graphql/iRe6ig5OV1EzOtldNIuGDQ/UnpinReply`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://api.twitter.com/graphql/jfgOtixrw3HNetx5aXBAcw/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://api.twitter.com/graphql/YMKyu5FADmnssxjcnBSjaw/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://api.twitter.com/graphql/r4VaQyR5QuWkKasEoCEkUQ/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://api.twitter.com/graphql/kLETGqO_uOt9dLJdC-J-mw/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://api.twitter.com/graphql/c5VMAz-0Ki0MIjAFxlgeaA/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserSuperFollowTweets<br>
Request URL: `https://api.twitter.com/graphql/Tml08EMRGi8BDWftATi2dQ/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://api.twitter.com/graphql/CKcd91tn0Zb0oO1jHxFmxA/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://api.twitter.com/graphql/RXmIZJyoYG44nu0XNgUSsQ/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SetDefault<br>
Request URL: `https://api.twitter.com/graphql/QEMLEzEMzoPNbeauKCCLbg/SetDefault`<br>
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
Request URL: `https://api.twitter.com/graphql/VaaLGwK5KNLoc7wsOmp4uw/DeletePaymentMethod`<br>
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
Request URL: `https://api.twitter.com/graphql/mPF_G9okpbZuLcD6mN8K9g/PaymentMethods`<br>
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
Request URL: `https://api.twitter.com/graphql/a8KxGfFQAmm3WxqemuqSRA/AdAccounts`<br>
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
Request URL: `https://api.twitter.com/graphql/1LYVUabJBYkPlUAWRabB3g/AudienceEstimate`<br>
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
Request URL: `https://api.twitter.com/graphql/mbK3oSQotwcJXyQIBE3uYw/Budgets`<br>
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
Request URL: `https://api.twitter.com/graphql/R1h43jnAl2bsDoUkgZb7NQ/Coupons`<br>
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
Request URL: `https://api.twitter.com/graphql/oDSoVgHhJxnd5IkckgPZdg/CreateQuickPromotion`<br>
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
Request URL: `https://api.twitter.com/graphql/LtpCXh66W-uXh7u7XSRA8Q/QuickPromoteEligibility`<br>
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
Request URL: `https://api.twitter.com/graphql/SOyGmNGaEXcvk15s5bqDrA/EnrollCoupon`<br>
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
Request URL: `https://api.twitter.com/graphql/vp-HquqeKTzfSDfCnVofrQ/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://api.twitter.com/graphql/PcvShP7arPJXFTqqtRyH4A/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/UUBoiYx0Yn0HX5_b7PejZQ/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoSuggestedActionsFacePile<br>
Request URL: `https://api.twitter.com/graphql/GnQKeEdL1LyeK3dTQCS1yw/RitoSuggestedActionsFacePile`<br>
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
Request URL: `https://api.twitter.com/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/CTOVqej0JBXAZSwkp1US0g/DeleteScheduledTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/ITtjAzvlZni2wWXwf295Qg/FetchScheduledTweets`<br>
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
Request URL: `https://api.twitter.com/graphql/g2m0pAOamawNtVIfjXNMJg/DisableVerifiedPhoneLabel`<br>
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
Request URL: `https://api.twitter.com/graphql/C3RJFfMsb_KcEytpKmRRkw/EnableVerifiedPhoneLabel`<br>
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
Request URL: `https://api.twitter.com/graphql/5kUWP8C1hcd6omvg6HXXTQ/ProfileUserPhoneState`<br>
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
Request URL: `https://api.twitter.com/graphql/vJ-XatpmQSG8bDch8-t9Jw/UserSessionsList`<br>
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
Request URL: `https://api.twitter.com/graphql/PFIxTk8owMoZgiMccP0r4g/getAltTextPromptPreference`<br>
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
Request URL: `https://api.twitter.com/graphql/aQKrduk_DA46XfOQDkcEng/updateAltTextPromptPreference`<br>
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
Request URL: `https://api.twitter.com/graphql/BwgMOGpOViDS0ri7VUgglg/getCaptionsAlwaysDisplayPreference`<br>
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
Request URL: `https://api.twitter.com/graphql/uCUQhvZ5sJ9qHinRp6CFlQ/updateCaptionsAlwaysDisplayPreference`<br>
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
Request URL: `https://api.twitter.com/graphql/xF6sXnKJfS2AOylzxRjf6A/DataSaverMode`<br>
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
Request URL: `https://api.twitter.com/graphql/H03etWvZGz41YASxAU2YPg/WriteDataSaverPreferences`<br>
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
Request URL: `https://api.twitter.com/graphql/of_N6O33zfyD4qsFJMYFxA/DmNsfwMediaFilterUpdate`<br>
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
Request URL: `https://api.twitter.com/graphql/AhxTX0lkbIos4WG53xwzSA/GetSafetyModeSettings`<br>
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
Request URL: `https://api.twitter.com/graphql/qSJIPIpf4gA7Wn21bT3D4w/SetSafetyModeSettings`<br>
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
Request URL: `https://api.twitter.com/graphql/5h0kNbk3ii97rmfY6CdgAA/SharingAudiospacesListeningDataWithFollowersUpdate`<br>
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
Request URL: `https://api.twitter.com/graphql/lFi3xnx0auUUnyG4YwpCNw/GetUserClaims`<br>
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
Request URL: `https://api.twitter.com/graphql/2LHXrd1uYeaMWhciZgPZFw/CreateCustomerPortalSession`<br>
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
Request URL: `https://api.twitter.com/graphql/wwdBYgScze0_Jnan79jEUw/ListProductSubscriptions`<br>
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
Request URL: `https://api.twitter.com/graphql/hKfOOObQr5JmfmxW0YtPvg/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://api.twitter.com/graphql/GZF6Vha91bWrZjDmZZ-VNA/SubscriptionProductDetails`<br>
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
Request URL: `https://api.twitter.com/graphql/-btar_vkBwWA7s3YWfp_9g/FeatureSettingsUpdate`<br>
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
Request URL: `https://api.twitter.com/graphql/Me2CVcAXxvK2WMr-Nh_Qqg/SubscriptionProductFeaturesFetch`<br>
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
Request URL: `https://api.twitter.com/graphql/TXNbVIgcVuATxNfx2t3fZA/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...t                | ...    | _          |
| ...()(0,r.d)        | ...    | _          |
| articleListSeedType | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/b0lhI9swFfVDggq3xINpDQ/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...t                | ...    | _          |
| ...()(0,r.d)        | ...    | _          |
| articleListSeedType | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://api.twitter.com/graphql/frg3cVKofEtRyMZQRFam4g/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| rest_id      | ...    | a          |
| cursor       | ...    | _          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicFollow<br>
Request URL: `https://api.twitter.com/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
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
Request URL: `https://api.twitter.com/graphql/5j54XULzzn9gYYV_4o4-GQ/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"o","cursor":"_","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","r.di"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://api.twitter.com/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
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
Request URL: `https://api.twitter.com/graphql/4OUZZOonV2h60I0wdlQb_w/TopicByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| topicId | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://api.twitter.com/graphql/-M17kxFyZfAGMsdmAat1kw/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | _          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://api.twitter.com/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
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
Request URL: `https://api.twitter.com/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
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
Request URL: `https://api.twitter.com/graphql/XOekghho2P2hsywFXuzJrg/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | ...    | _          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://api.twitter.com/graphql/Ba3hd01UmE5Ko5jnQTUOxA/TopicsPickerPage`<br>
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
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://api.twitter.com/graphql/0sG-VDMZD5rKfQJqtm3-EQ/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | ...    | _          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://api.twitter.com/graphql/qzpa9rOP572bI7_E_t0rlw/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| userId       | ...    | o          |
| cursor       | ...    | a          |
| context      | ...    | _          |
| ...()(0,r.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AuthenticatedUserTFLists<br>
Request URL: `https://api.twitter.com/graphql/QjN8ZdavFDqxUjNn3r9cig/AuthenticatedUserTFLists`<br>
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
Request URL: `https://api.twitter.com/graphql/2tP8XUYeLHKjq5RHvuvpZw/CreateTrustedFriendsList`<br>
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
Request URL: `https://api.twitter.com/graphql/Wr1Rk_fMameEt5H5l8s-8Q/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://api.twitter.com/graphql/WauXLKiC63Mg_xjn3Nbpvw/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://api.twitter.com/graphql/LX-MqIcSA6SDWpETtigA8A/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://api.twitter.com/graphql/OBV8ZtjXrdCKFk8Lov2VkQ/GetTweetReactionTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://api.twitter.com/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                             | type    | variable   |
|:------------------------------------------------|:--------|:-----------|
| profile_foundations_tweet_stats_enabled         | boolean | False      |
| profile_foundations_tweet_stats_tweet_frequency | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleCreate<br>
Request URL: `https://api.twitter.com/graphql/U9C3l0cL7SblfEREFtB6kA/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleDelete<br>
Request URL: `https://api.twitter.com/graphql/6st-stMDc7KBqLT8KvWhHg/TwitterArticleDelete`<br>
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
Request URL: `https://api.twitter.com/graphql/cZLOSWyYj02RIkC7Gk3ANw/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://api.twitter.com/graphql/zn8-3pSOLrdsVudr6quI9w/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://api.twitter.com/graphql/mdhVc9ZhIDtu0brvTp-aZA/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://api.twitter.com/graphql/A4gZIZWNr79F-cR1oTgPDQ/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://api.twitter.com/graphql/t3cL8-BwBCtzimES07csSw/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://api.twitter.com/graphql/yPcjvguL17eULiSn8z9SGw/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://api.twitter.com/graphql/Nef6gfAZu9_bBXf5vLL5lQ/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://api.twitter.com/graphql/npEFiYc3sCX-YDHZ1B69nw/CommunityMemberRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityUserRelationshipTypeahead<br>
Request URL: `https://api.twitter.com/graphql/C9CUCfAvlaMEhJBmM2hZkg/CommunityUserRelationshipTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://api.twitter.com/graphql/_vUIWq3vpyL0amiNTjrM-w/TrustedFriendsTypeahead`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
## ConnectTabTimeline<br>
Request URL: `https://api.twitter.com/graphql/bGrYp4EpO03iUUbehJtJDQ/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## timelinesFeedback<br>
Request URL: `https://api.twitter.com/graphql/vfVbgvTPTQ-dF_PQ5lD1WQ/timelinesFeedback`<br>
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
Request URL: `https://api.twitter.com/graphql/amDMtsGUWVdyTOb-9wYpJg/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | boolean | False      |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RemoveFollower<br>
Request URL: `https://api.twitter.com/graphql/QpNfg0kpPRfjROQ_9eOLXA/RemoveFollower`<br>
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
Request URL: `https://api.twitter.com/graphql/5c2eMhUFkmmuDrOHbsrO3A/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://api.twitter.com/graphql/lhB3zXD3M7e-VfBkR-5A8g/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://api.twitter.com/graphql/T8nnx2b4Y3ixaey5qGTjpg/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## Viewer<br>
Request URL: `https://api.twitter.com/graphql/260l1LN3DPTJ5UXMUE-3Rw/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesTabBarItemQuery<br>
Request URL: `https://api.twitter.com/graphql/ZesI-zwzK86uoWFu5IhLDg/CommunitiesTabBarItemQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## VerifiedRouteQuery<br>
Request URL: `https://api.twitter.com/graphql/inQHR9aa8pXO9Jqy4swaJw/VerifiedRouteQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/null/urtModuleOperationsInjectEntryQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/null/urtModuleOperationsUpdateEntryQuery`<br>
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
Request URL: `https://api.twitter.com/graphql//usersModuleProtectedQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/2e1gWggB2hQfGZyLKGFTog/CommunitiesFetchOneQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsRecentQuery<br>
Request URL: `https://api.twitter.com/graphql/TFTvqAwDJMrlVwTDDxg8Qw/CommunitiesMembershipsRecentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## UsersGraphQLFetchByScreenNameQuery<br>
Request URL: `https://api.twitter.com/graphql/88oBTp46afhKmPsvyX0_WQ/UsersGraphQLFetchByScreenNameQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesDashMenuItemQuery<br>
Request URL: `https://api.twitter.com/graphql/cFC8pqLWsfzTUOY674C6OA/CommunitiesDashMenuItemQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/zuUTzlnI-XomL9lfWFqSKg/DelegateAlertBannerContainerQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/BJ6DtxA2llfjnRoRjaiIiw/DMMessageDeleteMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/VvqwjKXjT6j6CTqvlqdYCw/useDMReactionMutationAddMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/-vqtYGrnU8xx1d_9tVE0lw/useDMReactionMutationRemoveMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/HL96-xZ3Y81IEzAdczDokg/useTypingNotifierMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useSendMessageMutation<br>
Request URL: `https://api.twitter.com/graphql/MaxK2PKX1F9Z-9SwqwavTw/useSendMessageMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/8D8KoSq5q9d5Su3emu2dwg/DMConversationSearchTabGroupsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/qno3lU4_eSHtSFoWQUhEag/DMConversationSearchTabPeopleQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/OvnYOmhTZiFhKBDXS0CrqA/DMMessageSearchTabQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## DMPinnedInboxAppend_Mutation<br>
Request URL: `https://api.twitter.com/graphql/o0aymgGiJY-53Y52YSUGVA/DMPinnedInboxAppend_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/_TQxP2Rb0expwVP9ktGrTQ/DMPinnedInboxDelete_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/_gBQBgClVuMQb8efxWkbbQ/DMPinnedInboxQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EvolutionDMInboxSecondaryNoQualityFilterQuery<br>
Request URL: `https://api.twitter.com/graphql/rj0wAEzfARRw5Lxv6vA9tA/EvolutionDMInboxSecondaryNoQualityFilterQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## EvolutionDMInboxSecondaryQuery<br>
Request URL: `https://api.twitter.com/graphql/CR5eoCBq5F7Ot49qXfjzKQ/EvolutionDMInboxSecondaryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMAllSearchTabQuery<br>
Request URL: `https://api.twitter.com/graphql/l4jKiQDei9_XUmp4dSvAow/evolutionDMAllSearchTabQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## evolutionDMConversationSearchTabGroupsQuery<br>
Request URL: `https://api.twitter.com/graphql/jU2lHFnuiEBmYbTBiLuBSA/evolutionDMConversationSearchTabGroupsQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMConversationSearchTabPeopleQuery<br>
Request URL: `https://api.twitter.com/graphql/PMTCRjntjEssRRwk5s9ezg/evolutionDMConversationSearchTabPeopleQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMInboxPollQuery<br>
Request URL: `https://api.twitter.com/graphql/XyU1n6dQq8tKdnDVXhp-bA/evolutionDMInboxPollQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMInboxPrimaryQuery<br>
Request URL: `https://api.twitter.com/graphql/yWKGySeJxM-6SB-nb6RwWw/evolutionDMInboxPrimaryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMInboxTertiaryQuery<br>
Request URL: `https://api.twitter.com/graphql/Fb14pDVMBtYifaNOE5h9xQ/evolutionDMInboxTertiaryQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMMessageSearchTabQuery<br>
Request URL: `https://api.twitter.com/graphql/5Xk9MApoC_dE-b0HXpqF7w/evolutionDMMessageSearchTabQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_exclude_directive_enabled                  | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled             | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |

#### queryId<br>
`None`<br>
## evolutionPinConversationMutation<br>
Request URL: `https://api.twitter.com/graphql/ZHTYqgRlFOIozAdfcLAF_A/evolutionPinConversationMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionUnpinConversationMutation<br>
Request URL: `https://api.twitter.com/graphql/uZN4IpDCjHJcya7TpOKoNA/evolutionUnpinConversationMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
