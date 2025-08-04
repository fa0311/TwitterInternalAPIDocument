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
Request URL: `https://x.com/i/api/graphql/R9NLasCuk0-vbzJ8wO3glA/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://x.com/i/api/graphql/wbpPOx1Hfe5NgYIce_fOxg/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://x.com/i/api/graphql/5DNV_MuXFKqEeL_Zsedtuw/BlueVerifiedFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/kLQN6uCuQluVfQ2qI_TK0g/BookmarkSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BroadcastQuery<br>
Request URL: `https://x.com/i/api/graphql/SD2r4LGLgL3eJv4MY0idhQ/BroadcastQuery`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/l6rUwSIBA0uyLFTEm7jS-g/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/VyBZcPSvJCrQKE7L46RT_Q/CreateNoteTweet`<br>
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
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
## CreateTweet<br>
Request URL: `https://x.com/i/api/graphql/pv-WrwtRJiLTCn7O_DsO-Q/CreateTweet`<br>
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
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/-nXrv1qPpTnhpKMPA1ADRg/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/S3mzV-AGKiWthXfw436_Hg/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ExploreSidebar<br>
Request URL: `https://x.com/i/api/graphql/HmbDwo1sohZhtwxTuWEr4w/ExploreSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/vEutMf9rimpMRXE7hcA0uw/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://x.com/i/api/graphql/kE3Z4FsCX3Igfo92AfLjLA/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://x.com/i/api/graphql/Jw8Gkemc3DMxVHz5dcwdWw/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## GenericTimelineById<br>
Request URL: `https://x.com/i/api/graphql/dqOVQ5zQw0zw5lQqiAvGSg/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GlobalCommunitiesLatestPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/slidOsoGZRZnQgqMBfYlCg/GlobalCommunitiesLatestPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GlobalCommunitiesPostSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/CYQBD5BmLA3sg5w7KpOb7g/GlobalCommunitiesPostSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://x.com/i/api/graphql/SPRenxTHTuP55m6j17ZghQ/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://x.com/i/api/graphql/kTpapPBq29WTffNLNjWutA/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://x.com/i/api/graphql/T7eJq_gXVKkxGBXa7NHbpQ/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://x.com/i/api/graphql/b879x8YaMhulpOT17r_3Xg/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MediaTabVideoMixer<br>
Request URL: `https://x.com/i/api/graphql/QPyf02CJLTfALGaKL_Mgfg/MediaTabVideoMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/tIEIxqiHgfErgnBh5Y89tA/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://x.com/i/api/graphql/epUPvXPCIByEaDbwO9i_-g/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## PaymentsUsersTypeahead<br>
Request URL: `https://x.com/i/api/graphql/AZURUk27ksncblQUCg6_Rw/PaymentsUsersTypeahead`<br>
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
Request URL: `https://x.com/i/api/graphql/zl1jxgu7LLbJApF1BZjWsQ/PinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/YurVqWpk90cTaQYxu_UC0Q/PinnedTimelines`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/o5fcb0IYqUf2bC8zuc30tA/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/kAOiXQQ5sBmabDI1pb9_Bg/SimilarPosts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://x.com/i/api/graphql/bDz3_QwyS7qszoJJBlhIxg/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/5GJ5Bvgv8BNalX7SBIuylw/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/qCqI5k2e2AI4GoI-2I7LAA/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/7pT2k70Fl7OlgAuQppgMAg/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://x.com/i/api/graphql/rwHXSmvQJgHJgiy7DTDpVQ/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://x.com/i/api/graphql/3__vWUzmPeXzbkMA47kGog/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrendHistory<br>
Request URL: `https://x.com/i/api/graphql/qVnGHzU8_LxelI2A3DJQsw/TrendHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TrendRelevantUsers<br>
Request URL: `https://x.com/i/api/graphql/9rRNYRi15t-jmV3HMKM0rw/TrendRelevantUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVHomeMixer<br>
Request URL: `https://x.com/i/api/graphql/qjcB_QJS9iACZj_AYrB-ZQ/TVHomeMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetDetail<br>
Request URL: `https://x.com/i/api/graphql/Vrkl31e9tzfybLjkgNUEmg/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/R6GplwGiXiKZpRHBkyukYA/TweetResultByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://x.com/i/api/graphql/ojqRcmSpUKZTi-md0ej6mA/TweetResultsByRestIds`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/mYj5TSPAEGtMbP7S_t-BXw/UnpinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/U4AmOKUoNtDGpvvUjCTKJg/Upsells`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                               | type    | variable   |
|:----------------------------------|:--------|:-----------|
| subscriptions_upsells_api_enabled | boolean | True       |

