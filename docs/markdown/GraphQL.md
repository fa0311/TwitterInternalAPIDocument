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
## ListProductSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/V8-RP7SxlI4qzRmpCmEqgw/ListProductSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                              | type    | variable   |
|:-------------------------------------------------|:--------|:-----------|
| subscriptions_management_fetch_next_billing_time | boolean | True       |
| subscriptions_marketing_page_fetch_promotions    | boolean | True       |

#### queryId<br>
`None`<br>
## NotABotCheckoutUrlWithEligibility<br>
Request URL: `https://x.com/i/api/graphql/RM4x9h3tF8bCn69VV3-gRg/NotABotCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/fatCCOgstk_uPEl-zNlX8w/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/el6V21NAvHxCSbMqcuY45w/SubscriptionProductDetails`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                           | type    | variable   |
|:----------------------------------------------|:--------|:-----------|
| subscriptions_marketing_page_fetch_promotions | boolean | True       |

#### queryId<br>
`None`<br>
## SwitchTier<br>
Request URL: `https://x.com/i/api/graphql/73t92vAzJ9DI1WygCcD7WQ/SwitchTier`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## AudioSpaceAddSharing<br>
Request URL: `https://x.com/i/api/graphql/IDcuD1j-AWe79bsOVm7dVA/AudioSpaceAddSharing`<br>
Request Method: `POST`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://x.com/i/api/graphql/sSuYIbdpe1f2v9AtD-sYeQ/AudioSpaceById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| spaces_2022_h2_spaces_communities                                       | boolean |          1 | nan       |
| spaces_2022_h2_clipping                                                 | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |

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
## CommunitiesExploreTimeline<br>
Request URL: `https://x.com/i/api/graphql/Dv5noA3XlcegYD_nIRs0lA/CommunitiesExploreTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://x.com/i/api/graphql/zYuPIeJhU_DGQ0QHgJDOCQ/CommunitiesMainDiscoveryModule`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/RrIk4numJExVTXlpmD-_9A/CommunitiesMainPageTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://x.com/i/api/graphql/8-kNxc96lbqWqGPNyRkTVA/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://x.com/i/api/graphql/DTHCv4VqBeCylhibcUaY2Q/CommunitiesMembershipsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://x.com/i/api/graphql/RP7MUDwIF83cj8gTe2POnA/CommunityAboutTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://x.com/i/api/graphql/UmeMHNkWqTAZn_Azz3YhBg/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://x.com/i/api/graphql/bAviGE8lhUdwJmGtYwdhDw/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://x.com/i/api/graphql/Q09zXXRL9twh6SlnRaOUMg/CommunityDiscoveryTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/crsWMaxUlcLPnsylMcNlEw/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://x.com/i/api/graphql/amli-DxLZmf-6plKBJVhTw/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://x.com/i/api/graphql/W0xo3qTwAkn-WMm2_-lIZg/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditQuestion<br>
Request URL: `https://x.com/i/api/graphql/QJqHk5aUDYVU5L_SLloQ7Q/CommunityEditQuestion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://x.com/i/api/graphql/oalhYbYkwDSgFsoO9FFc9A/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://x.com/i/api/graphql/iMDyRADcGz4r9ZrJMpxz1A/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://x.com/i/api/graphql/ypG1eTPpZIxSvqtOTwnTHw/CommunityHashtagsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/3jItWhb1PKC9lute3hWWXA/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://x.com/i/api/graphql/0qehtlwzUschfhKTAv0lKQ/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityMediaLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/wES5DfWoy3MWW5l3-sNi1g/CommunityMediaLoggedOutTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://x.com/i/api/graphql/yxMlTG2M9KO6zSmu8gcfAg/CommunityMediaTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://x.com/i/api/graphql/guIquIb4YgcIhq-UHXT-mA/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://x.com/i/api/graphql/rHjjrgvqPLzbxDGg93y19A/CommunityModerationTweetCasesSlice`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/ldKQTORuHp6D6cU86gh3FQ/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://x.com/i/api/graphql/dAVZg1IecFWOftHoNgz9Vg/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://x.com/i/api/graphql/BmlTKv5TiVlAnWf1CblX6Q/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/QclqoN95uHtO18c5AFihUw/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetModerationLogSlice<br>
Request URL: `https://x.com/i/api/graphql/3hBGMDGwFeoXULnyyh2q2g/CommunityTweetModerationLogSlice`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/2ZI-uuHEoiww3Yu_T2t8Wg/CommunityTweetsLoggedOutTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/VhXNK9wiuIk7ptG1tOTlfg/CommunityTweetsRankedLoggedOutTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/wXey4HQTUdYUlWWXltWMpg/CommunityTweetsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://x.com/i/api/graphql/B-hDLcK_UDsjH8mL52z9hw/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

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
## CommunitiesRankedTimeline<br>
Request URL: `https://x.com/i/api/graphql/B-mLs6i8q2a_IG8JnWlUkQ/CommunitiesRankedTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## DeleteDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/h0rzaIYc9-v3zTQvx1J8OA/DeleteDraftTweets`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/L9RqKWmAWxK6vGtR3Qdsxw/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchScheduledTweets<br>
Request URL: `https://x.com/i/api/graphql/H2elmT2R9DLhWoo0DZFNkA/FetchScheduledTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BroadcastReplayEdit<br>
Request URL: `https://x.com/i/api/graphql/CZFRymYV43d3egrZbhsnPg/BroadcastReplayEdit`<br>
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
Request URL: `https://x.com/i/api/graphql/NtEAlAR40O3S7Lf8s6XUTQ/BroadcastQuery`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
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
Request URL: `https://x.com/i/api/graphql/70JIli1rci1EkuMbkjGBiw/AiTrendByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
Request URL: `https://x.com/i/api/graphql/8hpdcfFniawLzEQ7CD2WMQ/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/fCkdrI6zrnw_UtVa3WDHhw/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/86zqyWZeIoccSyBxmxcd6w/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/eUiP53I_YemhBOI2TMCI3A/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/hRtkxfQu7M6mnlP1FRcGgg/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/FMC9CKP145f5wgXYCsmtiA/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/Rlvhkuecg1z_7O5vC2G1fQ/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/wTWiDSxOe1ZsImjXyuoiYw/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://x.com/i/api/graphql/VylcAECK1LWwr_7O5Np4eg/ImmersiveMedia`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ImmersiveProfile<br>
Request URL: `https://x.com/i/api/graphql/Poq_RUCOxgJ9qxsVG4Ngyw/ImmersiveProfile`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenerateDrmToken<br>
Request URL: `https://x.com/i/api/graphql/6csp1Dw5r5zveD-1qaqXdA/GenerateDrmToken`<br>
Request Method: `GET`<br>
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
## QuickPromoteBoostContentCheck<br>
Request URL: `https://x.com/i/api/graphql/TUZ0ApqccaHdSfkwmH9aGg/QuickPromoteBoostContentCheck`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |

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
## BudgetsByCurrency<br>
Request URL: `https://x.com/i/api/graphql/WKAPUeb7AOpuxWasFAJ1Dw/BudgetsByCurrency`<br>
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
Request URL: `https://x.com/i/api/graphql/1nVomZMCriTpwOvy2jYs9g/CreateQuickPromotion`<br>
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
## TargetingCatalogSearch<br>
Request URL: `https://x.com/i/api/graphql/z7Ij1OnFDsb1Is08hkBDKw/TargetingCatalogSearch`<br>
Request Method: `GET`<br>
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
## CommunityBoostFetchPublicData<br>
Request URL: `https://x.com/i/api/graphql/mtel1c9ozKWaWr9-D2wMwg/CommunityBoostFetchPublicData`<br>
Request Method: `GET`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserUnderTheHoodReport<br>
Request URL: `https://x.com/i/api/graphql/jI8tWg6m5Yj4nCwc4jXbUQ/UserUnderTheHoodReport`<br>
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
Request URL: `https://x.com/i/api/graphql/n2SrvFA8CstWa-JLzim6OA/BookmarkFolderTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/VjWsfItbiMLeajpZ90NJeg/Bookmarks`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## UniversalSearchFeedbackMutation<br>
Request URL: `https://x.com/i/api/graphql/qaIzg304L134B5-NI43j2A/UniversalSearchFeedbackMutation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## UserSportsProfile<br>
Request URL: `https://x.com/i/api/graphql/u7J50a1cN3sp5ejJ4nTuEA/UserSportsProfile`<br>
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
Request URL: `https://x.com/i/api/graphql/qTetuWKS8n_vXeOifKNTOQ/GrokConversationItemsByRestId`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## GrokHistory<br>
Request URL: `https://x.com/i/api/graphql/9Hyh5D4-WXLnExZkONSkZg/GrokHistory`<br>
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
Request URL: `https://x.com/i/api/graphql/QAPGIKJVaPXYD-gO9kxc9w/GrokHome`<br>
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
## GrokPinConversation<br>
Request URL: `https://x.com/i/api/graphql/_6czUDKiWzcvBUKMoDZ19w/GrokPinConversation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokPinnedConversations<br>
Request URL: `https://x.com/i/api/graphql/BHKxYTkc5SCupV7oqJBr0g/GrokPinnedConversations`<br>
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
Request URL: `https://x.com/i/api/graphql/6TiCfQxK8W-2cQxEX7L0mw/GrokShare`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## GrokUnpinConversation<br>
Request URL: `https://x.com/i/api/graphql/-5e798p4EVbuhGGFFuw3Tg/GrokUnpinConversation`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GrokUserEventsLog<br>
Request URL: `https://x.com/i/api/graphql/AB0damyVo0wBhhebQIwtsg/GrokUserEventsLog`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SportsLeagueFollow<br>
Request URL: `https://x.com/i/api/graphql/ROSPydUYihwVnF1940yA3A/SportsLeagueFollow`<br>
Request Method: `GET`<br>
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
## DeleteDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/h0rzaIYc9-v3zTQvx1J8OA/DeleteDraftTweets`<br>
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
## GifEnumerateCategory<br>
Request URL: `https://x.com/i/api/graphql/LtO2mAjgSf_RwA51ACMbkA/GifEnumerateCategory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GifSearch<br>
Request URL: `https://x.com/i/api/graphql/bKYBmwqIxMGZv04iU_lLWg/GifSearch`<br>
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
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/L9RqKWmAWxK6vGtR3Qdsxw/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchScheduledTweets<br>
Request URL: `https://x.com/i/api/graphql/H2elmT2R9DLhWoo0DZFNkA/FetchScheduledTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
Request URL: `https://x.com/i/api/graphql/VCGc5tQL49llkWlWJMvCWQ/BirdwatchFetchAuthenticatedBirdwatchMatchSlice`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://x.com/i/api/graphql/I-tH41siP78FjfJEqdUPhQ/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_media_notes_enabled                            | boolean |          1 | nan       |
| responsive_web_birdwatch_fast_notes_badge_enabled                       | boolean |          0 | nan       |
| responsive_web_birdwatch_url_notes_enabled                              | boolean |          0 | nan       |
| responsive_web_birdwatch_live_note_enabled                              | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
Request URL: `https://x.com/i/api/graphql/oCnZiCgsZJe8WEOKuS-xZw/BirdwatchCreateBatSignal`<br>
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
Request URL: `https://x.com/i/api/graphql/dZ5t9-LyPZD4kGNP5PEQMQ/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                            | type    | variable   |
|:---------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                   | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                     | boolean | False      |
| responsive_web_grok_community_note_translation_is_enabled      | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled              | boolean | False      |
| responsive_web_birdwatch_live_note_enabled                     | boolean | True       |
| responsive_web_birdwatch_note_internal_insights_enabled        | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled             | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled           | boolean | True       |
| responsive_web_profile_redirect_enabled                        | boolean | True       |
| rweb_tipjar_consumption_enabled                                | boolean | False      |
| verified_phone_label_enabled                                   | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateRating<br>
Request URL: `https://x.com/i/api/graphql/gbshFt1Vmddrlio4vHWhhQ/BirdwatchCreateRating`<br>
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
Request URL: `https://x.com/i/api/graphql/kD74-qBfrdRT5rO9YOl57g/BirdwatchFetchAuthenticatedUserProfile`<br>
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
Request URL: `https://x.com/i/api/graphql/7LFdey6iP2bf5f2_aN80Ng/BirdwatchFetchBatSignal`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_note_request_sources_enabled | boolean | True       |
| responsive_web_birdwatch_live_note_enabled            | boolean | True       |

