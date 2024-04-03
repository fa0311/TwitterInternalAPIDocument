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
Request URL: `https://twitter.com/i/api/graphql/nxSG4eYi--0b87DwfO-okw/BlockedAccountsAll`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## BlockedAccountsAutoBlock<br>
Request URL: `https://twitter.com/i/api/graphql/I1ZEkV49X0P-lu4M24tMfA/BlockedAccountsAutoBlock`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## BlockedAccountsImported<br>
Request URL: `https://twitter.com/i/api/graphql/gz6NMOxjSBBTHZfrRQ5PwQ/BlockedAccountsImported`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## BlueVerifiedFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/r6GvSZe482ka6Jx6biiSLg/BlueVerifiedFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityMemberRelationshipTypeahead<br>
Request URL: `https://twitter.com/i/api/graphql/_h1cVpB5J1-jg2iU8uv6bw/CommunityMemberRelationshipTypeahead`<br>
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
Request URL: `https://twitter.com/i/api/graphql/ZqX6ivkf1G5EqRw12ZJ30w/CommunityUserRelationshipTypeahead`<br>
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
Request URL: `https://twitter.com/i/api/graphql/3vmhNhCPXcUOcsD4WBX--A/ConnectTabTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/uaSYozkLvtGu160F7t3Bcg/CreateNoteTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/-3UcjnwU3eTckbhxoOPJjg/CreateTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CreatorSubscriptionsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/ueTi2zPrANkwC6ct0jLeyg/CreatorSubscriptionsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/F_d_W0FOTzWiKb86rs_jrQ/ExplorePage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/dmd4bcFlD-lggjAeLxh9Wg/Followers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## FollowersYouKnow<br>
Request URL: `https://twitter.com/i/api/graphql/0C5j-z-I0hXSRe4xlop6MQ/FollowersYouKnow`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## Following<br>
Request URL: `https://twitter.com/i/api/graphql/WgjYKVZDew7yLCPt1h5w3g/Following`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## GenericTimelineById<br>
Request URL: `https://twitter.com/i/api/graphql/vJic3l3zrxFRBugioXWlCQ/GenericTimelineById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## HomeLatestTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/x8cw2DejWgTiItCF7ePoAw/HomeLatestTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## HomeTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/a-K3Ib4ROCtNY8GZC9GJ7w/HomeTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## Likes<br>
Request URL: `https://twitter.com/i/api/graphql/p19VXUX6-JPMC50YaVhVsg/Likes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListSearchTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/gQ9b3Em3vI87Mvrq-Umo4Q/ListSearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/rYY3LE40kXeWWgEYgGU4fQ/ModeratedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## MutedAccounts<br>
Request URL: `https://twitter.com/i/api/graphql/49OBP7Oi_1pLoD7XElu7Ag/MutedAccounts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## PinTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/iJn3WyDOHDmZWYBMDXFD5A/PinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## PinTweet<br>
Request URL: `https://twitter.com/i/api/graphql/VIHsNu89pK-kW35JpHq7Xw/PinTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/jhQR0wHkD0C3HPVJipWVJA/PinnedTimelines`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/2ZxQwqrH2gyQZzU5Jcvpxw/SearchTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/4PnykkJrqQy2YJboMLF35Q/SimilarPosts`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## SuperFollowers<br>
Request URL: `https://twitter.com/i/api/graphql/sGfRomQn0UnGGp_6-wtjhA/SuperFollowers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/8g1PCkG0A63zUP5pYhqb5Q/TopicLandingPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/Gk-7KCZNMIsEwDP5tD8LUw/TopicToFollowSidebar`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/Vuq_FzN43t4sRYDj8sLdbQ/TopicsManagementPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## TopicsPickerPage<br>
Request URL: `https://twitter.com/i/api/graphql/TLCxI4CHSfLi6e80HxovJg/TopicsPickerPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## TopicsPickerPageById<br>
Request URL: `https://twitter.com/i/api/graphql/pPX-KkVvaE5JS5tuCueMww/TopicsPickerPageById`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
## TweetDetail<br>
Request URL: `https://twitter.com/i/api/graphql/nz90rnWCU72rA6b0KwUIow/TweetDetail`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## TweetResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/7ieDirzd5dipfzjuv3VSmw/TweetResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## TweetResultsByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/r7W4IlnOGSnZl7vG1MfoUw/TweetResultsByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/5WE81TO98pARQzpLIVUtmw/UnpinTimeline`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## UnpinTweet<br>
Request URL: `https://twitter.com/i/api/graphql/BhKei844ypCyLYCg0nwigw/UnpinTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/YUUFGu66K-zP0eYoGK4wFQ/UpdatePinnedTimelines`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## UrtFixtures<br>
Request URL: `https://twitter.com/i/api/graphql/EMpwdTHkrc9zpEvRjil4Gg/UrtFixtures`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/VHeVbuMhpcQLQxz-EkBaVw/UserAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserArticlesTweets<br>
Request URL: `https://twitter.com/i/api/graphql/AjzRYOgHrOvtC_BHyCImMQ/UserArticlesTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserBusinessProfileTeamTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/CGG0Mo58GN-8j5IqbJvrxg/UserBusinessProfileTeamTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/BNfUANkqWTZZdOE4xnhPiQ/UserByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| hidden_profile_likes_enabled                                      | boolean |          1 | nan       |
| hidden_profile_subscriptions_enabled                              | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| highlights_tweets_tab_ui_enabled                                  | boolean |          1 | nan       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |

#### queryId<br>
`None`<br>
## UserByScreenName<br>
Request URL: `https://twitter.com/i/api/graphql/qW5u-DAuXpMEG0zA1F7UGQ/UserByScreenName`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| hidden_profile_likes_enabled                                      | boolean |          1 | nan       |
| hidden_profile_subscriptions_enabled                              | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| subscriptions_verification_info_is_identity_verified_enabled      | boolean |          1 | nan       |
| subscriptions_verification_info_verified_since_enabled            | boolean |          1 | nan       |
| highlights_tweets_tab_ui_enabled                                  | boolean |          1 | nan       |
| responsive_web_twitter_article_notes_tab_enabled                  | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/GXBVLS10uu44npd36Oc-Dg/UserCreatorSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserCreatorSubscriptions<br>
Request URL: `https://twitter.com/i/api/graphql/JMQ0Oc7FzBeZkTJTxlZIJg/UserCreatorSubscriptions`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserHighlightsTweets<br>
Request URL: `https://twitter.com/i/api/graphql/ba1izzveLaWniQuW4pGGmA/UserHighlightsTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserMedia<br>
Request URL: `https://twitter.com/i/api/graphql/3-viBY0wVGpDCI818H_D5Q/UserMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/FDeP8_L9GCXdinTi1bN0eQ/UserPromotableTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/kpWy4-dDIbyDb0Z0RUhaxw/UserSuperFollowTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserTweets<br>
Request URL: `https://twitter.com/i/api/graphql/LxVacKhIjjbWHu1DxjMvsQ/UserTweets`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| userId                 | ...     | t.userId   |
| withVoice              | boolean | False      |
| count                  | ...     | 1          |
| includePromotedContent | boolean | False      |

