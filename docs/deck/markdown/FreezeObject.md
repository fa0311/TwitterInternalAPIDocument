# Twitter Internal Constants Document<br>
This document is entirely auto-generated and may contain errors.<br>
| constant         | value           |
|:-----------------|:----------------|
| LIVE_BROADCAST   | liveBroadcast   |
| REPLAY_BROADCAST | replayBroadcast |
| AUDIOSPACE       | audiospace      |
| VOD              | vod             |
| GIF              | gif             |
| SLATE            | slate           |

| constant   | value     |
|:-----------|:----------|
| DISMISSED  | dismissed |
| APPROVED   | approved  |
| NOT_SEEN   | not_seen  |
| SEEN       | seen      |

| constant   | value                                     |
|:-----------|:------------------------------------------|
| REQUEST    | rweb/loggedOutNotifications/FETCH_REQUEST |
| SUCCESS    | rweb/loggedOutNotifications/FETCH_SUCCESS |
| FAILURE    | rweb/loggedOutNotifications/FETCH_FAILURE |

| constant   | value                                               |
|:-----------|:----------------------------------------------------|
| REQUEST    | rweb/loggedOutNotifications/SAVE_PUSH_TOKEN_REQUEST |
| SUCCESS    | rweb/loggedOutNotifications/SAVE_PUSH_TOKEN_SUCCESS |
| FAILURE    | rweb/loggedOutNotifications/SAVE_PUSH_TOKEN_FAILURE |

| constant        | value           |
|:----------------|:----------------|
| Compact         | Compact         |
| Normal          | Normal          |
| Large           | Large           |
| ThumbsUpAndDown | ThumbsUpAndDown |

| constant       | value        |
|:---------------|:-------------|
| ON_LINGER      | onLinger     |
| ON_IS_RELEVANT | onIsRelevant |
| ON_SHOW_MORE   | onShowMore   |
| ON_LIKE        | onLike       |
| ON_FOLLOW      | onFollow     |

| constant   | value      |
|:-----------|:-----------|
| Scheduled  | Scheduled  |
| InProgress | InProgress |
| Completed  | Completed  |
| Postponed  | Postponed  |
| Cancelled  | Cancelled  |
| Unused6    | _Unused6   |
| Unused7    | _Unused7   |

| constant              | value   |
|:----------------------|:--------|
| __proto__             | null    |
| ArcCurve              | wc      |
| CatmullRomCurve3      | Lc      |
| CubicBezierCurve      | zc      |
| CubicBezierCurve3     | Nc      |
| EllipseCurve          | Sc      |
| LineCurve             | Oc      |
| LineCurve3            | kc      |
| QuadraticBezierCurve  | Uc      |
| QuadraticBezierCurve3 | Fc      |
| SplineCurve           | Bc      |

| constant             | value   |
|:---------------------|:--------|
| __proto__            | null    |
| BoxGeometry          | us      |
| CapsuleGeometry      | jc      |
| CircleGeometry       | qc      |
| ConeGeometry         | Yc      |
| CylinderGeometry     | Xc      |
| DodecahedronGeometry | Jc      |
| EdgesGeometry        | eu      |
| ExtrudeGeometry      | Iu      |
| IcosahedronGeometry  | Du      |
| LatheGeometry        | Hc      |
| OctahedronGeometry   | zu      |
| PlaneGeometry        | Ls      |
| PolyhedronGeometry   | Zc      |
| RingGeometry         | Nu      |
| ShapeGeometry        | Ou      |
| SphereGeometry       | ku      |
| TetrahedronGeometry  | Uu      |
| TorusGeometry        | Fu      |
| TorusKnotGeometry    | Bu      |
| TubeGeometry         | Vu      |
| WireframeGeometry    | Gu      |

```internal process
# Error
{"__proto__":"null","arraySlice":"eh","convertArray":"nh","isTypedArray":"ih","getKeyframeOrder":"rh","sortedArray":"sh","flattenJSON":"ah","subclip":"function()"{const s=t.clone();s.name=e;const a=[];for(){const e=s.tracks[t],o=e.getValueSize(),l=[],c=[];for(){const s=e.times[t]*r;if(){l.push();for...
```
```internal process
# Error
{"__proto__":"null","toHalfFloat":"function()"{"Math.abs()",t=Mn(t),kp.floatView[0]=t;const e=kp.uint32View[0],n=e>>23&511;return kp.baseTable[n]+(t,-65504,65504)},"fromHalfFloat":"function()"{const e=t>>10;return kp.uint32View[0]=kp.mantissaTable[kp.offsetTable[e]+()]+kp.exponentTable[e],kp.floatVi...
```
| constant   | value    |
|:-----------|:---------|
| confetti   | confetti |
| image      | image    |

```internal process
# Error
{"__proto__":"null","DEG2RAD":"xn","RAD2DEG":"_n","generateUUID":"bn","clamp":"Mn","euclideanModulo":"Sn","mapLinear":"function()"{return i+()*(t-e)/(r-i)},"inverseLerp":"function()"{return t!==e?()/(n-t):"0"},"lerp":"wn","damp":"function()"{"return wn()"},"pingpong":"function()"{return e-Math.abs()...
```
| constant   | value      |
|:-----------|:-----------|
| wide       | wide       |
| narrow     | narrow     |
| veryNarrow | veryNarrow |

```internal process
# Error
{[s.wide]:"500",[s.narrow]:"300",[s.veryNarrow]:"200"}
```
| constant   | value   |
|:-----------|:--------|
| IOS        | ios     |
| ANDROID    | android |