#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://x.com/i/api/graphql/e8Srh1DY1xcK6Qnv1Cy2Fg/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://x.com/i/api/graphql/q3Lw4Q0MLUKgkvk68c8dMw/UserArticlesTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://x.com/i/api/graphql/0ZkCwrwjBHroEmfF-gMs9A/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://x.com/i/api/graphql/ZaIR0zFoOtftpc1JMn7mXg/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/IHyLL37gkgw1TgIXAL6Wlw/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/zPbLjWmwpkOeME2ILnhwBg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://x.com/i/api/graphql/jE_R9GhtwupUqKwtg9QahQ/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://x.com/i/api/graphql/vD0tcQUj6haQizxKEc6NRA/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://x.com/i/api/graphql/8dtEhqk3EZYHZXTPJ9-peA/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/cl9awOb_EhdHF3ksJ8vNrg/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/fFz-WT-pOfH3XZ1FE0JWCg/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://x.com/i/api/graphql/p8aXzC3mi1Zjdv4H1E0O1Q/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://x.com/i/api/graphql/UAU-rlr1uBbAqCx7SpL4YQ/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://x.com/i/api/graphql/STYo0TGfVYsaMiRBQo4H4w/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UsersByScreenNames<br>
Request URL: `https://x.com/i/api/graphql/1TZhR3HdGV3Eys5kvidR8g/UsersByScreenNames`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| hidden_profile_subscriptions_enabled                              | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/ksXgYui6VaK-ri5gzhCKRw/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| subscriptions_upsells_api_enabled                                 | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://x.com/i/api/graphql/rU1PcXkbsJxidSz-aQi7yA/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceAddSharing<br>
Request URL: `https://x.com/i/api/graphql/yvmjWhVtcLfZIxUvhQcGWg/AudioSpaceAddSharing`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://x.com/i/api/graphql/xWDZQaBbymqJpmJ6C1viiw/AudioSpaceById`<br>
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
| spaces_2022_h2_spaces_communities                                       | boolean | True       |
| spaces_2022_h2_clipping                                                 | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
## CombinedLists<br>
Request URL: `https://x.com/i/api/graphql/9D1wJAT__4z_FBXBRo_bng/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://x.com/i/api/graphql/hUTiGU_nOa2BYQKDR0exAA/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://x.com/i/api/graphql/5cOWaNxR8d0oljljVB-7DA/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://x.com/i/api/graphql/ZvKab44mTYPKerJj2EUFOg/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://x.com/i/api/graphql/J58Of9ptO6Vknj62Yr35gw/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://x.com/i/api/graphql/BMdgNlyXbkaMoLTQLpB-SQ/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://x.com/i/api/graphql/kw3S5EE90GPppYM3FYiEOw/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/u58tNZHDoVhAbj9Zm_iJXw/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/jA2asPaj8O5cSy9Zp6cmsQ/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key            | type   | variable   |
|:---------------|:-------|:-----------|
| conversationId | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://x.com/i/api/graphql/IYkDLLiyDG8O3Vd6913t2Q/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://x.com/i/api/graphql/z9afkl-utUiC9JmtjnHV_Q/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/mSLoSayo2UCBUyFF7HZm2g/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://x.com/i/api/graphql/x14Jwzvk9lXzOEeaHhF-Vg/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/7Z0xzqoo-Iv3roEoNOXDdQ/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://x.com/i/api/graphql/65ifFtqo5UHU32fUahZrxg/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://x.com/i/api/graphql/cfQUR9LYlRq1Tanv4ogFtA/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://x.com/i/api/graphql/pGxPBCTUNbqfBmYZrp_qZQ/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/DkwoON2eS6R6Vm-Qiog9xw/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://x.com/i/api/graphql/lwVW_MRJoYJpaTZMDKB6zw/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...()(0,i.d) | ...    | _          |

#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://x.com/i/api/graphql/VkuU9vcNhPxQZlzihZ2IYQ/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/61Nxy_Aw8e96FN8wW2jKAQ/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## CommunitiesExploreTimeline<br>
Request URL: `https://x.com/i/api/graphql/RG4mGNHKeNF7Yd_CpuD-eA/CommunitiesExploreTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://x.com/i/api/graphql/WjQzzZcFzvPbYMEC7hSYGQ/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://x.com/i/api/graphql/EeJmOnPkdOak2TqE61nemQ/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://x.com/i/api/graphql/CPTy16qOKdXj7xp8-Na1lQ/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://x.com/i/api/graphql/yXUwdo47Y2u8fBqRnrvJOg/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://x.com/i/api/graphql/HCsnQRzb92O_yErsHJNrSw/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://x.com/i/api/graphql/uaPexJcdODRHejf0e-USQw/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://x.com/i/api/graphql/OWxm5IqOuq_jRPbNLS7ATg/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://x.com/i/api/graphql/V_4VbOYZ2Slv6XgsROUgbw/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/9hXk-zS4TRhUkk7ri9MJeg/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://x.com/i/api/graphql/e3v2BstDksc0-djiBLJfbw/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://x.com/i/api/graphql/IdowT-jqYoK6QzcRWnAQ4w/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditQuestion<br>
Request URL: `https://x.com/i/api/graphql/puQcOKD01rx__r_vfPjAdA/CommunityEditQuestion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://x.com/i/api/graphql/Bf2YCRbbHhszPYOb2X3QSA/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://x.com/i/api/graphql/IuR0iqGMpRzRMMaK_Cg0NQ/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://x.com/i/api/graphql/sdQtGmdNfPwhN0FkBFGVjg/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/rylcLRRbgyYOSU2Ja5SeeQ/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://x.com/i/api/graphql/quQU4fIRAQTzJ4y1DERLRg/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityMediaLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/fbyNG99Cuw6rosJ5GOTXQg/CommunityMediaLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://x.com/i/api/graphql/PyP2EKnfiKX-joyg7dnWEw/CommunityMediaTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://x.com/i/api/graphql/k9p-dxfeT7z7VcqFBPiUgw/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://x.com/i/api/graphql/lnQboRvn2dlHfuO3UUtI4g/CommunityModerationTweetCasesSlice`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://x.com/i/api/graphql/4ax2xADjJBW6SD-vTYT6JQ/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://x.com/i/api/graphql/ZpmsEcsOXST7OhWC3tyDkA/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://x.com/i/api/graphql/FQclQmQtTkrlXDe9m8OTfQ/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://x.com/i/api/graphql/Bqu3IL7-OzJhn86UhspXOA/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## CommunityTweetModerationLogSlice<br>
Request URL: `https://x.com/i/api/graphql/-ERS7y1FUvbvqRcrTCtwlw/CommunityTweetModerationLogSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/ob5i3we2XL53QU6cDdZbqQ/CommunityTweetsLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://x.com/i/api/graphql/MmAd0KNaaZVTLRWoaL_Yzw/CommunityTweetsRankedLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/IhLdbTuY44S4MTCF5gib5g/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://x.com/i/api/graphql/EhN3IlsH_Uo4ZVSmyBCMAQ/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
## CommunitiesRankedTimeline<br>
Request URL: `https://x.com/i/api/graphql/kxqkaMISRbmetW0NJwLLVg/CommunitiesRankedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/wMeA2oqn69Qjto1AX6pIIQ/FetchDraftTweets`<br>
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
Request URL: `https://x.com/i/api/graphql/UtDUBQrevIwphY7mzPj3IQ/FetchScheduledTweets`<br>
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
Request URL: `https://x.com/i/api/graphql/vQjWKrakVpP1LV4jSX0Pig/BirdwatchFetchAuthenticatedBirdwatchMatchSlice`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchContributorNotesSlice<br>
Request URL: `https://x.com/i/api/graphql/lNwF6DNVlfGOuDUnah7-2A/BirdwatchFetchContributorNotesSlice`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/PvSK35com_c1weGyyC0UgA/BirdwatchCreateNote`<br>
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
| responsive_web_grok_community_note_translation_is_enabled         | boolean | False      |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled    | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchCreateRating<br>
Request URL: `https://x.com/i/api/graphql/e3UGQnUm1M3BSDUgUt4oHA/BirdwatchCreateRating`<br>
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
## BirdwatchFetchGlobalTimeline<br>
Request URL: `https://x.com/i/api/graphql/TWW6hSz5jtZEqCcakQz2Tg/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNoteTranslation<br>
Request URL: `https://x.com/i/api/graphql/3JGQA2d3yYTakWz2-VtcZw/BirdwatchFetchNoteTranslation`<br>
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
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://x.com/i/api/graphql/2YbknhtutZWw5C5h2wDooA/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| responsive_web_birdwatch_enforce_author_user_quotas               | boolean | True       |
| responsive_web_birdwatch_media_notes_enabled                      | boolean | True       |
| responsive_web_birdwatch_url_notes_enabled                        | boolean | False      |
| responsive_web_grok_community_note_translation_is_enabled         | boolean | False      |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled    | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://x.com/i/api/graphql/3XEJutxychLpIlpEk5cXXw/BirdwatchFetchOneNote`<br>
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
| responsive_web_grok_community_note_translation_is_enabled         | boolean | False      |
| responsive_web_birdwatch_fast_notes_badge_enabled                 | boolean | False      |
| responsive_web_grok_community_note_auto_translation_is_enabled    | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/sNgcG-_xNW9-JLf5YyfcCA/BirdwatchFetchSourceLinkSlice`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/Olw-OJOhKTC30FzvBW4Lbg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/FiBK5AU13TfLV9K0R_rQ2w/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
## GrokConversationItemsByRestId<br>
Request URL: `https://x.com/i/api/graphql/b5KcXWCNr_I_O-m7_WjKBA/GrokConversationItemsByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/ZYQK0wvMfoTAwGTKIu71zQ/GrokHome`<br>
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
Request URL: `https://x.com/i/api/graphql/gxbY2KieRwxhs7i8Km5Ixw/GrokShare`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/tqY-LSUu1Br5lXcnaXGOHw/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveProfile<br>
Request URL: `https://x.com/i/api/graphql/ywiAUHqfsK823_t7IUrpLA/ImmersiveProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVTrend<br>
Request URL: `https://x.com/i/api/graphql/rcx6pxMcTziRuRydZ-s7hQ/TVTrend`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TVUserProfile<br>
Request URL: `https://x.com/i/api/graphql/WsnXcsydgfblEoGjbtV04g/TVUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| rweb_video_screen_enabled                                               | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetRelatedVideos<br>
Request URL: `https://x.com/i/api/graphql/-6sqIZOslzsPyHLeMlR0hA/TweetRelatedVideos`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## NotificationsTimeline<br>
Request URL: `https://x.com/i/api/graphql/Jizym-xYEiKIUsJ0xn6hFg/NotificationsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## SubscriptionCheckoutUrlWithEligibility<br>
Request URL: `https://x.com/i/api/graphql/-kH-xt82ZhKnAMTXv1Fuzg/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/yIGOH-WMQSU-AdbfVRZm9A/SubscriptionProductDetails`<br>
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
Request URL: `https://x.com/i/api/graphql/NEMw3cw4v0-Oo-nTMI8reQ/SwitchTier`<br>
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
Request URL: `https://x.com/i/api/graphql/Olw-OJOhKTC30FzvBW4Lbg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/FiBK5AU13TfLV9K0R_rQ2w/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/fl4oqe0ZsuqPBjfOCH5SWQ/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_grok_image_annotation_enabled                      | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/FTQHoYhR32I56JLHcftc8g/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/b5KcXWCNr_I_O-m7_WjKBA/GrokConversationItemsByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/ZYQK0wvMfoTAwGTKIu71zQ/GrokHome`<br>
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
Request URL: `https://x.com/i/api/graphql/gxbY2KieRwxhs7i8Km5Ixw/GrokShare`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## ArticleTimeline<br>
Request URL: `https://x.com/i/api/graphql/LsarpG-hv4BZC3J09kid5w/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://x.com/i/api/graphql/RgF6ogCrylwhL--cRgWd3w/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/Olw-OJOhKTC30FzvBW4Lbg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/FiBK5AU13TfLV9K0R_rQ2w/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/59ltWnIdjLJmhOgcgTF3Gg/AiTrendByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| premium_content_api_read_enabled                                        | boolean | False      |
| communities_web_enable_tweet_community_results_fetch                    | boolean | True       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | True       |
| responsive_web_grok_analyze_button_fetch_trends_enabled                 | boolean | False      |
| responsive_web_grok_analyze_post_followups_enabled                      | boolean | False      |
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/TvFMyNDWWtwmv2_ezCyZ8w/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/i2Z_t0UQZhmylm3h9hGYTg/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/OFRzhLDq2vuXmX53Hkko1A/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/H9s2G_pxsLeXZ_dOwr3KkA/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/sJRQivNUklhzx6dGGwNOGw/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/EoI7bGdg2WjHKBCmx-8I7w/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/AUGlhvOeVE6_xzESTisN0g/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/rwdN3ccamfl8uWHRhTEANw/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

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
## DmAllSearchSlice<br>
Request URL: `https://x.com/i/api/graphql/fl4oqe0ZsuqPBjfOCH5SWQ/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_grok_image_annotation_enabled                      | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/FTQHoYhR32I56JLHcftc8g/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/b5KcXWCNr_I_O-m7_WjKBA/GrokConversationItemsByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/ZYQK0wvMfoTAwGTKIu71zQ/GrokHome`<br>
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
Request URL: `https://x.com/i/api/graphql/gxbY2KieRwxhs7i8Km5Ixw/GrokShare`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## SubscriptionCheckoutUrlWithEligibility<br>
Request URL: `https://x.com/i/api/graphql/-kH-xt82ZhKnAMTXv1Fuzg/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/yIGOH-WMQSU-AdbfVRZm9A/SubscriptionProductDetails`<br>
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
Request URL: `https://x.com/i/api/graphql/NEMw3cw4v0-Oo-nTMI8reQ/SwitchTier`<br>
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
Request URL: `https://x.com/i/api/graphql/b5KcXWCNr_I_O-m7_WjKBA/GrokConversationItemsByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/ZYQK0wvMfoTAwGTKIu71zQ/GrokHome`<br>
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
Request URL: `https://x.com/i/api/graphql/gxbY2KieRwxhs7i8Km5Ixw/GrokShare`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/-kH-xt82ZhKnAMTXv1Fuzg/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/yIGOH-WMQSU-AdbfVRZm9A/SubscriptionProductDetails`<br>
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
Request URL: `https://x.com/i/api/graphql/NEMw3cw4v0-Oo-nTMI8reQ/SwitchTier`<br>
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
Request URL: `https://x.com/i/api/graphql/-kH-xt82ZhKnAMTXv1Fuzg/SubscriptionCheckoutUrlWithEligibility`<br>
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
Request URL: `https://x.com/i/api/graphql/yIGOH-WMQSU-AdbfVRZm9A/SubscriptionProductDetails`<br>
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
Request URL: `https://x.com/i/api/graphql/NEMw3cw4v0-Oo-nTMI8reQ/SwitchTier`<br>
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
Request URL: `https://x.com/i/api/graphql/WA8W4-Ph-LVJQUCb5g2nEw/SidebarUserRecommendations`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://x.com/i/api/graphql/D1a15fRsmitdfrc3Ci5JMA/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/D483nsMMRRpAaJo4BvQXcA/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/_4cCVD9onCLI5F88Q97psg/TweetEditHistory`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_screen_enabled                                               | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://x.com/i/api/graphql/D1a15fRsmitdfrc3Ci5JMA/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://x.com/i/api/graphql/D483nsMMRRpAaJo4BvQXcA/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://x.com/i/api/graphql/_4cCVD9onCLI5F88Q97psg/TweetEditHistory`<br>
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
| responsive_web_jetfuel_frame                                            | boolean | True       |
| responsive_web_grok_share_attachment_enabled                            | boolean | True       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| rweb_video_screen_enabled                                               | boolean | False      |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/b5KcXWCNr_I_O-m7_WjKBA/GrokConversationItemsByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/ZYQK0wvMfoTAwGTKIu71zQ/GrokHome`<br>
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
Request URL: `https://x.com/i/api/graphql/gxbY2KieRwxhs7i8Km5Ixw/GrokShare`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/Olw-OJOhKTC30FzvBW4Lbg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/FiBK5AU13TfLV9K0R_rQ2w/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## BookmarkFolderTimeline<br>
Request URL: `https://x.com/i/api/graphql/Olw-OJOhKTC30FzvBW4Lbg/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
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
Request URL: `https://x.com/i/api/graphql/FiBK5AU13TfLV9K0R_rQ2w/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| rweb_video_screen_enabled                                               | boolean | False      |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/b5KcXWCNr_I_O-m7_WjKBA/GrokConversationItemsByRestId`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
Request URL: `https://x.com/i/api/graphql/ZYQK0wvMfoTAwGTKIu71zQ/GrokHome`<br>
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
Request URL: `https://x.com/i/api/graphql/gxbY2KieRwxhs7i8Km5Ixw/GrokShare`<br>
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
| articles_preview_enabled                                                | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | True       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | True       |
| tweet_awards_web_tipping_enabled                                        | boolean | False      |
| responsive_web_grok_show_grok_translated_post                           | boolean | False      |
| responsive_web_grok_analysis_button_from_backend                        | boolean | False      |
| creator_subscriptions_quote_tweet_preview_enabled                       | boolean | False      |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | True       |
| longform_notetweets_rich_text_read_enabled                              | boolean | True       |
| longform_notetweets_inline_media_enabled                                | boolean | True       |
| payments_enabled                                                        | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled                    | boolean | True       |
| rweb_tipjar_consumption_enabled                                         | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_grok_image_annotation_enabled                            | boolean | True       |
| responsive_web_grok_community_note_auto_translation_is_enabled          | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

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
## ArticleEntitiesSlice<br>
Request URL: `https://x.com/i/api/graphql/TvFMyNDWWtwmv2_ezCyZ8w/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
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
Request URL: `https://x.com/i/api/graphql/i2Z_t0UQZhmylm3h9hGYTg/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://x.com/i/api/graphql/OFRzhLDq2vuXmX53Hkko1A/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://x.com/i/api/graphql/H9s2G_pxsLeXZ_dOwr3KkA/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://x.com/i/api/graphql/sJRQivNUklhzx6dGGwNOGw/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://x.com/i/api/graphql/EoI7bGdg2WjHKBCmx-8I7w/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://x.com/i/api/graphql/AUGlhvOeVE6_xzESTisN0g/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://x.com/i/api/graphql/rwdN3ccamfl8uWHRhTEANw/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
## SidebarUserRecommendations<br>
Request URL: `https://x.com/i/api/graphql/WA8W4-Ph-LVJQUCb5g2nEw/SidebarUserRecommendations`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | variable   |
|:------------------------------------------------------------------|:--------|:-----------|
| payments_enabled                                                  | boolean | False      |
| profile_label_improvements_pcf_label_in_post_enabled              | boolean | True       |
| rweb_tipjar_consumption_enabled                                   | boolean | True       |
| verified_phone_label_enabled                                      | boolean | False      |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | True       |

#### queryId<br>
`None`<br>
