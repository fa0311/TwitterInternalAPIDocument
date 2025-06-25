# Twitter Internal Constants Document<br>
This document is entirely auto-generated and may contain errors.<br>
| constant    | value        |
|:------------|:-------------|
| joinSpace   | s().h400d7c2 |
| replaySpace | s().g66c8348 |
| comingUp    | s().be6ef5b4 |

| constant   | value   |
|:-----------|:--------|
| Active     | active  |
| Expand     | expand  |
| Remove     | remove  |

| constant     | value        |
|:-------------|:-------------|
| Canceled     | Canceled     |
| Ended        | Ended        |
| NotStarted   | NotStarted   |
| PrePublished | PrePublished |
| Running      | Running      |
| TimedOut     | TimedOut     |

| constant    | value       |
|:------------|:------------|
| scheduled   | scheduled   |
| ended       | ended       |
| live        | live        |
| canceled    | canceled    |
| unavailable | unavailable |
| replay      | replay      |

| constant           |   value |
|:-------------------|--------:|
| general            |       0 |
| employeesOnly      |       1 |
| superFollowersOnly |       2 |

| constant           | value        |
|:-------------------|:-------------|
| relativeDays       | i().c333da63 |
| time               | i().d725a289 |
| weekdayMonthAndDay | i().h8054d91 |
| scheduledStart     | i().d0e7b11b |

| constant   | value               |
|:-----------|:--------------------|
| today      | m().relativeDays()  |
| tomorrow   | m(0).relativeDays() |

| constant     | value        |
|:-------------|:-------------|
| Canceled     | Canceled     |
| Ended        | Ended        |
| NotStarted   | NotStarted   |
| PrePublished | PrePublished |
| Running      | Running      |
| TimedOut     | TimedOut     |

| constant               |   value |
|:-----------------------|--------:|
| RequestSubmitted       |       1 |
| RequestCancelled       |       2 |
| RequestRejected        |       3 |
| RequestApproved        |       4 |
| InvitationSent         |       5 |
| InvitationWithdrawn    |       6 |
| InvitationDeclined     |       7 |
| InvitationAccepted     |       8 |
| StreamNegotiated       |       9 |
| StreamPublished        |      10 |
| StreamEjected          |      11 |
| StreamEnded            |      12 |
| StreamTimedOut         |      13 |
| SessionTerminated      |      14 |
| StreamCountdown        |      15 |
| AdminStreamPublished   |      16 |
| HostStreamPublished    |      17 |
| HostStreamReconnecting |      18 |

| constant                                            | value                                               |
|:----------------------------------------------------|:----------------------------------------------------|
| JanusPollerResponseEnumWebRtcUp                     | JanusPollerResponseEnumWebRtcUp                     |
| JanusPollerResponseEnumMediaVideo                   | JanusPollerResponseEnumMediaVideo                   |
| JanusPollerResponseEnumMediaAudio                   | JanusPollerResponseEnumMediaAudio                   |
| JanusPollerResponseEnumJanusSlowLink                | JanusPollerResponseEnumJanusSlowLink                |
| JanusPollerResponseEnumKeepAlive                    | JanusPollerResponseEnumKeepAlive                    |
| JanusPollerResponseEnumHangup                       | JanusPollerResponseEnumHangup                       |
| JanusPollerResponseEnumDetached                     | JanusPollerResponseEnumDetached                     |
| JanusPollerResponseEnumVideoRoomDestroyed           | JanusPollerResponseEnumVideoRoomDestroyed           |
| JanusPollerResponseEnumEventPublishersList          | JanusPollerResponseEnumEventPublishersList          |
| JanusPollerResponseEnumUpdated                      | JanusPollerResponseEnumUpdated                      |
| JanusPollerResponseEnumEventUnpublished             | JanusPollerResponseEnumEventUnpublished             |
| JanusPollerResponseEnumEventLoggedInUserUnpublished | JanusPollerResponseEnumEventLoggedInUserUnpublished |
| JanusPollerResponseEnumEventKicked                  | JanusPollerResponseEnumEventKicked                  |
| JanusPollerResponseEnumEventLoggedInUserLeaving     | JanusPollerResponseEnumEventLoggedInUserLeaving     |
| JanusPollerResponseEnumEventLeaving                 | JanusPollerResponseEnumEventLeaving                 |
| JanusPollerResponseEnumVideoRoomSlowLink            | JanusPollerResponseEnumVideoRoomSlowLink            |
| JanusPollerResponseEnumEventJoined                  | JanusPollerResponseEnumEventJoined                  |
| JanusPollerResponseEnumEventConfigured              | JanusPollerResponseEnumEventConfigured              |
| JanusPollerResponseEnumEventListenerAttached        | JanusPollerResponseEnumEventListenerAttached        |
| JanusPollerResponseEnumEventStarted                 | JanusPollerResponseEnumEventStarted                 |
| JanusPollerResponseEnumEventLeft                    | JanusPollerResponseEnumEventLeft                    |
| JanusPollerResponseParseError                       | JanusPollerResponseParseError                       |
| JanusPollerResponseEnumUnknown                      | JanusPollerResponseEnumUnknown                      |
| JanusPollerResponseEnumError                        | JanusPollerResponseEnumError                        |

