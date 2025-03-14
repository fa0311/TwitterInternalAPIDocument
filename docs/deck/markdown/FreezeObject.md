# Twitter Internal Constants Document<br>
This document is entirely auto-generated and may contain errors.<br>
| constant   | value                                                                |
|:-----------|:---------------------------------------------------------------------|
| REQUEST    | rweb/subscriptionPayments/FETCH_SUBSCRIPTION_PRODUCT_DETAILS_REQUEST |
| SUCCESS    | rweb/subscriptionPayments/FETCH_SUBSCRIPTION_PRODUCT_DETAILS_SUCCESS |
| FAILURE    | rweb/subscriptionPayments/FETCH_SUBSCRIPTION_PRODUCT_DETAILS_FAILURE |

| constant   | value                                                                     |
|:-----------|:--------------------------------------------------------------------------|
| REQUEST    | rweb/subscriptionPayments/FETCH_SUBSCRIPTION_PRODUCT_CHECKOUT_URL_REQUEST |
| SUCCESS    | rweb/subscriptionPayments/FETCH_SUBSCRIPTION_PRODUCT_CHECKOUT_URL_SUCCESS |
| FAILURE    | rweb/subscriptionPayments/FETCH_SUBSCRIPTION_PRODUCT_CHECKOUT_URL_FAILURE |

| constant   | value                                                         |
|:-----------|:--------------------------------------------------------------|
| REQUEST    | rweb/subscriptionPayments/FETCH_PRODUCT_SUBSCRIPTIONS_REQUEST |
| SUCCESS    | rweb/subscriptionPayments/FETCH_PRODUCT_SUBSCRIPTIONS_SUCCESS |
| FAILURE    | rweb/subscriptionPayments/FETCH_PRODUCT_SUBSCRIPTIONS_FAILURE |

| constant   | value                                         |
|:-----------|:----------------------------------------------|
| REQUEST    | rweb/subscriptionPayments/TIER_SWITCH_REQUEST |
| SUCCESS    | rweb/subscriptionPayments/TIER_SWITCH_SUCCESS |
| FAILURE    | rweb/subscriptionPayments/TIER_SWITCH_FAILURE |

| constant                       | value                          |
|:-------------------------------|:-------------------------------|
| PaymentMethodFilterFunding     | PaymentMethodFilterFunding     |
| PaymentMethodFilterSpending    | PaymentMethodFilterSpending    |
| PaymentMethodFilterUnspecified | PaymentMethodFilterUnspecified |

| constant      | value         |
|:--------------|:--------------|
| Active        | Active        |
| Canceled      | Canceled      |
| Inactive      | Inactive      |
| Invalid       | Invalid       |
| LoginRequired | LoginRequired |
| Pending       | Pending       |
| Revoked       | Revoked       |
| ScaRequired   | ScaRequired   |
| Unspecified   | Unspecified   |

| constant   | value     |
|:-----------|:----------|
| Banking    | Banking   |
| Ecommerce  | Ecommerce |
| Interest   | Interest  |
| Issuing    | Issuing   |
| Transfer   | Transfer  |

| constant                    | value                       |
|:----------------------------|:----------------------------|
| AuthorizationClosed         | AuthorizationClosed         |
| AuthorizationOpen           | AuthorizationOpen           |
| AwaitingRequestAcceptance   | AwaitingRequestAcceptance   |
| Cancelled                   | Cancelled                   |
| Expired                     | Expired                     |
| Failed                      | Failed                      |
| Hold                        | Hold                        |
| Pending                     | Pending                     |
| PendingRecipientAcceptance  | PendingRecipientAcceptance  |
| PendingRecipientAction      | PendingRecipientAction      |
| PendingRecipientOnboarding  | PendingRecipientOnboarding  |
| PendingRequestAcceptance    | PendingRequestAcceptance    |
| PendingReview               | PendingReview               |
| PinVerificationRequired     | PinVerificationRequired     |
| RejectedByRecipient         | RejectedByRecipient         |
| RequestRejected             | RequestRejected             |
| RequestVerificationRequired | RequestVerificationRequired |
| Settled                     | Settled                     |
| SoftSettled                 | SoftSettled                 |
| Unspecified                 | Unspecified                 |
| VerificationRequired        | VerificationRequired        |

| constant    | value       |
|:------------|:------------|
| Deposit     | Deposit     |
| Payment     | Payment     |
| Refund      | Refund      |
| Reverse     | Reverse     |
| Transfer    | Transfer    |
| Unspecified | Unspecified |
| Withdraw    | Withdraw    |

| constant   | value   |
|:-----------|:--------|
| balance    | balance |
| credit     | credit  |
| debit      | debit   |

| constant   | value    |
|:-----------|:---------|
| small      | small    |
| xLarge     | xLarge   |
| xxxLarge   | xxxLarge |
| xJumbo     | xJumbo   |