#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UserTweetsAndReplies<br>
Request URL: `https://twitter.com/i/api/graphql/zddni7Ab5g_nl1jZalub5w/UserTweetsAndReplies`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## UsersByRestIds<br>
Request URL: `https://twitter.com/i/api/graphql/9UCmrCOmAn6TYy_Y13cSjA/UsersByRestIds`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/-876iyxD1O_0X0BqeykjZA/Viewer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                   | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ViewerTeams<br>
Request URL: `https://twitter.com/i/api/graphql/vbxJq7fg8J_92hVmiTnt3Q/ViewerTeams`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ViewingOtherUsersTopicsPage<br>
Request URL: `https://twitter.com/i/api/graphql/42ln3Z9hahW_OgXRopXynw/ViewingOtherUsersTopicsPage`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## AudioSpaceAddSharing<br>
Request URL: `https://twitter.com/i/api/graphql/iWrnmHikn_brZGG228r6Xw/AudioSpaceAddSharing`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## AudioSpaceById<br>
Request URL: `https://twitter.com/i/api/graphql/BlVQRI1BWqh27wknoN2wmA/AudioSpaceById`<br>
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
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## AuthenticatedUserTFLists<br>
Request URL: `https://twitter.com/i/api/graphql/QjN8ZdavFDqxUjNn3r9cig/AuthenticatedUserTFLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CommunitiesExploreTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/9FWjORHBuJAzRcimO08nEA/CommunitiesExploreTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunitiesMainDiscoveryModule<br>
Request URL: `https://twitter.com/i/api/graphql/5vJLxYiK3QVAmO70pZqCIA/CommunitiesMainDiscoveryModule`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunitiesMainPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/LulzpiBpytqbH4C7Ps6PpA/CommunitiesMainPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsSlice<br>
Request URL: `https://twitter.com/i/api/graphql/Aq9i_scYFxxgl0fD2cejnw/CommunitiesMembershipsSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunitiesMembershipsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/nH9-1IxDVdmNXypPusIVJA/CommunitiesMembershipsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityAboutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/4NSbRXJnInPvdQP6P5Hwug/CommunityAboutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CreateCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/2meBAYMbkMEaH5LFy6TW9w/CreateCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityCreateRule<br>
Request URL: `https://twitter.com/i/api/graphql/JHcO_L-194IX0fBQLGaTyg/CommunityCreateRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityDiscoveryTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/OUimIDdpxJt8e3quvT5QYg/CommunityDiscoveryTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityEditBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/nUkSg6srPhnERNZmU5BG5w/CommunityEditBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityEditName<br>
Request URL: `https://twitter.com/i/api/graphql/VoJIpk4IBqjTGYJED1QQAw/CommunityEditName`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityEditPurpose<br>
Request URL: `https://twitter.com/i/api/graphql/MtDYcO4LgJsxRf9J2M-5xw/CommunityEditPurpose`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityEditQuestion<br>
Request URL: `https://twitter.com/i/api/graphql/Gi26suJlIPJjULU47IX3eA/CommunityEditQuestion`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityEditRule<br>
Request URL: `https://twitter.com/i/api/graphql/QoiESR0ItvcMT5TNZspDew/CommunityEditRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/LDh2j3Z83EEbKiXOqpA51A/CommunityByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityHashtagsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/WXR5qbSLOqVx7WVvxyoQsg/CommunityHashtagsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## JoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/xZQLbDwbI585YTG0QIpokw/JoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## LeaveCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/OoS6Kd4-noNLXPZYHtygeA/LeaveCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityMediaLoggedOutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/YNMIg_nb3nkKBKo52uwRvg/CommunityMediaLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityMediaTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/l-g3wjA0mtXHwdwEGs0mmg/CommunityMediaTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityModerationKeepTweet<br>
Request URL: `https://twitter.com/i/api/graphql/SUmBZEHQZUgOXHNp3CbM6A/CommunityModerationKeepTweet`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityModerationTweetCasesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/1kXvVTp-VqWEl8ajDoqDKA/CommunityModerationTweetCasesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## CommunityRemoveBannerMedia<br>
Request URL: `https://twitter.com/i/api/graphql/t68d-P1q4885Qk-xcnU4Sw/CommunityRemoveBannerMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityRemoveRule<br>
Request URL: `https://twitter.com/i/api/graphql/8jDkMYq2VaS9Zm4sgleNKw/CommunityRemoveRule`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityReorderRules<br>
Request URL: `https://twitter.com/i/api/graphql/JaJQQZdvgHTRU8NgDsuX0w/CommunityReorderRules`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## RequestToJoinCommunity<br>
Request URL: `https://twitter.com/i/api/graphql/XwWChphD_6g7JnsFus2f2Q/RequestToJoinCommunity`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityTweetsLoggedOutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/BAWSkSaTFygexuuM7mwcUg/CommunityTweetsLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityTweetsRankedLoggedOutTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/3W5qGRu5nNmvz4KHXDCxVA/CommunityTweetsRankedLoggedOutTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/DxqKKVSdF4P5VPnFAuhadw/CommunityTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## CommunityUpdateRole<br>
Request URL: `https://twitter.com/i/api/graphql/iY1oiH1t6MnFrIES81Um2A/CommunityUpdateRole`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CommunityUserInvite<br>
Request URL: `https://twitter.com/i/api/graphql/pbeAbOjoklMKc0UV9mbsIA/CommunityUserInvite`<br>
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
## CreateDraftTweet<br>
Request URL: `https://twitter.com/i/api/graphql/cH9HZWz_EW9gnswvA4ZRiQ/CreateDraftTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/LCVzRQGxOaGnOnYH01NQXg/CreateScheduledTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/2tP8XUYeLHKjq5RHvuvpZw/CreateTrustedFriendsList`<br>
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
Request URL: `https://twitter.com/i/api/graphql/bkh9G3FGgTldS9iTKWWYYw/DeleteDraftTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/CTOVqej0JBXAZSwkp1US0g/DeleteScheduledTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/JIeXE-I6BZXHfxsgOkyHYQ/EditDraftTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/_mHkQ5LHpRRjSXKOcG6eZw/EditScheduledTweet`<br>
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
Request URL: `https://twitter.com/i/api/graphql/fMp3izG_gCZKVk3Aa1vVKw/FetchDraftTweets`<br>
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
Request URL: `https://twitter.com/i/api/graphql/ITtjAzvlZni2wWXwf295Qg/FetchScheduledTweets`<br>
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
## CombinedLists<br>
Request URL: `https://twitter.com/i/api/graphql/RQUrXp0U3EHh1bzPHD36vQ/CombinedLists`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListAddMember<br>
Request URL: `https://twitter.com/i/api/graphql/FpvDMFk4k8HXtkYjQGg_bw/ListAddMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## DeleteListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/RvTvAa5lxD80c-1V5Kc_GQ/DeleteListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## EditListBanner<br>
Request URL: `https://twitter.com/i/api/graphql/vEdHEoAaZZ6B3zJC0AAt4w/EditListBanner`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ListBySlug<br>
Request URL: `https://twitter.com/i/api/graphql/PlvgbIjXrPvBKGPVLUN55Q/ListBySlug`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## CreateList<br>
Request URL: `https://twitter.com/i/api/graphql/P51ZB9632Fy0Cv3LdqMNwg/CreateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ListCreationRecommendedUsers<br>
Request URL: `https://twitter.com/i/api/graphql/VLlFAhksracM0Ro2enrDmw/ListCreationRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MCGMbvsyFFWmfQs1ogJv0w/ListEditRecommendedUsers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListLatestTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/VOjXG8rjY9eBKL46Te9QuQ/ListLatestTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListMembers<br>
Request URL: `https://twitter.com/i/api/graphql/X-kRUdWD8EZI3THAm1V9Fg/ListMembers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListMemberships<br>
Request URL: `https://twitter.com/i/api/graphql/iy9AOUluCa7mXR3-CJCKjw/ListMemberships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/dgAnn6VQ4UWtq5FyyQ2dkw/ListOwnerships`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/ZMQOSpxDo0cP5Cdt8MgEVA/ListByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ListRankedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/bLG0E95yze595TalrKdG8w/ListRankedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListRemoveMember<br>
Request URL: `https://twitter.com/i/api/graphql/q1fNhjkWDJWoHTtsToP0CQ/ListRemoveMember`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ListSubscribe<br>
Request URL: `https://twitter.com/i/api/graphql/0nDMiT68xhXJI0uaQvKMTQ/ListSubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ListSubscribers<br>
Request URL: `https://twitter.com/i/api/graphql/My-MnFTzsmSv3EFqFQtZXw/ListSubscribers`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/yYYhFnbtydvQGf17qKfJkg/ListUnsubscribe`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## UpdateList<br>
Request URL: `https://twitter.com/i/api/graphql/bYkQRsxcmEm_YSpiMusY2g/UpdateList`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ListsDiscovery<br>
Request URL: `https://twitter.com/i/api/graphql/hnq5LTumAe_5j21yRQDf4g/ListsDiscovery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ListsManagementPageTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Ggby2HzzkYmvsCbZBXLteQ/ListsManagementPageTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/6dZJZQtHgz4A4i4N4xgf8Q/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MW5ifCoKJeYXvNuiUzYeGQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
## BroadcastQuery<br>
Request URL: `https://twitter.com/i/api/graphql/JbPqxAW5ti2Ccb5xnYpG1A/BroadcastQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/6dZJZQtHgz4A4i4N4xgf8Q/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MW5ifCoKJeYXvNuiUzYeGQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/C9lA1SVoKbH2GAa-GmJB1w/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_timestamps_enabled                                     | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/wIij_QApXqmRCktEDiq-ug/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/3J8UWw3qmSHbFO8A1QlmaQ/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/nZbnIY2Dpe4iQo8jtYOQqw/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MEcRwiHVOMpvVuM58JU29Q/BirdwatchFetchContributorNotesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_media_notes_enabled                            | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/7PHGVGPqFBbCUmC3YwI-Ew/BirdwatchCreateNote`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/mcG9ngPg9c12Ax0VYB6BMA/BirdwatchFetchGlobalTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## BirdwatchFetchNotes<br>
Request URL: `https://twitter.com/i/api/graphql/IRht0GVMIONwn55yLU9SZg/BirdwatchFetchNotes`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## BirdwatchFetchOneNote<br>
Request URL: `https://twitter.com/i/api/graphql/fKWPPj271aTM-AB9Xp48IA/BirdwatchFetchOneNote`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| responsive_web_birdwatch_media_notes_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/6dZJZQtHgz4A4i4N4xgf8Q/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MW5ifCoKJeYXvNuiUzYeGQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/6dZJZQtHgz4A4i4N4xgf8Q/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MW5ifCoKJeYXvNuiUzYeGQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/JbPqxAW5ti2Ccb5xnYpG1A/BroadcastQuery`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## AiTrendByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/yhirOc0b9qY71SK_8nNI3g/AiTrendByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

#### queryId<br>
`None`<br>
## ReportTrend<br>
Request URL: `https://twitter.com/i/api/graphql/3BZlCEmD645zQ-MpJM19CA/ReportTrend`<br>
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
Request URL: `https://twitter.com/i/api/graphql/_fJD2rm-lJI06lKxbUZT2Q/SaveTrend`<br>
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
Request URL: `https://twitter.com/i/api/graphql/yW-x_9qC1kTGnSVeAcy4QQ/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/JwLRVIs5Wt9_ci8RGYN6kw/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://twitter.com/i/api/graphql/O8a8X1HbrcrW8lUk9mvekg/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/Vj9iHq_4C-UQ-8ObgIFSxw/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://twitter.com/i/api/graphql/qJh1IbCjoouckPeDUzvljQ/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://twitter.com/i/api/graphql/hQOlHsanFNXl57VLZrvp7A/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://twitter.com/i/api/graphql/FgBTuAA6LHms8U18_N7ArA/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/NM8FFV_5VUigi1xfAI3F9g/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## DmAllSearchSlice<br>
Request URL: `https://twitter.com/i/api/graphql/C9lA1SVoKbH2GAa-GmJB1w/DmAllSearchSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    |   variable | default   |
|:------------------------------------------------------------------|:--------|-----------:|:----------|
| rweb_video_timestamps_enabled                                     | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                   | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                  | boolean |          1 | nan       |
| verified_phone_label_enabled                                      | boolean |          0 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                | boolean |          1 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/wIij_QApXqmRCktEDiq-ug/DmMutedTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/-u4at1S61H7uTLcPKtdEtw/GrokShare`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/Wwi8S0K3aH8hPFg2ehAozA/RitoActionedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## RitoFlaggedTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/dP1TuM_ahZ57FWRjS80mSw/RitoFlaggedTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/AwzZN5KvBdmjKJALpAX_SQ/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type   | variable                     |
|:----------------|:-------|:-----------------------------|
| pinned_tweet_id | ...    | (optional) t.pinned_tweet_id |
| page_name       | ...    | (optional) t.page_name       |
| ...()(0,_.d)    | ...    | _                            |

#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ImmersiveProfile<br>
Request URL: `https://twitter.com/i/api/graphql/COnUmSTcSKn3exqxCad3rA/ImmersiveProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type   | variable                     |
|:----------------|:-------|:-----------------------------|
| pinned_tweet_id | ...    | (optional) t.pinned_tweet_id |
| ...()(0,_.d)    | ...    | _                            |