| constant          |   value |
|:------------------|--------:|
| APPLE_APP_STORE   |       1 |
| GOOGLE_PLAY_STORE |       2 |

| constant   | value                                                     |
|:-----------|:----------------------------------------------------------|
| REQUEST    | rweb/settings/profile/ENABLE_VERIFIED_PHONE_LABEL_REQUEST |
| SUCCESS    | rweb/settings/profile/ENABLE_VERIFIED_PHONE_LABEL_SUCCESS |
| FAILURE    | rweb/settings/profile/ENABLE_VERIFIED_PHONE_LABEL_FAILURE |

| constant   | value                                                      |
|:-----------|:-----------------------------------------------------------|
| REQUEST    | rweb/settings/profile/DISABLE_VERIFIED_PHONE_LABEL_REQUEST |
| SUCCESS    | rweb/settings/profile/DISABLE_VERIFIED_PHONE_LABEL_SUCCESS |
| FAILURE    | rweb/settings/profile/DISABLE_VERIFIED_PHONE_LABEL_FAILURE |

| constant   | value                                                    |
|:-----------|:---------------------------------------------------------|
| REQUEST    | rweb/settings/profile/FETCH_VERIFIED_PHONE_LABEL_REQUEST |
| SUCCESS    | rweb/settings/profile/FETCH_VERIFIED_PHONE_LABEL_SUCCESS |
| FAILURE    | rweb/settings/profile/FETCH_VERIFIED_PHONE_LABEL_FAILURE |

| constant   | value      |
|:-----------|:-----------|
| wide       | wide       |
| narrow     | narrow     |
| veryNarrow | veryNarrow |

```internal process
# Error
{[a.wide]:"500",[a.narrow]:"300",[a.veryNarrow]:"200"}
```
```internal process
# Error
{[o.sj.AMPLIFY]:{"conversionHandler":"()"{"cardId":"e","cardType":"t","converterOptions":"a","data":"i"}{"const d=()(0,r.FL)",s=parseInt(i,\"image_value\",\"player_image_original\")/parseInt(0,r.SIi,\"string_value\",\"player_width\",10),_=(0,r.SIi,\"string_value\",\"player_height\",10)(0,r.SI),l=(i,...
```
| constant     | value        |
|:-------------|:-------------|
| CONVERSATION | conversation |
| TIMELINE     | timeline     |

| constant   | value                                         |
|:-----------|:----------------------------------------------|
| REQUEST    | rweb/accountVerification/FETCH_ACCESS_REQUEST |
| SUCCESS    | rweb/accountVerification/FETCH_ACCESS_SUCCESS |
| FAILURE    | rweb/accountVerification/FETCH_ACCESS_FAILURE |

| constant   | value                                                      |
|:-----------|:-----------------------------------------------------------|
| REQUEST    | rweb/accountVerification/FETCH_ACCOUNT_ELIGIBILITY_REQUEST |
| SUCCESS    | rweb/accountVerification/FETCH_ACCOUNT_ELIGIBILITY_SUCCESS |
| FAILURE    | rweb/accountVerification/FETCH_ACCOUNT_ELIGIBILITY_FAILURE |

| constant   | value                                                     |
|:-----------|:----------------------------------------------------------|
| REQUEST    | rweb/accountVerification/FETCH_ACCOUNT_VIOLATIONS_REQUEST |
| SUCCESS    | rweb/accountVerification/FETCH_ACCOUNT_VIOLATIONS_SUCCESS |
| FAILURE    | rweb/accountVerification/FETCH_ACCOUNT_VIOLATIONS_FAILURE |

| constant   | value                                                        |
|:-----------|:-------------------------------------------------------------|
| REQUEST    | rweb/accountVerification/FETCH_AUTHENTICATION_RESULT_REQUEST |
| SUCCESS    | rweb/accountVerification/FETCH_AUTHENTICATION_RESULT_SUCCESS |
| FAILURE    | rweb/accountVerification/FETCH_AUTHENTICATION_RESULT_FAILURE |

| constant   | value                                                   |
|:-----------|:--------------------------------------------------------|
| REQUEST    | rweb/accountVerification/FETCH_BADGE_VIOLATIONS_REQUEST |
| SUCCESS    | rweb/accountVerification/FETCH_BADGE_VIOLATIONS_SUCCESS |
| FAILURE    | rweb/accountVerification/FETCH_BADGE_VIOLATIONS_FAILURE |

| constant   | value                                                   |
|:-----------|:--------------------------------------------------------|
| REQUEST    | rweb/accountVerification/FETCH_DOCUMENT_FORMATS_REQUEST |
| SUCCESS    | rweb/accountVerification/FETCH_DOCUMENT_FORMATS_SUCCESS |
| FAILURE    | rweb/accountVerification/FETCH_DOCUMENT_FORMATS_FAILURE |

| constant   | value                                           |
|:-----------|:------------------------------------------------|
| REQUEST    | rweb/accountVerification/VERIFY_ACCOUNT_REQUEST |
| SUCCESS    | rweb/accountVerification/VERIFY_ACCOUNT_SUCCESS |
| FAILURE    | rweb/accountVerification/VERIFY_ACCOUNT_FAILURE |

| constant   | value                                               |
|:-----------|:----------------------------------------------------|
| REQUEST    | rweb/accountVerification/VERIFY_ID_DOCUMENT_REQUEST |
| SUCCESS    | rweb/accountVerification/VERIFY_ID_DOCUMENT_SUCCESS |
| FAILURE    | rweb/accountVerification/VERIFY_ID_DOCUMENT_FAILURE |

