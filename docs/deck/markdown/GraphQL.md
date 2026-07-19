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
Request URL: `https://x.com/i/api/graphql/vOjeHbXdNCi-ineWfwBRlw/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/wwgMLqOUxo6In8w1HgAGjw/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/94iKIFXsW369GcGrPaEBcA/BlueVerifiedFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/SpDsqmz6FfYESd1e7TPcAw/BookmarkSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/5fKmzgJzgNxisAdyoJTPdg/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/uGXMU9aKbNB9qxxAg4jxkA/CreateNoteTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/hIL9XdleMYEtVXOZVbr8Bg/CreateTweet`<br>
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
Request URL: `https://x.com/i/api/graphql/EZOfZI7WSkp08oj2jAC3rg/ExplorePage`<br>
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
Request URL: `https://x.com/i/api/graphql/RBRrfsYi3hlCzcKafukFWA/ExploreSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/18SNsfvwgu2CYIweeUVHAw/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/_eZH-acfZrss2leLwhIT6A/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/PEIBUtChvR2i_NZCxbK3fA/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/GswYtMwzaFKSDx_SvC-f6g/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/nzqDxknLcpQi7G1ls0qPGg/GlobalCommunitiesLatestPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/ztGVPpiTJzPjJBKrdQ3OMw/GlobalCommunitiesPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/4X8QeWbeJ0jwGHaXSxExRw/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
## ListSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/tI3qYJtL3fUohtSpcSuZyw/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/-wAxE0ebQU5S4ezBKZtn0g/MediaTabVideoMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/-_uCk6LsBVifr1EEQUXenw/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/E720dAlcGCWxWg24RFVUYQ/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
## PinnableTimelines<br>
Request URL: `https://x.com/i/api/graphql/Tx2WqUDEDSYRA7IKfQReAg/PinnableTimelines`<br>
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
Request URL: `https://x.com/i/api/graphql/01c84_HcRM5bt_DJw1abfQ/ProfileFilter`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/hz_94eVAtrtQo_vO3my7Rw/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/Igk9y9DSZ6N9360img7rrQ/SimilarPosts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/3pooAGeLLx7co1B7jrVptw/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/zuSCJJsjwFaJhJr2yfpUhg/TrendHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/yBPPLwk_fiJlAvMRMXVmEQ/TrendRelevantUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/Z134-7KxUTEZ0GYZLZd9oQ/TVHomeMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/rZA6K31W4E90vZKBmxXV3g/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/4hhGRbehkcUVTKf8n0f0xw/TweetResultByRestId`<br>
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
Request URL: `https://x.com/i/api/graphql/aSkhsainBPfEWA4mG8wnFA/TweetResultsByRestIds`<br>
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
Request URL: `https://x.com/i/api/graphql/zzu9yRLhFo1HiSho0Mulqw/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/tyokweQxa15NZbW0UOc3Uw/UserArticlesTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/l0-_GguB4sE4zMtIUFcDUA/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/EWi-Y-Rp-Kv4yF0BFS1yQA/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/qhT9BsaNXNYh4R-e1REj7Q/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/06hDMOiAMANzKwXHHUwD1w/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/IS3w9vvPg1SJysLErvnFGg/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/Iyg3GhUsD-8d51Rv_SJEYA/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/LQ2ew-e4jKprBsriYpTWRg/UserPromotedTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/wKBdaKL-JQVOXnQVWDxNuw/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/6r5OLCC_wFH4CpRyXKuAmQ/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
Request URL: `https://x.com/i/api/graphql/klja8a2iJX_3to5RdfVlgw/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
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
