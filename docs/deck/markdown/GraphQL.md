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
Request URL: `https://x.com/i/api/graphql/psKkxhd7FNG9Xar33Fqmng/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://x.com/i/api/graphql/6iR_P4R1Caje4cQRujEIBQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://x.com/i/api/graphql/zhpogrf30JrKmTss81AY8w/BlueVerifiedFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/I79RO1ZqoyWMPK1EST3FBw/BookmarkSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://x.com/i/api/graphql/APOFXqgNSVui9MQoRdubZQ/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesExploreTimeline<br>
Request URL: `https://x.com/i/api/graphql/JimO40MXCvku7681fBfQ1g/CommunitiesExploreTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://x.com/i/api/graphql/lEKwUVKUTc2_BDaOCjneXQ/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/uH91mNqzpGrKya5rb43eTA/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://x.com/i/api/graphql/LMcp64PdPFaWipsupdfy5w/CommunitiesMembershipsSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/k0klAY7pgFkYTA_gJ499vw/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://x.com/i/api/graphql/LTZmXENVT3xFWy1cBEe0Sw/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://x.com/i/api/graphql/Xy_GI7kOUYHAqWOQCMebzg/CreateCommunity`<br>
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
Request URL: `https://x.com/i/api/graphql/qRII1kSGK5JgUz-MB-zhsw/CommunityCreateRule`<br>
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
Request URL: `https://x.com/i/api/graphql/xSlJp5q5k5ftI3Zs6WoO-A/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/VqZIVzmTLy17I51eaZ1f1A/CommunityEditBannerMedia`<br>
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
Request URL: `https://x.com/i/api/graphql/BXJVAE57CDp8dvi-KqtTcA/CommunityEditName`<br>
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
Request URL: `https://x.com/i/api/graphql/Uh1AwmKL5FwbOtL23IO-Jw/CommunityEditPurpose`<br>
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
Request URL: `https://x.com/i/api/graphql/MGtTuMXrZZ9AQT3M0hNIBg/CommunityEditQuestion`<br>
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
Request URL: `https://x.com/i/api/graphql/g0GwfINCcJwW2Bsv77S4zQ/CommunityEditRule`<br>
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
Request URL: `https://x.com/i/api/graphql/Mt033iulrkGz0nqtHmXZvQ/CommunityByRestId`<br>
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
Request URL: `https://x.com/i/api/graphql/ofFTJyS28K8gGnKMvTcl9A/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/EwWKbkzZVAZlW_LMnlQSag/JoinCommunity`<br>
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
Request URL: `https://x.com/i/api/graphql/bsBmGQWp05WTu4bwUyj0ng/LeaveCommunity`<br>
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
Request URL: `https://x.com/i/api/graphql/hS7BNAy25EpInnpJ-TZh8g/CommunityMediaLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://x.com/i/api/graphql/nfoPBZM1l1vuu-glczWowg/CommunityMediaTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://x.com/i/api/graphql/6YgvBKI7c3YZ9d7zKKojng/CommunityMemberRelationshipTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/v0EP1TbhxeWyRMEe6-kSyw/CommunityModerationKeepTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/cpQNC4XPHarSjQzZfNfLNA/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/VBhjwL6YDQImVg_sBqboCw/CommunityRemoveBannerMedia`<br>
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
Request URL: `https://x.com/i/api/graphql/k9U3jXAFIwg7H9k2y7FEnw/CommunityRemoveRule`<br>
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
Request URL: `https://x.com/i/api/graphql/ei5EKRInzY_EQIWlexa-Eg/CommunityReorderRules`<br>
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
Request URL: `https://x.com/i/api/graphql/4qAnyub0YiRN9PulrU1yxw/RequestToJoinCommunity`<br>
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
Request URL: `https://x.com/i/api/graphql/3JV36hqD4NyIPt1GhFiLAQ/CommunityTweetModerationLogSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/hnX528Fqk9RHot7QZmJ5Rg/CommunityTweetsLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/UoUNQaGOPH0Ft7YXznQY0g/CommunityTweetsRankedLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/cW_FuuYQWRl5R6U5UhS7yA/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://x.com/i/api/graphql/NqLN0kOgaLI8NGs2NBwaUQ/CommunityUpdateRole`<br>
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
Request URL: `https://x.com/i/api/graphql/U1yIMRKtqjuHOf8d7eHQHA/CommunityUserInvite`<br>
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
Request URL: `https://x.com/i/api/graphql/MOKE3VjNMJ7BVsWdNkv32g/CommunityUserRelationshipTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/um4EWJszOgVpZIUG8o-ZQA/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/oG8ukUzg7L1BvmrpGovnWw/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
Request URL: `https://x.com/i/api/graphql/R5EPiGHgSqbTYFyozd-gFw/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
## DownvoteTweet<br>
Request URL: `https://x.com/i/api/graphql/Iu4kUV4vd_iHMupiHPPrAQ/DownvoteTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/elraodd34g1mfp4Y5nEhTA/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ExploreSidebar<br>
Request URL: `https://x.com/i/api/graphql/phr45Pnu6paVrBLOf--r2Q/ExploreSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/4VTsYZ3r4xYW9S0Rys5G0A/FinanceSearchTags`<br>
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
Request URL: `https://x.com/i/api/graphql/4yeuNabfz3qFlfncCAy8Yw/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://x.com/i/api/graphql/nYylIhG4f_mNxc5DGpmUkg/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://x.com/i/api/graphql/eNoXdfXv5rU75RBzlmfuPA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://x.com/i/api/graphql/VrAHfTlEBd6qq1IJlOvBqQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/9qgNH2YinBqvokSkcsrIcw/GlobalCommunitiesLatestPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GlobalCommunitiesPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/nYIToKwMyeayHLThw87UZg/GlobalCommunitiesPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/g9NSjyYXOBsmMiP9TmYGaA/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/gKia-nBM9kwuDEfSDeWMfQ/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://x.com/i/api/graphql/tl9f_I0xyREhFd5KMzuO7w/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://x.com/i/api/graphql/yhAkn9q5qaSCxPg_fpykDw/ListAddMember`<br>
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
Request URL: `https://x.com/i/api/graphql/dy79WygWHQcAGvpk0jgwjw/DeleteListBanner`<br>
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
Request URL: `https://x.com/i/api/graphql/IK1owq6gs9nSKFrNBzHaiA/EditListBanner`<br>
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
Request URL: `https://x.com/i/api/graphql/Ub9soKX1klaee2qdkHBI8Q/ListBySlug`<br>
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
Request URL: `https://x.com/i/api/graphql/JCpbk4JNzi51p7hxHQNz4g/CreateList`<br>
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
Request URL: `https://x.com/i/api/graphql/3GTUeO41i_0ZLysHvJX_xA/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/18Hx4wo5iQXTDoE0WxK-ww/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/Iql5aRVyFxNZ-ORcDV_TwQ/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://x.com/i/api/graphql/kcsJubZ1BIwpdKrYfiNRtg/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://x.com/i/api/graphql/qeV9WF3eN5V9SNj8iP7Kkg/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/S88Gftub7IcTsmSFl8mOHg/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://x.com/i/api/graphql/I1h1FzuuiD__nNvG466mKQ/ListByRestId`<br>
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
Request URL: `https://x.com/i/api/graphql/mgudchpiNyNs_XU7waFTbA/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://x.com/i/api/graphql/c2IzeyWiwaQBkFs2VV_vSA/ListRemoveMember`<br>
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
Request URL: `https://x.com/i/api/graphql/k19CQeohKqUeZSGsqkhAxA/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://x.com/i/api/graphql/8MQzqxfDoKWcZrUT1Zu70g/ListSubscribe`<br>
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
Request URL: `https://x.com/i/api/graphql/Vqgu6oSW1SuY3FWlyEcdoA/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/CetGppspal_5WXBjxIT-kg/ListUnsubscribe`<br>
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
Request URL: `https://x.com/i/api/graphql/4owP8HOGk7mXBu4Zl7qusQ/UpdateList`<br>
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
Request URL: `https://x.com/i/api/graphql/7pV1Wxo9P6E5cuytZPR_dA/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/wgVgVkLURZzQ6flLmOyprA/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MediaTabVideoMixer<br>
Request URL: `https://x.com/i/api/graphql/cmF3cF8HekXWPHdaeqZhbA/MediaTabVideoMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/LSJR2q0HSFy1laAmIZABQw/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://x.com/i/api/graphql/p-DYbUPy0A6VhHrB8e-l6w/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## PaymentsUsersTypeahead<br>
Request URL: `https://x.com/i/api/graphql/dlHFEO5q9vveDgITz9zELg/PaymentsUsersTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/bsZvqFjCSKNK1A21kfZnMg/PinTimeline`<br>
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
Request URL: `https://x.com/i/api/graphql/TRRXFHdz_saNdA9vVa94cg/PinnedTimelines`<br>
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
Request URL: `https://x.com/i/api/graphql/2eFyYTyflwQxN3q8vJ61FQ/ProfileFilter`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/CcRlWqXpkushCx6PlnBI2g/CommunitiesRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/Bcw3RzK-PatNAmbnw54hFw/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/4i7pEY6eFmW39Jb920MSgw/SimilarPosts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://x.com/i/api/graphql/wI96bTzdzylRGv4fdmePhw/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/A51p7ZTatS0PivJW4BWJiA/TrendHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TrendRelevantUsers<br>
Request URL: `https://x.com/i/api/graphql/YfZvsgMWEb9qMdvTPBC2Vw/TrendRelevantUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TVHomeMixer<br>
Request URL: `https://x.com/i/api/graphql/RG1M-FZYWbJn7UMqHCcIuQ/TVHomeMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://x.com/i/api/graphql/jd3V43oDY9cY7obs1YMfbQ/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/-4_LMahNlI4MuLJ-EAFEog/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://x.com/i/api/graphql/7nfIZg-03g-BuVG0Oa1fXA/TweetResultsByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## UndoDownvoteTweet<br>
Request URL: `https://x.com/i/api/graphql/yqhcbdyy59k-FCwOysvvGQ/UndoDownvoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
Request URL: `https://x.com/i/api/graphql/vDm_ZHzUXLbhcH0nRrJ-EA/UnpinTimeline`<br>
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
## UpdatePinnedTimelines<br>
Request URL: `https://x.com/i/api/graphql/clo5jsXXnCgmQfBeZZVRXQ/UpdatePinnedTimelines`<br>
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
Request URL: `https://x.com/i/api/graphql/U4SBl6gi2eBswitY28jA9Q/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://x.com/i/api/graphql/tC8Mkunj-1cqFwXmw0DQRg/UserArticlesTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://x.com/i/api/graphql/AklTVW0G16x9uK4zzoxlRw/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://x.com/i/api/graphql/DaeC_2LfMgwCujE03HSZtw/UserByRestId`<br>
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
Request URL: `https://x.com/i/api/graphql/2qvSHpkWTMS9i0zJAwDNiA/UserByScreenName`<br>
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
Request URL: `https://x.com/i/api/graphql/e-vTXEgjmjEv4P9bveUwNg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/jAbD4h4pLuogg19mnAeZ4w/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://x.com/i/api/graphql/8JbX6lREJ3BkwMjLH3ilOA/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://x.com/i/api/graphql/DpzwOu8Idtlbfqh-Hf718Q/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/YCFiR-jDNKerMo_b5-cfSQ/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserPromotedTweets<br>
Request URL: `https://x.com/i/api/graphql/HqN48IgPrIo01dE-NXMKwQ/UserPromotedTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/PitMhunmZvJdkh2j9uSqQA/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://x.com/i/api/graphql/hr4gzZONlq23okjU8fIe_A/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://x.com/i/api/graphql/FIFgycIi-CNJcV0R-135Uw/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| rweb_conversational_replies_downvote_enabled                            | ...     |        nan | error     |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| content_disclosure_indicator_enabled                                    | boolean |          1 | nan       |
| content_disclosure_ai_generated_indicator_enabled                       | boolean |          1 | nan       |
| responsive_web_grok_show_grok_translated_post                           | boolean |          1 | nan       |
| responsive_web_grok_analysis_button_from_backend                        | boolean |          1 | nan       |
| post_ctas_fetch_enabled                                                 | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://x.com/i/api/graphql/4s-T1XYy3__OdhkRmSlJBA/UsersByRestIds`<br>
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
Request URL: `https://x.com/i/api/graphql/Gf7lyQxeCREK2zuAiEMkOQ/UsersByScreenNames`<br>
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
Request URL: `https://x.com/i/api/graphql/O9O_O1iF0QffoOBjB2OGIQ/UsersVerifiedAvatars`<br>
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
Request URL: `https://x.com/i/api/graphql/u4ni7JqpqdAQxWQfkLsdUQ/Viewer`<br>
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