| constant          | value             |
|:------------------|:------------------|
| IN_COMPLIANCE     | in_compliance     |
| OUT_OF_COMPLIANCE | out_of_compliance |

| constant           | value              |
|:-------------------|:-------------------|
| PROFILE_COMPLETION | profile_completion |
| ACCOUNT_SECURITY   | account_security   |

| constant             | value                |
|:---------------------|:---------------------|
| DISABLED             | disabled             |
| INTAKE_PROGRESS      | intake_progress      |
| LOCKED               | locked               |
| NEW_ACCOUNT          | new_account          |
| NOT_ELIGIBLE         | not_eligible         |
| NOT_STARTED          | not_started          |
| VERIFICATION_DENIED  | verification_denied  |
| VERIFICATION_PENDING | verification_pending |
| VERIFIED             | verified             |

| constant          | value             |
|:------------------|:------------------|
| IDENTITY_DOCUMENT | identity_document |
| EMAIL             | email             |
| WEBSITE           | website           |

| constant     | value        |
|:-------------|:-------------|
| CONCLUSIVE   | conclusive   |
| INCONCLUSIVE | inconclusive |
| NOT_STARTED  | not_started  |
| PENDING      | pending      |

| constant         | value                      |
|:-----------------|:---------------------------|
| ACTIVISM         | activism                   |
| COMPANY          | brand_company_organization |
| ENTERTAINMENT    | entertainment              |
| GAMING           | gaming                     |
| GOVERNMENT       | government                 |
| INFLUENCER_OTHER | influencer_other           |
| NEWS             | news                       |
| SPORTS           | sports                     |

| constant   | value    |
|:-----------|:---------|
| ACTIVIST   | activist |

| constant   | value     |
|:-----------|:----------|
| COMPANY    | company   |
| EXECUTIVE  | executive |

| constant                 | value                    |
|:-------------------------|:-------------------------|
| ENTERTAINMENT_COMPANY    | entertainment_company    |
| ENTERTAINMENT_INDIVIDUAL | entertainment_individual |
| PRODUCTION               | production               |

| constant   | value     |
|:-----------|:----------|
| CANDIDATE  | candidate |
| OFFICE     | office    |
| OFFICIAL   | official  |

| constant               | value                  |
|:-----------------------|:-----------------------|
| CONTENT_CREATOR        | content_creator        |
| INFLUENTIAL_INDIVIDUAL | influential_individual |

| constant     | value        |
|:-------------|:-------------|
| FREELANCER   | freelancer   |
| JOURNALIST   | journalist   |
| ORGANIZATION | organization |

| constant          | value             |
|:------------------|:------------------|
| SPORTS_INDIVIDUAL | sports_individual |
| SPORTS_ENTITY     | sports_entity     |
| GAMING_INDIVIDUAL | gaming_individual |

| constant   | value   |
|:-----------|:--------|
| ...O       | _       |
| ...C       | _       |
| ...r       | _       |
| ...o       | _       |
| ...i       | _       |
| ...c       | _       |
| ...S       | _       |

```internal process
# Error
{[O.ACTIVIST]:"A.ACTIVISM",[C.COMPANY]:"A.COMPANY",[C.EXECUTIVE]:"A.COMPANY",[r.ENTERTAINMENT_COMPANY]:"A.ENTERTAINMENT",[r.ENTERTAINMENT_INDIVIDUAL]:"A.ENTERTAINMENT",[r.PRODUCTION]:"A.ENTERTAINMENT",[o.CANDIDATE]:"A.GOVERNMENT",[o.OFFICE]:"A.GOVERNMENT",[o.OFFICIAL]:"A.GOVERNMENT",[i.CONTENT_CREAT...
```
| constant               | value                            |
|:-----------------------|:---------------------------------|
| LANDING_PAGE           | landing_page                     |
| NOTABILITY_CATEGORY    | notability_category_select       |
| NOTABILITY_SUBCATEGORY | notability_subtype_select        |
| NOTABILITY_METHOD      | notability_qualifications_select |
| NOTABILITY_INPUT       | notability_qualifications_input  |
| AUTHENTICITY_TYPE      | authenticity_type_select         |
| ADD_EMAIL              | authenticity_add_email           |
| ADD_WEBSITE            | authenticity_add_website         |
| ID_UPLOAD              | authenticity_id_upload           |
| REVIEW_SUBMIT          | review_submit                    |
| THANK_YOU              | thank_you                        |