#### queryId<br>
`None`<br>
## BirdwatchFetchBirdwatchProfile<br>
Request URL: `https://x.com/i/api/graphql/id9iGfEQF47W1kvRBHUmRQ/BirdwatchFetchBirdwatchProfile`<br>
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
## BirdwatchFetchClusterData<br>
Request URL: `https://x.com/i/api/graphql/Pca1AGrw2NLa0pJ_s124gw/BirdwatchFetchClusterData`<br>
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
Request URL: `https://x.com/i/api/graphql/FAmIZKHUZkuRclhoxxRAuw/BirdwatchFetchGlobalTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchMediaMatchSlice<br>
Request URL: `https://x.com/i/api/graphql/RV-iQHgbSFQyN6t5Zx9MTw/BirdwatchFetchMediaMatchSlice`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchNoteTranslation<br>
Request URL: `https://x.com/i/api/graphql/77CUJOf_U7dZE66MriL3ug/BirdwatchFetchNoteTranslation`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_translation_enabled         | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://x.com/i/api/graphql/FXliMyVVZbAxaiRcs9USqA/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                            | type    | variable   |
|:---------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_live_note_enabled                     | boolean | True       |
| responsive_web_birdwatch_enforce_author_user_quotas            | boolean | True       |
| responsive_web_birdwatch_media_notes_enabled                   | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                     | boolean | False      |
| responsive_web_grok_community_note_translation_is_enabled      | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled              | boolean | False      |
| responsive_web_birdwatch_note_internal_insights_enabled        | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled             | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled           | boolean | True       |
| responsive_web_profile_redirect_enabled                        | boolean | True       |
| rweb_tipjar_consumption_enabled                                | boolean | False      |
| verified_phone_label_enabled                                   | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://x.com/i/api/graphql/eKB7Azg-Y5Yy0PhXFVDxiQ/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                            | type    | variable   |
|:---------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_media_notes_enabled                   | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                     | boolean | False      |
| responsive_web_grok_community_note_translation_is_enabled      | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled              | boolean | False      |
| responsive_web_birdwatch_live_note_enabled                     | boolean | True       |
| responsive_web_birdwatch_note_internal_insights_enabled        | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled             | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled           | boolean | True       |
| responsive_web_profile_redirect_enabled                        | boolean | True       |
| rweb_tipjar_consumption_enabled                                | boolean | False      |
| verified_phone_label_enabled                                   | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchProminentMediaMatchSlice<br>
Request URL: `https://x.com/i/api/graphql/a3s0C-CEB-UZNbEQd_dHHQ/BirdwatchFetchProminentMediaMatchSlice`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchPublicData<br>
Request URL: `https://x.com/i/api/graphql/T4Qdev0aBeS9tK9v4TkgQg/BirdwatchFetchPublicData`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                    | type    | variable   |
|:-------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_note_request_download_enabled | boolean | True       |

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
## BirdwatchFetchSimilarMediaMatchSlice<br>
Request URL: `https://x.com/i/api/graphql/sDuI5o8vy0DQIGdubquL7w/BirdwatchFetchSimilarMediaMatchSlice`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchSourceLinkSlice<br>
Request URL: `https://x.com/i/api/graphql/V5TkV88R2WEXfS_Omd38NA/BirdwatchFetchSourceLinkSlice`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
## BirdwatchFetchSuggestionFeedbackOverview<br>
Request URL: `https://x.com/i/api/graphql/77GLm95dYlDy_Y9UEWE8Sg/BirdwatchFetchSuggestionFeedbackOverview`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_media_notes_enabled                            | boolean |          1 | nan       |
| responsive_web_birdwatch_fast_notes_badge_enabled                       | boolean |          0 | nan       |
| responsive_web_birdwatch_url_notes_enabled                              | boolean |          0 | nan       |
| responsive_web_birdwatch_live_note_enabled                              | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |

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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/n2SrvFA8CstWa-JLzim6OA/BookmarkFolderTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/VjWsfItbiMLeajpZ90NJeg/Bookmarks`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/NtEAlAR40O3S7Lf8s6XUTQ/BroadcastQuery`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
## DeleteDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/h0rzaIYc9-v3zTQvx1J8OA/DeleteDraftTweets`<br>
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
## FetchDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/L9RqKWmAWxK6vGtR3Qdsxw/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
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
## QuickPromoteBoostContentCheck<br>
Request URL: `https://x.com/i/api/graphql/TUZ0ApqccaHdSfkwmH9aGg/QuickPromoteBoostContentCheck`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |

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
## BudgetsByCurrency<br>
Request URL: `https://x.com/i/api/graphql/WKAPUeb7AOpuxWasFAJ1Dw/BudgetsByCurrency`<br>
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
Request URL: `https://x.com/i/api/graphql/1nVomZMCriTpwOvy2jYs9g/CreateQuickPromotion`<br>
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
Request URL: `https://x.com/i/api/graphql/H2elmT2R9DLhWoo0DZFNkA/FetchScheduledTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## TargetingCatalogSearch<br>
Request URL: `https://x.com/i/api/graphql/z7Ij1OnFDsb1Is08hkBDKw/TargetingCatalogSearch`<br>
Request Method: `GET`<br>
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
## CurrentNflWeek<br>
Request URL: `https://x.com/i/api/graphql/39djCiLUxjpUpGgLWjaDOA/CurrentNflWeek`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NCAAFBGameHydrate<br>
Request URL: `https://x.com/i/api/graphql/N8vvLFO39cCqqPO75z6EuA/NCAAFBGameHydrate`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NCAAFBGameOdds<br>
Request URL: `https://x.com/i/api/graphql/49i53I9H-Q81ov3qL5mugA/NCAAFBGameOdds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NCAAFBLiveGame<br>
Request URL: `https://x.com/i/api/graphql/xj-PBD8Y9Vay8cc63b1n6w/NCAAFBLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NCAAFBSchedule<br>
Request URL: `https://x.com/i/api/graphql/bEwBKKlcX53j_Ku-VLF7rg/NCAAFBSchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NCAAFBSeasonStats<br>
Request URL: `https://x.com/i/api/graphql/BuJzI4ehbQSFAC1UJ0tqcQ/NCAAFBSeasonStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NCAAFBStandings<br>
Request URL: `https://x.com/i/api/graphql/uaLhNWnygGXoyIYcpxUhQg/NCAAFBStandings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FollowTeamRoster<br>
Request URL: `https://x.com/i/api/graphql/Dd76ifUtARWFkfQo3krDxA/FollowTeamRoster`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FollowedTeams<br>
Request URL: `https://x.com/i/api/graphql/Tx6_C2uyXyaW3TRIPy-6bw/FollowedTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGameHydrate<br>
Request URL: `https://x.com/i/api/graphql/CN2G3v-dUfNQe3NNv-Lxqw/NFLGameHydrate`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGameOdds<br>
Request URL: `https://x.com/i/api/graphql/BCsiVB5FamwjLHyEFBIOMA/NFLGameOdds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGamePlayerProps<br>
Request URL: `https://x.com/i/api/graphql/Bjp0zCvdw41fzm_Mgo8AWw/NFLGamePlayerProps`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGameRoster<br>
Request URL: `https://x.com/i/api/graphql/CiBu_xfyiOu_rBNyuBngcQ/NFLGameRoster`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## NFLLiveGame<br>
Request URL: `https://x.com/i/api/graphql/1ssBFzuY0MFqgTl9h6a3hw/NFLLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLMatchupSeason<br>
Request URL: `https://x.com/i/api/graphql/ZgAomd4chOrVRid_l06NGw/NFLMatchupSeason`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileSeasonSchedule<br>
Request URL: `https://x.com/i/api/graphql/M946jrb9CchmjVYMukJ6RQ/ProfileSeasonSchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileTeamRoster<br>
Request URL: `https://x.com/i/api/graphql/I5ALHyuvPb6h7soVmbcq9g/ProfileTeamRoster`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLSchedule<br>
Request URL: `https://x.com/i/api/graphql/I0s-QbdS2Bq_PRCSTCoz8g/NFLSchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NflScoresSidebarFollow<br>
Request URL: `https://x.com/i/api/graphql/JR_EpH80gwgFyOBOreLBZw/NflScoresSidebarFollow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NflScoresSidebarLiveGame<br>
Request URL: `https://x.com/i/api/graphql/W1N4RqPcDwRAoadnEiw4Sw/NflScoresSidebarLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLSeasonStats<br>
Request URL: `https://x.com/i/api/graphql/iqNfGoXGVQStcvnqTb_NcQ/NFLSeasonStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLStandings<br>
Request URL: `https://x.com/i/api/graphql/whFK1zt98nRCL8cRDsnqFg/NFLStandings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLTeamLastGameHighlights<br>
Request URL: `https://x.com/i/api/graphql/RJLJjyt4VPiQ5006q8Tteg/NFLTeamLastGameHighlights`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsTeamRosterFollowState<br>
Request URL: `https://x.com/i/api/graphql/7ULJsc0TrtBg5zOp5Ig2Bw/SportsTeamRosterFollowState`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLTeams<br>
Request URL: `https://x.com/i/api/graphql/bX6d7-kzFq9ol6o2iNdPEQ/NFLTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NflTop100<br>
Request URL: `https://x.com/i/api/graphql/spFdWZOST1RudOikZgun0g/NflTop100`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## NFLWeeklyInjuries<br>
Request URL: `https://x.com/i/api/graphql/2poNqI6fpHMh4K3ibcBC3g/NFLWeeklyInjuries`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLWeeklySchedule<br>
Request URL: `https://x.com/i/api/graphql/hsXGNRAhwRCPm9pv-pof4g/NFLWeeklySchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLWeeklyStats<br>
Request URL: `https://x.com/i/api/graphql/HSm_7hBIX3PcGxBUuZr9iA/NFLWeeklyStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsGameLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/42gNZTsRw6aPZ8kaUhEepw/SportsGameLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SportsGameTopTimeline<br>
Request URL: `https://x.com/i/api/graphql/kYTK7T6VUvMvsIUab_n_cA/SportsGameTopTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SportsHubTrends<br>
Request URL: `https://x.com/i/api/graphql/BjydpXiXlskVEro9jODW8g/SportsHubTrends`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductAdSlots<br>
Request URL: `https://x.com/i/api/graphql/pgakXvDW-RVau7vMG6En0A/SportsProductAdSlots`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductChatState<br>
Request URL: `https://x.com/i/api/graphql/x1B2DaFQ3OroLl5xCmnVXQ/SportsProductChatState`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductCreateGameReminder<br>
Request URL: `https://x.com/i/api/graphql/kvMykYCXADv3PpOR8i5OCQ/SportsProductCreateGameReminder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductDeleteGameReminder<br>
Request URL: `https://x.com/i/api/graphql/5AnaGMKLiKya6L083VqJkw/SportsProductDeleteGameReminder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductFollowTeam<br>
Request URL: `https://x.com/i/api/graphql/5oznYapzML9HParqmJLmGQ/SportsProductFollowTeam`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductFollowedTeams<br>
Request URL: `https://x.com/i/api/graphql/mwMrIqFCzatbGomEKBeDQA/SportsProductFollowedTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductGameReminders<br>
Request URL: `https://x.com/i/api/graphql/QdFo9scG5R4nB7Z90Em7Bg/SportsProductGameReminders`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductLiveViewers<br>
Request URL: `https://x.com/i/api/graphql/IYQhJtndjln44l9SoPk8AQ/SportsProductLiveViewers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductNflTeams<br>
Request URL: `https://x.com/i/api/graphql/GqvOnvJXEO7Q6PIHCWkxmw/SportsProductNflTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductOptInTeamNotifications<br>
Request URL: `https://x.com/i/api/graphql/0_uQ_PViA5F4-iBxETQLdA/SportsProductOptInTeamNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductOptOutTeamNotifications<br>
Request URL: `https://x.com/i/api/graphql/sBl09dL6QIIyGpj4jYEmwQ/SportsProductOptOutTeamNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductSetTeamPick<br>
Request URL: `https://x.com/i/api/graphql/wgQc8AbBeexw0Hx3kPtFFQ/SportsProductSetTeamPick`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductSnoozeGameReminder<br>
Request URL: `https://x.com/i/api/graphql/XFCgeRuGOTTVLjullAXKNQ/SportsProductSnoozeGameReminder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductTeamNotificationSettings<br>
Request URL: `https://x.com/i/api/graphql/o_ONtKkXGr4GQOvvihmVbA/SportsProductTeamNotificationSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductTeamPicker<br>
Request URL: `https://x.com/i/api/graphql/YnPoLqQRFbfG8Cpb41t8NQ/SportsProductTeamPicker`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductTeamTallies<br>
Request URL: `https://x.com/i/api/graphql/i4p1dyYRohDUQZCx22d0xA/SportsProductTeamTallies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductUnfollowTeam<br>
Request URL: `https://x.com/i/api/graphql/HH35015GvGXNGQlQHCYnGA/SportsProductUnfollowTeam`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## DeleteDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/h0rzaIYc9-v3zTQvx1J8OA/DeleteDraftTweets`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/L9RqKWmAWxK6vGtR3Qdsxw/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchScheduledTweets<br>
Request URL: `https://x.com/i/api/graphql/H2elmT2R9DLhWoo0DZFNkA/FetchScheduledTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SidebarUserRecommendations<br>
Request URL: `https://x.com/i/api/graphql/BSYrSirC_dVN6R9Q0Mpmvg/SidebarUserRecommendations`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListProductSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/V8-RP7SxlI4qzRmpCmEqgw/ListProductSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                              | type    | variable   |
|:-------------------------------------------------|:--------|:-----------|
| subscriptions_management_fetch_next_billing_time | boolean | True       |
| subscriptions_marketing_page_fetch_promotions    | boolean | True       |