#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## Favoriters<br>
Request URL: `https://twitter.com/i/api/graphql/U6ntA5s58aorF648jf4x2Q/Favoriters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## Retweeters<br>
Request URL: `https://twitter.com/i/api/graphql/mpmocZPG9sAl3NbT6Udckg/Retweeters`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## TweetEditHistory<br>
Request URL: `https://twitter.com/i/api/graphql/E-qm6rqt9YlnyIHAwk1hUw/TweetEditHistory`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
## TVHomeMixer<br>
Request URL: `https://twitter.com/i/api/graphql/-7eQC1DGxdKlAiZfHOtzzA/TVHomeMixer`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## TVUserProfile<br>
Request URL: `https://twitter.com/i/api/graphql/2lC6YkhZWMgNxjSfRaCvvA/TVUserProfile`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## TweetRelatedVideos<br>
Request URL: `https://twitter.com/i/api/graphql/h9ARxYfawy0SXIP9L11ecQ/TweetRelatedVideos`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/6dZJZQtHgz4A4i4N4xgf8Q/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MW5ifCoKJeYXvNuiUzYeGQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
## SidebarUserRecommendations<br>
Request URL: `https://twitter.com/i/api/graphql/jTviiQMKeTlfHiYFZfNOVg/SidebarUserRecommendations`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/6dZJZQtHgz4A4i4N4xgf8Q/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

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
Request URL: `https://twitter.com/i/api/graphql/MW5ifCoKJeYXvNuiUzYeGQ/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    |   variable | default   |
|:------------------------------------------------------------------------|:--------|-----------:|:----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean |          1 | nan       |
| rweb_tipjar_consumption_enabled                                         | ...     |        nan | error     |
| responsive_web_graphql_exclude_directive_enabled                        | boolean |          1 | nan       |
| verified_phone_label_enabled                                            | boolean |          0 | nan       |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean |          1 | nan       |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean |          1 | nan       |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean |          0 | nan       |
| communities_web_enable_tweet_community_results_fetch                    | boolean |          1 | nan       |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean |          1 | nan       |
| tweetypie_unmention_optimization_enabled                                | boolean |          1 | nan       |
| responsive_web_edit_tweet_api_enabled                                   | boolean |          1 | nan       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean |          1 | nan       |
| view_counts_everywhere_api_enabled                                      | boolean |          1 | nan       |
| longform_notetweets_consumption_enabled                                 | boolean |          1 | nan       |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean |          1 | nan       |
| tweet_awards_web_tipping_enabled                                        | boolean |          0 | nan       |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean |          1 | nan       |
| standardized_nudges_misinfo                                             | boolean |          1 | nan       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean |          1 | nan       |
| rweb_video_timestamps_enabled                                           | boolean |          1 | nan       |
| longform_notetweets_rich_text_read_enabled                              | boolean |          1 | nan       |
| longform_notetweets_inline_media_enabled                                | boolean |          1 | nan       |
| responsive_web_enhance_cards_enabled                                    | boolean |          0 | nan       |

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
Request URL: `https://twitter.com/i/api/graphql/smVCOvV33HpliNbxofWhMw/RitoFlaggedAccountsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                                     | type    | default   |   variable |
|:------------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                         | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                        | boolean | nan       |          1 |
| verified_phone_label_enabled                                            | boolean | nan       |          0 |
| creator_subscriptions_tweet_preview_api_enabled                         | boolean | nan       |          1 |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | nan       |          1 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled       | boolean | nan       |          0 |
| communities_web_enable_tweet_community_results_fetch                    | boolean | nan       |          1 |
| c9s_tweet_anatomy_moderator_badge_enabled                               | boolean | nan       |          1 |
| tweetypie_unmention_optimization_enabled                                | boolean | nan       |          1 |
| responsive_web_edit_tweet_api_enabled                                   | boolean | nan       |          1 |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | nan       |          1 |
| view_counts_everywhere_api_enabled                                      | boolean | nan       |          1 |
| longform_notetweets_consumption_enabled                                 | boolean | nan       |          1 |
| responsive_web_twitter_article_tweet_consumption_enabled                | boolean | nan       |          1 |
| tweet_awards_web_tipping_enabled                                        | boolean | nan       |          0 |
| freedom_of_speech_not_reach_fetch_enabled                               | boolean | nan       |          1 |
| standardized_nudges_misinfo                                             | boolean | nan       |          1 |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | nan       |          1 |
| rweb_video_timestamps_enabled                                           | boolean | nan       |          1 |
| longform_notetweets_rich_text_read_enabled                              | boolean | nan       |          1 |
| longform_notetweets_inline_media_enabled                                | boolean | nan       |          1 |
| responsive_web_enhance_cards_enabled                                    | boolean | nan       |          0 |

