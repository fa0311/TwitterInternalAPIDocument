# Twitter Internal Constants Document<br>
This document is entirely auto-generated and may contain errors.<br>
| constant           | value   |
|:-------------------|:--------|
| __proto__          | null    |
| assert             | l       |
| requireNonNull     | A       |
| requireInstance    | d       |
| abstractMethodFail | v       |

| constant   | value    |
|:-----------|:---------|
| position   | absolute |
| border     | 0        |
| width      | 1        |
| height     | 1        |
| padding    | 0        |
| margin     | -1       |
| overflow   | hidden   |
| clip       | rect()   |
| whiteSpace | nowrap   |
| wordWrap   | normal   |

| constant     | value             |
|:-------------|:------------------|
| navButtons   | navigationButtons |
| carouselRoot | carouselRoot      |

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

| constant   | value      |
|:-----------|:-----------|
| wide       | wide       |
| narrow     | narrow     |
| veryNarrow | veryNarrow |

| constant   |   value |
|:-----------|--------:|
| large      |      54 |
| medium     |      46 |
| small      |      36 |
| xSmall     |      12 |

```internal process
# Error
{"₊":"+","₋":"-","₌":"=","₍":"()","₀":"0","₁":"1","₂":"2","₃":"3","₄":"4","₅":"5","₆":"6","₇":"7","₈":"8","₉":"9",ₐ:"a",ₑ:"e",ₕ:"h",ᵢ:"i",ⱼ:"j",ₖ:"k",ₗ:"l",ₘ:"m",ₙ:"n",ₒ:"o",ₚ:"p",ᵣ:"r",ₛ:"s",ₜ:"t",ᵤ:"u",ᵥ:"v",ₓ:"x",ᵦ:"β",ᵧ:"γ",ᵨ:"ρ",ᵩ:"ϕ",ᵪ:"χ","⁺":"+","⁻":"-","⁼":"=","⁽":"(\",\"₎\":\")","⁰":"0","¹...
```
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

| constant   | value   |
|:-----------|:--------|
| IOS        | ios     |
| ANDROID    | android |

| constant          |   value |
|:------------------|--------:|
| APPLE_APP_STORE   |       1 |
| GOOGLE_PLAY_STORE |       2 |

| constant   | value                                                                                                                |
|:-----------|:---------------------------------------------------------------------------------------------------------------------|
| apple      | https://apps.apple.com/account/billing                                                                               |
| google     | https://play.google.com/store/account/subscriptions?sku=com.twitter.google.rogue.one.1.1&package=com.twitter.android |

| constant              | value   |
|:----------------------|:--------|
| __proto__             | null    |
| ArcCurve              | Cc      |
| CatmullRomCurve3      | Dc      |
| CubicBezierCurve      | kc      |
| CubicBezierCurve3     | Uc      |
| EllipseCurve          | Ac      |
| LineCurve             | Fc      |
| LineCurve3            | Bc      |
| QuadraticBezierCurve  | Vc      |
| QuadraticBezierCurve3 | Gc      |
| SplineCurve           | Wc      |

| constant             | value   |
|:---------------------|:--------|
| __proto__            | null    |
| BoxGeometry          | ps      |
| CapsuleGeometry      | Yc      |
| CircleGeometry       | Zc      |
| ConeGeometry         | Qc      |
| CylinderGeometry     | Jc      |
| DodecahedronGeometry | Kc      |
| EdgesGeometry        | ru      |
| ExtrudeGeometry      | zu      |
| IcosahedronGeometry  | Ou      |
| LatheGeometry        | Xc      |
| OctahedronGeometry   | ku      |
| PlaneGeometry        | Ds      |
| PolyhedronGeometry   | $c      |
| RingGeometry         | Uu      |
| ShapeGeometry        | Fu      |
| SphereGeometry       | Bu      |
| TetrahedronGeometry  | Vu      |
| TorusGeometry        | Gu      |
| TorusKnotGeometry    | Wu      |
| TubeGeometry         | Hu      |
| WireframeGeometry    | ju      |

```internal process
# Error
{"__proto__":"null","arraySlice":"rh","convertArray":"sh","isTypedArray":"ah","getKeyframeOrder":"oh","sortedArray":"lh","flattenJSON":"ch","subclip":"function()"{const s=t.clone();s.name=e;const a=[];for(){const e=s.tracks[t],o=e.getValueSize(),l=[],c=[];for(){const s=e.times[t]*r;if(){l.push();for...
```
```internal process
# Error
{"__proto__":"null","toHalfFloat":"function()"{"Math.abs()",t=Tn(t),Bp.floatView[0]=t;const e=Bp.uint32View[0],n=e>>23&511;return Bp.baseTable[n]+(t,-65504,65504)},"fromHalfFloat":"function()"{const e=t>>10;return Bp.uint32View[0]=Bp.mantissaTable[Bp.offsetTable[e]+()]+Bp.exponentTable[e],Bp.floatVi...
```
| constant   | value    |
|:-----------|:---------|
| confetti   | confetti |
| image      | image    |

```internal process
# Error
{"__proto__":"null","DEG2RAD":"Mn","RAD2DEG":"Sn","generateUUID":"wn","clamp":"Tn","euclideanModulo":"An","mapLinear":"function()"{return i+()*(t-e)/(r-i)},"inverseLerp":"function()"{return t!==e?()/(n-t):"0"},"lerp":"Cn","damp":"function()"{"return Cn()"},"pingpong":"function()"{return e-Math.abs()...
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

| constant   | value      |
|:-----------|:-----------|
| Scheduled  | Scheduled  |
| InProgress | InProgress |
| Completed  | Completed  |
| Postponed  | Postponed  |
| Cancelled  | Cancelled  |
| Unused6    | _Unused6   |
| Unused7    | _Unused7   |

| constant          | value             |
|:------------------|:------------------|
| InvalidAuth       | 0                 |
| 0                 | InvalidAuth       |
| UpgradeRequired   | 1                 |
| 1                 | UpgradeRequired   |
| RateLimitExceeded | 2                 |
| 2                 | RateLimitExceeded |
| Assertion         | 3                 |
| 3                 | Assertion         |
| Transient         | 4                 |
| 4                 | Transient         |

| constant          | value             |
|:------------------|:------------------|
| InvalidAuth       | 0                 |
| 0                 | InvalidAuth       |
| UpgradeRequired   | 1                 |
| 1                 | UpgradeRequired   |
| RateLimitExceeded | 2                 |
| 2                 | RateLimitExceeded |
| Assertion         | 3                 |
| 3                 | Assertion         |
| Transient         | 4                 |
| 4                 | Transient         |

| constant          | value             |
|:------------------|:------------------|
| InvalidPin        | 0                 |
| 0                 | InvalidPin        |
| NotRegistered     | 1                 |
| 1                 | NotRegistered     |
| InvalidAuth       | 2                 |
| 2                 | InvalidAuth       |
| UpgradeRequired   | 3                 |
| 3                 | UpgradeRequired   |
| RateLimitExceeded | 4                 |
| 4                 | RateLimitExceeded |
| Assertion         | 5                 |
| 5                 | Assertion         |
| Transient         | 6                 |
| 6                 | Transient         |

| constant         | value           |
|:-----------------|:----------------|
| LIVE_BROADCAST   | liveBroadcast   |
| REPLAY_BROADCAST | replayBroadcast |
| AUDIOSPACE       | audiospace      |
| VOD              | vod             |
| GIF              | gif             |
| SLATE            | slate           |