#### queryId<br>
`None`<br>
## NotABotCheckoutUrlWithEligibility<br>
Request URL: `https://x.com/i/api/graphql/RM4x9h3tF8bCn69VV3-gRg/NotABotCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/fatCCOgstk_uPEl-zNlX8w/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/el6V21NAvHxCSbMqcuY45w/SubscriptionProductDetails`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                           | type    | variable   |
|:----------------------------------------------|:--------|:-----------|
| subscriptions_marketing_page_fetch_promotions | boolean | True       |

#### queryId<br>
`None`<br>
## SwitchTier<br>
Request URL: `https://x.com/i/api/graphql/73t92vAzJ9DI1WygCcD7WQ/SwitchTier`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CurrentNflWeek<br>
Request URL: `https://x.com/i/api/graphql/39djCiLUxjpUpGgLWjaDOA/CurrentNflWeek`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FollowTeamRoster<br>
Request URL: `https://x.com/i/api/graphql/Dd76ifUtARWFkfQo3krDxA/FollowTeamRoster`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FollowedTeams<br>
Request URL: `https://x.com/i/api/graphql/Tx6_C2uyXyaW3TRIPy-6bw/FollowedTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGameHydrate<br>
Request URL: `https://x.com/i/api/graphql/CN2G3v-dUfNQe3NNv-Lxqw/NFLGameHydrate`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGameOdds<br>
Request URL: `https://x.com/i/api/graphql/BCsiVB5FamwjLHyEFBIOMA/NFLGameOdds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGamePlayerProps<br>
Request URL: `https://x.com/i/api/graphql/Bjp0zCvdw41fzm_Mgo8AWw/NFLGamePlayerProps`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLGameRoster<br>
Request URL: `https://x.com/i/api/graphql/CiBu_xfyiOu_rBNyuBngcQ/NFLGameRoster`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## NFLLiveGame<br>
Request URL: `https://x.com/i/api/graphql/1ssBFzuY0MFqgTl9h6a3hw/NFLLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLMatchupSeason<br>
Request URL: `https://x.com/i/api/graphql/ZgAomd4chOrVRid_l06NGw/NFLMatchupSeason`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileSeasonSchedule<br>
Request URL: `https://x.com/i/api/graphql/M946jrb9CchmjVYMukJ6RQ/ProfileSeasonSchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ProfileTeamRoster<br>
Request URL: `https://x.com/i/api/graphql/I5ALHyuvPb6h7soVmbcq9g/ProfileTeamRoster`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLSchedule<br>
Request URL: `https://x.com/i/api/graphql/I0s-QbdS2Bq_PRCSTCoz8g/NFLSchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NflScoresSidebarFollow<br>
Request URL: `https://x.com/i/api/graphql/JR_EpH80gwgFyOBOreLBZw/NflScoresSidebarFollow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NflScoresSidebarLiveGame<br>
Request URL: `https://x.com/i/api/graphql/W1N4RqPcDwRAoadnEiw4Sw/NflScoresSidebarLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLSeasonStats<br>
Request URL: `https://x.com/i/api/graphql/iqNfGoXGVQStcvnqTb_NcQ/NFLSeasonStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLStandings<br>
Request URL: `https://x.com/i/api/graphql/whFK1zt98nRCL8cRDsnqFg/NFLStandings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLTeamLastGameHighlights<br>
Request URL: `https://x.com/i/api/graphql/RJLJjyt4VPiQ5006q8Tteg/NFLTeamLastGameHighlights`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsTeamRosterFollowState<br>
Request URL: `https://x.com/i/api/graphql/7ULJsc0TrtBg5zOp5Ig2Bw/SportsTeamRosterFollowState`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLTeams<br>
Request URL: `https://x.com/i/api/graphql/bX6d7-kzFq9ol6o2iNdPEQ/NFLTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NflTop100<br>
Request URL: `https://x.com/i/api/graphql/spFdWZOST1RudOikZgun0g/NflTop100`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## NFLWeeklyInjuries<br>
Request URL: `https://x.com/i/api/graphql/2poNqI6fpHMh4K3ibcBC3g/NFLWeeklyInjuries`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLWeeklySchedule<br>
Request URL: `https://x.com/i/api/graphql/hsXGNRAhwRCPm9pv-pof4g/NFLWeeklySchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NFLWeeklyStats<br>
Request URL: `https://x.com/i/api/graphql/HSm_7hBIX3PcGxBUuZr9iA/NFLWeeklyStats`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsGameLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/42gNZTsRw6aPZ8kaUhEepw/SportsGameLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SportsGameTopTimeline<br>
Request URL: `https://x.com/i/api/graphql/kYTK7T6VUvMvsIUab_n_cA/SportsGameTopTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SportsHubTrends<br>
Request URL: `https://x.com/i/api/graphql/BjydpXiXlskVEro9jODW8g/SportsHubTrends`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductAdSlots<br>
Request URL: `https://x.com/i/api/graphql/pgakXvDW-RVau7vMG6En0A/SportsProductAdSlots`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductChatState<br>
Request URL: `https://x.com/i/api/graphql/x1B2DaFQ3OroLl5xCmnVXQ/SportsProductChatState`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductCreateGameReminder<br>
Request URL: `https://x.com/i/api/graphql/kvMykYCXADv3PpOR8i5OCQ/SportsProductCreateGameReminder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductDeleteGameReminder<br>
Request URL: `https://x.com/i/api/graphql/5AnaGMKLiKya6L083VqJkw/SportsProductDeleteGameReminder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductFollowTeam<br>
Request URL: `https://x.com/i/api/graphql/5oznYapzML9HParqmJLmGQ/SportsProductFollowTeam`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductFollowedTeams<br>
Request URL: `https://x.com/i/api/graphql/mwMrIqFCzatbGomEKBeDQA/SportsProductFollowedTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductGameReminders<br>
Request URL: `https://x.com/i/api/graphql/QdFo9scG5R4nB7Z90Em7Bg/SportsProductGameReminders`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductLiveViewers<br>
Request URL: `https://x.com/i/api/graphql/IYQhJtndjln44l9SoPk8AQ/SportsProductLiveViewers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductNflTeams<br>
Request URL: `https://x.com/i/api/graphql/GqvOnvJXEO7Q6PIHCWkxmw/SportsProductNflTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductOptInTeamNotifications<br>
Request URL: `https://x.com/i/api/graphql/0_uQ_PViA5F4-iBxETQLdA/SportsProductOptInTeamNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductOptOutTeamNotifications<br>
Request URL: `https://x.com/i/api/graphql/sBl09dL6QIIyGpj4jYEmwQ/SportsProductOptOutTeamNotifications`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductSetTeamPick<br>
Request URL: `https://x.com/i/api/graphql/wgQc8AbBeexw0Hx3kPtFFQ/SportsProductSetTeamPick`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductSnoozeGameReminder<br>
Request URL: `https://x.com/i/api/graphql/XFCgeRuGOTTVLjullAXKNQ/SportsProductSnoozeGameReminder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductTeamNotificationSettings<br>
Request URL: `https://x.com/i/api/graphql/o_ONtKkXGr4GQOvvihmVbA/SportsProductTeamNotificationSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductTeamPicker<br>
Request URL: `https://x.com/i/api/graphql/YnPoLqQRFbfG8Cpb41t8NQ/SportsProductTeamPicker`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductTeamTallies<br>
Request URL: `https://x.com/i/api/graphql/i4p1dyYRohDUQZCx22d0xA/SportsProductTeamTallies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductUnfollowTeam<br>
Request URL: `https://x.com/i/api/graphql/HH35015GvGXNGQlQHCYnGA/SportsProductUnfollowTeam`<br>
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
## DeleteDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/h0rzaIYc9-v3zTQvx1J8OA/DeleteDraftTweets`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/L9RqKWmAWxK6vGtR3Qdsxw/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchScheduledTweets<br>
Request URL: `https://x.com/i/api/graphql/H2elmT2R9DLhWoo0DZFNkA/FetchScheduledTweets`<br>
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
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ArticleEntitiesSlice<br>
Request URL: `https://x.com/i/api/graphql/8hpdcfFniawLzEQ7CD2WMQ/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/fCkdrI6zrnw_UtVa3WDHhw/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/86zqyWZeIoccSyBxmxcd6w/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/eUiP53I_YemhBOI2TMCI3A/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/hRtkxfQu7M6mnlP1FRcGgg/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/FMC9CKP145f5wgXYCsmtiA/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/Rlvhkuecg1z_7O5vC2G1fQ/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/wTWiDSxOe1ZsImjXyuoiYw/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## GifEnumerateCategory<br>
Request URL: `https://x.com/i/api/graphql/LtO2mAjgSf_RwA51ACMbkA/GifEnumerateCategory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## GifSearch<br>
Request URL: `https://x.com/i/api/graphql/bKYBmwqIxMGZv04iU_lLWg/GifSearch`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://x.com/i/api/graphql/q9xVNj4CiI9oHN3cUmFrgA/Favoriters`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/9gzvtg9l4CmhrfO6KMgKCA/Retweeters`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/FQ96gBQZX3HMMK-XSIb9Qg/TweetEditHistory`<br>
Request Method: `GET`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserSportsProfile<br>
Request URL: `https://x.com/i/api/graphql/u7J50a1cN3sp5ejJ4nTuEA/UserSportsProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/Sy2C0fq3p4y5h4YuteslPg/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| rweb_cashtags_enabled                                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_grok_image_annotation_enabled         | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled       | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## DmGroupSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/LxrvmqF3Lokl_BYZ1c83LA/DmGroupSearchSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/GZTVOgSQYvr3ZQ2ukSe3WA/DmMutedTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## DmPeopleSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/c1MnRRmI-_Bggpntlq9-hQ/DmPeopleSearchSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/YYJk-rhCD2EUmq49LugABA/ViewerEmailSettings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ListProductSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/V8-RP7SxlI4qzRmpCmEqgw/ListProductSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                              | type    | variable   |
|:-------------------------------------------------|:--------|:-----------|
| subscriptions_management_fetch_next_billing_time | boolean | True       |
| subscriptions_marketing_page_fetch_promotions    | boolean | True       |

#### queryId<br>
`None`<br>
## NotABotCheckoutUrlWithEligibility<br>
Request URL: `https://x.com/i/api/graphql/RM4x9h3tF8bCn69VV3-gRg/NotABotCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/fatCCOgstk_uPEl-zNlX8w/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/el6V21NAvHxCSbMqcuY45w/SubscriptionProductDetails`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                           | type    | variable   |
|:----------------------------------------------|:--------|:-----------|
| subscriptions_marketing_page_fetch_promotions | boolean | True       |

