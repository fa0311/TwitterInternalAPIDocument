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
## AddContentDisclosure<br>
Request URL: `https://x.com/i/api/graphql/D1nwFlsu_qHsX92YzoRaaA/AddContentDisclosure`<br>
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
Request URL: `https://x.com/i/api/graphql/ZdfhJqHpvIY1oiGdJgPbSQ/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://x.com/i/api/graphql/nttqnDpIp4zbXZZXpHrqkw/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://x.com/i/api/graphql/UQQCxKRFFIKXxHUr6vNdyA/BlueVerifiedFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/dYq-J2NvXZ2wz8qCpUymng/BookmarkSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://x.com/i/api/graphql/EQcT8B8mAvheY3MJX3rzGw/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesExploreTimeline<br>
Request URL: `https://x.com/i/api/graphql/NqDPWJEPKleS3rs0YodfhA/CommunitiesExploreTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://x.com/i/api/graphql/vZuf-hSFqml1u6iRQUAsQA/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/S_IQQzGncG2xPw8a1iOJoQ/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://x.com/i/api/graphql/keBi-IFOHQFR59XV8-JCbw/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://x.com/i/api/graphql/xH7hB5XQAdkmC1O3glS9ZA/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://x.com/i/api/graphql/qeE2Vlxa0R-mJTiKSMV23g/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://x.com/i/api/graphql/uL--Q0pdGxf9qKuHQpKXdw/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://x.com/i/api/graphql/-oxunWxVyyfBA7MkGMQqMQ/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://x.com/i/api/graphql/XKOY88dk-54yilctUR9EDg/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/GQ8By90KSKh4iUSgrsj0hw/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://x.com/i/api/graphql/QzEcwyG5-ePH_IFvN92Xgg/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://x.com/i/api/graphql/9TYpgbkD-c2rKmpeF_PZCw/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditQuestion<br>
Request URL: `https://x.com/i/api/graphql/Ps0w6za_U2yyixe8a3hCHA/CommunityEditQuestion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://x.com/i/api/graphql/ASqVyMPbvWMO2Jl2udvXcw/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://x.com/i/api/graphql/vLS7mhOqMLtGZdXqFP1DEg/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://x.com/i/api/graphql/h1Z6BjftMv-oSafn_QrBTA/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/TQ-ErN9XPSjNkSY4ZB7W6Q/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://x.com/i/api/graphql/q9LMMKLXMQ5t9AdHYjm7Ew/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityMediaLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/f4DQYBzXMHOLOKQ2MT2WAw/CommunityMediaLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://x.com/i/api/graphql/SzqSZ7ZLUyY__zXy-lPzwA/CommunityMediaTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://x.com/i/api/graphql/wLq8nJhuzS5Tzq2p-dgIlw/CommunityMemberRelationshipTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/QWQ2Z2nw2H3KiD3qqMb6UQ/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://x.com/i/api/graphql/mXjB-Qnr_QUNeUD_MqGd2Q/CommunityModerationTweetCasesSlice`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/7W5Im-Z2q-v81NbUkiAvKQ/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://x.com/i/api/graphql/0SkYzk2GE0vpHbvpZt1Ruw/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://x.com/i/api/graphql/SrCOaQHd6cmGFa0W3Q2rBg/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/u9NzT5-wCdzObx7_tGd5bg/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetModerationLogSlice<br>
Request URL: `https://x.com/i/api/graphql/88vKYcWrA71gSirGIdHSYQ/CommunityTweetModerationLogSlice`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/09HUq3x5PxXPSlkt01sNXA/CommunityTweetsLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/a8I4wK5RqV9AQp-nBj1G_A/CommunityTweetsRankedLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/d_wFLEGTl7W-aJYEDKFt0g/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://x.com/i/api/graphql/7SZnPJ1qwHqUsFVjbLEVig/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://x.com/i/api/graphql/bz8uZZOzk3SUQUKTPioZpQ/CommunityUserInvite`<br>
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
Request URL: `https://x.com/i/api/graphql/_qsnOaYZy00m-KSiTIFyEA/CommunityUserRelationshipTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/gbLALv1_-h_J5B-flp1k5g/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ConversationControlChange<br>
Request URL: `https://x.com/i/api/graphql/57WYJNnWH0vM3Ip_gm8B2g/ConversationControlChange`<br>
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
Request URL: `https://x.com/i/api/graphql/af8H4woJ-v1hWD4HwrDJbw/CreateNoteTweet`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| rweb_cashtags_enabled                                                   | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateRetweet<br>
Request URL: `https://x.com/i/api/graphql/mbRO74GrOvSfRcJnlMapnQ/CreateRetweet`<br>
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
Request URL: `https://x.com/i/api/graphql/c50A_puUoQGK_4SXseYz3A/CreateTweet`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| rweb_cashtags_enabled                                                   | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://x.com/i/api/graphql/YaJCcZGDrL-VsRY3b9sLFQ/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
## DeleteContentDisclosure<br>
Request URL: `https://x.com/i/api/graphql/YeIV-eqGwEZXDtYaDsJz2Q/DeleteContentDisclosure`<br>
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
Request URL: `https://x.com/i/api/graphql/ZyZigVsNiFO6v1dEks1eWg/DeleteRetweet`<br>
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
Request URL: `https://x.com/i/api/graphql/nxpZCY2K-I6QoFHAHeojFQ/DeleteTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/u9Xi4cGRUSdHjaKbSUrlBQ/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| rweb_cashtags_enabled                                                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ExploreSidebar<br>
Request URL: `https://x.com/i/api/graphql/sVqjh1GOtv__xqFDTgPkuA/ExploreSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
## FinanceSearchTags<br>
Request URL: `https://x.com/i/api/graphql/4BInQe9OX1qSSZYKT5LB2w/FinanceSearchTags`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Followers<br>
Request URL: `https://x.com/i/api/graphql/xOdl9jiaOqwHUm68qsq6Hg/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://x.com/i/api/graphql/OBA-ChVl1ZPvozFotXP0ag/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://x.com/i/api/graphql/lQxnNSmlJkQHod0yzbVYDg/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://x.com/i/api/graphql/v4_83wpxQZsqzcUNp2Hkcw/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GetUsernameAvailabilityAndSuggestions<br>
Request URL: `https://x.com/i/api/graphql/1bMz-9lPrmIXrhFmXntTHw/GetUsernameAvailabilityAndSuggestions`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GlobalCommunitiesLatestPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/dnW00zHgkuy5PqHM-0mOyw/GlobalCommunitiesLatestPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GlobalCommunitiesPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/JGLHkEflxQ7z1avM03znNQ/GlobalCommunitiesPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/eObmT5Nuapp04u8bYWf49Q/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/3tb-_5Lf7kdCZ1cFHmsEfg/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://x.com/i/api/graphql/y4xOvZQugvMN-SyqAXyEDA/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://x.com/i/api/graphql/vWPi0CTMoPFsjsL6W4IynQ/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://x.com/i/api/graphql/fgmmT4S2CMll4V15vcF9cQ/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://x.com/i/api/graphql/lzW0S5xhifd3MPGr0DAa0A/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://x.com/i/api/graphql/LDQpQ89B5ipR8izCKrWU0g/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://x.com/i/api/graphql/UQRa0jJ9doxGEIQRea1Y0w/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://x.com/i/api/graphql/TUfM9fS3y_bd-sUriFuB-g/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
## ListEditRecommendedUsers<br>
Request URL: `https://x.com/i/api/graphql/nGKrvDatPebeWmcZFGkIGg/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/gJSs2LdqumQ2a5G1J4VWFw/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://x.com/i/api/graphql/8ESZDii3ltN_xtM0FEdY7A/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://x.com/i/api/graphql/vJ8WBbKkoVPceWmWW12tzg/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/7yp5RkSJxnKX2LB6kh1M4A/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://x.com/i/api/graphql/t9AbdyHaJVfjL9jsODwgpQ/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/jAQN1OtMcb1VPNasKvsR8Q/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://x.com/i/api/graphql/cAGvZIu7SW0YlLYynz3VYA/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/q5L0qaDZbpk4W0b5eLFrtQ/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://x.com/i/api/graphql/Gpws7iVbAR7ebO3qCCYmPw/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://x.com/i/api/graphql/kFmm_DTnjs1zmzWdzY_NEQ/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/-diULb6PX5grQ_MvItGiJQ/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://x.com/i/api/graphql/zotgs3U-FVUY87mygvnsNQ/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://x.com/i/api/graphql/ZQH2KY6u5xcWn2CzC08gmQ/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/wy0Te8bKLoSkhq9We9pzYw/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MediaTabVideoMixer<br>
Request URL: `https://x.com/i/api/graphql/h2eb2JpZoStea82R195_kA/MediaTabVideoMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/u_2uGyTP8gnvVahzzVVz-g/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://x.com/i/api/graphql/jHbEW5Exxjak9yxgAMlM6A/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## PaymentsUsersTypeahead<br>
Request URL: `https://x.com/i/api/graphql/pnP0TpmPEJiiJuN9T-LU4Q/PaymentsUsersTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/Sf_ZnsZgswesjF-tu6Lxrg/PinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/SnNm4YWv4Xu26VSx-MIYlw/PinnedTimelines`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ProfileFilter<br>
Request URL: `https://x.com/i/api/graphql/qVSXJdUdr2IaFgUGcIxH3w/ProfileFilter`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesRankedTimeline<br>
Request URL: `https://x.com/i/api/graphql/a3PvPwO-y_MIu_2zs-Gk6g/CommunitiesRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
## SearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/XN_HccZ9SU-miQVvwTAlFQ/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SharingAudiospacesListeningDataWithFollowersUpdate<br>
Request URL: `https://x.com/i/api/graphql/5h0kNbk3ii97rmfY6CdgAA/SharingAudiospacesListeningDataWithFollowersUpdate`<br>
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
Request URL: `https://x.com/i/api/graphql/kAQqqmI_kuz6rxpmIEbt1g/SimilarPosts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://x.com/i/api/graphql/umXvDQ0ESrDAbfGiLQceNg/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SupportedLanguages<br>
Request URL: `https://x.com/i/api/graphql/fZ5uZVeledO5SAseKnmTUg/SupportedLanguages`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
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
## TrendHistory<br>
Request URL: `https://x.com/i/api/graphql/mRZDkyjyh6UTaoBBHHXAEg/TrendHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrendRelevantUsers<br>
Request URL: `https://x.com/i/api/graphql/3_21w3q3KYOiAhPSBdxdUA/TrendRelevantUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVHomeMixer<br>
Request URL: `https://x.com/i/api/graphql/eEV6bJ5fMPJndCSnxPUGog/TVHomeMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://x.com/i/api/graphql/QrLp7AR-eMyamw8D1N9l6A/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/fHLDP3qFEjnTqhWBVvsREg/TweetResultByRestId`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://x.com/i/api/graphql/i_WLNEi4e2JidkqGBR3ZIw/TweetResultsByRestIds`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_cashtags_enabled                                                   | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/fgh47BrqwIj91JnA2Kpxuw/UnpinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
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
## Upsells<br>
Request URL: `https://x.com/i/api/graphql/Sg3BvwapuCMIjLJ7LGPhMA/Upsells`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                               | type    | variable   |
|:----------------------------------|:--------|:-----------|
| subscriptions_upsells_api_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://x.com/i/api/graphql/TuA3ruLpy_qDskunrSHyWw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://x.com/i/api/graphql/uLgDqQVmNHat7X2YLORpuw/UserArticlesTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://x.com/i/api/graphql/AE3Kvx9fmXCUL8aLnSmpRw/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://x.com/i/api/graphql/VQfQ9wwYdk6j_u2O4vt64Q/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| subscriptions_feature_can_gift_premium                            | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://x.com/i/api/graphql/IGgvgiOx4QZndDHuD3x9TQ/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| subscriptions_verification_info_is_identity_verified_enabled      | boolean | True       |
| subscriptions_verification_info_verified_since_enabled            | boolean | True       |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| subscriptions_feature_can_gift_premium                            | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/_wpmd21tTm9G725KYcRGrw/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/5-tvnhs7N1chLN-FogAHiQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://x.com/i/api/graphql/Gz8B7g_ZkB5tJlwH9jAv_Q/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://x.com/i/api/graphql/d_uaoPr42_nSDblfvi7NPw/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/-qyLymgMGVYiKJLArTScMw/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/fOnc9Dv31cnkNWfMdfW1Sw/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://x.com/i/api/graphql/naBcZ4al-iTCFBYGOAMzBQ/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://x.com/i/api/graphql/YhE6S_TtdhVxLtpokXrRaA/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| rweb_cashtags_enabled                                                   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| responsive_web_profile_redirect_enabled                                 | boolean | False      |
| rweb_tipjar_consumption_enabled                                         | boolean | False      |
| verified_phone_label_enabled                                            | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| responsive_web_grok_annotations_enabled                                 | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| content_disclosure_indicator_enabled                                    | boolean | True       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean | True       |
| responsive_web_grok_show_grok_translated_post                           | boolean | True       |
| responsive_web_grok_analysis_button_from_backend                        | boolean | True       |
| post_ctas_fetch_enabled                                                 | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://x.com/i/api/graphql/a74irv24XPYDjy5LSNQUXg/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersByScreenNames<br>
Request URL: `https://x.com/i/api/graphql/BDxiyyoNcdR0I_mJcryMLA/UsersByScreenNames`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| subscriptions_verification_info_is_identity_verified_enabled      | boolean | True       |
| subscriptions_verification_info_verified_since_enabled            | boolean | True       |
| highlights_tweets_tab_ui_enabled                                  | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean | True       |
| subscriptions_feature_can_gift_premium                            | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersVerifiedAvatars<br>
Request URL: `https://x.com/i/api/graphql/x3JZoNX9ubSzoCIHoYo2NA/UsersVerifiedAvatars`<br>
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
Request URL: `https://x.com/i/api/graphql/_8ClT24oZ8tpylf_OSuNdg/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| subscriptions_upsells_api_enabled                                 | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