| constant     |   value |
|:-------------|--------:|
| Everyone     |       2 |
| FollowedOnly |       1 |
| InvitedOnly  |       0 |

| constant    |   value |
|:------------|--------:|
| All         |       0 |
| Employees   |       1 |
| Subscribers |       2 |

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

```internal process
# Error
{[r.wide]:"500",[r.narrow]:"300",[r.veryNarrow]:"200"}
```
| constant   | value   |
|:-----------|:--------|
| None       | None    |
| Home       | Home    |
| List       | List    |
| Player     | Player  |
| Setting    | Setting |
| Search     | Search  |
| Unknown    | Unknown |

| constant    | value       |
|:------------|:------------|
| VIDEO       | VIDEO       |
| SHORT_VIDEO | SHORT_VIDEO |

```internal process
# Error
{"__proto__":"null","formatCaption":"function()"{"return()(0,a.WU)"},"formatDay":"function()"{"return()(0,a.WU)"},"formatMonthCaption":"function()"{"return()(0,a.WU)"},"formatWeekNumber":"function()"{return"".concat()},"formatWeekdayName":"function()"{"return()(0,a.WU)"},"formatYearCaption":"functio...
```
```internal process
# Error
{"__proto__":"null","labelDay":"function()"{"return()(0,a.WU)"},"labelMonthDropdown":"function()"{return"Month: "},"labelNext":"function()"{return"Go to next month"},"labelPrevious":"function()"{return"Go to previous month"},"labelWeekNumber":"function()"{return"Week n. ".concat()},"labelWeekday":"f...
```
| constant                | value                   |
|:------------------------|:------------------------|
| AutoSpamDetectorEnabled | AutoSpamDetectorEnabled |
| BanQuotePostEnabled     | BanQuotePostEnabled     |
| BanSelfQuotePostEnabled | BanSelfQuotePostEnabled |
| HideUntilReviewEnabled  | HideUntilReviewEnabled  |

| constant       | value          |
|:---------------|:---------------|
| BannedKeywords | BannedKeywords |

| constant                                       | value                                          |
|:-----------------------------------------------|:-----------------------------------------------|
| Open                                           | Open                                           |
| RestrictedJoinRequestsDisabled                 | RestrictedJoinRequestsDisabled                 |
| RestrictedJoinRequestsRequireAdminApproval     | RestrictedJoinRequestsRequireAdminApproval     |
| RestrictedJoinRequestsRequireModeratorApproval | RestrictedJoinRequestsRequireModeratorApproval |
| SuperFollowRequired                            | SuperFollowRequired                            |

| constant                    | value                       |
|:----------------------------|:----------------------------|
| ChatStarted                 | ChatStarted                 |
| CreationEnabledPut          | CreationEnabledPut          |
| JoinRequestApproved         | JoinRequestApproved         |
| MemberAdded                 | MemberAdded                 |
| MemberLeftViaModeratorBlock | MemberLeftViaModeratorBlock |
| MemberRemoved               | MemberRemoved               |
| MemberRemovedRevert         | MemberRemovedRevert         |
| PinnedTweet                 | PinnedTweet                 |
| SpaceStarted                | SpaceStarted                |
| TweetHidden                 | TweetHidden                 |
| TweetHiddenRevert           | TweetHiddenRevert           |
| TweetReported               | TweetReported               |
| UserInvited                 | UserInvited                 |

```internal process
# Error
{"₊":"+","₋":"-","₌":"=","₍":"()","₀":"0","₁":"1","₂":"2","₃":"3","₄":"4","₅":"5","₆":"6","₇":"7","₈":"8","₉":"9",ₐ:"a",ₑ:"e",ₕ:"h",ᵢ:"i",ⱼ:"j",ₖ:"k",ₗ:"l",ₘ:"m",ₙ:"n",ₒ:"o",ₚ:"p",ᵣ:"r",ₛ:"s",ₜ:"t",ᵤ:"u",ᵥ:"v",ₓ:"x",ᵦ:"β",ᵧ:"γ",ᵨ:"ρ",ᵩ:"ϕ",ᵪ:"χ","⁺":"+","⁻":"-","⁼":"=","⁽":"(\",\"₎\":\")","⁰":"0","¹...
```
| constant          | value              |
|:------------------|:-------------------|
| Intro             | intro              |
| Objective         | objective          |
| Targeting         | targeting          |
| TargetingLocation | targeting_location |
| TargetingGender   | targeting_gender   |
| TargetingKeywords | targeting_keywords |
| BudgetSelect      | budget_select      |
| Review            | review             |
| Payment           | payment            |
| Done              | done               |
| PaymentSelect     | payment_select     |