#### queryId<br>
`None`<br>
## SwitchTier<br>
Request URL: `https://x.com/i/api/graphql/73t92vAzJ9DI1WygCcD7WQ/SwitchTier`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## DeleteDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/h0rzaIYc9-v3zTQvx1J8OA/DeleteDraftTweets`<br>
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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FetchDraftTweets<br>
Request URL: `https://x.com/i/api/graphql/L9RqKWmAWxK6vGtR3Qdsxw/FetchDraftTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## FetchScheduledTweets<br>
Request URL: `https://x.com/i/api/graphql/H2elmT2R9DLhWoo0DZFNkA/FetchScheduledTweets`<br>
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
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/NtEAlAR40O3S7Lf8s6XUTQ/BroadcastQuery`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BroadcastUpdateViewerSession<br>
Request URL: `https://x.com/i/api/graphql/MRPwWxSUacJB61vTj1mF9g/BroadcastUpdateViewerSession`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CombinedLists<br>
Request URL: `https://x.com/i/api/graphql/HoclSXITeTmRfg1TF3G-RQ/CombinedLists`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://x.com/i/api/graphql/-Kf1YVC1rNKkPvPFk7YXZw/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://x.com/i/api/graphql/my6Lh9X_pvMtrK_c3VjfNA/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://x.com/i/api/graphql/PSBi0stSrf3-hDy3G_O_0Q/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://x.com/i/api/graphql/ZX5ei7t018bDaDcy4VWBeA/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://x.com/i/api/graphql/zdGzorOEOslDL4XEbe2INw/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://x.com/i/api/graphql/NCdb-TPGFi_6Tpvs3WmAFg/ListCreationRecommendedUsers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/8VcpjisNYiVaGOemxfDJ3A/ListEditRecommendedUsers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/RgfF9JYDXXI1F-ZrDqjUfQ/ListLatestTweetsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://x.com/i/api/graphql/yQ_0-CTekcCY2oFRTskpSw/ListMembers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://x.com/i/api/graphql/4xBNevulxGhaqiO6-pCJMA/ListMemberships`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/f1u5dCI80zd4-YFYSkVCVQ/ListOwnerships`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://x.com/i/api/graphql/T-YE5ZY0cd0UVtWu8AP04Q/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/kbgGefrdaL-KIAWqOohUfg/ListRankedTweetsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://x.com/i/api/graphql/_2o1-wSMWGFSi5HUscn1Hw/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://x.com/i/api/graphql/k5mwUiaPTQ_Hhr8DNXQ5YA/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://x.com/i/api/graphql/n52ZU-g4FEWzgdPkv1UC2g/ListSubscribers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/HwX1NRCSksXzmpolnY0Xhw/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://x.com/i/api/graphql/oe5s3-_kb6-t8iFv4hLH3A/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://x.com/i/api/graphql/RFtg_Vc7j01gXTQZtHvrpg/ListsDiscovery`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/FMDRDwDKo_nl4kT_AKWOCg/ListsManagementPageTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/Rw4ivbTs2WE0tZyJvqLpjQ/TopicToFollowSidebar`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListProductSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/V8-RP7SxlI4qzRmpCmEqgw/ListProductSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                              | type    | variable   |
|:-------------------------------------------------|:--------|:-----------|
| subscriptions_management_fetch_next_billing_time | boolean | True       |
| subscriptions_marketing_page_fetch_promotions    | boolean | True       |