| constant                                                | value                                                   |
|:--------------------------------------------------------|:--------------------------------------------------------|
| ACTIVIST_GOOGLE_TRENDS                                  | ACTIVIST_GOOGLE_TRENDS                                  |
| ACTIVIST_LEADERSHIP                                     | ACTIVIST_LEADERSHIP                                     |
| ACTIVIST_NEWS                                           | ACTIVIST_NEWS                                           |
| ACTIVIST_QUALIFICATIONS                                 | ACTIVIST_QUALIFICATIONS                                 |
| ACTIVIST_QUALIFICATIONS_INELIGIBLE                      | ACTIVIST_QUALIFICATIONS_INELIGIBLE                      |
| ACTIVIST_SUBCATEGORY                                    | ACTIVIST_SUBCATEGORY                                    |
| ACTIVIST_WIKIPEDIA                                      | ACTIVIST_WIKIPEDIA                                      |
| AUTHENTICITY_TYPE_SELECT                                | AUTHENTICITY_TYPE_SELECT                                |
| COMPANY_GOOGLE_TRENDS                                   | COMPANY_GOOGLE_TRENDS                                   |
| COMPANY_INDIVIDUAL_LEADERSHIP                           | COMPANY_INDIVIDUAL_LEADERSHIP                           |
| COMPANY_INDIVIDUAL_NEWS_REFERENCE                       | COMPANY_INDIVIDUAL_NEWS_REFERENCE                       |
| COMPANY_INDIVIDUAL_NOTABILITY_METHOD                    | COMPANY_INDIVIDUAL_NOTABILITY_METHOD                    |
| COMPANY_INDIVIDUAL_SCREENNAME_CONFIRM                   | COMPANY_INDIVIDUAL_SCREENNAME_CONFIRM                   |
| COMPANY_NEWS_REFERENCE                                  | COMPANY_NEWS_REFERENCE                                  |
| COMPANY_NOTABILITY_METHOD                               | COMPANY_NOTABILITY_METHOD                               |
| COMPANY_STOCK_EXCHANGE                                  | COMPANY_STOCK_EXCHANGE                                  |
| COMPANY_SUBCATEGORY                                     | COMPANY_SUBCATEGORY                                     |
| COMPANY_WIKIPEDIA                                       | COMPANY_WIKIPEDIA                                       |
| CONTENT_CREATOR_GOOGLE_TRENDS                           | CONTENT_CREATOR_GOOGLE_TRENDS                           |
| CONTENT_CREATOR_NEWS                                    | CONTENT_CREATOR_NEWS                                    |
| CONTENT_CREATOR_QUALIFICATIONS                          | CONTENT_CREATOR_QUALIFICATIONS                          |
| CONTENT_CREATOR_WIKIPEDIA                               | CONTENT_CREATOR_WIKIPEDIA                               |
| CREATOR_PROFILE                                         | CREATOR_PROFILE                                         |
| EMAIL_VERIFICATION                                      | EMAIL_VERIFICATION                                      |
| ENTERTAINMENT_COMPANY_GOOGLE_TRENDS                     | ENTERTAINMENT_COMPANY_GOOGLE_TRENDS                     |
| ENTERTAINMENT_COMPANY_NEWS_REFERENCE                    | ENTERTAINMENT_COMPANY_NEWS_REFERENCE                    |
| ENTERTAINMENT_COMPANY_NOTABILITY_METHOD                 | ENTERTAINMENT_COMPANY_NOTABILITY_METHOD                 |
| ENTERTAINMENT_COMPANY_STOCK_REFERENCE                   | ENTERTAINMENT_COMPANY_STOCK_REFERENCE                   |
| ENTERTAINMENT_COMPANY_WIKIPEDIA                         | ENTERTAINMENT_COMPANY_WIKIPEDIA                         |
| ENTERTAINMENT_INDIVIDUAL_IMDB_URL                       | ENTERTAINMENT_INDIVIDUAL_IMDB_URL                       |
| ENTERTAINMENT_INDIVIDUAL_MAIN_REFERENCE_URL             | ENTERTAINMENT_INDIVIDUAL_MAIN_REFERENCE_URL             |
| ENTERTAINMENT_INDIVIDUAL_NEWS_COVERAGE_URLS             | ENTERTAINMENT_INDIVIDUAL_NEWS_COVERAGE_URLS             |
| ENTERTAINMENT_INDIVIDUAL_QUALIFICATIONS                 | ENTERTAINMENT_INDIVIDUAL_QUALIFICATIONS                 |
| ENTERTAINMENT_PRODUCTION_ORGANIZATION_GOOGLE_TRENDS     | ENTERTAINMENT_PRODUCTION_ORGANIZATION_GOOGLE_TRENDS     |
| ENTERTAINMENT_PRODUCTION_ORGANIZATION_NEWS_REFERENCE    | ENTERTAINMENT_PRODUCTION_ORGANIZATION_NEWS_REFERENCE    |
| ENTERTAINMENT_PRODUCTION_ORGANIZATION_NOTABILITY_METHOD | ENTERTAINMENT_PRODUCTION_ORGANIZATION_NOTABILITY_METHOD |
| ENTERTAINMENT_PRODUCTION_ORGANIZATION_STOCK_EXCHANGE    | ENTERTAINMENT_PRODUCTION_ORGANIZATION_STOCK_EXCHANGE    |
| ENTERTAINMENT_PRODUCTION_ORGANIZATION_WIKIPEDIA         | ENTERTAINMENT_PRODUCTION_ORGANIZATION_WIKIPEDIA         |
| ENTERTAINMENT_QUALIFICATIONS                            | ENTERTAINMENT_QUALIFICATIONS                            |
| GAMING_INDIVIDUAL_INELIGIBLE                            | GAMING_INDIVIDUAL_INELIGIBLE                            |
| GAMING_INDIVIDUAL_NEWS_REFERENCE_URLS                   | GAMING_INDIVIDUAL_NEWS_REFERENCE_URLS                   |
| GAMING_INDIVIDUAL_NOTABILITY_METHOD                     | GAMING_INDIVIDUAL_NOTABILITY_METHOD                     |
| GAMING_INDIVIDUAL_SCREENNAME_CONFIRM                    | GAMING_INDIVIDUAL_SCREENNAME_CONFIRM                    |
| GAMING_INDIVIDUAL_TEAM_REFERENCE_URL                    | GAMING_INDIVIDUAL_TEAM_REFERENCE_URL                    |
| GAMING_SUBCATEGORY                                      | GAMING_SUBCATEGORY                                      |
| GOVERNMENT_CANDIDATE_LEVEL_CONFIRM                      | GOVERNMENT_CANDIDATE_LEVEL_CONFIRM                      |
| GOVERNMENT_CANDIDATE_NEWS_REFERENCE_URLS                | GOVERNMENT_CANDIDATE_NEWS_REFERENCE_URLS                |
| GOVERNMENT_CANDIDATE_PROFILE_CONFIRM                    | GOVERNMENT_CANDIDATE_PROFILE_CONFIRM                    |
| GOVERNMENT_CANDIDATE_PUBLIC_REFERENCE_URL               | GOVERNMENT_CANDIDATE_PUBLIC_REFERENCE_URL               |
| GOVERNMENT_OFFICE_NEWS_REFERENCE_URLS                   | GOVERNMENT_OFFICE_NEWS_REFERENCE_URLS                   |
| GOVERNMENT_OFFICE_PROFILE_CONFIRM                       | GOVERNMENT_OFFICE_PROFILE_CONFIRM                       |
| GOVERNMENT_OFFICE_PUBLIC_REFERENCE_URL                  | GOVERNMENT_OFFICE_PUBLIC_REFERENCE_URL                  |
| GOVERNMENT_OFFICIAL_LEVEL_CONFIRM                       | GOVERNMENT_OFFICIAL_LEVEL_CONFIRM                       |
| GOVERNMENT_OFFICIAL_NEWS_REFERENCE_URLS                 | GOVERNMENT_OFFICIAL_NEWS_REFERENCE_URLS                 |
| GOVERNMENT_OFFICIAL_PROFILE_CONFIRM                     | GOVERNMENT_OFFICIAL_PROFILE_CONFIRM                     |
| GOVERNMENT_OFFICIAL_PUBLIC_REFERENCE_URL                | GOVERNMENT_OFFICIAL_PUBLIC_REFERENCE_URL                |
| GOVERNMENT_SUBCATEGORY                                  | GOVERNMENT_SUBCATEGORY                                  |
| ID_COUNTRY_SELECT                                       | ID_COUNTRY_SELECT                                       |
| ID_TYPE_SELECT                                          | ID_TYPE_SELECT                                          |
| INFLUENCER_GOOGLE_TRENDS                                | INFLUENCER_GOOGLE_TRENDS                                |
| INFLUENCER_NEWS                                         | INFLUENCER_NEWS                                         |
| INFLUENCER_QUALIFICATIONS                               | INFLUENCER_QUALIFICATIONS                               |
| INFLUENCER_QUALIFICATIONS_INELIGIBLE                    | INFLUENCER_QUALIFICATIONS_INELIGIBLE                    |
| INFLUENCER_SUBCATEGORY                                  | INFLUENCER_SUBCATEGORY                                  |
| INFLUENCER_WIKIPEDIA                                    | INFLUENCER_WIKIPEDIA                                    |
| INTAKE_LOADING                                          | INTAKE_LOADING                                          |
| INTAKE_TYPE_SELECT                                      | INTAKE_TYPE_SELECT                                      |
| INTAKE_UPLOAD                                           | INTAKE_UPLOAD                                           |
| LANDING_PAGE                                            | LANDING_PAGE                                            |
| NEWS_CREDIBILITY_ARTICLE_REFERENCE_URLS                 | NEWS_CREDIBILITY_ARTICLE_REFERENCE_URLS                 |
| NEWS_CREDIBILITY_AUTHOR_REFERENCE_URL                   | NEWS_CREDIBILITY_AUTHOR_REFERENCE_URL                   |
| NEWS_CREDIBILITY_GOOGLE_TRENDS_REFERENCE_URL            | NEWS_CREDIBILITY_GOOGLE_TRENDS_REFERENCE_URL            |
| NEWS_CREDIBILITY_PUBLICATION_REFERENCE_URL              | NEWS_CREDIBILITY_PUBLICATION_REFERENCE_URL              |
| NEWS_CREDIBILITY_STOCK_REFERENCE_URL                    | NEWS_CREDIBILITY_STOCK_REFERENCE_URL                    |
| NEWS_CREDIBILITY_WIKIPEDIA_REFERENCE_URL                | NEWS_CREDIBILITY_WIKIPEDIA_REFERENCE_URL                |
| NEWS_FREELANCER_CREDIBILITY_ARTICLE_REFERENCE_URLS      | NEWS_FREELANCER_CREDIBILITY_ARTICLE_REFERENCE_URLS      |
| NEWS_JOURNALIST_CRITERIA_CONFIRMATION                   | NEWS_JOURNALIST_CRITERIA_CONFIRMATION                   |
| NEWS_JOURNALIST_QUALIFICATIONS                          | NEWS_JOURNALIST_QUALIFICATIONS                          |
| NEWS_JOURNALIST_SCREENNAME_CONFIRMATION                 | NEWS_JOURNALIST_SCREENNAME_CONFIRMATION                 |
| NEWS_NOTABILITY_CRITERIA_CONFIRMATION                   | NEWS_NOTABILITY_CRITERIA_CONFIRMATION                   |
| NEWS_ORGANIZATION_CREDIBILITY_ARTICLE_REFERENCE_URLS    | NEWS_ORGANIZATION_CREDIBILITY_ARTICLES_REFERENCE_URLS   |
| NEWS_ORGANIZATION_QUALIFICATIONS                        | NEWS_ORGANIZATION_QUALIFICATIONS                        |
| NEWS_ORGANIZATION_REQUIREMENTS_CONFIRMATION             | NEWS_ORGANIZATION_REQUIREMENTS_CONFIRMATION             |
| NEWS_QUALIFICATIONS                                     | NEWS_QUALIFICATIONS                                     |
| NOTABILITY_CATEGORY_SELECT                              | NOTABILITY_CATEGORY_SELECT                              |
| REVIEW_SUBMIT                                           | REVIEW_SUBMIT                                           |
| SITE_VERIFICATION                                       | SITE_VERIFICATION                                       |
| SPORTS_ENTITY_GOOGLE_TRENDS                             | SPORTS_ENTITY_GOOGLE_TRENDS                             |
| SPORTS_ENTITY_NEWS_REFERENCE                            | SPORTS_ENTITY_NEWS_REFERENCE                            |
| SPORTS_ENTITY_NOTABILITY_METHOD                         | SPORTS_ENTITY_NOTABILITY_METHOD                         |
| SPORTS_ENTITY_STOCK_REFERENCE                           | SPORTS_ENTITY_STOCK_REFERENCE                           |
| SPORTS_ENTITY_WEBSITE                                   | SPORTS_ENTITY_WEBSITE                                   |
| SPORTS_ENTITY_WIKIPEDIA                                 | SPORTS_ENTITY_WIKIPEDIA                                 |
| SPORTS_INDIVIDUAL_NEWS_REFERENCE_URLS                   | SPORTS_INDIVIDUAL_NEWS_REFERENCE_URLS                   |
| SPORTS_INDIVIDUAL_NOTABILITY_METHOD                     | SPORTS_INDIVIDUAL_NOTABILITY_METHOD                     |
| SPORTS_INDIVIDUAL_SCREENNAME_CONFIRM                    | SPORTS_INDIVIDUAL_SCREENNAME_CONFIRM                    |
| SPORTS_INDIVIDUAL_TEAM_REFERENCE_URL                    | SPORTS_INDIVIDUAL_TEAM_REFERENCE_URL                    |
| SPORTS_SUBCATEGORY                                      | SPORTS_SUBCATEGORY                                      |
| TEST_INPUT                                              | TEST_INPUT                                              |
| TEST_PIVOT                                              | TEST_PIVOT                                              |
| TEST_RADIO                                              | TEST_RADIO                                              |
| THANK_YOU                                               | THANK_YOU                                               |
| WEBSITE_REFERENCE_CONFIRM_AUTOFILL                      | WEBSITE_REFERENCE_CONFIRM_AUTOFILL                      |
| WEBSITE_REFERENCE_CONFIRM_PROCEED                       | WEBSITE_REFERENCE_CONFIRM_PROCEED                       |