#### queryId<br>
`None`<br>
## ArticleEntitiesSlice<br>
Request URL: `https://twitter.com/i/api/graphql/yW-x_9qC1kTGnSVeAcy4QQ/ArticleEntitiesSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

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
Request URL: `https://twitter.com/i/api/graphql/JwLRVIs5Wt9_ci8RGYN6kw/ArticleEntityDraftCreate`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityPublish<br>
Request URL: `https://twitter.com/i/api/graphql/O8a8X1HbrcrW8lUk9mvekg/ArticleEntityPublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityResultByRestId<br>
Request URL: `https://twitter.com/i/api/graphql/Vj9iHq_4C-UQ-8ObgIFSxw/ArticleEntityResultByRestId`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUnpublish<br>
Request URL: `https://twitter.com/i/api/graphql/qJh1IbCjoouckPeDUzvljQ/ArticleEntityUnpublish`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateContent<br>
Request URL: `https://twitter.com/i/api/graphql/hQOlHsanFNXl57VLZrvp7A/ArticleEntityUpdateContent`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateCoverMedia<br>
Request URL: `https://twitter.com/i/api/graphql/FgBTuAA6LHms8U18_N7ArA/ArticleEntityUpdateCoverMedia`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
## ArticleEntityUpdateTitle<br>
Request URL: `https://twitter.com/i/api/graphql/NM8FFV_5VUigi1xfAI3F9g/ArticleEntityUpdateTitle`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                               | type    | default   |   variable |
|:------------------------------------------------------------------|:--------|:----------|-----------:|
| rweb_tipjar_consumption_enabled                                   | ...     | error     |        nan |
| responsive_web_graphql_exclude_directive_enabled                  | boolean | nan       |          1 |
| verified_phone_label_enabled                                      | boolean | nan       |          0 |
| responsive_web_graphql_skip_user_profile_image_extensions_enabled | boolean | nan       |          0 |
| responsive_web_graphql_timeline_navigation_enabled                | boolean | nan       |          1 |

#### queryId<br>
`None`<br>