#### queryId<br>
`None`<br>
## NotABotCheckoutUrlWithEligibility<br>
Request URL: `https://x.com/i/api/graphql/RM4x9h3tF8bCn69VV3-gRg/NotABotCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/fatCCOgstk_uPEl-zNlX8w/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/el6V21NAvHxCSbMqcuY45w/SubscriptionProductDetails`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                           | type    | variable   |
|:----------------------------------------------|:--------|:-----------|
| subscriptions_marketing_page_fetch_promotions | boolean | True       |

#### queryId<br>
`None`<br>
## SwitchTier<br>
Request URL: `https://x.com/i/api/graphql/73t92vAzJ9DI1WygCcD7WQ/SwitchTier`<br>
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
Request URL: `https://x.com/i/api/graphql/q9xVNj4CiI9oHN3cUmFrgA/Favoriters`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/9gzvtg9l4CmhrfO6KMgKCA/Retweeters`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/FQ96gBQZX3HMMK-XSIb9Qg/TweetEditHistory`<br>
Request Method: `GET`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_screen_enabled                                               | boolean |          0 | nan       |
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/n2SrvFA8CstWa-JLzim6OA/BookmarkFolderTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/VjWsfItbiMLeajpZ90NJeg/Bookmarks`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/NmDBT3APtNxDpMqIEauu7A/HomeLatestTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/svLglq6U2wlTyZMGDDcLYQ/HomeTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MLBGameHydrate<br>
Request URL: `https://x.com/i/api/graphql/Lj3UyfijNawe_Nov84F7-w/MLBGameHydrate`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBGameOdds<br>
Request URL: `https://x.com/i/api/graphql/ROiXANCNUoqr28usraFW-Q/MLBGameOdds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBGamePlayerProps<br>
Request URL: `https://x.com/i/api/graphql/U2niAYPZ3GDoQphnZuVRBQ/MLBGamePlayerProps`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBLeaders<br>
Request URL: `https://x.com/i/api/graphql/QIU6Qc5Bdwd-zcls7jtCwA/MLBLeaders`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBLiveGame<br>
Request URL: `https://x.com/i/api/graphql/Y48JDK9LNvh1IAuRAVOJjQ/MLBLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBMatchup<br>
Request URL: `https://x.com/i/api/graphql/h-qGvM4sZDshcH8R2epuXA/MLBMatchup`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBPlayerProfile<br>
Request URL: `https://x.com/i/api/graphql/C6sGvj7Qq3J4MZWHmxa2pA/MLBPlayerProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBPostseasonRounds<br>
Request URL: `https://x.com/i/api/graphql/thgZnfjQjxqkh0hmoVvGew/MLBPostseasonRounds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBSchedule<br>
Request URL: `https://x.com/i/api/graphql/LF20hIABrq6kjc7fhInf7Q/MLBSchedule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBScheduleDays<br>
Request URL: `https://x.com/i/api/graphql/iFzaptv3YWPZEHn0msgOXA/MLBScheduleDays`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MlbScoresSidebarLiveGame<br>
Request URL: `https://x.com/i/api/graphql/vSoV7RqhrtJTMFUheOH1uQ/MlbScoresSidebarLiveGame`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBStandings<br>
Request URL: `https://x.com/i/api/graphql/o_Gw2WYhPTFqKKhMR_udrQ/MLBStandings`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## MLBTeams<br>
Request URL: `https://x.com/i/api/graphql/bSzG6BGhJO0it5IPuYnniw/MLBTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsHubBySport<br>
Request URL: `https://x.com/i/api/graphql/jn8sGMIC8-f2CzSZw2L6Rw/SportsHubBySport`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductFollowedTeamsV2<br>
Request URL: `https://x.com/i/api/graphql/anze-HOj0RlxxNJ3-wMJKA/SportsProductFollowedTeamsV2`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## SportsProductLeagueMediaSeries<br>
Request URL: `https://x.com/i/api/graphql/dX2jA3OPUo65OPH6N0DBxA/SportsProductLeagueMediaSeries`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## SportsProductLeagueTeams<br>
Request URL: `https://x.com/i/api/graphql/SuJhAYUuVr3K8SbhcQlWMw/SportsProductLeagueTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## NotificationsTimeline<br>
Request URL: `https://x.com/i/api/graphql/EUX2EwvgT4f9F7sC4A59Eg/NotificationsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## ViewerBadgeCounts<br>
Request URL: `https://x.com/i/api/graphql/q4Npr1-FYRWyXsRzPckwEA/ViewerBadgeCounts`<br>
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
Request URL: `https://x.com/i/api/graphql/9gQUtZmRLsKAsGCedwML0g/BlockedAccountsAll`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://x.com/i/api/graphql/hM_geO3VhVPapTRoGmFEog/BlockedAccountsImported`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://x.com/i/api/graphql/1fjk4lmK45a-giaZTubqbg/BlueVerifiedFollowers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/VxJMx0-NXe-GO_4jC1lNhw/BookmarkSearchTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/IMQS8zyOjCLnWBkm6wNcQg/ConnectTabTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/H7QXYuKegEKuUJvkuW5_dg/CreateNoteTweet`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/wR5Z_lEibLvkew3tF9w-Sg/CreateTweet`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/BMib5Px-wibex8mYlOUhmQ/ExplorePage`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ExploreSidebar<br>
Request URL: `https://x.com/i/api/graphql/bY118dk8ns_5JzfzIMeiBw/ExploreSidebar`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/stpzFPAIZ2qv8s2lRzPOnQ/Followers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://x.com/i/api/graphql/479-dF4nq3sH1uu0n4Wdxg/FollowersYouKnow`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://x.com/i/api/graphql/ath0FIohYC_c3Hj3SsxoCg/Following`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://x.com/i/api/graphql/cW93hZ3nlNYbYcUROF5r5A/GenericTimelineById`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/XtgLdT7L-zyrDDKH2dO0lw/GlobalCommunitiesLatestPostSearchTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## GlobalCommunitiesPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/z3OlkLD0_MFgCvUXcN1XeA/GlobalCommunitiesPostSearchTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://x.com/i/api/graphql/mu4us66Q6RRNOywVQhGtRg/Likes`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/9kXBVnbdRxymiEvafaXCQA/ListSearchTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MediaTabVideoMixer<br>
Request URL: `https://x.com/i/api/graphql/cbgcKS_qpavOmwMyWy6Ufg/MediaTabVideoMixer`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/8WssE8nvyh6zLlc8G9kOCQ/ModeratedTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://x.com/i/api/graphql/_p01XKzLM3kfwiW0ptPByw/MutedAccounts`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/qaz5JhPxqI3UqAgkTpsGyQ/PinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

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
## PinnableTimelines<br>
Request URL: `https://x.com/i/api/graphql/HQ-MFOr09c_gbFjDGPJn-w/PinnableTimelines`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## PinnedTimelines<br>
Request URL: `https://x.com/i/api/graphql/8J1r9u3VjUveEdTY4WUTwQ/PinnedTimelines`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## ProfileFilter<br>
Request URL: `https://x.com/i/api/graphql/e-9v4-3Y6VwNrg31xgDYfQ/ProfileFilter`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/irezafrnzav4Ulf1vDkEBg/SearchTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/o1hIGXCGvgeFbR-EV8oqVw/SimilarPosts`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://x.com/i/api/graphql/ETUYtgt-7ODFW0rEfuI8RA/SuperFollowers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/Z1kaoaqgNPpRRoXHK6OPug/TrendHistory`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TrendRelevantUsers<br>
Request URL: `https://x.com/i/api/graphql/mVoSlW4Ep91zz-pNhkLH0Q/TrendRelevantUsers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TVHomeMixer<br>
Request URL: `https://x.com/i/api/graphql/BMTYddUdvimu_voVh12qWw/TVHomeMixer`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://x.com/i/api/graphql/3BlMtudy4N-d78ch7zTLZQ/TweetDetail`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/xZfFqfOmKQu_OXekGI59mg/TweetResultByRestId`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://x.com/i/api/graphql/aiX7QIJ4jp1QR8wT32vkHQ/TweetResultsByRestIds`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/u_Nxpj-y-PoTFHEM9saz2Q/UnpinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/J6-7gyMkcVWna0u0KkPU7g/UpdatePinnedTimelines`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/0MAr19lWhBkKwNGHtK5BrQ/UrtFixtures`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://x.com/i/api/graphql/G9ehBUadUrsNfz-XnAcV4A/UserArticlesTweets`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://x.com/i/api/graphql/JyMBv5W5h6A_TWJk398yoA/UserBusinessProfileTeamTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://x.com/i/api/graphql/mxaYWwt52eAb6OAzYHMVzg/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                 | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| highlights_tweets_tab_ui_enabled                     | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled     | boolean | True       |
| subscriptions_feature_can_gift_premium               | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled      | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://x.com/i/api/graphql/AMIBMjtxEEATh4z8V9GtRg/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                          | type    | variable   |
|:-------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                         | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled         | boolean | True       |
| responsive_web_profile_redirect_enabled                      | boolean | True       |
| rweb_tipjar_consumption_enabled                              | boolean | False      |
| verified_phone_label_enabled                                 | boolean | False      |
| subscriptions_verification_info_is_identity_verified_enabled | boolean | True       |
| subscriptions_verification_info_verified_since_enabled       | boolean | True       |
| highlights_tweets_tab_ui_enabled                             | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled             | boolean | True       |
| subscriptions_feature_can_gift_premium                       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled              | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled           | boolean | True       |