```internal process
# Error
{[l.LANDING_PAGE]:{"next":"l.NOTABILITY_CATEGORY_SELECT","scribeComponent":"U.LANDING_PAGE"},[l.NOTABILITY_CATEGORY_SELECT]:{"next":"null","scribeComponent":"U.NOTABILITY_CATEGORY"},[l.ACTIVIST_QUALIFICATIONS]:{"next":"null","scribeComponent":"U.NOTABILITY_METHOD"},[l.ACTIVIST_GOOGLE_TRENDS]:{"next"...
```
| constant     | value             |
|:-------------|:------------------|
| navButtons   | navigationButtons |
| carouselRoot | carouselRoot      |

| constant         | value               |
|:-----------------|:--------------------|
| Abort            | abort               |
| ChromelessWeb    | chromeless_web_link |
| Deeplink         | deep_link           |
| DeeplinkAndAbort | deep_link_and_abort |
| DeeplinkInPlace  | deep_link_in_place  |
| Finish           | finish              |
| Subtask          | subtask             |
| Task             | task                |
| Web              | web_link            |
| WeblinkAndAbort  | web_link_and_abort  |

| constant        | value             |
|:----------------|:------------------|
| Allow           | allow             |
| CancelFlow      | cancel_flow       |
| HideExplicitCta | hide_explicit_cta |
| Disallow        | disallow          |

