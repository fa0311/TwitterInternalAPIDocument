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
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserAccountLabel<br>
Request URL: `https://api.twitter.com/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
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
`None`<br>
#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
Request URL: `https://api.twitter.com/graphql/hdqJoN5xktcmnuT2Z-QTTg/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| spaces_2022_h2_clipping                                                 | boolean |          1 | nan       |
| spaces_2022_h2_spaces_communities                                       | boolean |          1 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/NniaFaodmave9wh_4cV6Qg/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/0fOzFT_8za8AUyJv3pERkA/BirdwatchCreateNote`<br>
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
Request URL: `https://api.twitter.com/graphql/Z8WSxZPMSFzoT-H5ixJS2A/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://api.twitter.com/graphql/-pJbOdvuR19SngusywIjRA/BirdwatchFetchNotes`<br>
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
Request URL: `https://api.twitter.com/graphql/LT8P2AoBObbK2tQL75vwPA/BirdwatchFetchOneNote`<br>
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
Request URL: `https://api.twitter.com/graphql/1qjoaVoGRJBt4E4FDHlecA/BookmarkFolderTimeline`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://api.twitter.com/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
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
Request URL: `https://api.twitter.com/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://api.twitter.com/graphql/1phu5l_3fn7wzxXnTowSow/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | ...    | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | s                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,u.d) | ...     | _                                                        |

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
`None`<br>
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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://api.twitter.com/graphql/41gySBRZ3tanuCx9lhB31Q/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://api.twitter.com/graphql/iXnyDqb_1Fs9aaRWeeMNFw/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://api.twitter.com/graphql/oGlWHAR0sUlzCexh6AuAiw/CommunitiesMembershipsSlice`<br>
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
Request URL: `https://api.twitter.com/graphql/lZG-KW65UV5ghOtQR2BCdw/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://api.twitter.com/graphql/pU4HF2R5UtYPkX6uSY0v3Q/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://api.twitter.com/graphql/FRwKGFOc5TketEaA8am7pA/CreateCommunity`<br>
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
Request URL: `https://api.twitter.com/graphql/ZSRRFf_fC96oweoaYNrhdQ/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://api.twitter.com/graphql/RTazUCzfsW4JAAho85cyFA/CommunityByRestId`<br>
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
Request URL: `https://api.twitter.com/graphql/jzs9RS8JsLLOliVd0gNGNg/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://api.twitter.com/graphql/n7b-wm-4reLhE-pA0W_PMQ/JoinCommunity`<br>
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
Request URL: `https://api.twitter.com/graphql/zZT5owXUfqlc-bBDulvUcA/LeaveCommunity`<br>
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
Request URL: `https://api.twitter.com/graphql/rQAQ-rOuZ5Rco0BX_04PvQ/CommunityModerationKeepTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/H_Jh88TLQbBxoEmarkl30w/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://api.twitter.com/graphql/fxoBRimnPBZde7Jy7oX8Vg/RequestToJoinCommunity`<br>
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
Request URL: `https://api.twitter.com/graphql/gkAfamX9Zm6fTvN7wIhCUg/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/4lNPxuwqWWyJ8NvMLtXWZg/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://api.twitter.com/graphql/--KsROq_U4xbD_wd0ILuzg/CommunityUpdateRole`<br>
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
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
## CommunityCreateRule<br>
Request URL: `https://api.twitter.com/graphql/oP6AkKK7cj6f2DcKNxoRlQ/CommunityCreateRule`<br>
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
## CommunityEditBannerMedia<br>
Request URL: `https://api.twitter.com/graphql/PZNCgKSCnONh2jsgN-k0_A/CommunityEditBannerMedia`<br>
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
## CommunityEditName<br>
Request URL: `https://api.twitter.com/graphql/kn6YYszpnCudapuWHGxnkg/CommunityEditName`<br>
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
## CommunityEditPurpose<br>
Request URL: `https://api.twitter.com/graphql/uuOoZHAHPWv1_V8k998eZg/CommunityEditPurpose`<br>
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
## CommunityEditRule<br>
Request URL: `https://api.twitter.com/graphql/5V5kR0PJpOSlo1IZHHC4CQ/CommunityEditRule`<br>
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
## CommunityEditTheme<br>
Request URL: `https://api.twitter.com/graphql/tFy6WYNhA-KWvlF29JN3ZA/CommunityEditTheme`<br>
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
## CommunityRemoveBannerMedia<br>
Request URL: `https://api.twitter.com/graphql/wntlkO39ggnplYowqbbSvw/CommunityRemoveBannerMedia`<br>
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
## CommunityRemoveRule<br>
Request URL: `https://api.twitter.com/graphql/SmX6I1rX0PyvsEcE-8Y-LA/CommunityRemoveRule`<br>
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
## CommunityReorderRules<br>
Request URL: `https://api.twitter.com/graphql/SlND0s8g7vaWfR5bomaWiQ/CommunityReorderRules`<br>
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
## TweetDetail<br>
Request URL: `https://api.twitter.com/graphql/jQsVWg0cwt1_J6XQbnmqqA/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## DmAllSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/xjNr82LL27R7K9-FxWnirA/DmAllSearchSlice`<br>
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
| withSuperFollowsUserFields      | ...    | i.isTrue("rito_safety_mode_blocked_profile_enabled")                                                                                                                                 |

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
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...t                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://api.twitter.com/graphql/74Iz7QVS-PBcTNzFBc0mfw/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | l          |
| includePromotedContent | boolean | False      |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
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
Request URL: `https://api.twitter.com/graphql/m-dyD4xFEOflQnNZQNUpdA/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://api.twitter.com/graphql/R0lS8D960f9kaSWk9NyAgQ/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
## HomeLatestTimeline<br>
Request URL: `https://api.twitter.com/graphql/MsfQTkink2J9_M0YzCl36w/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://api.twitter.com/graphql/1HRBWbW4cIexJ-v--qANEw/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://api.twitter.com/graphql/mDT5pi--P4qMjgtOPDN1Fw/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## CombinedLists<br>
Request URL: `https://api.twitter.com/graphql/3s5Yw1XhZff2HLmD1GP6nw/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://api.twitter.com/graphql/P8tyfv2_0HzofrB5f6_ugw/ListAddMember`<br>
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
Request URL: `https://api.twitter.com/graphql/-bOKetDVCMl20qXn7YDXIA/DeleteListBanner`<br>
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
Request URL: `https://api.twitter.com/graphql/Uk0ZwKSMYng56aQdeJD1yw/EditListBanner`<br>
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
Request URL: `https://api.twitter.com/graphql/i08_qAU5nG5EkjnbcCeg0g/ListBySlug`<br>
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
Request URL: `https://api.twitter.com/graphql/hQAsnViq2BrMLbPuQ9umDA/CreateList`<br>
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
Request URL: `https://api.twitter.com/graphql/JKw3vkYWKIqsGRe2OLvXpQ/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/B8RZdqNM3__PI7cN3itk5A/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/Z8YdDe3BYP6LvThf-ZMJ4g/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://api.twitter.com/graphql/gJkhsiYPji3li3Zq4Mz47w/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://api.twitter.com/graphql/Hvbm2TPxZOl6a5jZeUHk8w/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/tboKMxJXpl8JxFmVQLxBUA/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://api.twitter.com/graphql/PdFLmbN9FAT3kxuYphbO6A/ListPinOne`<br>
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
Request URL: `https://api.twitter.com/graphql/KwDtNPZP8xL57bCxHCIvOg/ListPins`<br>
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
Request URL: `https://api.twitter.com/graphql/Bc-6GPUtWnyr3PN0fNffyA/ListByRestId`<br>
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
Request URL: `https://api.twitter.com/graphql/F6M293ntNNBQPnIvmEPlsw/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://api.twitter.com/graphql/DBZowzFN492FFkBPBptCwg/ListRemoveMember`<br>
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
Request URL: `https://api.twitter.com/graphql/JZ_OVzM4b32pPufdXa5vgw/ListSubscribe`<br>
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
Request URL: `https://api.twitter.com/graphql/Vbau4f6capvfv-9vtEUxcQ/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/oVn3dJ4Q1HDvq-UYT8AUdg/ListUnpinOne`<br>
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
Request URL: `https://api.twitter.com/graphql/AhfcWLFMXGaFMpzeUYtayA/ListUnsubscribe`<br>
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
Request URL: `https://api.twitter.com/graphql/4dCEFWtxEbhnSLcJdJ6PNg/UpdateList`<br>
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
Request URL: `https://api.twitter.com/graphql/20k5E-Qwu9G57Ir0aKjWBg/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://api.twitter.com/graphql/08AQh7H2j-tSxEhRqj1Z4g/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://api.twitter.com/graphql/2X4Vqu6XLneR-XZnGK5MAw/ListsPinMany`<br>
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
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://api.twitter.com/graphql/SUP2pAgabuUDaxT_3TuMLw/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | n                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | i                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://api.twitter.com/graphql/IgwxSNyc9Ixm6dC8tBs1DQ/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rest_id                | ...     | n          |
| count                  | ...     | t          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://api.twitter.com/graphql/Ni4jXGCPWM6UUnXKi3BFOQ/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | r           |
| count                  | ...     | t           |
| cursor                 | ...     | i           |
| teamName               | ...     | n           |
| includePromotedContent | boolean | False       |
| ...()(0,a.d)           | ...     | _           |
| withClientEventToken   | boolean | False       |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://api.twitter.com/graphql/DNG20tsZuTl88SGWEuNbZw/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | n                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | i                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://api.twitter.com/graphql/uDB7F0tK7eDFBQb1leJ0oQ/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserSuperFollowTweets<br>
Request URL: `https://api.twitter.com/graphql/zLUG3r5SjOItnTta4hQ4Eg/UserSuperFollowTweets`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://api.twitter.com/graphql/ns5lx7OYUtNZ46KtFoVAIw/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable                              |
|:---------------------------------------|:--------|:--------------------------------------|
| userId                                 | ...     | r                                     |
| count                                  | ...     | t                                     |
| cursor                                 | ...     | i                                     |
| includePromotedContent                 | boolean | True                                  |
| withQuickPromoteEligibilityTweetFields | boolean | True                                  |
| ...()(0,a.d)                           | ...     | _                                     |
| withVoice                              | ...     | _.isTrue(_)                           |
| withV2Timeline                         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://api.twitter.com/graphql/uWo3HphOAo7HicMHBhzlWQ/UserTweetsAndReplies`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
Request URL: `https://api.twitter.com/graphql/Kj8tiyV4856P41egVvfz9Q/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://api.twitter.com/graphql/oYgn786hHl9YKjDnqndq8g/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | ...    | t           |
| ...()(0,l.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | i.isTrue(i) |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/Qp9WiropfSUk9Qk8irSlmQ/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/eAn5FkK6qLR4e2NkJ5Zufw/ArticleTimeline`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/HfK0WlmDaOgMKQvLjVltNA/ArticleTweetsTimeline`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://api.twitter.com/graphql/jRCXZBRyVgMo37F2GN1WgQ/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicFollow<br>
Request URL: `https://api.twitter.com/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://api.twitter.com/graphql/3CIsxSmM8R12ATLZm5kGxw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://api.twitter.com/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://api.twitter.com/graphql/s6OElB7YH-EsA6KQy6KtDg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://api.twitter.com/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://api.twitter.com/graphql/lpFWSn5LdCBhhsH5owJaaw/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://api.twitter.com/graphql/doM7xJzckI91wfwFXKvwxQ/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://api.twitter.com/graphql/LaDntW-MvH_P0hIDPDXcDg/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://api.twitter.com/graphql/aOjnwtyoxuBxKHqrRPoCRw/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/IrBt2kZv7mpiSeULfuOlrA/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://api.twitter.com/graphql/dEgQz0_l6o3Y952LD887oQ/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://api.twitter.com/graphql/osP-8bRl9yqtQj7PXifW1g/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     | error     |        nan |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          0 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| vibe_api_enabled                                                        | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| interactive_text_enabled                                                | boolean | nan       |          1 |
| responsive_web_text_conversations_enabled                               | boolean | nan       |          0 |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | nan       |          1 |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          0 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://api.twitter.com/graphql/ihIcULrtrtPGlCuprduRrA/GetTweetReactionTimeline`<br>
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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://api.twitter.com/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
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
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## TwitterArticleCreate<br>
Request URL: `https://api.twitter.com/graphql/oNEfhcsRqZvhqxE88Yh-Tw/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/1DLxPdJT_4M86KQiH3qk6g/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://api.twitter.com/graphql/Wizo2F_j08T0yE_BFGHKuw/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://api.twitter.com/graphql/rckcCk5RJc2HqLE71mREtA/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://api.twitter.com/graphql/e1nSF9uo_39fpyRzyzle0w/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://api.twitter.com/graphql/OiiGcR-kmpMpuzYBAkqnSw/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://api.twitter.com/graphql/BZRo75_0Tk-hINWQ5Yy8iw/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://api.twitter.com/graphql/CbM6Ve-amDAA4WkubiGv_g/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## ConnectTabTimeline<br>
Request URL: `https://api.twitter.com/graphql/Vaz7QNCk7OfdTXM2PKpLGg/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## TweetResultByRestId<br>
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## UrtFixtures<br>
Request URL: `https://api.twitter.com/graphql/8yAVwFecHrpSD4eym1Wp0g/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/gUIQEk2xDGzQTX8Ii0Yesw/UserByRestId`<br>
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
Request URL: `https://api.twitter.com/graphql/rePnxwe9LZ51nQ7Sn_xN_A/UserByScreenName`<br>
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
Request URL: `https://api.twitter.com/graphql/zaTqxMKJ1kzpOxhVbYr1YQ/UsersByRestIds`<br>
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
Request URL: `https://api.twitter.com/graphql/QXO9SjUJXid3NNEovZXydw/Viewer`<br>
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
## ArticleTimeline<br>
Request URL: `https://api.twitter.com/graphql/eAn5FkK6qLR4e2NkJ5Zufw/ArticleTimeline`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/HfK0WlmDaOgMKQvLjVltNA/ArticleTweetsTimeline`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://api.twitter.com/graphql/hdqJoN5xktcmnuT2Z-QTTg/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| spaces_2022_h2_clipping                                                 | boolean |          1 | nan       |
| spaces_2022_h2_spaces_communities                                       | boolean |          1 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/NniaFaodmave9wh_4cV6Qg/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/0fOzFT_8za8AUyJv3pERkA/BirdwatchCreateNote`<br>
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
Request URL: `https://api.twitter.com/graphql/Z8WSxZPMSFzoT-H5ixJS2A/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://api.twitter.com/graphql/-pJbOdvuR19SngusywIjRA/BirdwatchFetchNotes`<br>
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
Request URL: `https://api.twitter.com/graphql/LT8P2AoBObbK2tQL75vwPA/BirdwatchFetchOneNote`<br>
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
## BlockedAccountsAll<br>
Request URL: `https://api.twitter.com/graphql/KlrRmyvlF1SUjFgyIJXp-Q/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://api.twitter.com/graphql/qGREDvqUhjNjinD5YS8ESw/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | r          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://api.twitter.com/graphql/ODq6OHNa8_prnNm2A2EKRQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |
| mode     | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://api.twitter.com/graphql/1qjoaVoGRJBt4E4FDHlecA/BookmarkFolderTimeline`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://api.twitter.com/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
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
Request URL: `https://api.twitter.com/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://api.twitter.com/graphql/1phu5l_3fn7wzxXnTowSow/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | ...    | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://api.twitter.com/graphql/mDT5pi--P4qMjgtOPDN1Fw/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
## CombinedLists<br>
Request URL: `https://api.twitter.com/graphql/3s5Yw1XhZff2HLmD1GP6nw/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://api.twitter.com/graphql/41gySBRZ3tanuCx9lhB31Q/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://api.twitter.com/graphql/iXnyDqb_1Fs9aaRWeeMNFw/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://api.twitter.com/graphql/oGlWHAR0sUlzCexh6AuAiw/CommunitiesMembershipsSlice`<br>
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
Request URL: `https://api.twitter.com/graphql/lZG-KW65UV5ghOtQR2BCdw/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://api.twitter.com/graphql/pU4HF2R5UtYPkX6uSY0v3Q/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://api.twitter.com/graphql/FRwKGFOc5TketEaA8am7pA/CreateCommunity`<br>
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
## CommunityCreateRule<br>
Request URL: `https://api.twitter.com/graphql/oP6AkKK7cj6f2DcKNxoRlQ/CommunityCreateRule`<br>
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
Request URL: `https://api.twitter.com/graphql/ZSRRFf_fC96oweoaYNrhdQ/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://api.twitter.com/graphql/PZNCgKSCnONh2jsgN-k0_A/CommunityEditBannerMedia`<br>
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
## CommunityEditName<br>
Request URL: `https://api.twitter.com/graphql/kn6YYszpnCudapuWHGxnkg/CommunityEditName`<br>
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
## CommunityEditPurpose<br>
Request URL: `https://api.twitter.com/graphql/uuOoZHAHPWv1_V8k998eZg/CommunityEditPurpose`<br>
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
## CommunityEditRule<br>
Request URL: `https://api.twitter.com/graphql/5V5kR0PJpOSlo1IZHHC4CQ/CommunityEditRule`<br>
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
## CommunityEditTheme<br>
Request URL: `https://api.twitter.com/graphql/tFy6WYNhA-KWvlF29JN3ZA/CommunityEditTheme`<br>
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
## CommunityByRestId<br>
Request URL: `https://api.twitter.com/graphql/RTazUCzfsW4JAAho85cyFA/CommunityByRestId`<br>
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
Request URL: `https://api.twitter.com/graphql/jzs9RS8JsLLOliVd0gNGNg/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://api.twitter.com/graphql/n7b-wm-4reLhE-pA0W_PMQ/JoinCommunity`<br>
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
Request URL: `https://api.twitter.com/graphql/zZT5owXUfqlc-bBDulvUcA/LeaveCommunity`<br>
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
## CommunityModerationKeepTweet<br>
Request URL: `https://api.twitter.com/graphql/rQAQ-rOuZ5Rco0BX_04PvQ/CommunityModerationKeepTweet`<br>
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
Request URL: `https://api.twitter.com/graphql/H_Jh88TLQbBxoEmarkl30w/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://api.twitter.com/graphql/wntlkO39ggnplYowqbbSvw/CommunityRemoveBannerMedia`<br>
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
## CommunityRemoveRule<br>
Request URL: `https://api.twitter.com/graphql/SmX6I1rX0PyvsEcE-8Y-LA/CommunityRemoveRule`<br>
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
## CommunityReorderRules<br>
Request URL: `https://api.twitter.com/graphql/SlND0s8g7vaWfR5bomaWiQ/CommunityReorderRules`<br>
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
## RequestToJoinCommunity<br>
Request URL: `https://api.twitter.com/graphql/fxoBRimnPBZde7Jy7oX8Vg/RequestToJoinCommunity`<br>
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
Request URL: `https://api.twitter.com/graphql/gkAfamX9Zm6fTvN7wIhCUg/CommunityTweetsRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/4lNPxuwqWWyJ8NvMLtXWZg/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://api.twitter.com/graphql/--KsROq_U4xbD_wd0ILuzg/CommunityUpdateRole`<br>
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
## ConnectTabTimeline<br>
Request URL: `https://api.twitter.com/graphql/Vaz7QNCk7OfdTXM2PKpLGg/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ContentControlToolDisable<br>
Request URL: `https://api.twitter.com/graphql/N6oDUH0bX-7w9Cj4Wd6zXA/ContentControlToolDisable`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolEnable<br>
Request URL: `https://api.twitter.com/graphql/4dMgLjwMMTqp33sMQ6IrJA/ContentControlToolEnable`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolFetchAll<br>
Request URL: `https://api.twitter.com/graphql/nMDl1pqwn1QotVzqPAjjOw/ContentControlToolFetchAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolFetchAllUserEnabled<br>
Request URL: `https://api.twitter.com/graphql/kOKEPqQB769u1TI5FJt-tw/ContentControlToolFetchAllUserEnabled`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ContentControlToolFetchOne<br>
Request URL: `https://api.twitter.com/graphql/JD2EtsNFZ3uvvTP_lfn9Bg/ContentControlToolFetchOne`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
## ConvertRitoSuggestedActions<br>
Request URL: `https://api.twitter.com/graphql/2njnYoE69O2jdUM7KMEnDw/ConvertRitoSuggestedActions`<br>
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
## CreateNoteTweet<br>
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## CreateTweet<br>
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## DeleteBookmarkFolder<br>
Request URL: `https://api.twitter.com/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | s                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,u.d) | ...     | _                                                        |

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
## DmAllSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/xjNr82LL27R7K9-FxWnirA/DmAllSearchSlice`<br>
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
| withSuperFollowsUserFields      | ...    | i.isTrue("rito_safety_mode_blocked_profile_enabled")                                                                                                                                 |

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
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...t                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://api.twitter.com/graphql/74Iz7QVS-PBcTNzFBc0mfw/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | l          |
| includePromotedContent | boolean | False      |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## DmPeopleSearchSlice<br>
Request URL: `https://api.twitter.com/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
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
## Favoriters<br>
Request URL: `https://api.twitter.com/graphql/IrBt2kZv7mpiSeULfuOlrA/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## Followers<br>
Request URL: `https://api.twitter.com/graphql/0EZz1aXXW9ixZEYMQ_-97Q/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | n                                                    |
| withSafetyModeUserFields   | ...    | t.isTrue()                                           |
| withSuperFollowsUserFields | ...    | t.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://api.twitter.com/graphql/OTdE5uw_D_xczrSJQFSlYA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://api.twitter.com/graphql/Xwlg7-LoVy_Pw0dYkFwQlQ/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ForYouExplore<br>
Request URL: `https://api.twitter.com/graphql/m-dyD4xFEOflQnNZQNUpdA/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://api.twitter.com/graphql/he0-jVs_1P_lZN9-uhTByA/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | o          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/MsfQTkink2J9_M0YzCl36w/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://api.twitter.com/graphql/1HRBWbW4cIexJ-v--qANEw/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://api.twitter.com/graphql/R0lS8D960f9kaSWk9NyAgQ/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://api.twitter.com/graphql/SUP2pAgabuUDaxT_3TuMLw/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | n                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | i                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://api.twitter.com/graphql/P8tyfv2_0HzofrB5f6_ugw/ListAddMember`<br>
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
Request URL: `https://api.twitter.com/graphql/-bOKetDVCMl20qXn7YDXIA/DeleteListBanner`<br>
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
Request URL: `https://api.twitter.com/graphql/Uk0ZwKSMYng56aQdeJD1yw/EditListBanner`<br>
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
Request URL: `https://api.twitter.com/graphql/i08_qAU5nG5EkjnbcCeg0g/ListBySlug`<br>
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
Request URL: `https://api.twitter.com/graphql/hQAsnViq2BrMLbPuQ9umDA/CreateList`<br>
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
Request URL: `https://api.twitter.com/graphql/JKw3vkYWKIqsGRe2OLvXpQ/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## ListEditRecommendedUsers<br>
Request URL: `https://api.twitter.com/graphql/B8RZdqNM3__PI7cN3itk5A/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/Z8YdDe3BYP6LvThf-ZMJ4g/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://api.twitter.com/graphql/gJkhsiYPji3li3Zq4Mz47w/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://api.twitter.com/graphql/Hvbm2TPxZOl6a5jZeUHk8w/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/tboKMxJXpl8JxFmVQLxBUA/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListPinOne<br>
Request URL: `https://api.twitter.com/graphql/PdFLmbN9FAT3kxuYphbO6A/ListPinOne`<br>
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
Request URL: `https://api.twitter.com/graphql/KwDtNPZP8xL57bCxHCIvOg/ListPins`<br>
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
## ListByRestId<br>
Request URL: `https://api.twitter.com/graphql/Bc-6GPUtWnyr3PN0fNffyA/ListByRestId`<br>
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
Request URL: `https://api.twitter.com/graphql/F6M293ntNNBQPnIvmEPlsw/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://api.twitter.com/graphql/DBZowzFN492FFkBPBptCwg/ListRemoveMember`<br>
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
Request URL: `https://api.twitter.com/graphql/JZ_OVzM4b32pPufdXa5vgw/ListSubscribe`<br>
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
Request URL: `https://api.twitter.com/graphql/Vbau4f6capvfv-9vtEUxcQ/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/oVn3dJ4Q1HDvq-UYT8AUdg/ListUnpinOne`<br>
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
Request URL: `https://api.twitter.com/graphql/AhfcWLFMXGaFMpzeUYtayA/ListUnsubscribe`<br>
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
Request URL: `https://api.twitter.com/graphql/4dCEFWtxEbhnSLcJdJ6PNg/UpdateList`<br>
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
Request URL: `https://api.twitter.com/graphql/20k5E-Qwu9G57Ir0aKjWBg/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://api.twitter.com/graphql/08AQh7H2j-tSxEhRqj1Z4g/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListsPinMany<br>
Request URL: `https://api.twitter.com/graphql/2X4Vqu6XLneR-XZnGK5MAw/ListsPinMany`<br>
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
## ModeratedTimeline<br>
Request URL: `https://api.twitter.com/graphql/WxsJlF1rkuUSnfWqnaN9MQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable   |
|:--------------|:--------|:-----------|
| tweet_id      | ...     | a          |
| comparison_id | ...     | o          |
| dark_request  | boolean | True       |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://api.twitter.com/graphql/0ZzO97kaK9B83ByKdkdxUg/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type    | variable      |
|:--------------|:--------|:--------------|
| tweet_id      | ...     | a             |
| comparison_id | ...     | t             |
| ...()&&       | ...     | {'...n': '_'} |
| dark_request  | boolean | True          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## NoteworthyAccountsPage<br>
Request URL: `https://api.twitter.com/graphql/jRCXZBRyVgMo37F2GN1WgQ/NoteworthyAccountsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## PutClientEducationFlag<br>
Request URL: `https://api.twitter.com/graphql/IjQ-egg0uPkY11NyPMfRMQ/PutClientEducationFlag`<br>
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
## RemoveTweetFromBookmarkFolder<br>
Request URL: `https://api.twitter.com/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://api.twitter.com/graphql/dEgQz0_l6o3Y952LD887oQ/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## RitoActionedTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/Kj8tiyV4856P41egVvfz9Q/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://api.twitter.com/graphql/oYgn786hHl9YKjDnqndq8g/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                      | type   | variable    |
|:-------------------------|:-------|:------------|
| cursor                   | ...    | t           |
| ...()(0,l.d)             | ...    | _           |
| withSafetyModeUserFields | ...    | i.isTrue(i) |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://api.twitter.com/graphql/Qp9WiropfSUk9Qk8irSlmQ/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## SuperFollowers<br>
Request URL: `https://api.twitter.com/graphql/gE10DWlQTArlmfNxW0ZE2A/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type    | variable   |
|:----------------|:--------|:-----------|
| source_tweet_id | ...     | o          |
| dark_request    | boolean | False      |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## TopicFollow<br>
Request URL: `https://api.twitter.com/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://api.twitter.com/graphql/3CIsxSmM8R12ATLZm5kGxw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://api.twitter.com/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicToFollowSidebar<br>
Request URL: `https://api.twitter.com/graphql/s6OElB7YH-EsA6KQy6KtDg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://api.twitter.com/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicsManagementPage<br>
Request URL: `https://api.twitter.com/graphql/lpFWSn5LdCBhhsH5owJaaw/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://api.twitter.com/graphql/doM7xJzckI91wfwFXKvwxQ/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://api.twitter.com/graphql/LaDntW-MvH_P0hIDPDXcDg/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## TweetDetail<br>
Request URL: `https://api.twitter.com/graphql/jQsVWg0cwt1_J6XQbnmqqA/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://api.twitter.com/graphql/osP-8bRl9yqtQj7PXifW1g/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     | error     |        nan |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          0 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| vibe_api_enabled                                                        | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| interactive_text_enabled                                                | boolean | nan       |          1 |
| responsive_web_text_conversations_enabled                               | boolean | nan       |          0 |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | nan       |          1 |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          0 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## GetTweetReactionTimeline<br>
Request URL: `https://api.twitter.com/graphql/ihIcULrtrtPGlCuprduRrA/GetTweetReactionTimeline`<br>
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
## TweetResultByRestId<br>
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://api.twitter.com/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
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
Request URL: `https://api.twitter.com/graphql/oNEfhcsRqZvhqxE88Yh-Tw/TwitterArticleCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/1DLxPdJT_4M86KQiH3qk6g/TwitterArticleByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateCoverImage<br>
Request URL: `https://api.twitter.com/graphql/Wizo2F_j08T0yE_BFGHKuw/TwitterArticleUpdateCoverImage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateData<br>
Request URL: `https://api.twitter.com/graphql/rckcCk5RJc2HqLE71mREtA/TwitterArticleUpdateData`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateMedia<br>
Request URL: `https://api.twitter.com/graphql/e1nSF9uo_39fpyRzyzle0w/TwitterArticleUpdateMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateTitle<br>
Request URL: `https://api.twitter.com/graphql/OiiGcR-kmpMpuzYBAkqnSw/TwitterArticleUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticleUpdateVisibility<br>
Request URL: `https://api.twitter.com/graphql/BZRo75_0Tk-hINWQ5Yy8iw/TwitterArticleUpdateVisibility`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TwitterArticlesSlice<br>
Request URL: `https://api.twitter.com/graphql/CbM6Ve-amDAA4WkubiGv_g/TwitterArticlesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_article_data_v2_enabled                          | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## UrtFixtures<br>
Request URL: `https://api.twitter.com/graphql/8yAVwFecHrpSD4eym1Wp0g/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://api.twitter.com/graphql/IgwxSNyc9Ixm6dC8tBs1DQ/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| rest_id                | ...     | n          |
| count                  | ...     | t          |
| cursor                 | ...     | i          |
| includePromotedContent | boolean | False      |
| ...()(0,a.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserAccountLabel<br>
Request URL: `https://api.twitter.com/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
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
`None`<br>
#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://api.twitter.com/graphql/Ni4jXGCPWM6UUnXKi3BFOQ/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | r           |
| count                  | ...     | t           |
| cursor                 | ...     | i           |
| teamName               | ...     | n           |
| includePromotedContent | boolean | False       |
| ...()(0,a.d)           | ...     | _           |
| withClientEventToken   | boolean | False       |
| withVoice              | ...     | _.isTrue(_) |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://api.twitter.com/graphql/gUIQEk2xDGzQTX8Ii0Yesw/UserByRestId`<br>
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
Request URL: `https://api.twitter.com/graphql/rePnxwe9LZ51nQ7Sn_xN_A/UserByScreenName`<br>
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
## UserMedia<br>
Request URL: `https://api.twitter.com/graphql/DNG20tsZuTl88SGWEuNbZw/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | n                                     |
| count                  | ...     | t                                     |
| cursor                 | ...     | i                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,a.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | _.isTrue(_)                           |
| withV2Timeline         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://api.twitter.com/graphql/uDB7F0tK7eDFBQb1leJ0oQ/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## UserSuperFollowTweets<br>
Request URL: `https://api.twitter.com/graphql/zLUG3r5SjOItnTta4hQ4Eg/UserSuperFollowTweets`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://api.twitter.com/graphql/ns5lx7OYUtNZ46KtFoVAIw/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable                              |
|:---------------------------------------|:--------|:--------------------------------------|
| userId                                 | ...     | r                                     |
| count                                  | ...     | t                                     |
| cursor                                 | ...     | i                                     |
| includePromotedContent                 | boolean | True                                  |
| withQuickPromoteEligibilityTweetFields | boolean | True                                  |
| ...()(0,a.d)                           | ...     | _                                     |
| withVoice                              | ...     | _.isTrue(_)                           |
| withV2Timeline                         | ...     | _.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://api.twitter.com/graphql/uWo3HphOAo7HicMHBhzlWQ/UserTweetsAndReplies`<br>
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
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://api.twitter.com/graphql/zaTqxMKJ1kzpOxhVbYr1YQ/UsersByRestIds`<br>
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
## Viewer<br>
Request URL: `https://api.twitter.com/graphql/QXO9SjUJXid3NNEovZXydw/Viewer`<br>
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
## ViewerTeams<br>
Request URL: `https://api.twitter.com/graphql/jqQV7d1CMJ4El2nGSit6aA/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type    | variable                                                 |
|:--------------------------|:--------|:---------------------------------------------------------|
| tweetId                   | ...     | i                                                        |
| includePromotedContent    | boolean | True                                                     |
| withBirdwatchNotes        | ...     | t.isTrue()                                               |
| withVoice                 | ...     | t.isTrue("responsive_web_birdwatch_consumption_enabled") |
| withCommunity             | ...     | t.isTrue("voice_consumption_enabled")                    |
| ...("c9s_enabled")(0,_.d) | ...     | _                                                        |

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
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://api.twitter.com/graphql/aOjnwtyoxuBxKHqrRPoCRw/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/d6N8gtyuDH3UKW3G2Ucflg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/rg4vU4sNC1mE7yFCKkO2YQ/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/2NJkzSwq9NQs2Rbs3PI62A/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| vibe_api_enabled                                                        | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     |        nan | error     |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          0 | nan       |
| interactive_text_enabled                                                | boolean |          1 | nan       |
| responsive_web_text_conversations_enabled                               | boolean |          0 | nan       |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://api.twitter.com/graphql/MO8cE7aTvaenXJX_teUGcA/CommunitiesFetchOneQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/vemYHRCaiEcTbOZJcKLAfw/CommunitiesMembershipsRecentQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/tO6Sk1-6_VRyfzmhTY-hQg/UsersGraphQLFetchByScreenNameQuery`<br>
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
## CommunitiesFetchOneQuery<br>
Request URL: `https://api.twitter.com/graphql/MO8cE7aTvaenXJX_teUGcA/CommunitiesFetchOneQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/vemYHRCaiEcTbOZJcKLAfw/CommunitiesMembershipsRecentQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/tO6Sk1-6_VRyfzmhTY-hQg/UsersGraphQLFetchByScreenNameQuery`<br>
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
## managementListsPageTimelineQuery<br>
Request URL: `https://api.twitter.com/graphql/7_zXPbDt4Sf4akqB9V_mSg/managementListsPageTimelineQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     | error     |        nan |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| interactive_text_enabled                                                | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_text_conversations_enabled                               | boolean | nan       |          0 |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          0 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| vibe_api_enabled                                                        | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## DelegatedAccountListQuery<br>
Request URL: `https://api.twitter.com/graphql/jvbCW8kzIoL8ps8Ry_cDqQ/DelegatedAccountListQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/qkl5ZUdpNhtl0kq4dGX3uQ/DMMessageSearchTabQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/CLAP07vR0BB--Q6CNPAFVg/evolutionDMAllSearchTabQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/Pi59GUvQhq5aT-jHUUEnEw/evolutionDMMessageSearchTabQuery`<br>
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
## evolutionDMDrawerHeaderQuery<br>
Request URL: `https://api.twitter.com/graphql/3QhsL9LHWvfEHbIRXIb84g/evolutionDMDrawerHeaderQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDMDrawerQuery<br>
Request URL: `https://api.twitter.com/graphql/EaLKdvs0RLR9SFIi-XmwCg/evolutionDMDrawerQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CarouselQuery<br>
Request URL: `https://api.twitter.com/graphql/A9Lt_vHgiD1zkiB2fdU9Zw/CarouselQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/8daJzV6tGCTssiKBRFpXtQ/CommunitiesCreateButtonQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/ZnEsP44ZDzRe9aId7SVoZg/CommunitiesListActivityQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/JLnMuCshIrWkJlp7LRvWFw/CommunitiesSearchQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/hNQLWhD2pxRBtp7mg6hWEQ/CommunityAppBarButtonQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/8s4H3Tf6VXViIQuaHMJE1Q/CommunityInviteButtonQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityToolsScreenContainerQuery<br>
Request URL: `https://api.twitter.com/graphql/c7MAOYAoh0dfh_06YrxSpg/CommunityToolsScreenContainerQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/zHWYNyObppV8ZXY0o3oHTw/DeleteCommunityMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/ruZM8GnBs_0uuSjWLF6nkw/EditMembershipTypeQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/IqDv9dN3LO-GORp6lRMyoA/HashtagResultsCommunity_Query`<br>
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
Request URL: `https://api.twitter.com/graphql/WZkL3cX8Ht0d8TQO20Bk6w/MemberRequests_Query`<br>
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
Request URL: `https://api.twitter.com/graphql/d86C1tsqqQ-_2b7xStjYJQ/NotificationSettingsModalQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/GhfS-OCV4WH5I4aT2_i8jg/NotificationSettingsSaveButtonMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/t7j24Zrx2IjCj13ndCU2hA/PeopleCommunity_Query`<br>
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
Request URL: `https://api.twitter.com/graphql/lieM2QpB7PLqe0qyABV3KA/PrimaryContentQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    |   variable | default   |
|:------------------------------------------------------|:--------|-----------:|:----------|
| c9s_list_members_action_api_enabled                   | boolean |          0 | nan       |
| c9s_superc9s_indication_enabled                       | ...     |        nan | error     |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## actions_approveMemberRequest_Mutation<br>
Request URL: `https://api.twitter.com/graphql/LVHUDWQ4jsU9iixwJUbT4Q/actions_approveMemberRequest_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/5AncQiBia2eEnbL_0_jYAA/actions_denyMemberRequest_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/-z7ecfy5Y04vSJHD3xQ1aA/communityPeopleActionMenu_roleUpdate_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/YiJSKw8k6Mpy-pkVOwuQ7w/edit_membershipSettings_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/ohtbB6ZKiLYshYxPJz1RNw/membersSliceTimeline_Query`<br>
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
## moderatorsSliceTimeline_Query<br>
Request URL: `https://api.twitter.com/graphql/FFpRSheri8ikANi1pyAfSQ/moderatorsSliceTimeline_Query`<br>
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
## DelegateQuery<br>
Request URL: `https://api.twitter.com/graphql/GhQlWgEZ8wKf_JimVEG-Yw/DelegateQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/2sRv-icOf8xTqv9sG2859w/GroupDetailDelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GroupMenuMutation<br>
Request URL: `https://api.twitter.com/graphql/35IlHo3PPoKCgjGN9PyBEQ/GroupMenuMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/a8IpKTmRdGxQogYxbkvcaQ/GroupsDelegateQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/llQiaizf9GTqXkyUOk307Q/GroupsModalQuery`<br>
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
## InviteMenu_accept_Mutation<br>
Request URL: `https://api.twitter.com/graphql/DpdMDix7rAjl6SVAs3SNSQ/InviteMenu_accept_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/QLNN5GVLRMe93lHnX3Um2w/InviteMenu_reject_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/nw0Nxulg0nCzsnFi_R5WqQ/MembersDelegateQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## useAddMemberModalMutation_add_Mutation<br>
Request URL: `https://api.twitter.com/graphql/SFV2FWbGnq-s473RcXrDsg/useAddMemberModalMutation_add_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/bt_mUik7_sqXKofZmEBzAw/useChangeMemberRoleModalMutation_change_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/2HD9lnvauHCbl4wRw2P_QQ/useDelegateMutation_settings_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/QSkmmm7WG94DG9AfV2QHkg/useMemberMenuMutation_cancel_invite_Mutation`<br>
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
Request URL: `https://api.twitter.com/graphql/R8K9DRNeWen33po2wpZhZw/useMemberMenuMutation_remove_Mutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MonetizationSettingsQuery<br>
Request URL: `https://api.twitter.com/graphql/oi9OqvClsF9hkRsedoNvjw/MonetizationSettingsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/kmAhocLFK1cbzXxGq5Boow/RepliesGetUserToxicReplyFilterSettingQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/2DSpolLNDpVL7KDJ-UWHSg/useToggleToxicReplyFilterSettingMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SensitiveMediaSettingsQuery<br>
Request URL: `https://api.twitter.com/graphql/ft92vAsha0RhDxwgq_ojWQ/SensitiveMediaSettingsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/YWGRWrle16Fb6JvAjvjoTQ/useEditSensitiveMediaSettingsMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/K5_KjMpjdtjQXzKGLqyFXw/useSuperFollowsDeactivateMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/tYYBdo8fCA4AHLbLpVCjSg/useSuperFollowsSaveOnboardingMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/n_8DEszcTWYxHgUnMGR8vw/MonetizationAwardsRevenueQuery`<br>
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
## MonetizationAwardsSettingsQuery<br>
Request URL: `https://api.twitter.com/graphql/9aX5g4DnUZtOROAY-c4zxg/MonetizationAwardsSettingsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/6JGwvxtSd1eFTOWaHEkAUg/MonetizationAwardsTransactionsQuery`<br>
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
## MonetizationEarningsQuery<br>
Request URL: `https://api.twitter.com/graphql/OEDbqvCH79--KG7Qj-Ee7w/MonetizationEarningsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/7p0HY_Hd7ZcK3uXqAmAoSg/MonetizationPayoutHistoryQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/kzpLZ6KeDZ_lotfRoxIePg/MonetizationSuperFollowsNewSubscriptionsQuery`<br>
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
## MonetizationSuperFollowsPerksQuery<br>
Request URL: `https://api.twitter.com/graphql/R3oGONdm5lb25R25U94N8w/MonetizationSuperFollowsPerksQuery`<br>
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
## MonetizationSuperFollowsRenewalsQuery<br>
Request URL: `https://api.twitter.com/graphql/2QASyo6GGsSamHC_Oz_sqg/MonetizationSuperFollowsRenewalsQuery`<br>
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
## MonetizationSuperFollowsRevenueQuery<br>
Request URL: `https://api.twitter.com/graphql/1C4Ulpazk8NE0jzOx7krYw/MonetizationSuperFollowsRevenueQuery`<br>
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
## MonetizationSuperFollowsSettingsQuery<br>
Request URL: `https://api.twitter.com/graphql/FEgryu7DU8x4i1FBqzzGzw/MonetizationSuperFollowsSettingsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/EWp9dMVitYnNjmyidTUy1A/MonetizationSuperFollowsTransactionDetailsQuery`<br>
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
## useAwardsDeactivateMutation<br>
Request URL: `https://api.twitter.com/graphql/01C9DqWmpi6YUNYaIWMBwA/useAwardsDeactivateMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/3WMJN5LwxGA85U4iLzcfbg/SuperFollowsApplicationSubmitScreenMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/_97mdj3S3wU106zmC8Wy3A/SuperFollowsOnboardingPricingConfirmScreenMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/0O6t1hTvRxm_SLarwb1F9g/SuperFollowsSettingsQuery`<br>
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
## useSuperFollowsCreateStripeOnboardingUrlMutation<br>
Request URL: `https://api.twitter.com/graphql/KCzv96qeUky_-C22g3lZSw/useSuperFollowsCreateStripeOnboardingUrlMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/c_ww6XqjHvIqQAZWzaRR2g/AwardsSettingsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/ql0nbxLYZcgEQyw5Z0PlWw/useAwardsActivateMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDmConversationMetadataQuery<br>
Request URL: `https://api.twitter.com/graphql/IljetauiTK1r1nzm9zNY-g/evolutionDmConversationMetadataQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## evolutionDmConversationTimelineQuery<br>
Request URL: `https://api.twitter.com/graphql/Dn3VEKOs5dMcljLjtAWqQA/evolutionDmConversationTimelineQuery`<br>
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
## AddParticipantsMutation<br>
Request URL: `https://api.twitter.com/graphql/oBwyQ0_xVbAQ8FAyG0pCRA/AddParticipantsMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/GPZWK9bL2rpEJ9Dmq5urEQ/DMReportMessageListQuery`<br>
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
## ProfileSpotlights_EditableProfileSpotlightsQuery<br>
Request URL: `https://api.twitter.com/graphql/r3pgxpnbcR10hKon3pxNEg/ProfileSpotlights_EditableProfileSpotlightsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/mDq5tCOsuuDzxezaI30d3A/UpdateProfileSpotlightVisibilityMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/PtT7DMn9eI8yFh-jkG-fGg/LocationSpotlightQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/2ohYQLw6z3bqaCjSqs_LBQ/useDeleteLocationSpotlightMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/1fFcufgOXV2EXGD578RpQw/useMapImageLoaderQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/E4b4WwmzUESbbZJmz3vbjA/ProfessionalHomeQuery`<br>
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
## ReportDetailQuery<br>
Request URL: `https://api.twitter.com/graphql/iDoo9-T00DI2oypZ0YmRNQ/ReportDetailQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/1wRoskRvcqMJ66YJuIJVJA/ReportDetailSafetyCenterQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/jFSVxO6XekDkqa9LhEqxug/LoggedOutSearchHomeTrendsListQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/1PcjM2Rbmn8rKYj8trjO6w/TweetActivityQuery`<br>
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
## TwitterBlueSignUpV2Query<br>
Request URL: `https://api.twitter.com/graphql/E-4ViSQvATkpc-4y9zIbgA/TwitterBlueSignUpV2Query`<br>
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
Request URL: `https://api.twitter.com/graphql/7UIOQwnGlrNqaLd16fTwYg/TwitterCoinsManagementCoinBalanceQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/igqUnYeQrT3zZzgw5Tp0FQ/TwitterCoinsManagementCoinPackQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/QP5WVTrpvWikhlKybPX5jQ/useCoinPurchaseSessionUrlMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/_VDotBzHuuA7S_mVil4xJA/TrustedFriendsAddRemoveButtonAddMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsAddRemoveButtonRemoveMutation<br>
Request URL: `https://api.twitter.com/graphql/pwXaXTTpChehT6k27CLS9A/TrustedFriendsAddRemoveButtonRemoveMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsMembersQuery<br>
Request URL: `https://api.twitter.com/graphql/yQD4In2qJOzB634Gihn8OA/TrustedFriendsMembersQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## TrustedFriendsRecommendedQuery<br>
Request URL: `https://api.twitter.com/graphql/1OOnfeRa2lOFhK7sFUbT3g/TrustedFriendsRecommendedQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## combinedListsPageTimelineQuery<br>
Request URL: `https://api.twitter.com/graphql/fdngji2GPUmKzvkBpEt9vQ/combinedListsPageTimelineQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| freedom_of_speech_not_reach_appeal_label_enabled                        | ...     | error     |        nan |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| interactive_text_enabled                                                | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_text_conversations_enabled                               | boolean | nan       |          0 |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          0 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| vibe_api_enabled                                                        | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## userNftContainer_Query<br>
Request URL: `https://api.twitter.com/graphql/gTkKcR0rAOGFRHAU_uAkTQ/userNftContainer_Query`<br>
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
## SuperFollowsManageQuery<br>
Request URL: `https://api.twitter.com/graphql/9wSLGuGXeq_zKNUZYEAF6Q/SuperFollowsManageQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/X6X4JiyQHfLz0SdTaZPixw/useSuperFollowsChangeBadgePrivacyAddMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/Mg-0dMrg-__WGhnWqj4nfQ/useSuperFollowsChangeBadgePrivacyRemoveMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/cot9fAsCQIQGNYu9Rica6w/useSuperFollowsCreateStripePortalUrlMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/Kl7SMuZW91heufwOO_NAQw/SuperFollowsSubscribeQuery`<br>
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
## useSuperFollowsCreateStripeSubscriptionUrlMutation<br>
Request URL: `https://api.twitter.com/graphql/1nNykZ_aQohdxHKoykBVmg/useSuperFollowsCreateStripeSubscriptionUrlMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/9zwVLJ48lmVUk8u_Gh9DmA/ProfileSpotlightsQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/QSueyUwwWLaV6s50Z8Ct4Q/AffiliateListItemMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/dZT-8dKX9k4_0rplISnH5g/AffiliatesScreenAffiliatesQuery`<br>
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
## InvitationListItemDeleteInvitationMutation<br>
Request URL: `https://api.twitter.com/graphql/Lr0hNCXSzV_2klR0HhKAhg/InvitationListItemDeleteInvitationMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## InvitationListItemResendInvitationMutation<br>
Request URL: `https://api.twitter.com/graphql/Jk-kQiyU2Rh6r7gylTsLtA/InvitationListItemResendInvitationMutation`<br>
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
## InviteScreenMutation<br>
Request URL: `https://api.twitter.com/graphql/dvDIQlpJ0rXUiwhzoQfpBA/InviteScreenMutation`<br>
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
## InviteScreenQuery<br>
Request URL: `https://api.twitter.com/graphql/bv6PUXQe88oQ9ES6I7ZoKw/InviteScreenQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## WelcomeScreenMutation<br>
Request URL: `https://api.twitter.com/graphql/vmeQkOLp4CLZ2zG0AgIe3A/WelcomeScreenMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/kURURMFUKw2d-eHgilgSzA/FollowHostButtonQuery`<br>
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
Request URL: `https://api.twitter.com/graphql/5jpFuDdu111UuWpne0_ajg/PinTweetToCommunityMutation`<br>
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
Request URL: `https://api.twitter.com/graphql/GJ-aDJmAPMnisHg-52fI3g/UnpinTweetFromCommunityMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