| constant   | value             |
|:-----------|:------------------|
| Webview    | quick_promote     |
| Rweb       | quick_promote_web |

| constant     |   value |
|:-------------|--------:|
| Objective    |     0.2 |
| Targeting    |     0.4 |
| BudgetSelect |     0.6 |
| Review       |     0.8 |
| Finish       |     1   |

| constant            | value               |
|:--------------------|:--------------------|
| CurrentCountryMatch | currentCountryMatch |
| Match               | match               |
| NoMatch             | noMatch             |

| constant   | value                                                    |
|:-----------|:---------------------------------------------------------|
| AU         | ()(0,c.ju)                                               |
| BR         | ("https://legal.x.com/ads-terms/apac.html")(0,c.ju)      |
| GB         | ("https://legal.x.com/ads-terms/brazil.html")(0,c.ju)    |
| ID         | ("https://legal.x.com/ads-terms/uk.html")(0,c.ju)        |
| JP         | ("https://legal.x.com/ads-terms/indonesia.html")(0,c.ju) |
| NZ         | ("https://legal.x.com/ads-terms/japan.html")(0,c.ju)     |
| US         | ("https://legal.x.com/ads-terms/apac.html")(0,c.ju)      |

| constant   | value                                                                                      |
|:-----------|:-------------------------------------------------------------------------------------------|
| en         | ()(0,c.ju)                                                                                 |
| de         | ("https://business.x.com/en/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |
| es         | ("https://business.x.com/de/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |
| fr         | ("https://business.x.com/es/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |
| ja         | ("https://business.x.com/fr/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |
| pt         | ("https://business.x.com/ja/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |
| ar         | ("https://business.x.com/pt/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |
| zh-cn      | ("https://business.x.com/ar/campaign/quick-promote-conditional-coupon-terms.html")(0,c.ju) |

| constant   | value                                                                          |
|:-----------|:-------------------------------------------------------------------------------|
| en         | ()(0,c.ju)                                                                     |
| de         | ("https://business.x.com/en/campaign/quick-promote-coupon-terms.html")(0,c.ju) |
| es         | ("https://business.x.com/de/campaign/quick-promote-coupon-terms.html")(0,c.ju) |
| fr         | ("https://business.x.com/es/campaign/quick-promote-coupon-terms.html")(0,c.ju) |
| ja         | ("https://business.x.com/fr/campaign/quick-promote-coupon-terms.html")(0,c.ju) |
| pt         | ("https://business.x.com/ja/campaign/quick-promote-coupon-terms.html")(0,c.ju) |
| ar         | ("https://business.x.com/pt/campaign/quick-promote-coupon-terms.html")(0,c.ju) |
| zh-cn      | ("https://business.x.com/ar/campaign/quick-promote-coupon-terms.html")(0,c.ju) |

| constant   | value   |
|:-----------|:--------|
| START      | start   |
| LOADING    | loading |
| SENT       | sent    |

```internal process
# Error
{[E.pl.AUTHENTICITY_TYPE_SELECT]:"()"{"notabilityCategory":"e","notabilitySubcategory":"t","userEmail":"i"}{"type":"radio","props":{"description":"N().description","getNextFormStep":e=>{"switch()"{"case E.L_.IDENTITY_DOCUMENT":return E.pl.INTAKE_TYPE_SELECT;case E.L_.EMAIL:return E.pl.EMAIL_VERIFICA...
```
```internal process
# Error
{[E.pl.NOTABILITY_CATEGORY_SELECT]:"()"{"followersEligible":"e=!1","mentionsEligible":"t=!1"}{"type":"radio","props":{"description":"o.$c.description","getNextFormStep":e=>{"switch()"{"case E.eV.ACTIVISM":return E.pl.ACTIVIST_SUBCATEGORY;case E.eV.INFLUENCER_OTHER:return E.pl.INFLUENCER_SUBCATEGORY;...
```
| constant   | value   |
|:-----------|:--------|
| ...T       | _       |
| ...n       | _       |
| ...l.k     | _       |

| constant   | value     |
|:-----------|:----------|
| AppStore   | AppStore  |
| PlayStore  | PlayStore |
| Stripe     | Stripe    |
| Web        | Web       |

| constant    | value       |
|:------------|:------------|
| InitialSale | InitialSale |
| Renewal     | Renewal     |

| constant   | value    |
|:-----------|:---------|
| UP         | up       |
| DOWN       | down     |
| NOCHANGE   | nochange |

| constant   | value      |
|:-----------|:-----------|
| SINGLE     | SINGLE     |
| COMPARISON | COMPARISON |

| constant   | value        |
|:-----------|:-------------|
| preMarket  | g().a50aaa10 |
| today      | g().g02dacc0 |
| afterHours | g().dd614d10 |

| constant                   | value   |
|:---------------------------|:--------|
| PRICE_LEVEL_UNSPECIFIED    |         |
| PRICE_LEVEL_FREE           |         |
| PRICE_LEVEL_INEXPENSIVE    | $       |
| PRICE_LEVEL_MODERATE       | $$      |
| PRICE_LEVEL_EXPENSIVE      | $$$     |
| PRICE_LEVEL_VERY_EXPENSIVE | $$$$    |

| constant   | value                                        |
|:-----------|:---------------------------------------------|
| OVERVIEW   | {'id': 'OVERVIEW', 'label': 'a().d59dbf8a'}  |
| MATCHES    | {'id': 'GAMES', 'label': 'a().e2811afc'}     |
| STANDINGS  | {'id': 'STANDINGS', 'label': 'a().j081fa34'} |

| constant     | value        |
|:-------------|:-------------|
| Cashback     | Cashback     |
| Unspecified  | Unspecified  |
| UserInterest | UserInterest |
| UserMain     | UserMain     |

| constant   | value    |
|:-----------|:---------|
| Checking   | Checking |
| Savings    | Savings  |

| constant                                                                      | value                                                                         |
|:------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| BankCardLinkingSessionRejectionReasonCardAlreadyExists                        | BankCardLinkingSessionRejectionReasonCardAlreadyExists                        |
| BankCardLinkingSessionRejectionReasonInaccurateCardDetails                    | BankCardLinkingSessionRejectionReasonInaccurateCardDetails                    |
| BankCardLinkingSessionRejectionReasonProviderDidNotCarryNameVerificationCheck | BankCardLinkingSessionRejectionReasonProviderDidNotCarryNameVerificationCheck |
| BankCardLinkingSessionRejectionReasonProviderFailedToAuthorizeCard            | BankCardLinkingSessionRejectionReasonProviderFailedToAuthorizeCard            |
| BankCardLinkingSessionRejectionReasonProviderFailedToVerifyAddress            | BankCardLinkingSessionRejectionReasonProviderFailedToVerifyAddress            |
| BankCardLinkingSessionRejectionReasonProviderFailedToVerifyCardholderName     | BankCardLinkingSessionRejectionReasonProviderFailedToVerifyCardholderName     |
| BankCardLinkingSessionRejectionReasonProviderInternalFailure                  | BankCardLinkingSessionRejectionReasonProviderInternalFailure                  |
| BankCardLinkingSessionRejectionReasonUnspecified                              | BankCardLinkingSessionRejectionReasonUnspecified                              |
| BankCardLinkingSessionRejectionReasonUnsupportedCardType                      | BankCardLinkingSessionRejectionReasonUnsupportedCardType                      |
| BankCardLinkingSessionRejectionReasonUnsupportedIssuerCountry                 | BankCardLinkingSessionRejectionReasonUnsupportedIssuerCountry                 |
| BankCardLinkingSessionRejectionReasonUnusableCard                             | BankCardLinkingSessionRejectionReasonUnusableCard                             |

| constant                                | value                                   |
|:----------------------------------------|:----------------------------------------|
| BankCardLinkingSessionStatusAuthorized  | BankCardLinkingSessionStatusAuthorized  |
| BankCardLinkingSessionStatusPending     | BankCardLinkingSessionStatusPending     |
| BankCardLinkingSessionStatusRejected    | BankCardLinkingSessionStatusRejected    |
| BankCardLinkingSessionStatusUnspecified | BankCardLinkingSessionStatusUnspecified |

| constant                               | value                                  |
|:---------------------------------------|:---------------------------------------|
| BankCardLinkingSessionThemeDark        | BankCardLinkingSessionThemeDark        |
| BankCardLinkingSessionThemeDimmed      | BankCardLinkingSessionThemeDimmed      |
| BankCardLinkingSessionThemeLight       | BankCardLinkingSessionThemeLight       |
| BankCardLinkingSessionThemeUnspecified | BankCardLinkingSessionThemeUnspecified |

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

| constant                         | value                            |
|:---------------------------------|:---------------------------------|
| ClaimTransferDecisionAccept      | ClaimTransferDecisionAccept      |
| ClaimTransferDecisionReject      | ClaimTransferDecisionReject      |
| ClaimTransferDecisionUnspecified | ClaimTransferDecisionUnspecified |

| constant   | value   |
|:-----------|:--------|
| Usd        | Usd     |

| constant           | value              |
|:-------------------|:-------------------|
| ContactSupport     | ContactSupport     |
| Deposit            | Deposit            |
| GetPremium         | GetPremium         |
| KycDocumentUpload  | KycDocumentUpload  |
| KycVerification    | KycVerification    |
| LearnMore          | LearnMore          |
| Questionnaire      | Questionnaire      |
| SelfieVerification | SelfieVerification |
| SetupPasskey       | SetupPasskey       |

| constant   | value   |
|:-----------|:--------|
| Alert      | Alert   |
| Info       | Info    |
| Warning    | Warning |

| constant   | value     |
|:-----------|:----------|
| Geography  | Geography |
| Interest   | Interest  |
| Premium    | Premium   |

| constant                     | value                        |
|:-----------------------------|:-----------------------------|
| DocumentTypeMonthlyStatement | DocumentTypeMonthlyStatement |
| DocumentTypeUnspecified      | DocumentTypeUnspecified      |

| constant   | value   |
|:-----------|:--------|
| Adyen      | Adyen   |
| Plaid      | Plaid   |
| Stripe     | Stripe  |
| Unknown    | Unknown |

| constant                               | value                                  |
|:---------------------------------------|:---------------------------------------|
| IssuedCardReplacementReasonDamaged     | IssuedCardReplacementReasonDamaged     |
| IssuedCardReplacementReasonExpired     | IssuedCardReplacementReasonExpired     |
| IssuedCardReplacementReasonLost        | IssuedCardReplacementReasonLost        |
| IssuedCardReplacementReasonStolen      | IssuedCardReplacementReasonStolen      |
| IssuedCardReplacementReasonUnspecified | IssuedCardReplacementReasonUnspecified |

| constant                            | value                               |
|:------------------------------------|:------------------------------------|
| IssuedCardShippingStatusCanceled    | IssuedCardShippingStatusCanceled    |
| IssuedCardShippingStatusDelivered   | IssuedCardShippingStatusDelivered   |
| IssuedCardShippingStatusFailure     | IssuedCardShippingStatusFailure     |
| IssuedCardShippingStatusPending     | IssuedCardShippingStatusPending     |
| IssuedCardShippingStatusReturned    | IssuedCardShippingStatusReturned    |
| IssuedCardShippingStatusShipped     | IssuedCardShippingStatusShipped     |
| IssuedCardShippingStatusSubmitted   | IssuedCardShippingStatusSubmitted   |
| IssuedCardShippingStatusUnspecified | IssuedCardShippingStatusUnspecified |

| constant                  | value                     |
|:--------------------------|:--------------------------|
| IssuedCardTypePhysical    | IssuedCardTypePhysical    |
| IssuedCardTypeUnspecified | IssuedCardTypeUnspecified |
| IssuedCardTypeVirtual     | IssuedCardTypeVirtual     |

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
| Cashback   | Cashback  |
| Ecommerce  | Ecommerce |
| Incentive  | Incentive |
| Interest   | Interest  |
| Issuing    | Issuing   |
| Transfer   | Transfer  |

| constant   | value   |
|:-----------|:--------|
| Ach        | Ach     |
| Aft        | Aft     |
| FedNow     | FedNow  |
| Rtp        | Rtp     |

| constant     | value        |
|:-------------|:-------------|
| Ach          | Ach          |
| DomesticWire | DomesticWire |
| FedNow       | FedNow       |
| Oct          | Oct          |
| Rtp          | Rtp          |

| constant                           | value                              |
|:-----------------------------------|:-----------------------------------|
| RequestTransferDecisionAccept      | RequestTransferDecisionAccept      |
| RequestTransferDecisionReject      | RequestTransferDecisionReject      |
| RequestTransferDecisionUnspecified | RequestTransferDecisionUnspecified |

| constant                      | value                         |
|:------------------------------|:------------------------------|
| Age                           | Age                           |
| Allowlist                     | Allowlist                     |
| BirthDate                     | BirthDate                     |
| Geography                     | Geography                     |
| PhoneNumber                   | PhoneNumber                   |
| PremiumOrVerifiedOrganization | PremiumOrVerifiedOrganization |
| Safety                        | Safety                        |
| Sanctions                     | Sanctions                     |
| TwoFactorAuth                 | TwoFactorAuth                 |
| Unknown                       | Unknown                       |

| constant                                 | value                                    |
|:-----------------------------------------|:-----------------------------------------|
| ThreeDsAuthenticationResponseAllow       | ThreeDsAuthenticationResponseAllow       |
| ThreeDsAuthenticationResponseDeny        | ThreeDsAuthenticationResponseDeny        |
| ThreeDsAuthenticationResponseUnspecified | ThreeDsAuthenticationResponseUnspecified |

| constant    | value       |
|:------------|:------------|
| Chip        | Chip        |
| Contactless | Contactless |
| KeyedIn     | KeyedIn     |
| Online      | Online      |
| Swipe       | Swipe       |

| constant             | value                |
|:---------------------|:---------------------|
| Ach                  | Ach                  |
| Aft                  | Aft                  |
| Oct                  | Oct                  |
| ProviderBankTransfer | ProviderBankTransfer |
| Wire                 | Wire                 |

| constant       | value          |
|:---------------|:---------------|
| Clock          | Clock          |
| CreditCardBack | CreditCardBack |
| FollowArrows   | FollowArrows   |
| PeopleStroke   | PeopleStroke   |

| constant                            | value                               |
|:------------------------------------|:------------------------------------|
| AuthorizationClosed                 | AuthorizationClosed                 |
| AuthorizationOpen                   | AuthorizationOpen                   |
| AwaitingRequestAcceptance           | AwaitingRequestAcceptance           |
| AwaitingUnrecognizedConfirmation    | AwaitingUnrecognizedConfirmation    |
| Cancelled                           | Cancelled                           |
| CreditedAwaitingSettlement          | CreditedAwaitingSettlement          |
| Expired                             | Expired                             |
| Failed                              | Failed                              |
| Hold                                | Hold                                |
| Pending                             | Pending                             |
| PendingFundingTransactionSettlement | PendingFundingTransactionSettlement |
| PendingRecipientAcceptance          | PendingRecipientAcceptance          |
| PendingRecipientAction              | PendingRecipientAction              |
| PendingRecipientOnboarding          | PendingRecipientOnboarding          |
| PendingRequestAcceptance            | PendingRequestAcceptance            |
| PendingReview                       | PendingReview                       |
| PinVerificationRequired             | PinVerificationRequired             |
| RejectedByRecipient                 | RejectedByRecipient                 |
| RequestRejected                     | RequestRejected                     |
| RequestVerificationRequired         | RequestVerificationRequired         |
| Settled                             | Settled                             |
| SoftSettled                         | SoftSettled                         |
| Unspecified                         | Unspecified                         |
| VerificationRequired                | VerificationRequired                |

| constant      | value         |
|:--------------|:--------------|
| AtmWithdrawal | AtmWithdrawal |
| Deposit       | Deposit       |
| DisputeCredit | DisputeCredit |
| Payment       | Payment       |
| Refund        | Refund        |
| Reverse       | Reverse       |
| Transfer      | Transfer      |
| Unspecified   | Unspecified   |
| Withdraw      | Withdraw      |

| constant   | value    |
|:-----------|:---------|
| Delayed    | Delayed  |
| RealTime   | RealTime |

| constant                          | value                             |
|:----------------------------------|:----------------------------------|
| Cancelled                         | Cancelled                         |
| InReview                          | InReview                          |
| RejectedByAutoReview              | RejectedByAutoReview              |
| RejectedByManualReview            | RejectedByManualReview            |
| RejectedByUnsupportedRegion       | RejectedByUnsupportedRegion       |
| RejectedCardInactive              | RejectedCardInactive              |
| RejectedCardPaymentsDisabled      | RejectedCardPaymentsDisabled      |
| RejectedLimitsExceeded            | RejectedLimitsExceeded            |
| RejectedMissingRequiredPermission | RejectedMissingRequiredPermission |
| RejectedNotSufficientFunds        | RejectedNotSufficientFunds        |
| Returned                          | Returned                          |
| ReversedByAgent                   | ReversedByAgent                   |
| UnrecognizedActivityConfirmed     | UnrecognizedActivityConfirmed     |
| UnrecognizedActivityRejected      | UnrecognizedActivityRejected      |
| Unspecified                       | Unspecified                       |

| constant       | value          |
|:---------------|:---------------|
| BackupCode     | BackupCode     |
| Passkey        | Passkey        |
| Sms            | Sms            |
| Totp           | Totp           |
| U2fSecurityKey | U2fSecurityKey |

| constant                               | value                                  |
|:---------------------------------------|:---------------------------------------|
| UnrecognizedPaymentDecisionAccept      | UnrecognizedPaymentDecisionAccept      |
| UnrecognizedPaymentDecisionReject      | UnrecognizedPaymentDecisionReject      |
| UnrecognizedPaymentDecisionUnspecified | UnrecognizedPaymentDecisionUnspecified |

| constant   | value    |
|:-----------|:---------|
| small      | small    |
| xLarge     | xLarge   |
| xxLarge    | xxLarge  |
| xxxLarge   | xxxLarge |
| xJumbo     | xJumbo   |

```internal process
# Error
{[v.S.Alert]:"danger",[v.S.Info]:"primary",[v.S.Warning]:"warning"}
```
```internal process
# Error
{[v.S.Alert]:"u.default",[v.S.Info]:"p.default",[v.S.Warning]:"u.default"}
```
```internal process
# Error
{"InsufficientFunds":{"message":"Your account balance is insufficient to make this transfer. Please fund your account and then try again.","action":{"link":"l.IN","label":"Deposit"}},"InvalidReceiver":{"message":"Transfers to this account are unavailable right now. Please try again later."},"Invalid...
```
```internal process
# Error
{[T.g.Cancelled]:"Cancelled",[T.g.Failed]:"Failed",[T.g.Expired]:"Expired",[T.g.Pending]:"Pending",[T.g.Hold]:"Pending",[T.g.AuthorizationOpen]:"Pending",[T.g.AwaitingUnrecognizedConfirmation]:"Awaiting approval",[T.g.PendingReview]:"Under review",[T.g.PendingRecipientAction]:"Pending",[T.g.PendingR...
```
```internal process
# Error
{[D.P.RejectedLimitsExceeded]:"Declined due to exceeded limits",[D.P.InReview]:"Under review",[D.P.RejectedByUnsupportedRegion]:"Unsupported region",[D.P.RejectedNotSufficientFunds]:"Declined due to insufficient funds",[D.P.RejectedCardPaymentsDisabled]:"Flagged as suspicious",[D.P.UnrecognizedActiv...
```
```internal process
# Error
{[T.g.PendingRecipientAcceptance]:"F",[T.g.PendingRecipientOnboarding]:"F",[T.g.PendingRecipientAction]:"F"}
```
```internal process
# Error
{[T.g.AwaitingRequestAcceptance]:"F",[T.g.PendingRequestAcceptance]:"F",[T.g.RequestVerificationRequired]:"F"}
```
```internal process
# Error
{[g.t.Checking]:"Checking",[g.t.Savings]:"Savings"}
```
```internal process
# Error
{[w.W.IssuedCardTypePhysical]:"Physical Card",[w.W.IssuedCardTypeVirtual]:"Virtual Card"}
```
```internal process
# Error
{[m.l.Charge]:"Charge",[m.l.Combo]:"Combo",[m.l.Debit]:"Debit",[m.l.Credit]:"Credit",[m.l.DeferredDebit]:"DeferredDebit",[m.l.Prepaid]:"Prepaid"}
```
```internal process
# Error
{[f.U.AmericanExpress]:"American Express",[f.U.Mastercard]:"Mastercard",[f.U.Visa]:"Visa"}
```
```internal process
# Error
{[b.D.LoginRequired]:"Login required",[b.D.Invalid]:"Invalid",[b.D.Pending]:"Pending",[b.D.Revoked]:"Revoked",[b.D.Canceled]:"Canceled",[b.D.Inactive]:"Inactive"}
```
```internal process
# Error
{[R.y.Online]:"Online",[R.y.Chip]:"Chip",[R.y.Contactless]:"Contactless",[R.y.KeyedIn]:"Keyed In",[R.y.Swipe]:"Swipe"}
```
```internal process
# Error
{[P.B.Ach]:"Bank Transfer ()",[P.B.Aft]:"Funds Transfer (ACH)",[P.B.Oct]:"Instant Payment (AFT)",[P.B.Wire]:"Wire Transfer",[P.B.ProviderBankTransfer]:"Third-Party Bank Transfer"}
```
```internal process
# Error
{[f.U.AmericanExpress]:"https://abs.twimg.com/responsive-web/client-web/payment-method-amex.b2cd046a.svg",[f.U.Mastercard]:"https://abs.twimg.com/responsive-web/client-web/payment-method-mastercard.f126316a.svg",[f.U.Visa]:"https://abs.twimg.com/responsive-web/client-web/payment-method-visa.c768170a...
```
| constant                     | value                        |
|:-----------------------------|:-----------------------------|
| ApplicationInReview          | ApplicationInReview          |
| ApplicationRequestInfo       | ApplicationRequestInfo       |
| NotStart                     | NotStart                     |
| Onboarded                    | Onboarded                    |
| UpfrontApplicationInProgress | UpfrontApplicationInProgress |
| UpfrontPromotionInProgress   | UpfrontPromotionInProgress   |

| constant           | value   |
|:-------------------|:--------|
| full_time          | r       |
| full_time_contract | t       |
| part_time          | s       |
| contract_to_hire   | u       |

|   constant | value   |
|-----------:|:--------|
|          1 | d       |
|          2 | c       |

| constant   | value                        |
|:-----------|:-----------------------------|
| annually   | {'label': 'd', 'value': '1'} |
| hourly     | {'label': 'c', 'value': '2'} |

| constant   | value     |
|:-----------|:----------|
| Affiliate  | Affiliate |

| constant   | value                                                                                                                |
|:-----------|:---------------------------------------------------------------------------------------------------------------------|
| apple      | https://apps.apple.com/account/billing                                                                               |
| google     | https://play.google.com/store/account/subscriptions?sku=com.twitter.google.rogue.one.1.1&package=com.twitter.android |

| constant   | value   |
|:-----------|:--------|
| Badge      | Badge   |
| Inline     | Inline  |

| constant          | value             |
|:------------------|:------------------|
| AutomatedLabel    | AutomatedLabel    |
| BusinessLabel     | BusinessLabel     |
| ElectionsLabel    | ElectionsLabel    |
| GenericBadgeLabel | GenericBadgeLabel |
| GenericInfoLabel  | GenericInfoLabel  |
| OfficialLabel     | OfficialLabel     |
| Reserved4         | Reserved4         |
| Reserved5         | Reserved5         |
| Reserved6         | Reserved6         |
| Reserved7         | Reserved7         |

| constant           | value   |
|:-------------------|:--------|
| __proto__          | null    |
| assert             | _       |
| requireNonNull     | d       |
| requireInstance    | p       |
| abstractMethodFail | m       |

| constant   | value    |
|:-----------|:---------|
| confetti   | confetti |
| image      | image    |

| constant              | value   |
|:----------------------|:--------|
| __proto__             | null    |
| ArcCurve              | bh      |
| CatmullRomCurve3      | Eh      |
| CubicBezierCurve      | Dh      |
| CubicBezierCurve3     | Rh      |
| EllipseCurve          | Mh      |
| LineCurve             | Nh      |
| LineCurve3            | Oh      |
| QuadraticBezierCurve  | zh      |
| QuadraticBezierCurve3 | Uh      |
| SplineCurve           | Fh      |

| constant             | value   |
|:---------------------|:--------|
| __proto__            | null    |
| BoxGeometry          | ls      |
| CapsuleGeometry      | Wh      |
| CircleGeometry       | Hh      |
| ConeGeometry         | qh      |
| CylinderGeometry     | jh      |
| DodecahedronGeometry | Yh      |
| EdgesGeometry        | Qh      |
| ExtrudeGeometry      | Lc      |
| IcosahedronGeometry  | Ic      |
| LatheGeometry        | Gh      |
| OctahedronGeometry   | Dc      |
| PlaneGeometry        | Es      |
| PolyhedronGeometry   | Xh      |
| RingGeometry         | Rc      |
| ShapeGeometry        | Nc      |
| SphereGeometry       | Oc      |
| TetrahedronGeometry  | zc      |
| TorusGeometry        | Uc      |
| TorusKnotGeometry    | Fc      |
| TubeGeometry         | Bc      |
| WireframeGeometry    | kc      |

```internal process
# Error
{"__proto__":"null","arraySlice":"Qc","convertArray":"tu","isTypedArray":"eu","getKeyframeOrder":"iu","sortedArray":"nu","flattenJSON":"ru","subclip":"function()"{const s=t.clone();s.name=e;const a=[];for(){const e=s.tracks[t],o=e.getValueSize(),l=[],h=[];for(){const s=e.times[t]*r;if(){l.push();for...
```
```internal process
# Error
{"__proto__":"null","toHalfFloat":"function()"{"Math.abs()",t=xi(t),Op.floatView[0]=t;const e=Op.uint32View[0],i=e>>23&511;return Op.baseTable[i]+(t,-65504,65504)},"fromHalfFloat":"function()"{const e=t>>10;return Op.uint32View[0]=Op.mantissaTable[Op.offsetTable[e]+()]+Op.exponentTable[e],Op.floatVi...
```
```internal process
# Error
{"__proto__":"null","DEG2RAD":"gi","RAD2DEG":"vi","generateUUID":"_i","clamp":"xi","euclideanModulo":"yi","mapLinear":"function()"{return n+()*(t-e)/(r-n)},"inverseLerp":"function()"{return t!==e?()/(i-t):"0"},"lerp":"Mi","damp":"function()"{"return Mi()"},"pingpong":"function()"{return e-Math.abs()...
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