| constant   | value       |
|:-----------|:------------|
| Default    | default     |
| BulletList | bullet_list |

| constant             | value                 |
|:---------------------|:----------------------|
| DestructiveSecondary | destructive_secondary |
| Primary              | primary               |
| Secondary            | secondary             |
| Text                 | text                  |
| Brand                | brand                 |
| TwitterBrand         | twitter_brand         |

| constant      | value          |
|:--------------|:---------------|
| Small         | small          |
| NormalCompact | normal_compact |
| Normal        | normal         |
| LargeCompact  | large_compact  |
| Large         | large          |

| constant          | value     |
|:------------------|:----------|
| CheckmarkAndClose | checkmark |
| Text              | text      |
| ThumbsUpAndDown   | thumbs    |

| constant   | value   |
|:-----------|:--------|
| Toolbar    | toolbar |

| constant       | value           |
|:---------------|:----------------|
| Scrollable     | scrollable      |
| Centered       | centered        |
| CenteredHeader | centered_header |
| HalfCover      | half_cover      |

| constant   | value   |
|:-----------|:--------|
| Success    | success |
| Failure    | failure |
| Cancel     | cancel  |

| constant     | value          |
|:-------------|:---------------|
| Icon         | icon           |
| FullWidth    | full_width     |
| FullBleedTop | full_bleed_top |

| constant       | value            |
|:---------------|:-----------------|
| PhoneOnly      | phone_only       |
| EmailOnly      | email_only       |
| PhoneThenEmail | phone_then_email |
| EmailThenPhone | email_then_phone |