| constant                    | value                       |
|:----------------------------|:----------------------------|
| Cancelled                   | Cancelled                   |
| InReview                    | InReview                    |
| RejectedByAutoReview        | RejectedByAutoReview        |
| RejectedByManualReview      | RejectedByManualReview      |
| RejectedByUnsupportedRegion | RejectedByUnsupportedRegion |
| RejectedLimitsExceeded      | RejectedLimitsExceeded      |
| RejectedNotSufficientFunds  | RejectedNotSufficientFunds  |
| Returned                    | Returned                    |
| ReversedByAgent             | ReversedByAgent             |
| Unspecified                 | Unspecified                 |

```internal process
# Error
{[s.RejectedByManualReview]:{"sender":"u","receiver":"u","Component":"i.Z.Attention"},[s.RejectedByAutoReview]:{"sender":"u","receiver":"u","Component":"i.Z.Attention"},[s.InReview]:{"sender":"r","receiver":"r","Component":"i.Z.Attention"},[t.g.PendingRecipientAcceptance]:{"sender":"c","Component":"...
```
| constant   | value    |
|:-----------|:---------|
| Interest   | Interest |
| Premium    | Premium  |

| constant                      | value                         |
|:------------------------------|:------------------------------|
| onboarding                    | onboarding                    |
| upgradeToKycDocumentsVerified | upgradeToKycDocumentsVerified |

| constant   | value   |
|:-----------|:--------|
| credit     | credit  |
| debit      | debit   |

| constant   | value     |
|:-----------|:----------|
| XPayments  | XPayments |

| constant    | value       |
|:------------|:------------|
| reviewPane  | reviewPane  |
| amountPane  | amountPane  |
| successPane | successPane |

| constant   | value     |
|:-----------|:----------|
| termsPane  | termsPane |

| constant        | value           |
|:----------------|:----------------|
| reviewPane      | reviewPane      |
| amountPane      | amountPane      |
| participantPane | participantPane |

| constant   | value   |
|:-----------|:--------|
| bank       | bank    |
| card       | card    |
| x          | x       |

| constant       | value                     |
|:---------------|:--------------------------|
| initiate       | initiate-challenge        |
| complete2fa    | 2fa-complete-challenge    |
| completeKyc    | kyc-complete-challenge    |
| completeDocv   | docv-complete-challenge   |
| completeSelfie | selfie-complete-challenge |

| constant   | value    |
|:-----------|:---------|
| Checking   | Checking |
| Savings    | Savings  |

| constant        | value           |
|:----------------|:----------------|
| AmericanExpress | AmericanExpress |
| Mastercard      | Mastercard      |
| Visa            | Visa            |

| constant      | value         |
|:--------------|:--------------|
| Charge        | Charge        |
| Combo         | Combo         |
| Credit        | Credit        |
| Debit         | Debit         |
| DeferredDebit | DeferredDebit |
| Prepaid       | Prepaid       |

```internal process
# Error
{[h.g.Cancelled]:"Cancelled",[h.g.Failed]:"Failed",[h.g.Expired]:"Expired",[h.g.Pending]:"Pending",[h.g.AuthorizationOpen]:"Pending",[h.g.PendingReview]:"Pending",[h.g.PendingRecipientAction]:"Pending",[h.g.PendingRecipientOnboarding]:"Pending",[h.g.AwaitingRequestAcceptance]:"Pending",[h.g.PendingR...
```
```internal process
# Error
{[m.Checking]:"Checking",[m.Savings]:"Savings"}
```
```internal process
# Error
{[p.Charge]:"Charge",[p.Combo]:"Combo",[p.Debit]:"Debit",[p.Credit]:"Credit",[p.DeferredDebit]:"DeferredDebit",[p.Prepaid]:"Prepaid"}
```
```internal process
# Error
{[y.AmericanExpress]:"American Express",[y.Mastercard]:"Mastercard",[y.Visa]:"Visa"}
```
```internal process
# Error
{[K.D.LoginRequired]:"Login required",[K.D.Invalid]:"Invalid",[K.D.Pending]:"Pending",[K.D.Revoked]:"Revoked",[K.D.Canceled]:"Canceled",[K.D.Inactive]:"Inactive"}
```
```internal process
# Error
{[y.AmericanExpress]:"https://abs.twimg.com/responsive-web/client-web/payment-method-amex.b2cd046a.svg",[y.Mastercard]:"https://abs.twimg.com/responsive-web/client-web/payment-method-mastercard.f126316a.svg",[y.Visa]:"https://abs.twimg.com/responsive-web/client-web/payment-method-visa.c768170a.svg"}
```
| constant     | value             |
|:-------------|:------------------|
| navButtons   | navigationButtons |
| carouselRoot | carouselRoot      |

| constant                | value                     |
|:------------------------|:--------------------------|
| FakeAccount             | fake_account              |
| OffensiveProfileContent | offensive_profile_content |
| SensitiveMedia          | sensitive_media           |
| Timeout                 | timeout                   |

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

```internal process
# Error
{[a.wide]:"500",[a.narrow]:"285",[a.veryNarrow]:"200"}
```
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

| constant   | value   |
|:-----------|:--------|
| ...a       | _       |
| ...C       | _       |
| ...r       | _       |
| ...o       | _       |
| ...i       | _       |
| ...c       | _       |
| ...S       | _       |

