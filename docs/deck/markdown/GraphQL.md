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
## ActionTrend<br>
Request URL: `https://x.com/i/api/graphql/imr0xefZmILHTgb6-9pe3g/ActionTrend`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AiTrendByRestId<br>
Request URL: `https://x.com/i/api/graphql/jeDK3ynFQB7lf5WfJIvBHA/AiTrendByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ReportTrend<br>
Request URL: `https://x.com/i/api/graphql/3BZlCEmD645zQ-MpJM19CA/ReportTrend`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SaveTrend<br>
Request URL: `https://x.com/i/api/graphql/_fJD2rm-lJI06lKxbUZT2Q/SaveTrend`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## AuthenticatePeriscope<br>
Request URL: `https://x.com/i/api/graphql/r7VUmxbfqNkx7uwjgONSNw/AuthenticatePeriscope`<br>
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
Request URL: `https://x.com/i/api/graphql/PFIxTk8owMoZgiMccP0r4g/getAltTextPromptPreference`<br>
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
Request URL: `https://x.com/i/api/graphql/aQKrduk_DA46XfOQDkcEng/updateAltTextPromptPreference`<br>
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
Request URL: `https://x.com/i/api/graphql/QjN8ZdavFDqxUjNn3r9cig/AuthenticatedUserTFLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BakeryQuery<br>
Request URL: `https://x.com/i/api/graphql/pROR-yRiBVsEjJyHt3fvhg/BakeryQuery`<br>
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
Request URL: `https://x.com/i/api/graphql/0353rMT3W69bBCUmax6fLw/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://x.com/i/api/graphql/13O8Z3IXH98PedoVsnl8cg/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://x.com/i/api/graphql/40yp-fr85OSvG-zgBqzjoQ/BlueVerifiedFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/YogsYxSdBXVmmZJ8ree8DA/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://x.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/BCOWUpH-INJvc1ClF7O91Q/BookmarkSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://x.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
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
Request URL: `https://x.com/i/api/graphql/Z6-zEzG4zK9cPD6GJWMJKg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/i8SaWIjevzaZJIsQt5rpsw/BroadcastQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://x.com/i/api/graphql/O4uUIAMxFGKCEKIiZ7b_VA/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesExploreTimeline<br>
Request URL: `https://x.com/i/api/graphql/3d3TeJlLFR7PcRpJgSOchA/CommunitiesExploreTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://x.com/i/api/graphql/6hdH89a9VK9j2UfHbS-m3w/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/_jjUzIOQHh_R0880K9n_Kw/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://x.com/i/api/graphql/HnfvxaoTm6MEqAXMNz-zaA/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://x.com/i/api/graphql/n3lOg4I-bb0oEk05oDc1cg/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://x.com/i/api/graphql/-Ck7awbHZCgzXiQuQYvkfw/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://x.com/i/api/graphql/4kOxoaE221Yc8kzqMJzPMg/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://x.com/i/api/graphql/2Fo8hU-y2MCWE6D0dmz8jg/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://x.com/i/api/graphql/_CjBwmt7IUJjKFF0Lq1BXA/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/PJpjF46R_MBtFt0y19XX5Q/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://x.com/i/api/graphql/dEP_L--hwTajQiMIZBmR6A/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://x.com/i/api/graphql/bvds0mOCWa3MpNVLSTej4A/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditQuestion<br>
Request URL: `https://x.com/i/api/graphql/2UkmWdZ82NhN3F3k1X0ckQ/CommunityEditQuestion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://x.com/i/api/graphql/2WJ_LqrjEgiobbpwjJh2ow/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://x.com/i/api/graphql/o5M-3G_1fTbscKNqE3NOLg/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key           | type   | variable      |
|:--------------|:-------|:--------------|
| communityId   | ...    | t.communityId |
| ...()(0,$n.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://x.com/i/api/graphql/0lvFq9v9HfqqGmgG6lbuwA/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/dZ5DPgXcYhRpaTzN5jfGBg/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://x.com/i/api/graphql/SdvGOFosGXtlBiqeGhpoSg/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityMediaLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/HMSqCw1a8QnmR6qkkjOuuQ/CommunityMediaLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://x.com/i/api/graphql/VOx6nsVRFj78PqM9Ak_WKw/CommunityMediaTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://x.com/i/api/graphql/_h1cVpB5J1-jg2iU8uv6bw/CommunityMemberRelationshipTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/luDCqQS9LRcg_Ueqfw-Gxw/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://x.com/i/api/graphql/2V3IHFkmeQB1iJ_MK33a7w/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/QC-6R0khXPL0vRBTwQjWsA/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://x.com/i/api/graphql/_ZJqesEGzTiQNB9IqDlAmA/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | t.communityId |
| ruleId       | ...    | t.ruleId      |
| ...()(0,d.S) | ...    | _             |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://x.com/i/api/graphql/KolJuP0vuLbQXkl8NoVZ0A/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/wdAlV3VGr105zkF2vcG4cw/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetModerationLogSlice<br>
Request URL: `https://x.com/i/api/graphql/mXYa3PDeB_g3xzY6RDACpg/CommunityTweetModerationLogSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/yNDS_7pdbNT3EASGwX8APg/CommunityTweetsLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/g8rb7-oc4CQlxyjMJNoaIQ/CommunityTweetsRankedLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/OkvXlqyRbfh6vd1fjJhDiA/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://x.com/i/api/graphql/0EUpMRF3RSljLFVXy9pZDg/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://x.com/i/api/graphql/pbeAbOjoklMKc0UV9mbsIA/CommunityUserInvite`<br>
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
Request URL: `https://x.com/i/api/graphql/ZqX6ivkf1G5EqRw12ZJ30w/CommunityUserRelationshipTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/vIcOpuIILpABMMfhdPVRKQ/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ConversationControlChange<br>
Request URL: `https://x.com/i/api/graphql/hb1elGcj6769uT8qVYqtjw/ConversationControlChange`<br>
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
Request URL: `https://x.com/i/api/graphql/OoMO_aSZ1ZXjegeamF9QmA/ConversationControlDelete`<br>
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
Request URL: `https://x.com/i/api/graphql/aoDbu3RHznuiSkQ9aNM67Q/CreateBookmark`<br>
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
Request URL: `https://x.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
Request URL: `https://x.com/i/api/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/7jEc7ECTTDcNaqsMhjTxXg/CreateHighlight`<br>
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
Request URL: `https://x.com/i/api/graphql/Pn3VQrqJL8wMlIRQVUcajg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://x.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet`<br>
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
Request URL: `https://x.com/i/api/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/2tP8XUYeLHKjq5RHvuvpZw/CreateTrustedFriendsList`<br>
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
Request URL: `https://x.com/i/api/graphql/u517yrEkTIlETJ4LCO6sog/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://x.com/i/api/graphql/yn6DRrqv-0tscLqUt-zJXg/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DataSaverMode<br>
Request URL: `https://x.com/i/api/graphql/xF6sXnKJfS2AOylzxRjf6A/DataSaverMode`<br>
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
Request URL: `https://x.com/i/api/graphql/H03etWvZGz41YASxAU2YPg/WriteDataSaverPreferences`<br>
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
Request URL: `https://x.com/i/api/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
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
Request URL: `https://x.com/i/api/graphql/Wlmlj2-xzyS1GN3a6cj-mQ/DeleteBookmark`<br>
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
Request URL: `https://x.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
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
Request URL: `https://x.com/i/api/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/ea-VVDSLIEYNY2_2aPg3Uw/DeleteHighlight`<br>
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
Request URL: `https://x.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet`<br>
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
Request URL: `https://x.com/i/api/graphql/CTOVqej0JBXAZSwkp1US0g/DeleteScheduledTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/g2m0pAOamawNtVIfjXNMJg/DisableVerifiedPhoneLabel`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## dmBlockUser<br>
Request URL: `https://x.com/i/api/graphql/IYw9u1KEhrS-t-BXsau4Uw/dmBlockUser`<br>
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
Request URL: `https://x.com/i/api/graphql/of_N6O33zfyD4qsFJMYFxA/DmNsfwMediaFilterUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## dmUnblockUser<br>
Request URL: `https://x.com/i/api/graphql/Krbs6Nak_o7liWQwfV1jOQ/dmUnblockUser`<br>
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
Request URL: `https://x.com/i/api/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
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
Request URL: `https://x.com/i/api/graphql/JIeXE-I6BZXHfxsgOkyHYQ/EditDraftTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/C3RJFfMsb_KcEytpKmRRkw/EnableVerifiedPhoneLabel`<br>
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
Request URL: `https://x.com/i/api/graphql/AO0wqcj9R80t7LZapf7LaA/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ExploreSidebar<br>
Request URL: `https://x.com/i/api/graphql/8sobPXXWdmNvK8y9ZYNqBg/ExploreSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FavoriteTweet<br>
Request URL: `https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/xS88j64OVBZWNtQ2suz2tw/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://x.com/i/api/graphql/UyYOyYlbsoSTCsKYJDq0mA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://x.com/i/api/graphql/rx1y84Ch2jkmavgLAww2ww/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://x.com/i/api/graphql/n7h049i-3iM-EPRbGUeSFg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GlobalCommunitiesLatestPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/ScY4rADavvROz7TdMZa2UQ/GlobalCommunitiesLatestPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GlobalCommunitiesPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/mxVo__pK7u8Ka2j8VaBGSA/GlobalCommunitiesPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| cursor | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateColumn<br>
Request URL: `https://x.com/i/api/graphql/O4iIdjZUiZpm0KBSiftNGQ/CreateColumn`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateDeck<br>
Request URL: `https://x.com/i/api/graphql/fVIC9NDfk0-Auids8FlqQQ/CreateDeck`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GryphonDeleteAccountSync<br>
Request URL: `https://x.com/i/api/graphql/DiJkSLAFULTIt7Z6ZnFhgQ/GryphonDeleteAccountSync`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GryphonImportClientSyncColumns<br>
Request URL: `https://x.com/i/api/graphql/DIubYz5FD1NQk6-O1GEUgg/GryphonImportClientSyncColumns`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RemoveColumn<br>
Request URL: `https://x.com/i/api/graphql/lfB7GP4w9oCpx5F_BxwRkw/RemoveColumn`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## RemoveDeck<br>
Request URL: `https://x.com/i/api/graphql/c20tuAQJznmUHtmOAvHLyA/RemoveDeck`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ReorderColumns<br>
Request URL: `https://x.com/i/api/graphql/JJpn5RKFDbYXC957QragBQ/ReorderColumns`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ReorderDecks<br>
Request URL: `https://x.com/i/api/graphql/u2A0QRHa7bBRBhZZSmJKXQ/ReorderDecks`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateClientSettings<br>
Request URL: `https://x.com/i/api/graphql/MlAbo_-7Kslvk5mojg9ttg/UpdateClientSettings`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateColumn<br>
Request URL: `https://x.com/i/api/graphql/suRGd49L2EZ0nuuU4he4aw/UpdateColumn`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateDeck<br>
Request URL: `https://x.com/i/api/graphql/XW307yOKJINBAvlwOnLteg/UpdateDeck`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UpdateGryphonOnboardingState<br>
Request URL: `https://x.com/i/api/graphql/zCQ0LjxvX0Ky0br3nE__PA/UpdateGryphonOnboardingState`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ViewerAccountSync<br>
Request URL: `https://x.com/i/api/graphql/f0FCSjsFhha0z_ez821WIA/ViewerAccountSync`<br>
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
Request URL: `https://x.com/i/api/graphql/YDHDr9I-8A7qerlgVpwh3w/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/PCtxIFNPGycy-SC55MJ-1g/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://x.com/i/api/graphql/k7gNzdMUNqYRfdv3iXyjEw/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://x.com/i/api/graphql/Z_Hm7xmKNmyTkkYBXQnJ4Q/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://x.com/i/api/graphql/Cd0cVNaU_jTi3orlfRfPeg/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://x.com/i/api/graphql/5JsOASfB6W015_dEm7MmgQ/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://x.com/i/api/graphql/mBGC0yBw82sMmeE9FbByQg/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://x.com/i/api/graphql/T33_bCOV4JuKzdb-0I9XJw/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://x.com/i/api/graphql/Kq28sylhi0GwMAmWnn2d5A/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DeleteList<br>
Request URL: `https://x.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList`<br>
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
Request URL: `https://x.com/i/api/graphql/_wZic234DLvY-ej1LADArQ/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | ...    | _          |
| ...n  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListEditRecommendedUsers<br>
Request URL: `https://x.com/i/api/graphql/RVZkW0uWCa7HTW220QF9YA/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/KvI7TbDVa7VRyN72ZwJDzg/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://x.com/i/api/graphql/SyyI594cT4OrOKq-zs3zcA/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://x.com/i/api/graphql/dKr0LJBXPECFgFBmzpJboA/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MuteList<br>
Request URL: `https://x.com/i/api/graphql/ZYyanJsskNUcltu9bliMLA/MuteList`<br>
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
Request URL: `https://x.com/i/api/graphql/F7x0RWISPoEIQHpwwVHjRA/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://x.com/i/api/graphql/smn3p8ZgN724FbaK4roVtQ/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | t.list_id  |
| ...()(0,i.S) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/Vh6-tvwjUAN-Fy9Nb6sIxQ/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://x.com/i/api/graphql/ET9QYYAaZ3QEVa0qEFefwA/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/S8pm9J64N8dXJOGDjfsJUw/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://x.com/i/api/graphql/-E9GctYNv83S8k8QeO3p-g/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://x.com/i/api/graphql/e2m6PAtuTCO1DBOEzBlRWA/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnmuteList<br>
Request URL: `https://x.com/i/api/graphql/pMZrHRNsmEkXgbn3tOyr7Q/UnmuteList`<br>
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
Request URL: `https://x.com/i/api/graphql/tZkstWIOVhBkCjhpdREshQ/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://x.com/i/api/graphql/Jl7VrKOzAcXW-vQAw3gmTg/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://x.com/i/api/graphql/nyvhNx2_a6cK754NcE5OKQ/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/nf7WYf6REbjDBHhGxvoBeQ/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| tweet_id | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ModerateTweet<br>
Request URL: `https://x.com/i/api/graphql/pjFnHGVqCjTcZol0xcBJjw/ModerateTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/x_kuX0dId8XTlYfh3jmNLw/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://x.com/i/api/graphql/BUmJ8PKhbQ0PuGr5SsRcdQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## PaymentsUsersTypeahead<br>
Request URL: `https://x.com/i/api/graphql/5dZxwH3Tfg0yUmG11eC5jQ/PaymentsUsersTypeahead`<br>
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
## PinTimeline<br>
Request URL: `https://x.com/i/api/graphql/bo5Cdo_0waFVymLSASsp7w/PinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## PinTweet<br>
Request URL: `https://x.com/i/api/graphql/VIHsNu89pK-kW35JpHq7Xw/PinTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## PinnedTimelines<br>
Request URL: `https://x.com/i/api/graphql/0PstbMztRIA0BFvq2gWyxQ/PinnedTimelines`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ProfileUserPhoneState<br>
Request URL: `https://x.com/i/api/graphql/5kUWP8C1hcd6omvg6HXXTQ/ProfileUserPhoneState`<br>
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
Request URL: `https://x.com/i/api/graphql/IjQ-egg0uPkY11NyPMfRMQ/PutClientEducationFlag`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| flag  | ...    | n          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesRankedTimeline<br>
Request URL: `https://x.com/i/api/graphql/hSfrfdPDWB-uDaGrqNYikA/CommunitiesRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## RemoveFollower<br>
Request URL: `https://x.com/i/api/graphql/QpNfg0kpPRfjROQ_9eOLXA/RemoveFollower`<br>
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
Request URL: `https://x.com/i/api/graphql/2Qbj9XZvtUvyJB4gFwWfaA/RemoveTweetFromBookmarkFolder`<br>
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
Request URL: `https://x.com/i/api/graphql/ffT6na2E9ReT4yfB5uzw_g/FetchScheduledTweets`<br>
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
Request URL: `https://x.com/i/api/graphql/S9Y5e9vylJCliXvZ8MOB3g/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key               | type   | variable   |
|:------------------|:-------|:-----------|
| grokMode          | ...    | t          |
| grokModelOptionId | ...    | s          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SharingAudiospacesListeningDataWithFollowersUpdate<br>
Request URL: `https://x.com/i/api/graphql/5h0kNbk3ii97rmfY6CdgAA/SharingAudiospacesListeningDataWithFollowersUpdate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key    | type   | variable   |
|:-------|:-------|:-----------|
| cursor | ...    | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SimilarPosts<br>
Request URL: `https://x.com/i/api/graphql/M2m349LkmKcw-TbYe5R8Dw/SimilarPosts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://x.com/i/api/graphql/g968ahK3hUVB5mIKEEHwew/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SupportedLanguages<br>
Request URL: `https://x.com/i/api/graphql/fZ5uZVeledO5SAseKnmTUg/SupportedLanguages`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| keyword | ...    | t          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## timelinesFeedback<br>
Request URL: `https://x.com/i/api/graphql/vfVbgvTPTQ-dF_PQ5lD1WQ/timelinesFeedback`<br>
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
Request URL: `https://x.com/i/api/graphql/ElqSLWFmsPL4NlZI5e1Grg/TopicFollow`<br>
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
Request URL: `https://x.com/i/api/graphql/eF6Adel-VV-6ra2bsFNczw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicNotInterested<br>
Request URL: `https://x.com/i/api/graphql/cPCFdDAaqRjlMRYInZzoDA/TopicNotInterested`<br>
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
Request URL: `https://x.com/i/api/graphql/4OUZZOonV2h60I0wdlQb_w/TopicByRestId`<br>
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
Request URL: `https://x.com/i/api/graphql/Pre2nFmfKIHz6MXZ9g5-Rg/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicUndoNotInterested<br>
Request URL: `https://x.com/i/api/graphql/4tVnt6FoSxaX8L-mDDJo4Q/TopicUndoNotInterested`<br>
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
Request URL: `https://x.com/i/api/graphql/srwjU6JM_ZKTj_QMfUGNcw/TopicUnfollow`<br>
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
Request URL: `https://x.com/i/api/graphql/NfOIXlmL1f-gPIPZdGIhAg/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://x.com/i/api/graphql/9iBwHVx9nnh8IOnUuimv6A/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://x.com/i/api/graphql/ukZolUYmhqTEuBDhs62W_A/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key     | type   | variable   |
|:--------|:-------|:-----------|
| keyword | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrendHistory<br>
Request URL: `https://x.com/i/api/graphql/CMTYz0S1ZD8zRaochs5Xew/TrendHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrendRelevantUsers<br>
Request URL: `https://x.com/i/api/graphql/G_AFTnJw-h4VkC5Bzd_ToQ/TrendRelevantUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVHomeMixer<br>
Request URL: `https://x.com/i/api/graphql/woeiDZCHJIeyRSprkC18iA/TVHomeMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://x.com/i/api/graphql/jSqDD18MkxfdFfMd6Cmk6A/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/jRn3kmDFHt1BmUA-h-OCbA/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://x.com/i/api/graphql/-9XWSmJ9JIBV6aNL8CLmrw/TweetResultsByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UnfavoriteTweet<br>
Request URL: `https://x.com/i/api/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/xVW9j3OqoBRY9d6_2OONEg/UnmentionUserFromConversation`<br>
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
Request URL: `https://x.com/i/api/graphql/pVSyu6PA57TLvIE4nN2tsA/UnmoderateTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/msjW42bS89FZV5Wcm7N2mA/UnpinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                | type   | variable                                 |
|:-------------------|:-------|:-----------------------------------------|
| pinnedTimelineItem | ...    | {'id': 'n', 'pinned_timeline_type': 't'} |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UnpinTweet<br>
Request URL: `https://x.com/i/api/graphql/BhKei844ypCyLYCg0nwigw/UnpinTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/AFIfGGJrJGkib_jNDrBjsw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://x.com/i/api/graphql/riPf_1HZP2MBgcKplZBzhw/UserArticlesTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://x.com/i/api/graphql/kd54Lhx6WSFuSBh_4GJkMQ/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://x.com/i/api/graphql/LWxkCeL8Hlx0-f24DmPAJw/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| subscriptions_feature_can_gift_premium                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://x.com/i/api/graphql/QGIw94L0abhuohrr76cSbw/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| subscriptions_verification_info_is_identity_verified_enabled      | boolean | True       |
| subscriptions_verification_info_verified_since_enabled            | boolean | True       |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| subscriptions_feature_can_gift_premium                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## GetUserClaims<br>
Request URL: `https://x.com/i/api/graphql/aQ-b88K_Lp7dgHX53MqNQQ/GetUserClaims`<br>
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
Request URL: `https://x.com/i/api/graphql/_gNmvdsf4R-nJIq8eTv1yA/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/4W3eI-dhOiz0ESzuV_uPpw/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"articleEntityId":"i","coverMedia":"r&&o?"{"media_id":"r","media_category":"o"}:"void 0"}
```
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://x.com/i/api/graphql/NIKPV1E--0oKmaCxCnDCxg/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://x.com/i/api/graphql/xA1_3UDP7KcWiieazu3SVg/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserPreferences<br>
Request URL: `https://x.com/i/api/graphql/xFxU-O8hEYe74ovNVU74jA/UserPreferences`<br>
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
Request URL: `https://x.com/i/api/graphql/TwxNJyaJwqJdcghuPn9vDw/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserSessionsList<br>
Request URL: `https://x.com/i/api/graphql/vJ-XatpmQSG8bDch8-t9Jw/UserSessionsList`<br>
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
Request URL: `https://x.com/i/api/graphql/LqXgpI2Pl9Hi7jOZLRpGYA/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://x.com/i/api/graphql/MpOINUGH_YVb2BKjYZOPaQ/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://x.com/i/api/graphql/gSfrT_yWq1AL1b93hyMyxg/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://x.com/i/api/graphql/JnwU1UO8J1tWlOJktPZIzg/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersVerifiedAvatars<br>
Request URL: `https://x.com/i/api/graphql/aLfvAoX6xy2ojqzOnkbrIA/UsersVerifiedAvatars`<br>
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
Request URL: `https://x.com/i/api/graphql/LbrhFqsERmthxdKfFoJvPQ/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://x.com/i/api/graphql/yn7oahXbF7f8p2oDnk9eTA/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceAddSharing<br>
Request URL: `https://x.com/i/api/graphql/ieljRpakd25peL4460LmGw/AudioSpaceAddSharing`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://x.com/i/api/graphql/gZz6RNjFbKcjgtK5BxBFdQ/AudioSpaceById`<br>
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceDeleteSharing<br>
Request URL: `https://x.com/i/api/graphql/YMbfLMTUUEzEEMibvvR26Q/AudioSpaceDeleteSharing`<br>
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
Request URL: `https://x.com/i/api/graphql/NTq79TuSz6fHj8lQaferJw/AudioSpaceSearch`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BrowseSpaceTopics<br>
Request URL: `https://x.com/i/api/graphql/TYpVV9QioZfViHqEqRZxJA/BrowseSpaceTopics`<br>
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
Request URL: `https://x.com/i/api/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
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
Request URL: `https://x.com/i/api/graphql/Zevhh76Msw574ZSs2NQHGQ/UnsubscribeFromScheduledSpace`<br>
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
Request URL: `https://x.com/i/api/graphql/88Bu08U2ddaVVjKmmXjVYg/articleNudgeDomains`<br>
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
Request URL: `https://x.com/i/api/graphql/83Gg0lfI-47Z3-ZOxyUjiQ/ClearGrokConversations`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateGrokConversation<br>
Request URL: `https://x.com/i/api/graphql/vvC5uy7pWWHXS2aDi1FZeA/CreateGrokConversation`<br>
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
Request URL: `https://x.com/i/api/graphql/QEMLEzEMzoPNbeauKCCLbg/SetDefault`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteGrokMessage<br>
Request URL: `https://x.com/i/api/graphql/kaH0vdJmbuocpRAeWpRC7A/DeleteGrokMessage`<br>
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
Request URL: `https://x.com/i/api/graphql/VaaLGwK5KNLoc7wsOmp4uw/DeletePaymentMethod`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokConversationItemsByRestId<br>
Request URL: `https://x.com/i/api/graphql/uUVIyvyS0p5t0A9YeCJeHg/GrokConversationItemsByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GrokHistory<br>
Request URL: `https://x.com/i/api/graphql/-eT71yhF_ZA4h_a1_U_gSw/GrokHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokHome<br>
Request URL: `https://x.com/i/api/graphql/6XWajjn0XQS14L2mfpqouw/GrokHome`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokMediaHistory<br>
Request URL: `https://x.com/i/api/graphql/azn3Sg0APPjb2Jtd7gqxsw/GrokMediaHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SearchGrokConversations<br>
Request URL: `https://x.com/i/api/graphql/Sr2QEitvnemma5D2NJlA2Q/SearchGrokConversations`<br>
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
Request URL: `https://x.com/i/api/graphql/xHgo03MMmyxESELMXP_7Kg/GrokShare`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## PaymentMethods<br>
Request URL: `https://x.com/i/api/graphql/mPF_G9okpbZuLcD6mN8K9g/PaymentMethods`<br>
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
Request URL: `https://x.com/i/api/graphql/a8KxGfFQAmm3WxqemuqSRA/AdAccounts`<br>
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
Request URL: `https://x.com/i/api/graphql/1LYVUabJBYkPlUAWRabB3g/AudienceEstimate`<br>
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
Request URL: `https://x.com/i/api/graphql/hiAXpFX4zFb6vOvGctGYyQ/BoostAudienceEstimate`<br>
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
Request URL: `https://x.com/i/api/graphql/mbK3oSQotwcJXyQIBE3uYw/Budgets`<br>
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
Request URL: `https://x.com/i/api/graphql/R1h43jnAl2bsDoUkgZb7NQ/Coupons`<br>
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
Request URL: `https://x.com/i/api/graphql/oDSoVgHhJxnd5IkckgPZdg/CreateQuickPromotion`<br>
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
Request URL: `https://x.com/i/api/graphql/LtpCXh66W-uXh7u7XSRA8Q/QuickPromoteEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/SOyGmNGaEXcvk15s5bqDrA/EnrollCoupon`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SetGrokPreferences<br>
Request URL: `https://x.com/i/api/graphql/NqLS09LPofalCjVhFolKtA/SetGrokPreferences`<br>
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
Request URL: `https://x.com/i/api/graphql/GA2_1uKP9b_GyR4MVAQXAw/PinReply`<br>
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
Request URL: `https://x.com/i/api/graphql/iRe6ig5OV1EzOtldNIuGDQ/UnpinReply`<br>
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
Request URL: `https://x.com/i/api/graphql/_384ihv8PithUm1UbGfAyA/DeviceIsVerified`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GeneratePinCode<br>
Request URL: `https://x.com/i/api/graphql/-Ja49b1NyF9nkZtiMQ4iiw/GeneratePinCode`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://x.com/i/api/graphql/NB-wREiWbDStJ_uel6Nu1g/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveProfile<br>
Request URL: `https://x.com/i/api/graphql/h5GTi7ojBvnmZiwy1X_PSQ/ImmersiveProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVTrend<br>
Request URL: `https://x.com/i/api/graphql/MHdEQm6a5ldxpb3yY-h_eA/TVTrend`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVUserProfile<br>
Request URL: `https://x.com/i/api/graphql/6VNPwtV8Olg4SqQHEfs7qw/TVUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetRelatedVideos<br>
Request URL: `https://x.com/i/api/graphql/g8Fvucfm4WMqEhQAAkTjhg/TweetRelatedVideos`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## EnableLoggedOutWebNotifications<br>
Request URL: `https://x.com/i/api/graphql/BqIHKmwZKtiUBPi07jKctg/EnableLoggedOutWebNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BrowseSpaceTopics<br>
Request URL: `https://x.com/i/api/graphql/TYpVV9QioZfViHqEqRZxJA/BrowseSpaceTopics`<br>
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
Request URL: `https://x.com/i/api/graphql/Sxn4YOlaAwEKjnjWV0h7Mw/SubscribeToScheduledSpace`<br>
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
Request URL: `https://x.com/i/api/graphql/Zevhh76Msw574ZSs2NQHGQ/UnsubscribeFromScheduledSpace`<br>
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
Request URL: `https://x.com/i/api/graphql/IWwmfpCe0CHPFrgj7Kj0Jw/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_video_timestamps_enabled                                     | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_grok_image_annotation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/5zpY1dCR-8NyxQJS_CFJoQ/DmGroupSearchSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/WQOx4Q1rn8LKdGN7fYbsqw/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/83Gg0lfI-47Z3-ZOxyUjiQ/ClearGrokConversations`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteGrokMessage<br>
Request URL: `https://x.com/i/api/graphql/kaH0vdJmbuocpRAeWpRC7A/DeleteGrokMessage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokConversationItemsByRestId<br>
Request URL: `https://x.com/i/api/graphql/uUVIyvyS0p5t0A9YeCJeHg/GrokConversationItemsByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GrokHistory<br>
Request URL: `https://x.com/i/api/graphql/-eT71yhF_ZA4h_a1_U_gSw/GrokHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokHome<br>
Request URL: `https://x.com/i/api/graphql/6XWajjn0XQS14L2mfpqouw/GrokHome`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokMediaHistory<br>
Request URL: `https://x.com/i/api/graphql/azn3Sg0APPjb2Jtd7gqxsw/GrokMediaHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SearchGrokConversations<br>
Request URL: `https://x.com/i/api/graphql/Sr2QEitvnemma5D2NJlA2Q/SearchGrokConversations`<br>
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
Request URL: `https://x.com/i/api/graphql/xHgo03MMmyxESELMXP_7Kg/GrokShare`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SetGrokPreferences<br>
Request URL: `https://x.com/i/api/graphql/NqLS09LPofalCjVhFolKtA/SetGrokPreferences`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://x.com/i/api/graphql/M-Y-nxSZ-udZH2Pfq0yqIA/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/O70V_cf3ZCQXRq2Acu3H3w/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchAdmitUser<br>
Request URL: `https://x.com/i/api/graphql/s_L4H2iPhZoMtWiqHxd9LA/BirdwatchAdmitUser`<br>
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
Request URL: `https://x.com/i/api/graphql/3ss48WFwGokBH_gj8t_8aQ/BirdwatchAliasSelect`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchFetchAuthenticatedBirdwatchMatchSlice<br>
Request URL: `https://x.com/i/api/graphql/XUBxGOfD72SfnibfY0-d-g/BirdwatchFetchAuthenticatedBirdwatchMatchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://x.com/i/api/graphql/lRm-_0j7gY2GhJLy95qzig/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                            | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                       | boolean | False      |
| responsive_web_birdwatch_url_notes_enabled                              | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateAppeal<br>
Request URL: `https://x.com/i/api/graphql/TKdL0YFsX4DMOpMKeneLvA/BirdwatchCreateAppeal`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchCreateBatSignal<br>
Request URL: `https://x.com/i/api/graphql/hflLsUawCquMOPVnpZuNPg/BirdwatchCreateBatSignal`<br>
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
Request URL: `https://x.com/i/api/graphql/aqfuQgpoLBGiikQy_xBwyQ/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                        | boolean | False      |
| responsive_web_birdwatch_translation_enabled                      | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateRating<br>
Request URL: `https://x.com/i/api/graphql/bD3AEK9BMCSpRods_ng2fA/BirdwatchCreateRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchDeleteBatSignal<br>
Request URL: `https://x.com/i/api/graphql/yQF40wfWdHfXeKL4ZVklcw/BirdwatchDeleteBatSignal`<br>
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
Request URL: `https://x.com/i/api/graphql/IKS_qrShkDyor6Ri1ahd9g/BirdwatchDeleteNote`<br>
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
Request URL: `https://x.com/i/api/graphql/OpvCOyOoQClUND66zDzrnA/BirdwatchDeleteRating`<br>
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
Request URL: `https://x.com/i/api/graphql/FLgLReVIssXjB_ui3wcrRQ/BirdwatchEditNotificationSettings`<br>
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
Request URL: `https://x.com/i/api/graphql/k1Unfqb74V4sf2d7-kFkhg/BirdwatchEditUserSettings`<br>
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
Request URL: `https://x.com/i/api/graphql/szoXMke8AZOErso908iglw/BirdwatchFetchAliasSelfSelectOptions`<br>
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
Request URL: `https://x.com/i/api/graphql/LUEdtkcpBlGktUtms4BvwA/BirdwatchFetchAliasSelfSelectStatus`<br>
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
Request URL: `https://x.com/i/api/graphql/hkYn13HnxM_eVCEGGl-Fdw/BirdwatchFetchAuthenticatedUserProfile`<br>
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
## BirdwatchFetchBatSignal<br>
Request URL: `https://x.com/i/api/graphql/Gwdf60Q7tL2KCvoPmqTPag/BirdwatchFetchBatSignal`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_note_request_sources_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://x.com/i/api/graphql/iL_0nGf1nelAd9Kz-pZJlA/BirdwatchFetchBirdwatchProfile`<br>
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
Request URL: `https://x.com/i/api/graphql/0EW8KDGMK0g3EfCF0iAhsg/BirdwatchFetchCanTweetBeMediaNote`<br>
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
Request URL: `https://x.com/i/api/graphql/P80WKmzgbAsRMLEkU5Rq0w/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNoteTranslation<br>
Request URL: `https://x.com/i/api/graphql/PilMxjmtNKJ92F1MsiQeGg/BirdwatchFetchNoteTranslation`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_translation_enabled                      | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://x.com/i/api/graphql/6Wt9Ejoc0-eFRBW6ct37UQ/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                        | boolean | False      |
| responsive_web_birdwatch_translation_enabled                      | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://x.com/i/api/graphql/Kt-GryZ4scejMhOAUGDAXw/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                        | boolean | False      |
| responsive_web_birdwatch_translation_enabled                      | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://x.com/i/api/graphql/9bDdJ6AL26RLkcUShEcF-A/BirdwatchFetchPublicData`<br>
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
Request URL: `https://x.com/i/api/graphql/yASGrjmFWghK2T0XC3uGVg/BirdwatchFetchSignUpEligiblity`<br>
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
## BirdwatchFetchSourceLinkSlice<br>
Request URL: `https://x.com/i/api/graphql/8lqLv8g6OoE3gN9_qtIB0w/BirdwatchFetchSourceLinkSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchSourceLinkTweet<br>
Request URL: `https://x.com/i/api/graphql/izQ6fkwrtwKkpNB4M-J0SA/BirdwatchFetchSourceLinkTweet`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_note_request_sources_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchProfileAcknowledgeEarnOut<br>
Request URL: `https://x.com/i/api/graphql/cED9wJy8Nd1kZCCYuIq9zQ/BirdwatchProfileAcknowledgeEarnOut`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BirdwatchRemoveUser<br>
Request URL: `https://x.com/i/api/graphql/6ZEO6UxqjlK4nefrhotZHw/BirdwatchRemoveUser`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityBoostCreateRating<br>
Request URL: `https://x.com/i/api/graphql/k1gINntkffB5NvtVgJBFKw/CommunityBoostCreateRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityBoostDeleteRating<br>
Request URL: `https://x.com/i/api/graphql/Az1pj83H-fBSENAeV-lNMA/CommunityBoostDeleteRating`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunityBoostFetchPivot<br>
Request URL: `https://x.com/i/api/graphql/ob-WH21vXAVZP7S4JwqN1Q/CommunityBoostFetchPivot`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## LiveCommerceItemsSlice<br>
Request URL: `https://x.com/i/api/graphql/-lnNX56S2YrZYrLzbccFAQ/LiveCommerceItemsSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/oUXOj2nghX-6MIRLH8TNRQ/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityDelete<br>
Request URL: `https://x.com/i/api/graphql/e4lWqB6m2TA8Fn_j9L9xEA/ArticleEntityDelete`<br>
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
Request URL: `https://x.com/i/api/graphql/Rp4zu5S6zaikV197RP_QRw/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/CIj4KXh1c5WoGx7_4LvMLQ/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/EdwAxdNYKoQ82eEbGnlZRQ/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/MYtEhsQavOxAD39II014bw/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/o020yZd6kNrGfKJSszCOXQ/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/IEuPBbFp7lNdQzU1chlFfg/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/kyaWn9oU-MP87IX90-4yoA/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/IWwmfpCe0CHPFrgj7Kj0Jw/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_video_timestamps_enabled                                     | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_grok_image_annotation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/5zpY1dCR-8NyxQJS_CFJoQ/DmGroupSearchSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/WQOx4Q1rn8LKdGN7fYbsqw/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/xYSm8m5kJnzm_gFCn5GH-w/DmPeopleSearchSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/2qKKYFQift8p5-J1k6kqxQ/WriteEmailNotificationSettings`<br>
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
Request URL: `https://x.com/i/api/graphql/JpjlNgn4sLGvS6tgpTzYBg/ViewerEmailSettings`<br>
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
Request URL: `https://x.com/i/api/graphql/83Gg0lfI-47Z3-ZOxyUjiQ/ClearGrokConversations`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteGrokMessage<br>
Request URL: `https://x.com/i/api/graphql/kaH0vdJmbuocpRAeWpRC7A/DeleteGrokMessage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokConversationItemsByRestId<br>
Request URL: `https://x.com/i/api/graphql/uUVIyvyS0p5t0A9YeCJeHg/GrokConversationItemsByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GrokHistory<br>
Request URL: `https://x.com/i/api/graphql/-eT71yhF_ZA4h_a1_U_gSw/GrokHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokHome<br>
Request URL: `https://x.com/i/api/graphql/6XWajjn0XQS14L2mfpqouw/GrokHome`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokMediaHistory<br>
Request URL: `https://x.com/i/api/graphql/azn3Sg0APPjb2Jtd7gqxsw/GrokMediaHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SearchGrokConversations<br>
Request URL: `https://x.com/i/api/graphql/Sr2QEitvnemma5D2NJlA2Q/SearchGrokConversations`<br>
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
Request URL: `https://x.com/i/api/graphql/xHgo03MMmyxESELMXP_7Kg/GrokShare`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SetGrokPreferences<br>
Request URL: `https://x.com/i/api/graphql/NqLS09LPofalCjVhFolKtA/SetGrokPreferences`<br>
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
Request URL: `https://x.com/i/api/graphql/_ckHEj05gan2VfNHG6thBA/DisableUserAccountLabel`<br>
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
Request URL: `https://x.com/i/api/graphql/rD5gLxVmMvtdtYU1UHWlFQ/UserAccountLabel`<br>
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
Request URL: `https://x.com/i/api/graphql/83Gg0lfI-47Z3-ZOxyUjiQ/ClearGrokConversations`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateGrokConversation<br>
Request URL: `https://x.com/i/api/graphql/vvC5uy7pWWHXS2aDi1FZeA/CreateGrokConversation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteGrokMessage<br>
Request URL: `https://x.com/i/api/graphql/kaH0vdJmbuocpRAeWpRC7A/DeleteGrokMessage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokConversationItemsByRestId<br>
Request URL: `https://x.com/i/api/graphql/uUVIyvyS0p5t0A9YeCJeHg/GrokConversationItemsByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GrokHistory<br>
Request URL: `https://x.com/i/api/graphql/-eT71yhF_ZA4h_a1_U_gSw/GrokHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokHome<br>
Request URL: `https://x.com/i/api/graphql/6XWajjn0XQS14L2mfpqouw/GrokHome`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokMediaHistory<br>
Request URL: `https://x.com/i/api/graphql/azn3Sg0APPjb2Jtd7gqxsw/GrokMediaHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SearchGrokConversations<br>
Request URL: `https://x.com/i/api/graphql/Sr2QEitvnemma5D2NJlA2Q/SearchGrokConversations`<br>
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
Request URL: `https://x.com/i/api/graphql/xHgo03MMmyxESELMXP_7Kg/GrokShare`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SetGrokPreferences<br>
Request URL: `https://x.com/i/api/graphql/NqLS09LPofalCjVhFolKtA/SetGrokPreferences`<br>
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
Request URL: `https://x.com/i/api/graphql/NrJKto7TWOe5AAljs7OvIw/SidebarUserRecommendations`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://x.com/i/api/graphql/5sL7391G3Y8LvIJnKOs8pQ/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/Hxt5qSNpMuD5ZD1d2uAdPg/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/OYYCrxu4OaI0tGzmikyiIQ/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ClearGrokConversations<br>
Request URL: `https://x.com/i/api/graphql/83Gg0lfI-47Z3-ZOxyUjiQ/ClearGrokConversations`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CreateGrokConversation<br>
Request URL: `https://x.com/i/api/graphql/vvC5uy7pWWHXS2aDi1FZeA/CreateGrokConversation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DeleteGrokMessage<br>
Request URL: `https://x.com/i/api/graphql/kaH0vdJmbuocpRAeWpRC7A/DeleteGrokMessage`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokConversationItemsByRestId<br>
Request URL: `https://x.com/i/api/graphql/uUVIyvyS0p5t0A9YeCJeHg/GrokConversationItemsByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GrokHistory<br>
Request URL: `https://x.com/i/api/graphql/-eT71yhF_ZA4h_a1_U_gSw/GrokHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokHome<br>
Request URL: `https://x.com/i/api/graphql/6XWajjn0XQS14L2mfpqouw/GrokHome`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokMediaHistory<br>
Request URL: `https://x.com/i/api/graphql/azn3Sg0APPjb2Jtd7gqxsw/GrokMediaHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SearchGrokConversations<br>
Request URL: `https://x.com/i/api/graphql/Sr2QEitvnemma5D2NJlA2Q/SearchGrokConversations`<br>
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
Request URL: `https://x.com/i/api/graphql/xHgo03MMmyxESELMXP_7Kg/GrokShare`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | False      |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_timestamps_enabled                                           | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SetGrokPreferences<br>
Request URL: `https://x.com/i/api/graphql/NqLS09LPofalCjVhFolKtA/SetGrokPreferences`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ArticleEntitiesSlice<br>
Request URL: `https://x.com/i/api/graphql/oUXOj2nghX-6MIRLH8TNRQ/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityDelete<br>
Request URL: `https://x.com/i/api/graphql/e4lWqB6m2TA8Fn_j9L9xEA/ArticleEntityDelete`<br>
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
Request URL: `https://x.com/i/api/graphql/Rp4zu5S6zaikV197RP_QRw/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/CIj4KXh1c5WoGx7_4LvMLQ/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/EdwAxdNYKoQ82eEbGnlZRQ/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/MYtEhsQavOxAD39II014bw/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/o020yZd6kNrGfKJSszCOXQ/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/IEuPBbFp7lNdQzU1chlFfg/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/kyaWn9oU-MP87IX90-4yoA/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
