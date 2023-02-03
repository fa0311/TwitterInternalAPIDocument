# Twitter Internal GraphQL API Document<br>
This document is entirely auto-generated and may contain errors.<br>
## Usage<br>
If the parameter is an array type, encode it in json format.<br>
Body example:<br>
```Python
json.dumps({
        "queryId": "kV0jgNRI3ofhHK_G5yhlZg",
        "variables": json.dumps({
            "tweet_text": "Hello, world!",
            "media": {"media_entities": [], "possibly_sensitive": False},
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": True,
            "withSuperFollowsUserFields": False,
            "semantic_annotation_ids": [],
            "dark_request": False,
            "withBirdwatchPivots": False,
        }),
    })
```
`json.dumps` is equivalent to `JSON.stringify` in javaScript<br>
## EditBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/a6kPp1cS1Dgbsjhapz1PNw/EditBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| id    | ...    | t          |

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
| key   | type   | variable   |
|:------|:-------|:-----------|
| alias | ...    | t.alias    |

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
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |

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
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |
| name                   | ...    | r          |

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
| key                    | type   | variable   |
|:-----------------------|:-------|:-----------|
| bookmark_collection_id | ...    | t          |
| tweet_id               | ...    | r          |

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
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...o  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
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
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | t          |
| cursor                 | ...     | r          |
| includePromotedContent | boolean | True       |
| ...()(0,n.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
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
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                       | type   | variable   |
|:--------------------------|:-------|:-----------|
| ...n                      | ...    | _          |
| withCommunity             | ...    | l.isTrue() |
| ...("c9s_enabled")(0,s.d) | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://twitter.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | i.communityId |
| name         | ...    | i.name        |
| ...()(0,m.S) | ...    | _             |

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
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | i.communityId |
| theme        | ...    | i.theme       |
| ...()(0,m.S) | ...    | _             |

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
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | i.communityId |
| ruleId       | ...    | i.ruleId      |
| ...()(0,m.S) | ...    | _             |

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
| key          | type   | variable      |
|:-------------|:-------|:--------------|
| communityId  | ...    | i.communityId |
| ...()(0,m.S) | ...    | _             |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://twitter.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                                        | type    | variable                              |
|:-----------------------------------------------------------|:--------|:--------------------------------------|
| focalTweetId                                               | ...     | _                                     |
| cursor                                                     | ...     | n                                     |
| referrer                                                   | ...     | a                                     |
| controller_data                                            | ...     | i                                     |
| rux_context                                                | ...     | w                                     |
| with_rux_injections                                        | ...     | c                                     |
| includePromotedContent                                     | boolean | True                                  |
| withCommunity                                              | ...     | t.isTrue()                            |
| withQuickPromoteEligibilityTweetFields                     | boolean | True                                  |
| withBirdwatchNotes                                         | ...     | t.isTrue("c9s_enabled")               |
| ...("responsive_web_birdwatch_consumption_enabled")(0,r.d) | ...     | _                                     |
| withVoice                                                  | ...     | t.isTrue(t)                           |
| withV2Timeline                                             | ...     | t.isTrue("voice_consumption_enabled") |
| isReaderMode                                               | ...     | o                                     |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                             | type   | variable                                                                                |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------------|
| ...n                            | ...    | _                                                                                       |
| withConversationQueryHighlights | ...    | i.isTrue()&&i.isTrue("dm_inbox_search_query_highlighting_conversation_results_enabled") |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarksAllDelete<br>
Request URL: `https://twitter.com/i/api/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| count                  | ...     | n          |
| cursor                 | ...     | t          |
| includePromotedContent | boolean | False      |
| ...()(0,r.d)           | ...     | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...r  | ...    | _          |
| ...t  | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://twitter.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key      | type   | variable   |
|:---------|:-------|:-----------|
| userId   | ...    | n          |
| settings | ...    | i          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## ForYouExplore<br>
Request URL: `https://twitter.com/i/api/graphql/ggw0DFpYRNeR2pmEQ3r3GQ/ForYouExplore`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable            |
|:-------------|:-------|:--------------------|
| count        | ...    | (optional) t.count  |
| cursor       | ...    | (optional) t.cursor |
| ...()(0,r.d) | ...    | _                   |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ImmersiveMedia<br>
Request URL: `https://twitter.com/i/api/graphql/5hFzRHD3y8LtZu8GpkI30A/ImmersiveMedia`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key             | type   | variable                     |
|:----------------|:-------|:-----------------------------|
| pinned_tweet_id | ...    | (optional) t.pinned_tweet_id |
| page_name       | ...    | (optional) t.page_name       |
| ...()(0,r.d)    | ...    | _                            |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## GraphQLError<br>
Request URL: `https://twitter.com/i/api/graphql/2V2W3HIBuMW83vEMtfo_Rg/GraphQLError`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| tweetText | ...    | d          |

#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                  | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| verified_phone_label_enabled                          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| userId       | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                  | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| verified_phone_label_enabled                          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
## DeleteBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable                  |
|:-------------|:-------|:--------------------------|
| isPrivate    | ...    | private===r.toLowerCase() |
| name         | ...    | o                         |
| description  | ...    | a                         |
| ...()(0,s.S) | ...    | _                         |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| listId       | ...    | a          |
| mediaId      | ...    | r          |
| ...()(0,s.S) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarksAllDelete<br>
Request URL: `https://twitter.com/i/api/graphql/skiACZKC1GDYli-M8RzEPQ/BookmarksAllDelete`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| screenName   | ...    | _          |
| listSlug     | ...    | a          |
| ...()(0,s.S) | ...    | _          |

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
| key                       | type    | variable                              |
|:--------------------------|:--------|:--------------------------------------|
| userId                    | ...     | _                                     |
| count                     | ...     | i                                     |
| cursor                    | ...     | n                                     |
| includePromotedContent    | boolean | True                                  |
| withCommunity             | ...     | t.isTrue()                            |
| ...("c9s_enabled")(0,r.d) | ...     | _                                     |
| withVoice                 | ...     | t.isTrue(t)                           |
| withV2Timeline            | ...     | t.isTrue("voice_consumption_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | _           |
| count                  | ...     | i           |
| cursor                 | ...     | n           |
| includePromotedContent | boolean | True        |
| ...()(0,r.d)           | ...     | _           |
| withVoice              | ...     | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://twitter.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"userId":"n","count":"t","cursor":"string"==typeof i?i:"void 0","includePromotedContent":"!1","withDownvotePerspective":"!1","withReactionsMetadata":"!1","withReactionsPerspective":"!1","withSuperFollowsTweetFields":"!1","withSuperFollowsUserFields":"!1","withVoice":"!1"}
```
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable                              |
|:-----------------------|:--------|:--------------------------------------|
| userId                 | ...     | _                                     |
| count                  | ...     | i                                     |
| cursor                 | ...     | n                                     |
| includePromotedContent | boolean | False                                 |
| ...()(0,r.d)           | ...     | _                                     |
| withClientEventToken   | boolean | False                                 |
| withBirdwatchNotes     | boolean | False                                 |
| withVoice              | ...     | t.isTrue(t)                           |
| withV2Timeline         | ...     | t.isTrue("voice_consumption_enabled") |

#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                  | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| verified_phone_label_enabled                          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable    |
|:-----------------------|:--------|:------------|
| userId                 | ...     | s           |
| count                  | ...     | i           |
| cursor                 | ...     | n           |
| teamName               | ...     | _           |
| includePromotedContent | boolean | False       |
| ...()(0,r.d)           | ...     | _           |
| withClientEventToken   | boolean | False       |
| withVoice              | ...     | t.isTrue(t) |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFoldersSlice<br>
Request URL: `https://twitter.com/i/api/graphql/i78YDd0Tza-dV4SYs58kRg/BookmarkFoldersSlice`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                | type   | variable   |
|:-------------------|:-------|:-----------|
| post_tweet_request | ...    | i          |
| execute_at         | ...    | p()        |

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
| key        | type   | variable   |
|:-----------|:-------|:-----------|
| promptType | ...    | a          |

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
| key               | type   | variable   |
|:------------------|:-------|:-----------|
| displayPreference | ...    | a          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
`None`<br>
#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                  | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| verified_phone_label_enabled                          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

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
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key       | type   | variable   |
|:----------|:-------|:-----------|
| device_id | ...    | t          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTweetsTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/rvC1orOh3vabuEq3gEQD4w/ArticleTweetsTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...t                | ...    | _          |
| ...()(0,r.d)        | ...    | _          |
| articleListSeedType | ...    | n          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## ArticleTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/_S2Cdk40cEGNF0J13dBj9Q/ArticleTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                 | type   | variable   |
|:--------------------|:-------|:-----------|
| ...t                | ...    | _          |
| ...()(0,r.d)        | ...    | _          |
| articleListSeedType | ...    | n          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://twitter.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
```internal process
# Error
{"rest_id":"r","cursor":"o","context":"JSON.stringify()"{"data_lookup_id":"a"}"0","_.dt"}
```
#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| cursor       | ...    | o          |
| ...()(0,_.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## DeleteBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/2UTTsO-6zs93XqlEUZPsSg/DeleteBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| topicId      | ...    | o          |
| ...()(0,_.d) | ...    | _          |

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
| key                        | type   | variable   |
|:---------------------------|:-------|:-----------|
| tweetId                    | ...    | i          |
| withSuperFollowsUserFields | ...    | t.isTrue() |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| tweetId                | ...     | r          |
| count                  | ...     | i          |
| cursor                 | ...     | n          |
| includePromotedContent | boolean | True       |
| ...()(0,_.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                                    | type    | variable   |
|:---------------------------------------|:--------|:-----------|
| tweetId                                | ...     | i          |
| ...()(0,_.d)                           | ...     | _          |
| withQuickPromoteEligibilityTweetFields | boolean | True       |

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
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| ...()(0,n.d)     | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## createBookmarkFolder<br>
Request URL: `https://twitter.com/i/api/graphql/6Xxqpq8TM_CREYiuof_h5w/createBookmarkFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | i          |

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
| key              | type   | variable   |
|:-----------------|:-------|:-----------|
| twitterArticleId | ...    | l          |
| mediaId          | ...    | a          |
| ...()(0,n.d)     | ...    | _          |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key          | type   | variable   |
|:-------------|:-------|:-----------|
| ...i         | ...    | _          |
| ...()(0,n.d) | ...    | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## BookmarkFolderTimeline<br>
Request URL: `https://twitter.com/i/api/graphql/Jhbzk0gqF6YGD3iI0NEIJQ/BookmarkFolderTimeline`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | ...    | t.communityId |
| prefix      | ...    | t.prefix      |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key         | type   | variable      |
|:------------|:-------|:--------------|
| communityId | ...    | t.communityId |
| prefix      | ...    | t.prefix      |

#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                  | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| verified_phone_label_enabled                          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
## Bookmarks<br>
Request URL: `https://twitter.com/i/api/graphql/wKrHDZP968TKLalTSCLWwg/Bookmarks`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                    | type    | variable   |
|:-----------------------|:--------|:-----------|
| includePromotedContent | boolean | True       |
| ...()(0,_.d)           | ...     | _          |

#### features<br>
| key                                                                     | type    | variable   |
|:------------------------------------------------------------------------|:--------|:-----------|
| graphql_timeline_v2_bookmark_timeline                                   | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled                   | boolean | True       |
| verified_phone_label_enabled                                            | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled                      | boolean | True       |
| longform_notetweets_consumption_enabled                                 | boolean | False      |
| tweetypie_unmention_optimization_enabled                                | boolean | True       |
| vibe_api_enabled                                                        | boolean | True       |
| responsive_web_edit_tweet_api_enabled                                   | boolean | True       |
| graphql_is_translatable_rweb_tweet_is_translatable_enabled              | boolean | True       |
| view_counts_everywhere_api_enabled                                      | boolean | True       |
| standardized_nudges_misinfo                                             | boolean | True       |
| tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled | boolean | False      |
| interactive_text_enabled                                                | boolean | True       |
| responsive_web_text_conversations_enabled                               | boolean | False      |
| responsive_web_enhance_cards_enabled                                    | boolean | False      |

#### queryId<br>
`None`<br>
## bookmarkTweetToFolder<br>
Request URL: `https://twitter.com/i/api/graphql/4KHZvvNbHNf07bsgnL9gWA/bookmarkTweetToFolder`<br>
Request Method: `POST`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key   | type   | variable   |
|:------|:-------|:-----------|
| ...t  | ...    | _          |

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
| key                        | type   | variable                                   |
|:---------------------------|:-------|:-------------------------------------------|
| withCommunitiesMemberships | ...    | l.isTrue()                                 |
| withCommunitiesCreation    | ...    | l.isTrue("c9s_enabled")                    |
| withSuperFollowsUserFields | ...    | l.isTrue("c9s_community_creation_enabled") |

#### features<br>
`None`<br>
#### queryId<br>
`None`<br>
## CardPreviewByTweetText<br>
Request URL: `https://twitter.com/i/api/graphql/mic41-i8OiQ6XvDW8Rz8Ng/CardPreviewByTweetText`<br>
Request Method: `GET`<br>
Login Required: `...`<br>
### Param<br>
#### variables<br>
| key                        | type   | variable                                             |
|:---------------------------|:-------|:-----------------------------------------------------|
| userId                     | ...    | a                                                    |
| withSafetyModeUserFields   | ...    | l.isTrue()                                           |
| withSuperFollowsUserFields | ...    | l.isTrue("rito_safety_mode_blocked_profile_enabled") |

#### features<br>
| key                                                   | type    | variable   |
|:------------------------------------------------------|:--------|:-----------|
| responsive_web_enhance_cards_enabled                  | boolean | False      |
| responsive_web_twitter_blue_verified_badge_is_enabled | boolean | True       |
| verified_phone_label_enabled                          | boolean | False      |
| responsive_web_graphql_timeline_navigation_enabled    | boolean | True       |

#### queryId<br>
`None`<br>