| constant                         | value                                |
|:---------------------------------|:-------------------------------------|
| ActionList                       | ACTION_LIST                          |
| AlertDialog                      | ALERT_DIALOG                         |
| AlertDialogSupressClientEvents   | ALERT_DIALOG_SUPRESS_CLIENT_EVENTS   |
| AppDownloadCTA                   | APP_DOWNLOAD_CTA                     |
| AppLocaleUpdate                  | APP_LOCALE_UPDATE                    |
| BrowsableNux                     | BROWSABLE_NUX                        |
| CallToAction                     | CALL_TO_ACTION                       |
| CheckLoggedInAccount             | CHECK_LOGGED_IN_ACCOUNT              |
| ChoiceSelection                  | CHOICE_SELECTION                     |
| ContactsLiveSyncPermissionPrompt | CONTACTS_LIVE_SYNC_PERMISSION_PROMPT |
| EmailContactsSync                | EMAIL_CONTACTS_SYNC                  |
| EmailVerification                | EMAIL_VERIFICATION                   |
| EndFlow                          | END_FLOW                             |
| EnterDate                        | ENTER_DATE                           |
| EnterEmail                       | ENTER_EMAIL                          |
| EnterPassword                    | ENTER_PASSWORD                       |
| EnterPhone                       | ENTER_PHONE                          |
| EnterRecaptcha                   | ENTER_RECAPTCHA                      |
| EnterText                        | ENTER_TEXT                           |
| EnterUsername                    | ENTER_USERNAME                       |
| FetchPassword                    | FETCH_PASSWORD                       |
| GenericURT                       | GENERIC_URT                          |
| InAppNotification                | IN_APP_NOTIFICATION                  |
| InterestPicker                   | INTEREST_PICKER                      |
| JsInstrumentation                | JS_INSTRUMENTATION                   |
| MenuDialog                       | MENU_DIALOG                          |
| NotificationsPermissionPrompt    | NOTIFICATIONS_PERMISSION_PROMPT      |
| OpenAccount                      | OPEN_ACCOUNT                         |
| OpenHomeTimeline                 | OPEN_HOME_TIMELINE                   |
| OpenLink                         | OPEN_LINK                            |
| Passkey                          | PASSKEY                              |
| PhoneVerification                | PHONE_VERIFICATION                   |
| PrivacyOptions                   | PRIVACY_OPTIONS                      |
| Recaptcha                        | RECAPTCHA                            |
| SecurityKey                      | SECURITY_KEY                         |
| SelectAvatar                     | SELECT_AVATAR                        |
| SelectBanner                     | SELECT_BANNER                        |
| SettingsList                     | SETTINGS_LIST                        |
| ShowCode                         | SHOW_CODE                            |
| Signup                           | SIGNUP                               |
| SignupReview                     | SIGNUP_REVIEW                        |
| TopicsSelector                   | TOPICS_SELECTOR                      |
| TweetSelectionURT                | TWEET_SELECTION_URT                  |
| TypeaheadSearch                  | TYPEAHEAD_SEARCH                     |
| UpdateUsers                      | UPDATE_USERS                         |
| UploadMedia                      | UPLOAD_MEDIA                         |
| UserRecommendations              | USER_RECOMMENDATIONS_LIST            |
| UserRecommendationsURT           | USER_RECOMMENDATIONS_URT             |
| WaitSpinner                      | WAIT_SPINNER                         |
| WebModal                         | WEB_MODAL                            |

| constant   | value    |
|:-----------|:---------|
| Centered   | centered |
| Left       | left     |

| constant          | value              |
|:------------------|:-------------------|
| Action            | action             |
| Boolean           | boolean            |
| DestructiveAction | destructive_action |
| PreciseLocation   | precise_location   |
| SettingsGroup     | settings_group     |
| StaticText        | static_text        |
| Separator         | separator          |
| TextField         | text_field         |
| Button            | button             |
| Tweet             | tweet              |

| constant        | value             |
|:----------------|:------------------|
| AppleSSOButton  | apple_sso_button  |
| GoogleSSOButton | google_sso_button |
| NextButton      | next_button       |
| UserIdentifier  | user_identifier   |

| constant                 | value          |
|:-------------------------|:---------------|
| DEPRECATED_UnorderedList | UnorderedList  |
| DEPRECATED_ListItem      | ListItem       |
| UnorderedList            | unordered_list |
| ListItem                 | list_item      |

| constant   | value   |
|:-----------|:--------|
| Normal     | Normal  |
| Bold       | Bold    |

| constant   | value   |
|:-----------|:--------|
| Small      | Small   |
| Normal     | Normal  |
| Large      | Large   |
| XLarge     | XLarge  |
| Jumbo      | Jumbo   |

| constant   | value   |
|:-----------|:--------|
| Qr         | qr      |
| Text       | text    |

| constant   | value   |
|:-----------|:--------|
| Avatar     | avatar  |
| Banner     | banner  |

| constant   | value     |
|:-----------|:----------|
| Success    | success   |
| NotFound   | not_found |
| Error      | error     |

| constant   | value    |
|:-----------|:---------|
| Favorite   | favorite |
| Follow     | follow   |
| Reply      | reply    |
| Retweet    | retweet  |

| constant   | value    |
|:-----------|:---------|
| Checkbox   | checkbox |
| Follow     | follow   |

| constant         | value           |
|:-----------------|:----------------|
| Tile             | tile            |
| List             | list            |
| TileFollowButton | tile_follow_btn |

| constant   | value     |
|:-----------|:----------|
| Always     | always    |
| Never      | never     |
| Preprompt  | preprompt |

| constant   | value     |
|:-----------|:----------|
| Email      | email     |
| Number     | number    |
| Password   | password  |
| Telephone  | telephone |
| Text       | text      |

| constant    | value        |
|:------------|:-------------|
| ResendSms   | resend_sms   |
| ResendVoice | resend_voice |
| ResendEmail | resend_email |

