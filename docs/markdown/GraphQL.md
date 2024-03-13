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
## AudioSpaceAddSharing<br>
Request URL: `https://twitter.com/i/api/graphql/-degz0CEDrE8KeC9JhYtCA/AudioSpaceAddSharing`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://twitter.com/i/api/graphql/ARXL11vi9i1d3TrrweT9gw/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| spaces_2022_h2_spaces_communities                                       | boolean | True       |
| spaces_2022_h2_clipping                                                 | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceDeleteSharing<br>
Request URL: `https://twitter.com/i/api/graphql/YMbfLMTUUEzEEMibvvR26Q/AudioSpaceDeleteSharing`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
## BlockedAccountsAll<br>
Request URL: `https://twitter.com/i/api/graphql/EDuJJnhTxj5gMtDd6iifiA/BlockedAccountsAll`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/yxlxyywYdkgokB5GpJnd0w/BlockedAccountsAutoBlock`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/5-oylmTaDoBpUmPyepNHfA/BlockedAccountsImported`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/OCqNU1yUnXcDgiv79zV1IQ/BlueVerifiedFollowers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesExploreTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/AGTKMunUB7Bn26VlLuPSkw/CommunitiesExploreTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/T1fday42OzT6YWRIT7ZHlQ/CommunitiesMainDiscoveryModule`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/icvUKM_PyWc2sGv5P13L8g/CommunitiesMainPageTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/q_LI09hbvJrRl646bC86Dw/CommunitiesMembershipsSlice`<br>
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
Request URL: `https://twitter.com/i/api/graphql/r-o8pcZDMTRJXyAsc0btFg/CommunitiesMembershipsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/HM4f51TQ6-BY7Wmt0A3LAg/CommunityAboutTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/9UY0HBnKiqJD9TAKBVpdLg/CreateCommunity`<br>
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
Request URL: `https://twitter.com/i/api/graphql/nasoTTTgdeFZOvKeppXYDw/CommunityCreateRule`<br>
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
Request URL: `https://twitter.com/i/api/graphql/FCiDsDzfruPKqNi-HCijMg/CommunityDiscoveryTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/mfiSARwzqYdE17FiIQjkZA/CommunityEditBannerMedia`<br>
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
Request URL: `https://twitter.com/i/api/graphql/mp7rCMJJ8em308yjaQgp7w/CommunityEditName`<br>
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
Request URL: `https://twitter.com/i/api/graphql/1bYccjtPTiehdB2cBDK8mw/CommunityEditPurpose`<br>
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
## CommunityEditQuestion<br>
Request URL: `https://twitter.com/i/api/graphql/t6mR9H84IPRd1Ua6uxXFjw/CommunityEditQuestion`<br>
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
Request URL: `https://twitter.com/i/api/graphql/DadeX3LUOz-5GTKAPk7uJg/CommunityEditRule`<br>
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
Request URL: `https://twitter.com/i/api/graphql/doln0W7AwnuAHfDgjPN3Lw/CommunityByRestId`<br>
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
Request URL: `https://twitter.com/i/api/graphql/Bc0ShkpWa8A83SsSf4Jc3Q/CommunityHashtagsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/VrS7ikKsDI84HLH4Ojpe6Q/JoinCommunity`<br>
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
Request URL: `https://twitter.com/i/api/graphql/p8A270ekyor6dU4kuqixcg/LeaveCommunity`<br>
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
## CommunityMediaLoggedOutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/uq2cFMGiHYHGJWLBdv6hPA/CommunityMediaLoggedOutTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/JfInZ_PdK_gQPh49VwmAEw/CommunityMediaTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/86YkIGxz61T7fUY3NvDlRA/CommunityMemberRelationshipTypeahead`<br>
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
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/lVhstscV70SAHhEVAcIz1Q/CommunityModerationKeepTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/ovXhN0RIzUniM-QUIDV0Qw/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/Qn_QdyjB_KS3oZO5nLj4ig/CommunityRemoveBannerMedia`<br>
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
Request URL: `https://twitter.com/i/api/graphql/viWJLKB3XoLg4hcKuViipw/CommunityRemoveRule`<br>
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
Request URL: `https://twitter.com/i/api/graphql/nfYPGNzDiCiYSq3ojgM0OQ/CommunityReorderRules`<br>
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
Request URL: `https://twitter.com/i/api/graphql/ZWoMvZwTfTfearQ-V8RPuA/RequestToJoinCommunity`<br>
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
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ixLrytv_2T9O7e17mHjRvw/CommunityTweetsLoggedOutTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/o_PtvKGxoDWb--H6CeeE-g/CommunityTweetsRankedLoggedOutTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/wQrb8zGUGlhJwv8wjrthKA/CommunityTweetsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/uPaWoQfJcMqFr4ueXPL3gQ/CommunityUpdateRole`<br>
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
Request URL: `https://twitter.com/i/api/graphql/oqB1AvA-9spIq10wud3aLw/CommunityUserInvite`<br>
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
## CommunityUserRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/eQTgFdeMBmJvds7r3islQg/CommunityUserRelationshipTypeahead`<br>
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
Request URL: `https://twitter.com/i/api/graphql/swy-dotP7MdnXISPwmHkjQ/ConnectTabTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://twitter.com/i/api/graphql/e2uaOT_n-Xc06x0IWmCHog/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/sgqau0P5BUJPMU_lgjpd_w/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/yF2c0w5957TlqlTYElsF7g/CreatorSubscriptionsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
## DeviceIsVerified<br>
Request URL: `https://twitter.com/i/api/graphql/_384ihv8PithUm1UbGfAyA/DeviceIsVerified`<br>
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
Request URL: `https://twitter.com/i/api/graphql/qfoQ_hkAs_9eDfBNtlmMew/ExplorePage`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## Followers<br>
Request URL: `https://twitter.com/i/api/graphql/Uc7ZOJrxsJAzMVCcaxis8Q/Followers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/B4bFvrNDN-O-DN-Vy5faLg/FollowersYouKnow`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/PiHWpObvX9tbClrUl6rL9g/Following`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GeneratePinCode<br>
Request URL: `https://twitter.com/i/api/graphql/-Ja49b1NyF9nkZtiMQ4iiw/GeneratePinCode`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/5zmdXuijsrIUfuQMsazaZQ/GenericTimelineById`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/U0cdisy7QFIoTfu3-Okw0A/HomeLatestTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/k3YiLNE_MAy5J-NANLERdg/HomeTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/SREeOPloC_w3bBN_JIDomQ/ImmersiveMedia`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveProfile<br>
Request URL: `https://twitter.com/i/api/graphql/IemIzGlPF2ycK4XaEBYNSA/ImmersiveProfile`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://twitter.com/i/api/graphql/B8I_QCljDBVfin21TTWMqA/Likes`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/-FT_rm03o7MvVlol1i25sQ/ListSearchTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## ModeratedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/O1d3E-kr128XIXQU2KAxVA/ModeratedTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/7gmS7e2n-S0uFC1TqweqGA/MutedAccounts`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## PinTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/dv8wNEwVhTKXdY7mYhbTSg/PinTimeline`<br>
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
## PinnedTimelines<br>
Request URL: `https://twitter.com/i/api/graphql/OnFhOoO-fqqzg7fkNbVFuA/PinnedTimelines`<br>
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
## SearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/flaR-PUMshxFWZWPNpq4zA/SearchTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
## SimilarPosts<br>
Request URL: `https://twitter.com/i/api/graphql/65CGgtjeTRo1S8YE2UPXmQ/SimilarPosts`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/GLkj58KHySSaorFasJrzYQ/SuperFollowers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TopicLandingPage<br>
Request URL: `https://twitter.com/i/api/graphql/xBERNyZ8xL8IU_fOu4psTw/TopicLandingPage`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
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
Request URL: `https://twitter.com/i/api/graphql/4OUZZOonV2h60I0wdlQb_w/TopicByRestId`<br>
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
Request URL: `https://twitter.com/i/api/graphql/oR3Wl5Bc7K5IV5tu57OQLQ/TopicToFollowSidebar`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://twitter.com/i/api/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
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
Request URL: `https://twitter.com/i/api/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
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
Request URL: `https://twitter.com/i/api/graphql/c-x3VLQT_gRnYEu6ZbqyDQ/TopicsManagementPage`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://twitter.com/i/api/graphql/1g-7gqaaY82sdG2Xku5XFg/TopicsPickerPage`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://twitter.com/i/api/graphql/Zlx7E-tCZwZznfQ0FR9YRw/TopicsPickerPageById`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrustedFriendsTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/hSylacaUe1Umga6Ro75mmw/TrustedFriendsTypeahead`<br>
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
## TVHomeMixer<br>
Request URL: `https://twitter.com/i/api/graphql/1dbXChcG5ubJXI5ZEeqFOQ/TVHomeMixer`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVUserProfile<br>
Request URL: `https://twitter.com/i/api/graphql/j8eauG9b8-1qaFg0-oFnUw/TVUserProfile`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/ZkD-1KkxjcrLKp60DPY_dQ/TweetDetail`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetRelatedVideos<br>
Request URL: `https://twitter.com/i/api/graphql/J6iFsMwU6m2DyMJgQtQTKQ/TweetRelatedVideos`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/OUKdeWm3g4tDbW5hffX_QA/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/aGRumfuBRlOaI5aO6-YaPA/TweetResultsByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
## UnpinTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/9PxaHu17tTsVrxirSWKH8Q/UnpinTimeline`<br>
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
## UpdatePinnedTimelines<br>
Request URL: `https://twitter.com/i/api/graphql/UMpFFKUAPQ7Tm4byVksTUA/UpdatePinnedTimelines`<br>
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
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/aKq5eZ3n3TYu9TewxYkdHg/UrtFixtures`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/bM54kELwOuErgco8aCe8BA/UserAboutTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://twitter.com/i/api/graphql/7d7BlnOsLiZMXdBoteftrA/UserArticlesTweets`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/OjfBE1VOn0dS_KJfZRmAKw/UserBusinessProfileTeamTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/tD8zKvQzwY3kdx5yz6YmOw/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_likes_enabled                                      | boolean | True       |
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/k5XapwcSikNsEsILW5FvgA/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_likes_enabled                                      | boolean | True       |
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| subscriptions_verification_info_is_identity_verified_enabled      | boolean | True       |
| subscriptions_verification_info_verified_since_enabled            | boolean | True       |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## GetUserClaims<br>
Request URL: `https://twitter.com/i/api/graphql/aQ-b88K_Lp7dgHX53MqNQQ/GetUserClaims`<br>
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
Request URL: `https://twitter.com/i/api/graphql/PED4razsnkK14_Ee5wf4gg/UserCreatorSubscribers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/LMoxqAemnLyrDaBbJnMi9Q/UserCreatorSubscriptions`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://twitter.com/i/api/graphql/eOTTj_P8aj8rRzED2BzzLQ/UserHighlightsTweets`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://twitter.com/i/api/graphql/TOU4gQw8wXIqpSzA4TYKgg/UserMedia`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserPreferences<br>
Request URL: `https://twitter.com/i/api/graphql/xFxU-O8hEYe74ovNVU74jA/UserPreferences`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserPromotableTweets<br>
Request URL: `https://twitter.com/i/api/graphql/ARYDO8ik8axlJwteqcmKgQ/UserPromotableTweets`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/hTWLq0kDe2kqglxKZlXUmQ/UserSuperFollowTweets`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://twitter.com/i/api/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://twitter.com/i/api/graphql/3GeIaLmNhTm1YsUmxR57tg/UserTweetsAndReplies`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/itEhGywpgX9b3GJCzOtSrA/UsersByRestIds`<br>
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
## UsersVerifiedAvatars<br>
Request URL: `https://twitter.com/i/api/graphql/aLfvAoX6xy2ojqzOnkbrIA/UsersVerifiedAvatars`<br>
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
## Viewer<br>
Request URL: `https://twitter.com/i/api/graphql/W62NnYgkgziw9bwyoVht0g/Viewer`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/lGiFAIYrFZ023hAfp7SoyA/ViewerTeams`<br>
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
Request URL: `https://twitter.com/i/api/graphql/H5-6GCnkFLKGlsF0Mc52Vw/ViewingOtherUsersTopicsPage`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/9PezbW92Zt1JUPDum2CfXg/CombinedLists`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://twitter.com/i/api/graphql/lLNsL7mW6gSEQG6rXP7TNw/ListAddMember`<br>
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
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/Y90WuxdWugtMRJhkXTdvzg/DeleteListBanner`<br>
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
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/t_DsROHldculsB0B9BUAWw/EditListBanner`<br>
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
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/v19WqbBKzI6_N-2LrtrQ6A/ListBySlug`<br>
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
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/EYg7JZU3A1eJ-wr2eygPHQ/CreateList`<br>
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
## ListCreationRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/X9aCIVmL-sc7ZUmsSKpH-w/ListCreationRecommendedUsers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/lTulZsGyh-cYSyaidDEpnw/ListEditRecommendedUsers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/TOTgqavWmxywKv5IbMMK1w/ListLatestTweetsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/FOtiCTKXhMqD4Gk7AFf3uw/ListMembers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/14FSuiF03a6rXSW8HOmRQw/ListMemberships`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/bvcalunVs8AYM0Y3gR6x2g/ListOwnerships`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/9hbYpeVBMq8-yB8slayGWQ/ListByRestId`<br>
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
## ListRankedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/8EyeRtm8ktRkXlZUBNq4vQ/ListRankedTweetsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/cvDFkG5WjcXV0Qw5nfe1qQ/ListRemoveMember`<br>
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
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/fP4EIb8O_6YwOhCw3_n2YQ/ListSubscribe`<br>
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
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/mXIy0GuRDoGn8zHzfItSFA/ListSubscribers`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
## ListUnsubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/xqm4TdOxDYhy1UhouKelsA/ListUnsubscribe`<br>
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
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/dIEI1sbSAuZlxhE0ggrezA/UpdateList`<br>
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
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/ctRonD4cJxrUqiVyWRsPhg/ListsDiscovery`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/PX5iJwulupq2wTQU8TEbXA/ListsManagementPageTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fR4X9Ngp_4XWAIOV0WV5Ww/BookmarkFolderTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/uNowfj04D8HFVFMbjm6xrQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
## EditBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
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
## RemoveTweetFromBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
## BroadcastQuery<br>
Request URL: `https://twitter.com/i/api/graphql/IYpwyDhAxS89lVXmffLHlQ/BroadcastQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fR4X9Ngp_4XWAIOV0WV5Ww/BookmarkFolderTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/uNowfj04D8HFVFMbjm6xrQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/V1c7MX8SMNc-KBBnoTsWsQ/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_video_timestamps_enabled                                     | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/NiOYlTJLvftMmVgiFAKi5A/DmMutedTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
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
Request URL: `https://twitter.com/i/api/graphql/g4ALTtGcHsYTpqnKb3eSAg/ArticleTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/YAWDXAgDnXGAQ_-Bk-uutg/ArticleTweetsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://twitter.com/i/api/graphql/LUOeqffAhl-m4Xtwj5lz8g/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                            | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
Request URL: `https://twitter.com/i/api/graphql/foo0JuZNivom_19CQNNN4w/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
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
## BirdwatchEditUserSettings<br>
Request URL: `https://twitter.com/i/api/graphql/k1Unfqb74V4sf2d7-kFkhg/BirdwatchEditUserSettings`<br>
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
Request URL: `https://twitter.com/i/api/graphql/JSf0I8AZFRLzAuay4E0eZw/BirdwatchFetchAuthenticatedUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                 | type    |   variable | default   |
|:----------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_top_contributor_enabled    | boolean |          1 | nan       |
| responsive_web_birdwatch_mobile_nav_setting_enabled | ...     |        nan | error     |
| responsive_web_birdwatch_note_limit_enabled         | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://twitter.com/i/api/graphql/iL_0nGf1nelAd9Kz-pZJlA/BirdwatchFetchBirdwatchProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                              | type    | variable   |
|:-------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_top_contributor_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchFetchCanTweetBeMediaNote<br>
Request URL: `https://twitter.com/i/api/graphql/631X76cvyQ0CtLViMsdulw/BirdwatchFetchCanTweetBeMediaNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                          | type    | variable   |
|:---------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchFetchGlobalTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/6N3cz6I2MxBn7pO4XGJrgQ/BirdwatchFetchGlobalTimeline`<br>
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://twitter.com/i/api/graphql/sUWMyBP-QZBbcPYg4O3dvA/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/a0bIhEpz8oeSAK5A0MN_Rg/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
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
## BirdwatchFetchSignUpEligiblity<br>
Request URL: `https://twitter.com/i/api/graphql/yASGrjmFWghK2T0XC3uGVg/BirdwatchFetchSignUpEligiblity`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                            | type    | variable   |
|:-----------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_signup_prompt_enabled | boolean | True       |

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
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fR4X9Ngp_4XWAIOV0WV5Ww/BookmarkFolderTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/uNowfj04D8HFVFMbjm6xrQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fR4X9Ngp_4XWAIOV0WV5Ww/BookmarkFolderTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/uNowfj04D8HFVFMbjm6xrQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BroadcastQuery<br>
Request URL: `https://twitter.com/i/api/graphql/IYpwyDhAxS89lVXmffLHlQ/BroadcastQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AiTrendByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/7gDQhOOHu7q8MANKo-1pTg/AiTrendByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## ArticleEntitiesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/3Br16o1APwCIK5eoKh2Sfg/ArticleEntitiesSlice`<br>
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
## ArticleEntityDelete<br>
Request URL: `https://twitter.com/i/api/graphql/e4lWqB6m2TA8Fn_j9L9xEA/ArticleEntityDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleEntityDraftCreate<br>
Request URL: `https://twitter.com/i/api/graphql/6Q1x5qlomuvdN1DxviJHvg/ArticleEntityDraftCreate`<br>
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
## ArticleEntityPublish<br>
Request URL: `https://twitter.com/i/api/graphql/zzzF-JLFd7NB3mrMmmGzpQ/ArticleEntityPublish`<br>
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
## ArticleEntityResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/yLPnbPrMsE8d2dZoZs69Kw/ArticleEntityResultByRestId`<br>
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
## ArticleEntityUnpublish<br>
Request URL: `https://twitter.com/i/api/graphql/FfqlYgdQygtoTu5O8eo0iA/ArticleEntityUnpublish`<br>
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
## ArticleEntityUpdateContent<br>
Request URL: `https://twitter.com/i/api/graphql/WZyC-MOKHpfxXURSn0Vf4Q/ArticleEntityUpdateContent`<br>
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
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://twitter.com/i/api/graphql/MkPEBG7D5XfkWzLRTtAMEQ/ArticleEntityUpdateCoverMedia`<br>
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
## ArticleEntityUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/_UEosgudh7FOwEESnzFK2Q/ArticleEntityUpdateTitle`<br>
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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://twitter.com/i/api/graphql/V1c7MX8SMNc-KBBnoTsWsQ/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_video_timestamps_enabled                                     | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmMutedTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/NiOYlTJLvftMmVgiFAKi5A/DmMutedTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## ClearGrokConversations<br>
Request URL: `https://twitter.com/i/api/graphql/83Gg0lfI-47Z3-ZOxyUjiQ/ClearGrokConversations`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokHome<br>
Request URL: `https://twitter.com/i/api/graphql/cdHoKeM-ZKjVA4Mu7mYz7A/GrokHome`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokShare<br>
Request URL: `https://twitter.com/i/api/graphql/g-yY63EIIwut1NBcDeSN5g/GrokShare`<br>
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
## SetGrokPreferences<br>
Request URL: `https://twitter.com/i/api/graphql/FdptFc7p_xMhafpNkbCW8A/SetGrokPreferences`<br>
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
Request URL: `https://twitter.com/i/api/graphql/KF6aISQR75s_UpLeocZ0TA/RitoActionedTweetsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/uTdw7Mwdh-zGsS_gG_j49Q/RitoFlaggedTweetsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
## UserAccountLabel<br>
Request URL: `https://twitter.com/i/api/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/3Y3356PTjeY9RfKYULEtng/Favoriters`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://twitter.com/i/api/graphql/EvCvYif_Wh6UgW1nQunmLA/Retweeters`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://twitter.com/i/api/graphql/C7alo51WakHqnRmaW0RFXg/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetStats<br>
Request URL: `https://twitter.com/i/api/graphql/EvbTkPDT-xQCfupPu0rWMA/TweetStats`<br>
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
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fR4X9Ngp_4XWAIOV0WV5Ww/BookmarkFolderTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/uNowfj04D8HFVFMbjm6xrQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
`None`<br>
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SidebarUserRecommendations<br>
Request URL: `https://twitter.com/i/api/graphql/65tMH0mJcP4Z24f1RbYvrA/SidebarUserRecommendations`<br>
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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/fR4X9Ngp_4XWAIOV0WV5Ww/BookmarkFolderTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/uNowfj04D8HFVFMbjm6xrQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
`None`<br>
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
## RitoFlaggedAccountsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/J3BxyfyCRUBzJrm0_JPgow/RitoFlaggedAccountsTimeline`<br>
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
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleEntitiesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/3Br16o1APwCIK5eoKh2Sfg/ArticleEntitiesSlice`<br>
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
## ArticleEntityDelete<br>
Request URL: `https://twitter.com/i/api/graphql/e4lWqB6m2TA8Fn_j9L9xEA/ArticleEntityDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleEntityDraftCreate<br>
Request URL: `https://twitter.com/i/api/graphql/6Q1x5qlomuvdN1DxviJHvg/ArticleEntityDraftCreate`<br>
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
## ArticleEntityPublish<br>
Request URL: `https://twitter.com/i/api/graphql/zzzF-JLFd7NB3mrMmmGzpQ/ArticleEntityPublish`<br>
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
## ArticleEntityResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/yLPnbPrMsE8d2dZoZs69Kw/ArticleEntityResultByRestId`<br>
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
## ArticleEntityUnpublish<br>
Request URL: `https://twitter.com/i/api/graphql/FfqlYgdQygtoTu5O8eo0iA/ArticleEntityUnpublish`<br>
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
## ArticleEntityUpdateContent<br>
Request URL: `https://twitter.com/i/api/graphql/WZyC-MOKHpfxXURSn0Vf4Q/ArticleEntityUpdateContent`<br>
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
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://twitter.com/i/api/graphql/MkPEBG7D5XfkWzLRTtAMEQ/ArticleEntityUpdateCoverMedia`<br>
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
## ArticleEntityUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/_UEosgudh7FOwEESnzFK2Q/ArticleEntityUpdateTitle`<br>
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