#### queryId<br>
`None`<br>
## GetUserClaims<br>
Request URL: `https://x.com/i/api/graphql/AqTNiqohgRK_0DarLzqUvg/GetUserClaims`<br>
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
Request URL: `https://x.com/i/api/graphql/WdOv4T4CRGozks_e4iIpKw/UserCreatorSubscribers`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/hoDpKXk4ulppcM8ReGNLlQ/UserCreatorSubscriptions`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://x.com/i/api/graphql/Ducf_uu7enyuuE2kjOwFcw/UserHighlightsTweets`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://x.com/i/api/graphql/QWOimofaocjeRda7Tm5pNA/UserMedia`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserOriginalsTimeline<br>
Request URL: `https://x.com/i/api/graphql/QLGv_wL7wziqsHhU0K100w/UserOriginalsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserPhotoTimeline<br>
Request URL: `https://x.com/i/api/graphql/sa-ZQ0jW0FT_VnNKT1PtYg/UserPhotoTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/ajc72R9dmILUYBcF5JlzBA/UserPromotableTweets`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserPromotedTweets<br>
Request URL: `https://x.com/i/api/graphql/tY-UcVvOU284pAfE_Y004w/UserPromotedTweets`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserRepliesTimeline<br>
Request URL: `https://x.com/i/api/graphql/X9Te-FyiGcoV2qNrnx9w3w/UserRepliesTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserRepostsTimeline<br>
Request URL: `https://x.com/i/api/graphql/jVw4ob-dDfVzoaz2G6NpVA/UserRepostsTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
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
Request URL: `https://x.com/i/api/graphql/SgMBGaLeFpBoPYftpsn8fw/UserSuperFollowTweets`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://x.com/i/api/graphql/7_KBXBpG0zBPRN6UCIV0-w/UserTweets`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://x.com/i/api/graphql/bnsYxFljT6y98rFwiGr3fw/UserTweetsAndReplies`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UserVideoTimeline<br>
Request URL: `https://x.com/i/api/graphql/oAFGPinlLUFMoa3u70mnAw/UserVideoTimeline`<br>
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
| responsive_web_profile_redirect_enabled                                 | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| premium_content_api_read_enabled                                        | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean |          0 | nan       |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          1 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| rweb_sports_post_context_enabled                                        | boolean |          1 | nan       |
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
| responsive_web_nested_quote_preview_enabled                             | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://x.com/i/api/graphql/ubfbnAM4qTlMTOYleYhXSg/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
## UsersByScreenNames<br>
Request URL: `https://x.com/i/api/graphql/cACg_kWQkzNQ74lcK5rksQ/UsersByScreenNames`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                          | type    | variable   |
|:-------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                         | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled         | boolean | True       |
| responsive_web_profile_redirect_enabled                      | boolean | True       |
| rweb_tipjar_consumption_enabled                              | boolean | False      |
| verified_phone_label_enabled                                 | boolean | False      |
| subscriptions_verification_info_is_identity_verified_enabled | boolean | True       |
| subscriptions_verification_info_verified_since_enabled       | boolean | True       |
| highlights_tweets_tab_ui_enabled                             | boolean | True       |
| responsive_web_twitter_article_notes_tab_enabled             | boolean | True       |
| subscriptions_feature_can_gift_premium                       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled              | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled           | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/TpQxQtWMTMnIAMPlMGMqNw/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                  | type    | variable   |
|:-----------------------------------------------------|:--------|:-----------|
| subscriptions_upsells_api_enabled                    | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled | boolean | True       |
| responsive_web_profile_redirect_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                      | boolean | False      |
| verified_phone_label_enabled                         | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled      | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled   | boolean | True       |

#### queryId<br>
`None`<br>