| constant    | value        |
|:------------|:-------------|
| Password    | password     |
| NewPassword | new_password |
| Text        | text         |

| constant   | value   |
|:-----------|:--------|
| Normal     | normal  |
| Compact    | compact |

| constant    | value        |
|:------------|:-------------|
| Username    | username     |
| Password    | password     |
| NewPassword | new_password |
| Text        | text         |

| constant   | value    |
|:-----------|:---------|
| Mismatch   | mismatch |

| constant   | value   |
|:-----------|:--------|
| compact    | compact |
| stacked    | stacked |

| constant      | value          |
|:--------------|:---------------|
| Fixed         | fixed          |
| Floating      | floating       |
| FloatingLarge | floating_large |

| constant   | value      |
|:-----------|:-----------|
| Default    | default    |
| GoogleSSO  | google_sso |
| AppleSSO   | apple_sso  |

| constant   | value      |
|:-----------|:-----------|
| Impression | impression |
| Click      | click      |

| constant       | value           |
|:---------------|:----------------|
| HeaderTitle    | header_title    |
| HeaderSubtitle | header_subtitle |
| SectionTitle   | section_title   |
| Detail         | detail          |

| constant   | value   |
|:-----------|:--------|
| All        | all     |
| Users      | users   |
| Topics     | topics  |
| Events     | events  |

| constant   | value                  |
|:-----------|:-----------------------|
| REQUEST    | rweb/ocf/FETCH_REQUEST |
| SUCCESS    | rweb/ocf/FETCH_SUCCESS |
| FAILURE    | rweb/ocf/FETCH_FAILURE |

| constant   | value                  |
|:-----------|:-----------------------|
| REQUEST    | rweb/ocf/START_REQUEST |
| SUCCESS    | rweb/ocf/START_SUCCESS |
| FAILURE    | rweb/ocf/START_FAILURE |

| constant   | value                              |
|:-----------|:-----------------------------------|
| REQUEST    | rweb/ocf/VERIFY_IDENTIFIER_REQUEST |
| SUCCESS    | rweb/ocf/VERIFY_IDENTIFIER_SUCCESS |
| FAILURE    | rweb/ocf/VERIFY_IDENTIFIER_FAILURE |

| constant   | value                                                |
|:-----------|:-----------------------------------------------------|
| REQUEST    | rweb/ocf/FETCH_BROWSABLE_NUX_RECOMMENDATIONS_REQUEST |
| SUCCESS    | rweb/ocf/FETCH_BROWSABLE_NUX_RECOMMENDATIONS_SUCCESS |
| FAILURE    | rweb/ocf/FETCH_BROWSABLE_NUX_RECOMMENDATIONS_FAILURE |

| constant         | value           |
|:-----------------|:----------------|
| LIVE_BROADCAST   | liveBroadcast   |
| REPLAY_BROADCAST | replayBroadcast |
| VOD              | vod             |
| GIF              | gif             |
| SLATE            | slate           |

| constant         | value                                 |
|:-----------------|:--------------------------------------|
| A11YHook         | VideoPlayerDefaultUI-A11YHook         |
| ControlBar       | VideoPlayerDefaultUI-ControlBar       |
| HashtagHighlight | VideoPlayerDefaultUI-HashtagHighlight |
| Root             | VideoPlayerDefaultUI-Root             |
| VideoCTA         | VideoPlayerDefaultUI-VideoCTA         |

| constant         | value            |
|:-----------------|:-----------------|
| Classic          | Classic          |
| ClassicNoDivider | ClassicNoDivider |
| ContextEmphasis  | ContextEmphasis  |
| Feedback         | Feedback         |

| constant   | value    |
|:-----------|:---------|
| Classic    | Classic  |
| Footnote   | Footnote |
| Button     | Button   |

```internal process
# Error
{"₊":"+","₋":"-","₌":"=","₍":"()","₀":"0","₁":"1","₂":"2","₃":"3","₄":"4","₅":"5","₆":"6","₇":"7","₈":"8","₉":"9",ₐ:"a",ₑ:"e",ₕ:"h",ᵢ:"i",ⱼ:"j",ₖ:"k",ₗ:"l",ₘ:"m",ₙ:"n",ₒ:"o",ₚ:"p",ᵣ:"r",ₛ:"s",ₜ:"t",ᵤ:"u",ᵥ:"v",ₓ:"x",ᵦ:"β",ᵧ:"γ",ᵨ:"ρ",ᵩ:"ϕ",ᵪ:"χ","⁺":"+","⁻":"-","⁼":"=","⁽":"(\",\"₎\":\")","⁰":"0","¹...
```
| constant   | value      |
|:-----------|:-----------|
| Scheduled  | Scheduled  |
| InProgress | InProgress |
| Completed  | Completed  |
| Postponed  | Postponed  |
| Cancelled  | Cancelled  |
| Unused6    | _Unused6   |
| Unused7    | _Unused7   |

| constant        | value          |
|:----------------|:---------------|
| SCORE           | score          |
| SECONDARY_SCORE | secondaryScore |

| constant   | value      |
|:-----------|:-----------|
| Scheduled  | Scheduled  |
| InProgress | InProgress |
| Completed  | Completed  |
| Postponed  | Postponed  |
| Cancelled  | Cancelled  |
| Unused6    | _Unused6   |
| Unused7    | _Unused7   |

| constant   | value                                                                                                                |
|:-----------|:---------------------------------------------------------------------------------------------------------------------|
| apple      | https://apps.apple.com/account/billing                                                                               |
| google     | https://play.google.com/store/account/subscriptions?sku=com.twitter.google.rogue.one.1.1&package=com.twitter.android |

