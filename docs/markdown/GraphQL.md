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
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/4XVA9nlY4lEtinRVNyea0g/BroadcastQuery`<br>
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/oKopHt25pa6yhDn1ek7Qng/BookmarkFolderTimeline`<br>
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
Request URL: `https://x.com/i/api/graphql/tUVliYsHyxrQIT4HXUWNdA/Bookmarks`<br>
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
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/4XVA9nlY4lEtinRVNyea0g/BroadcastQuery`<br>
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
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
## DmAllSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/zd0F6a_svKAXdlMGbCZDFg/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_cashtags_enabled                                             | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_grok_image_annotation_enabled                      | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/8XKy5y9Eib8LTHpqHIA0zw/DmMutedTimeline`<br>
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
Request URL: `https://x.com/i/api/graphql/k4BM6zpJ-RnicgIzjpi8dw/BirdwatchFetchAuthenticatedBirdwatchMatchSlice`<br>
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
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://x.com/i/api/graphql/uVeNvPGlnoyCyQnDtGWy3w/BirdwatchFetchContributorNotesSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/wBxYJHZ10nvpg1XHAGs2Lw/BirdwatchCreateNote`<br>
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
| responsive_web_grok_community_note_translation_is_enabled         | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_birdwatch_live_note_enabled                        | boolean | True       |
| responsive_web_birdwatch_note_internal_insights_enabled           | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled    | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/m1B2Vwf-_Xuq4aou_9ncrA/BirdwatchFetchGlobalTimeline`<br>
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
## BirdwatchFetchMediaMatchSlice<br>
Request URL: `https://x.com/i/api/graphql/pk6o7FPcSwBMTxcrk3sv-A/BirdwatchFetchMediaMatchSlice`<br>
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
## BirdwatchFetchNoteTranslation<br>
Request URL: `https://x.com/i/api/graphql/AB94g3Hf1tt2DNgKCgK4xA/BirdwatchFetchNoteTranslation`<br>
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
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://x.com/i/api/graphql/-ZtpeA6Jwx93AcIY42pCZA/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_live_note_enabled                        | boolean | True       |
| responsive_web_birdwatch_enforce_author_user_quotas               | boolean | True       |
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                        | boolean | False      |
| responsive_web_grok_community_note_translation_is_enabled         | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_birdwatch_note_internal_insights_enabled           | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled    | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://x.com/i/api/graphql/MdavtH5FlrhKhqCeSRrlNg/BirdwatchFetchOneNote`<br>
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
| responsive_web_grok_community_note_translation_is_enabled         | boolean | True       |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_birdwatch_live_note_enabled                        | boolean | True       |
| responsive_web_birdwatch_note_internal_insights_enabled           | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled    | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchProminentMediaMatchSlice<br>
Request URL: `https://x.com/i/api/graphql/rxujZh7TPM0v7RGI9sYf6Q/BirdwatchFetchProminentMediaMatchSlice`<br>
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
## BirdwatchFetchSourceLinkSlice<br>
Request URL: `https://x.com/i/api/graphql/2KXwCt6WVkq8sdjAZjO6RQ/BirdwatchFetchSourceLinkSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/jP2KAOpKtqKWGgzCOK74dw/BirdwatchFetchSuggestionFeedbackOverview`<br>
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
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/oKopHt25pa6yhDn1ek7Qng/BookmarkFolderTimeline`<br>
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
Request URL: `https://x.com/i/api/graphql/tUVliYsHyxrQIT4HXUWNdA/Bookmarks`<br>
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
Request URL: `https://x.com/i/api/graphql/JzjKwvbH_B3EWjkVWgNVVA/TopicToFollowSidebar`<br>
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
Request URL: `https://x.com/i/api/graphql/89HaDqdHc0yOl_dpJT9R8A/AiTrendByRestId`<br>
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
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/dDmkonrnmZCNvGAddHYSHQ/ArticleEntitiesSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/rSvnWw6CAJo4F9xVieZhLA/ArticleEntityDraftCreate`<br>
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
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/xkPT5esHwPTNtJfp-1xKaQ/ArticleEntityPublish`<br>
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
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/NYcREZ9msGwridku2068ng/ArticleEntityResultByRestId`<br>
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
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/4M8Wv2IADEw61KFMrXqOSQ/ArticleEntityUnpublish`<br>
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
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/CPOMQigUs99fzPmNe_1-EA/ArticleEntityUpdateContent`<br>
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
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/AbzX20PDk6TTzqmN67hiPQ/ArticleEntityUpdateCoverMedia`<br>
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
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/PplP1XRcflB3VYMQJdd_hw/ArticleEntityUpdateTitle`<br>
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
## ImmersiveMedia<br>
Request URL: `https://x.com/i/api/graphql/PjsnOFgw9M8TYRvw7VfWSg/ImmersiveMedia`<br>
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
## ImmersiveProfile<br>
Request URL: `https://x.com/i/api/graphql/FqPuM4DP1HjKnhujH-va0w/ImmersiveProfile`<br>
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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/oKopHt25pa6yhDn1ek7Qng/BookmarkFolderTimeline`<br>
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
Request URL: `https://x.com/i/api/graphql/tUVliYsHyxrQIT4HXUWNdA/Bookmarks`<br>
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
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/4XVA9nlY4lEtinRVNyea0g/BroadcastQuery`<br>
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

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
Request URL: `https://x.com/i/api/graphql/JzjKwvbH_B3EWjkVWgNVVA/TopicToFollowSidebar`<br>
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
Request URL: `https://x.com/i/api/graphql/JzjKwvbH_B3EWjkVWgNVVA/TopicToFollowSidebar`<br>
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
Request URL: `https://x.com/i/api/graphql/JzjKwvbH_B3EWjkVWgNVVA/TopicToFollowSidebar`<br>
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
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/4XVA9nlY4lEtinRVNyea0g/BroadcastQuery`<br>
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## SidebarUserRecommendations<br>
Request URL: `https://x.com/i/api/graphql/CEM7EcfnKL9BjJZ-L9iBnw/SidebarUserRecommendations`<br>
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
## ArticleEntitiesSlice<br>
Request URL: `https://x.com/i/api/graphql/dDmkonrnmZCNvGAddHYSHQ/ArticleEntitiesSlice`<br>
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
Request URL: `https://x.com/i/api/graphql/rSvnWw6CAJo4F9xVieZhLA/ArticleEntityDraftCreate`<br>
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
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/xkPT5esHwPTNtJfp-1xKaQ/ArticleEntityPublish`<br>
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
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/NYcREZ9msGwridku2068ng/ArticleEntityResultByRestId`<br>
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
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/4M8Wv2IADEw61KFMrXqOSQ/ArticleEntityUnpublish`<br>
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
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/CPOMQigUs99fzPmNe_1-EA/ArticleEntityUpdateContent`<br>
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
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/AbzX20PDk6TTzqmN67hiPQ/ArticleEntityUpdateCoverMedia`<br>
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
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/PplP1XRcflB3VYMQJdd_hw/ArticleEntityUpdateTitle`<br>
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
Request URL: `https://x.com/i/api/graphql/DGPZeGl8lC0Nvps4afRHHQ/GrokConversationItemsByRestId`<br>
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
Request URL: `https://x.com/i/api/graphql/I-JK6m7TIan-Myb_k10zUQ/GrokShare`<br>
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
## Favoriters<br>
Request URL: `https://x.com/i/api/graphql/wEhgf2DGiblPeYbAgQMZsw/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| flag  | ...    | t          |

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
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/gClaCb5tCk0z2iwAis8CwA/Retweeters`<br>
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
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/LMsM9EUFN4eMV5exUHGJww/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key        | type   | variable   |
|:-----------|:-------|:-----------|
| promptType | ...    | r          |

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
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://x.com/i/api/graphql/JzjKwvbH_B3EWjkVWgNVVA/TopicToFollowSidebar`<br>
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
## DmAllSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/zd0F6a_svKAXdlMGbCZDFg/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| rweb_cashtags_enabled                                             | boolean | True       |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| responsive_web_profile_redirect_enabled                           | boolean | False      |
| rweb_tipjar_consumption_enabled                                   | boolean | False      |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_grok_image_annotation_enabled                      | boolean | True       |
| responsive_web_grok_imagine_annotation_enabled                    | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

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
Request URL: `https://x.com/i/api/graphql/8XKy5y9Eib8LTHpqHIA0zw/DmMutedTimeline`<br>
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
## AudioSpaceAddSharing<br>
Request URL: `https://x.com/i/api/graphql/khoD4-YEmluEU_arMj3mlA/AudioSpaceAddSharing`<br>
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
| responsive_web_grok_analyze_post_followups_enabled                      | boolean |          0 | nan       |
| rweb_cashtags_composer_attachment_enabled                               | boolean |          1 | nan       |
| responsive_web_jetfuel_frame                                            | boolean |          1 | nan       |
| responsive_web_grok_share_attachment_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_annotations_enabled                                 | boolean |          1 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://x.com/i/api/graphql/yeKQfBMP2KU6HpO1v0dRzA/AudioSpaceById`<br>
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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/oKopHt25pa6yhDn1ek7Qng/BookmarkFolderTimeline`<br>
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
Request URL: `https://x.com/i/api/graphql/tUVliYsHyxrQIT4HXUWNdA/Bookmarks`<br>
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
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/4XVA9nlY4lEtinRVNyea0g/BroadcastQuery`<br>
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
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean |          1 | nan       |
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
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
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
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
Request URL: `https://x.com/i/api/graphql/wEhgf2DGiblPeYbAgQMZsw/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| flag  | ...    | t          |

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
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/gClaCb5tCk0z2iwAis8CwA/Retweeters`<br>
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
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/LMsM9EUFN4eMV5exUHGJww/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key        | type   | variable   |
|:-----------|:-------|:-----------|
| promptType | ...    | r          |

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
| responsive_web_profile_redirect_enabled                                 | boolean |          0 | nan       |
| rweb_tipjar_consumption_enabled                                         | boolean |          0 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| rweb_cashtags_enabled                                                   | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          0 | nan       |
| articles_preview_enabled                                                | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean |          1 | nan       |
| responsive_web_grok_image_annotation_enabled                            | boolean |          1 | nan       |
| responsive_web_grok_imagine_annotation_enabled                          | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## NotificationsTimeline<br>
Request URL: `https://x.com/i/api/graphql/wNZHyvh2CreGJSdEm-vQYA/NotificationsTimeline`<br>
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