```internal process
# Error
{[a.ACTIVIST]:"A.ACTIVISM",[C.COMPANY]:"A.COMPANY",[C.EXECUTIVE]:"A.COMPANY",[r.ENTERTAINMENT_COMPANY]:"A.ENTERTAINMENT",[r.ENTERTAINMENT_INDIVIDUAL]:"A.ENTERTAINMENT",[r.PRODUCTION]:"A.ENTERTAINMENT",[o.CANDIDATE]:"A.GOVERNMENT",[o.OFFICE]:"A.GOVERNMENT",[o.OFFICIAL]:"A.GOVERNMENT",[i.CONTENT_CREAT...
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
{[D.LANDING_PAGE]:{"next":"D.NOTABILITY_CATEGORY_SELECT","scribeComponent":"s.LANDING_PAGE"},[D.NOTABILITY_CATEGORY_SELECT]:{"next":"null","scribeComponent":"s.NOTABILITY_CATEGORY"},[D.ACTIVIST_QUALIFICATIONS]:{"next":"null","scribeComponent":"s.NOTABILITY_METHOD"},[D.ACTIVIST_GOOGLE_TRENDS]:{"next"...
```
| constant      | value              |
|:--------------|:-------------------|
| adRev         | ad_revenue_sharing |
| subscriptions | creator_subs       |
| preRollAds    | pre_roll_video_ads |

```internal process
# Error
{"root":`${"t"}/application`,"eligibility":`${"t"}/application/eligibility`,"pricing":`${"t"}/application/pricing`,"completeProfile":`${"t"}/application/complete_profile`,"submit":`${"t"}/application/submit`,"submitted":`${"t"}/application/submitted`,"waitlisted":`${"t"}/application/waitlisted`,"rej...
```
```internal process
# Error
{"root":`${"t"}/onboarding`,"perksIntro":`${"t"}/onboarding/perks_intro`,"perksDescription":`${"t"}/onboarding/perks_description`,"perksBadges":`${"t"}/onboarding/perks_badges`,"perksConfirm":`${"t"}/onboarding/perks_confirm`,"pricing":`${"t"}/onboarding/pricing`,"pricingConfirm":`${"t"}/onboarding/...
```
```internal process
# Error
{"root":`${"t"}/management`,"perksIntro":`${"t"}/management/perks_intro`,"perksDescription":`${"t"}/management/perks_description`,"perksConfirm":`${"t"}/management/perks_confirm`,"perksPricing":`${"t"}/management/perks_pricing`}
```
| constant      | value         |
|:--------------|:--------------|
| single_line   | singleline    |
| format_inline | format-inline |

| constant           | value   |
|:-------------------|:--------|
| full_time          | r       |
| full_time_contract | i       |
| part_time          | s       |
| contract_to_hire   | o       |

|   constant | value   |
|-----------:|:--------|
|          1 | u       |
|          2 | d       |

| constant   | value                        |
|:-----------|:-----------------------------|
| annually   | {'label': 'u', 'value': '1'} |
| hourly     | {'label': 'd', 'value': '2'} |

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

| constant   | value    |
|:-----------|:---------|
| Fixed      | fixed    |
| Variable   | variable |

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
| wide       | wide       |
| narrow     | narrow     |
| veryNarrow | veryNarrow |

```internal process
# Error
{[n.wide]:"500",[n.narrow]:"285",[n.veryNarrow]:"200"}
```
```internal process
# Error
{"__proto__":"null","DEG2RAD":"at","RAD2DEG":"ot","generateUUID":"lt","clamp":"ct","euclideanModulo":"ht","mapLinear":"function()"{return n+()*(t-e)/(s-n)},"inverseLerp":"function()"{return t!==e?()/(i-t):"0"},"lerp":"ut","damp":"function()"{"return ut()"},"pingpong":"function()"{return e-Math.abs()...
```
```internal process
# Error
{"__proto__":"null","ArcCurve":"Na","CatmullRomCurve3":"za","CubicBezierCurve":"qa","CubicBezierCurve3":"ja","EllipseCurve":"Pa","LineCurve":"Ya","LineCurve3":"class extends Ra"{"constructor()"{"super()",this.type="LineCurve3",this.isLineCurve3=!0,this.v1=t,"this.v2=e"}"getPoint()"{const i=e;return ...
```
| constant   | value   |
|:-----------|:--------|
| type       | number  |
| number     | 0       |
| unit       | null    |

```internal process
# Error
{"minimumRadius":"0","maximumRadius":1/0,"minimumPolarAngle":Math.PI/8,"maximumPolarAngle":Math.PI-Math.PI/8,"minimumAzimuthalAngle":-1/0,"maximumAzimuthalAngle":1/0,"minimumFieldOfView":"10","maximumFieldOfView":"45","interactionPolicy":"always-allow","touchAction":"pan-y"}
```
| constant         | value           |
|:-----------------|:----------------|
| LIVE_BROADCAST   | liveBroadcast   |
| REPLAY_BROADCAST | replayBroadcast |
| AUDIOSPACE       | audiospace      |
| VOD              | vod             |
| GIF              | gif             |
| SLATE            | slate           |

