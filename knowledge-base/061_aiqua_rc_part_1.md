---
source: notebooklm_export
file_id: "061"
filename: "061_aiqua_rc_part_1.txt.txt"
doc_type: "reference_card"
product: "AIQUA"
content_type: "txt"
language: "en"
guide_summary: "This comprehensive documentation outlines AIQUA's capabilities for **personalized marketing campaigns** by leveraging extensive user data. The platform emphasizes collecting a **holistic view of users** by integrating both **online and offline data**, which includes attributes like birthdays and events such as in-store purchases. Once data is gathered, AIQUA enables **audience segmentation** for targeted outreach and supports various **campaign types** across multiple channels, including web pus"
guide_keywords: "User Data Collection, Audience Segmentation, Campaign Management, Third-Party Integrations, Web Push"
---

# 061 aiqua rc part 1

Getting Started with AIQUA [0]

https://docs.aiqua.appier.com/docs/getting-started-with-aiqua



Using AIQUA, you can engage your customers across various channels from a single platform. In a nutshell, AIQUA allows you to:

Collect User Data including user behaviors on your websites and apps as well as your own set of user data (e.g. your CRM system).

Segment Audience using the data collected as conditions.

Create customized Campaigns to target different audience segments.

Access Performance Reports to understand how your campaigns are performing. 

Having user data is crucial in creating campaigns that are relevant to your users. By integrating with Appier Enterprise Service SDK ("Appier SDK"), you will be able to collect the following data about your online users.

User attributes from your websites and apps (e.g. email submitted through account registration)

User events from your websites and apps (e.g. a user added products to cart)

In addition, you may have your own set of data for your registered members (e.g. your CRM system) that you can upload to AIQUA.

Offline user attributes (e.g. user's birthday from your CRM system)

Offline user events (e.g. purchase data of a registered member in your physical stores)

By linking the above online and offline data, AIQUA helps you gain a holistic view of your users across platforms. See User Data Collection for more details.

Once you have data about your users, you can segment audience and create personalized campaigns. Here's an example on how you can use AIQUA to reduce cart abandonment.

Collect User Data: Some users logged in to your website and added products to their shopping cart. By having purchase data from your online and offline platforms on AIQUA, you can single out the users who did not proceed to checkout.

Segment Audience: On AIQUA dashboard, you can create an audience segment to include users who have added products to cart, and then exclude those who have purchased. You now have a segment of users who left products in the cart without checking out.



Getting Started with AIQUA [1]

https://docs.aiqua.appier.com/docs/getting-started-with-aiqua



Create Customized Campaign: Now you can create an email campaign to remind users about products forgotten in their carts and offer free shipping. By utilizing AIQUA's Dynamic Content feature, you can include each user's name and information about the actual products in each user's cart.

To be able to collect user data and create campaigns, you will need to complete the following integrations.

First, you need to integrate your website and app with the Appier Enterprise Service SDK ("Appier SDK"). This enables your website and app to show campaign notifications to users, and to collect basic user data such as cookies, device types, and site visits. 

See instructions on how to integrate different platforms:

Website: See Integrating with the Appier Web SDK.

Android App: See Android SDK Overview.

iOS App: See iOS SDK Overview.

📘Note:

If your website is using multiple domains (e.g. www.abc.com, www.abc2.com) or subdomains (e.g. blog.abc.com, shop.abc.com), refer to Cross-Domain Integration.

If your mobile app uses React Native framework, refer to:

React Native: See Installing the SDK via React Native.

The basic user data Appier SDK can automatically collect by default is called default user data. In addition to default user data, you need to decide what other data you want to collect about your users and set your website and app to collect these custom user data.

User Data Collection: Read the overview on how user data is tracked and used in AIQUA.

Default user data: See the list of default events and attributes collected by Appier SDK.

Custom User Data: See how to collect custom events and attributes.

If you have additional user data in your database (e.g. your CRM system), you can upload these data to AIQUA using these methods:

Upload via dashboard as a CSV file 

Upload via API

If you want to send campaigns via email, SMS, LINE, or Kakao, you need to integrate AIQUA with these third-party services.

Email: See Email Integration.

SMS: See SMS Integration. 

LINE: See LINE Integration.



Getting Started with AIQUA [2]

https://docs.aiqua.appier.com/docs/getting-started-with-aiqua



Email: See Email Integration.

SMS: See SMS Integration. 

LINE: See LINE Integration.

Kakao: See Kakao Campaign Quick Start. 

Updated 7 months ago Table of Contents

What Can I Know About My Users?

What Can I Do with AIQUA?

1. Integrate Platforms with Appier SDK

2. Collect Custom User Data

3. Upload Offline User Data

4. Third-Party Integrations



AIQUA Resource Center

https://docs.aiqua.appier.com/



HomeGuidesAPI ReferenceAnnouncements中文首頁日本語ホーム한국어홈Home



Getting Started with AIQUA [0]

https://docs.aiqua.appier.com/docs



Using AIQUA, you can engage your customers across various channels from a single platform. In a nutshell, AIQUA allows you to:

Collect User Data including user behaviors on your websites and apps as well as your own set of user data (e.g. your CRM system).

Segment Audience using the data collected as conditions.

Create customized Campaigns to target different audience segments.

Access Performance Reports to understand how your campaigns are performing. 

Having user data is crucial in creating campaigns that are relevant to your users. By integrating with Appier Enterprise Service SDK ("Appier SDK"), you will be able to collect the following data about your online users.

User attributes from your websites and apps (e.g. email submitted through account registration)

User events from your websites and apps (e.g. a user added products to cart)

In addition, you may have your own set of data for your registered members (e.g. your CRM system) that you can upload to AIQUA.

Offline user attributes (e.g. user's birthday from your CRM system)

Offline user events (e.g. purchase data of a registered member in your physical stores)

By linking the above online and offline data, AIQUA helps you gain a holistic view of your users across platforms. See User Data Collection for more details.

Once you have data about your users, you can segment audience and create personalized campaigns. Here's an example on how you can use AIQUA to reduce cart abandonment.

Collect User Data: Some users logged in to your website and added products to their shopping cart. By having purchase data from your online and offline platforms on AIQUA, you can single out the users who did not proceed to checkout.

Segment Audience: On AIQUA dashboard, you can create an audience segment to include users who have added products to cart, and then exclude those who have purchased. You now have a segment of users who left products in the cart without checking out.



Getting Started with AIQUA [1]

https://docs.aiqua.appier.com/docs



Create Customized Campaign: Now you can create an email campaign to remind users about products forgotten in their carts and offer free shipping. By utilizing AIQUA's Dynamic Content feature, you can include each user's name and information about the actual products in each user's cart.

To be able to collect user data and create campaigns, you will need to complete the following integrations.

First, you need to integrate your website and app with the Appier Enterprise Service SDK ("Appier SDK"). This enables your website and app to show campaign notifications to users, and to collect basic user data such as cookies, device types, and site visits. 

See instructions on how to integrate different platforms:

Website: See Integrating with the Appier Web SDK.

Android App: See Android SDK Overview.

iOS App: See iOS SDK Overview.

📘Note:

If your website is using multiple domains (e.g. www.abc.com, www.abc2.com) or subdomains (e.g. blog.abc.com, shop.abc.com), refer to Cross-Domain Integration.

If your mobile app uses React Native framework, refer to:

React Native: See Installing the SDK via React Native.

The basic user data Appier SDK can automatically collect by default is called default user data. In addition to default user data, you need to decide what other data you want to collect about your users and set your website and app to collect these custom user data.

User Data Collection: Read the overview on how user data is tracked and used in AIQUA.

Default user data: See the list of default events and attributes collected by Appier SDK.

Custom User Data: See how to collect custom events and attributes.

If you have additional user data in your database (e.g. your CRM system), you can upload these data to AIQUA using these methods:

Upload via dashboard as a CSV file 

Upload via API

If you want to send campaigns via email, SMS, LINE, or Kakao, you need to integrate AIQUA with these third-party services.

Email: See Email Integration.

SMS: See SMS Integration. 

LINE: See LINE Integration.



Getting Started with AIQUA [2]

https://docs.aiqua.appier.com/docs



Email: See Email Integration.

SMS: See SMS Integration. 

LINE: See LINE Integration.

Kakao: See Kakao Campaign Quick Start. 

Updated 7 months ago Table of Contents

What Can I Know About My Users?

What Can I Do with AIQUA?

1. Integrate Platforms with Appier SDK

2. Collect Custom User Data

3. Upload Offline User Data

4. Third-Party Integrations



Getting Started

https://docs.aiqua.appier.com/reference



The AIQUA API endpoints provide programmatic access to several platform features, such as report exports, and Recommendation, and offline data uploading.

When making requests to many of the AIQUA API endpoints, you'll need to supply your account's app ID and API token in the request header.

The following sample cURL request demonstrates what your header should look like:

curl -X HTTP-METHOD 'https://api.enterprise.appier.net/api/v3' \

-H "Authorization: Token " \

-H "appid: "

Click your account name in the lower-left corner of the screen.

Select Account Settings. From the settings page, you'll be able to find your App ID and API Token.

📘NoteDepending on the access rights of your account, the API token may not be visible. If you can't view the API token, contact your account administrator. For details about account permissions, see Access Control List (ACL).

Table of Contents

Overview

Authentication

Retrieving your app ID and API key



Announcements [0]

https://docs.aiqua.appier.com/changelog



Introducing the Appier Enterprise Console (AEC)We're excited to announce that starting this month, we're initiating a rollout of Appier's new, unified enterprise platform: the Appier Enterprise Console, or AEC for short. Aiming to provide a seamless and consistent user experience, AEC will serve as the centralized, cross-product management platform for Appier's full-funnel marketing solutions, including AIQUA, BotBonnie, AIRIS, and AIXON.Single Sign-Onabout 1 year ago by AppierStarting from February 20, 2024, Single Sign-On (SSO) is applied to the following consoles, meaning that these consoles now share the same login credentials. New email sender requirements from Gmail and Yahooover 1 year ago by AppierStarting in early 2024, Gmail and Yahoo will begin enforcing new measures for bulk senders. These new email sender requirements are aimed at enhancing security and reducing spam in your inbox:Scheduled Maintenance, Tuesday Jun 28, 5:00 - 7:00 AM (UTC+8)almost 3 years ago by AppierOn Tuesday, June 28th at 5:00 AM (UTC+8), AIQUA will have a scheduled maintenance for approximately two hours. During the maintenance period, several AIQUA features will be unavailable and campaign deliveries will be paused. Enhancements to Campaign Reportsalmost 3 years ago by AppierIn order to enhance the quality and accuracy of campaign performance data, AIQUA has removed web bot traffic from Applebot, Googlebot, and AdsBot from campaign reports, effective May 31, 2022.Scheduled Maintenance: Thursday March 24, 5:00-8:00 AM (UTC+8)about 3 years ago by AppierOn Thursday, March 24 at 5:00 AM (UTC+8), AIQUA will have a scheduled downtime to release several new features, including single sign-on and two-factor authentication. The AIQUA Dashboard will be unavailable for approximately three hours



Announcements [1]

https://docs.aiqua.appier.com/changelog



. The AIQUA Dashboard will be unavailable for approximately three hours.Changes to app push metrics and delivery take effect on December 28, 2021over 3 years ago by AppierIn order to make the number of reachable users for app push campaigns more clear and accurate, the following changes will be applied to AIQUA starting from December 28, 2021.Recommendation 1.0 will be deprecated on December 31, 2021over 3 years ago by AppierAfter the deprecation date, all Appier SDK (Web, Android, iOS, and React Native) methods for Recommendation



Announcements [2]

https://docs.aiqua.appier.com/changelog



1.0 will return a non-HTTP 200 OK status code.Scheduled Maintenance: Tuesday November 16, 5:00-7:00 AM (UTC+8)over 3 years ago by AppierOn November 16 at 5:00 AM (UTC+8), there will be scheduled downtime for approximately 2 hours. During the maintenance window, AIQUA dashboard will not be accessible and campaign delivery will be paused.Important Updates about Appier Mobile SDKalmost 4 years ago by AppierRecently, there are several important updates regarding Appier Mobile SDK that require you to take actions.



User Data Collection [0]

https://docs.aiqua.appier.com/docs/user-data-collection



This page provides an overview on how user data is tracked and used in AIQUA.

Having user data allows you to utilize the following features on AIQUA and create personalized experience for your users.

Audience Segmentation: You can create subgroups of users based on the users' actions and profile information. For example, you can create a segment of users who have purchased within a week.

Campaigns: AIQUA campaigns (except regular campaigns) can be triggered based on the users' actions. For example, trigger a promotional popup message after the user visits a product page.

Dynamic Content: Dynamic content allows you to use a variable in your marketing messages that changes based on each user's actions or profile information. For example, show the image of the product previously viewed by each user in the email campaign.

Recommendation: Generates AI-powered recommended items based on each user's past behaviors.

In AIQUA, each user is uniquely identified by a user identifier. 

AIQUA assigns a unique identifier userId to each user who visits your website or installs your app. 

AIQUA treats each userId as a different user and stores the user data of your website visitors, Android app users, and iOS app users in separate databases. 

For example, let's say we have a user Jane, who visits your website from her work PC and installs your app on her Android mobile device and on her iPad. She will be tracked as three users on AIQUA, each with a different userId.

In addition to userId, AIQUA also uses other unique identifiers to track users, such as the device ID of the user's mobile phone or the email address and custom user ID from your CRM system.

Here are some of the unique identifiers used by AIQUA:



User Data Collection [1]

https://docs.aiqua.appier.com/docs/user-data-collection



Here are some of the unique identifiers used by AIQUA:

IdentifiersDescriptionuserIdThe AIQUA unique identifier assigned to every user.advertiserIdIdentifier for Advertiser for Android devicesIDFAIdentifier for Advertiser for iOS devices.IDFVIdentifier for Vendor for iOS devices.user_idCustom user ID used by your company (e.g. member ID from your CRM system).phoneNoUser's phone number.emailUser's email address.

User data can be categorized into user events and user attributes.

A user event is defined as the actions a user performs while on your website or app, such as clicking a button or loading a product page. 

Each user event has a timestamp.

AIQUA retains user events for 180 days.

A user event has a set of associated parameters, which contains additional data about the event.

For example, when a user adds a product to cart on your website, a product_added_to_cart event can be sent to AIQUA. And the event can contain parameters such as product_name and product_id of the product added to cart. 

Examples of default user events automatically tracked by Appier SDK:

page_viewed

subscribed_to_webpush

notification_clicked

app_launched

Examples of custom user events you can choose to track:

checkout_completed

registration_completed

login

User attributes are the profile information of a user, such as the user's name, gender, and birthday. User attributes can also be information about the user's device and various user identifiers.

Unlike user events, user attributes do not have timestamps, and are not subjected to the 180-day data retention period.

Examples of default user attributes automatically tracked by Appier SDK:

deviceType

browser

gcmId

line_current_follower

Examples of custom user attributes you can choose to track:

phoneNo

email

birthday

👍TipThe Appier iOS and Android SDKs allow you to set permissions for certain types of user data, e.g. disabling or enabling the collection of a device's IDFA or AAID. Refer to the following guides for details:

Android User Data Permissions

iOS User Data Permissions



User Data Collection [2]

https://docs.aiqua.appier.com/docs/user-data-collection



Android User Data Permissions

iOS User Data Permissions

Your user data can come from your online platforms (i.e. your websites and apps), as well as any user data you own offline.

Once Appier SDK is integrated in your website and app, you can collect data about users who visit your website or install your app. 

Default events and attributes: These are the user data that AIQUA automatically collects once SDK is integrated. No additional codes need to be added.

See the list of Default Events and Attributes collected.

Custom events and attributes: You can collect additional user data that is relevant for your business by setting up SDK to log custom events and attributes.

See guidelines on collecting Custom Events and Attributes.

If you have additional user data in your own database, you can upload these data to AIQUA. 

Offline user attributes: This can be email lists you have collected from marketing events or member data from your CRM system. There are two methods to upload: 

Method 1: Bulk Upload of Offline Users via API.

Method 2: Update User Profiles feature on AIQUA dashboard.

Offline user events (Beta feature): This can be transaction data that happened in your physical stores. You can upload via the Upload Offline Events API. 

Once offline user attributes are uploaded, AIQUA will try to match the uploaded offline user attributes with online users onboarded via SDK based on these identifiers: user_id, email, phoneNo. 

If an identifier matched, AIQUA merges the uploaded offline user attributes with the SDK-collected online user.

In case the identifiers of the offline user do not match with any Android, iOS, or web users, the uploaded user is stored in a common database for offline users. AIQUA will try to match the remaining unmatched offline users once per day since new online users will continue to be onboarded through SDK.



User Data Collection [3]

https://docs.aiqua.appier.com/docs/user-data-collection



This merging enriches your user data and allows you to reach previously offline users through other marketing channels such as push notifications.Updated over 1 year ago Table of Contents

Why collect user data?

User identifiers

User events and attributes

User events

User attributes

Online and offline user data

Tracking online users via Appier SDK

Uploading offline user data

Merging offline user attributes with online users



Default Events and Attributes [0]

https://docs.aiqua.appier.com/docs/default-aiqua-parameters



app_uninstalledAndroid

iOSIndicates that the user is marked as an uninstall and is only available for mobile apps. It can be used as a segmentation condition for targeting users marked as an uninstall.

This is a virtual event that cannot be used as a trigger condition in in-web campaigns, in-app campaigns and customer journey maps.app_launchedAndroid

iOSGenerated every time the user launches or opens the app.first_app_launchedAndroid

iOSGenerated when the user launches or opens the app for the first time. Supported versions: Android SDK 5.9.2 and above, iOS SDK 5.2.1 and above.

This event can be used as a trigger condition in in-app campaigns starting from Android SDK 7.1.0 and iOS SDK 7.11.0. This event cannot be used as a trigger condition in Journey Maps.notification_sentAndroid Push

iOS Push

Web Push

Email

LINE

SMS

KakaoGenerated when a push / email / LINE / SMS / Kakao notification is sent to the user.notification_deliveredEmail

LINE

SMS

KakaoEmail / SMS / Kakao: Generated when the Email / SMS / Kakao vendor reports that the notification has been delivered to the user.LINE: LINE does not provide delivery data. This event is generated when a LINE notification is sent to the user (same as notification_sent). This event will be deprecated in the future.notification_receivedAndroid Push

iOS Push

Web PushApp Push: Generated when the app push arrives at the end user's device.Web Push: Generated when the web push is delivered and shown on the screen.notification_displayedAndroid Push

iOS PushGenerated when the push notification is displayed.

A notification may be received but not displayed due to errors that result in display failure (e.g. failure to download notification data). Notifications blocked due to delivery restrictions generate an aiq_notification_blocked event instead.



Default Events and Attributes [1]

https://docs.aiqua.appier.com/docs/default-aiqua-parameters



For iOS, this event will not be generated if rich push notifications are not properly integrated.aiq_notification_blockedAndroid PushGenerated when a notification is blocked due to a delivery restriction (blackout window or time to live).notification_clickedAndroid Push

iOS Push

Web Push

Email

LINE

SMS

KakaoPush: Generated when the user clicks on a push notification.Email: Generated when the user clicks on a link in an email campaign.LINE: Generated when the user clicks on a LINE campaign (carousel or rich message) that redirects to an Appier SDK-integrated app or website. Supported app SDK versions: Android SDK 7.12.0 or later, iOS SDK 7.20.0 or later.SMS and Kakao: Generated when a user clicks on an AIQUA short URL (SMS, Kakao).notification_browsedAndroid Push

iOS PushGenerated when the user scrolls an item in the slider or carousel push or clicks the ▶▶ button.actionClickedAndroid PushGenerated when the user clicks on a customized button in the notification.qg_rich_push_openediOS PushGenerated when the user expands the carousel and slider notification using the View button or 3D touch.qg_carousel_clickedAndroid Push

iOS PushGenerated when the user clicks on an expanded carousel or slider item.qg_carousel_dismissediOS PushGenerated when the user closes a carousel or slider notification.qg_exceptionAndroid PushIndicates a system exception for an SDK.qg_inapp_displayedAndroid In-App

iOS In-AppGenerated when an in-app pop-up notification is displayed.qg_inapp_receivedAndroid In-AppGenerated when an in-app pop-up notification is fetched from the server.qg_inapp_clickedAndroid In-App

iOS In-AppGenerated when the user clicks on an in-app pop-up notification with a valid link, or when the user submits a form in creatives generated with Creative Studio.qg_inapp_lead_genAndroid In-App

iOS In-AppOnly supported for creatives generated with Creative Studio. Generated when the user submits a form by clicking on a creative element where the element's "Action" is set to Submit form.qg_inapp_toggledAndroid In-App



Default Events and Attributes [2]

https://docs.aiqua.appier.com/docs/default-aiqua-parameters



iOS In-AppGenerated when the user clicks on the floating icon of an in-app pop-up campaign or closes the creative.

Not supported for creatives generated with Creative Studio.qg_inapp_closedAndroid In-App

iOS In-AppGenerated when the in-app pop-up notification is closed.aiq_cg_receivedIn-Web

Android In-App

iOS In-AppGenerated when an in-app pop-up or in-web campaign is triggered for a user assigned to the control group in an Experiment.qg_inweb_closedIn-WebGenerated when the user closes the in-web creative.qg_inweb_displayedIn-WebGenerated when the In-Web creative pops up.qg_inweb_clickedIn-WebGenerated when the user clicks on the In-Web creative.qg_inweb_lead_genIn-WebGenerated when the user submits lead generation form.qg_email_openedEmailThe email sent by AIQUA was opened.qg_email_processedEmailAIQUA receives the email content and prepares to deliver the email.qg_email_deferredEmailThe email sent by AIQUA temporarily cannot be delivered, but AIQUA will continue to attempt delivery for 72 hours.qg_email_soft_bouncedEmailThe email sent by AIQUA soft-bounced. This means that the delivery failed due to a temporary reason. For example, the user's mailbox was full.qg_email_hard_bouncedEmailThe email sent by AIQUA hard-bounced. This means that the delivery failed due to a permanent reason. For example, the email address does not exist.qg_email_spammedEmailThe email sent by AIQUA was reported as spam.qg_email_unsubedEmailThe user unsubscribes from email campaigns.qg_email_resubedEmailThe user resubscribes to email campaigns.page_viewedWebThe user visits a web page. You can segment audience based on the URL of the webpage.



Default Events and Attributes [3]

https://docs.aiqua.appier.com/docs/default-aiqua-parameters



If your website is a single page application (SPA), the SDK doesn't collect page_viewed by default. Instead you'll need to log the event manually .subscribed_to_webpushWeb PushThe user allows the web push.unsubscribed_to_webpushWeb PushThe user blocks the web push.visitedWebThe user visits the website. This event is only generated once a day upon the user's first visit on that day.first_visitedAndroid

iOS

WebYou can use this parameter to create a segment for users who recently visited the site or app for the first time. (e.g. users first visited site in the past 1 day)

This is a virtual event generated from timestamps of the user’s activities on the website or app. This event cannot be used as a trigger condition in in-web campaigns, in-app campaigns and customer journey maps.qg_line_clickLINEGenerated when the user clicks on a LINE campaign (carousel or rich message) that redirects to an Appier SDK-integrated app or website.

Supported app SDK versions: Android SDK 7.12.0 or later, iOS SDK 7.20.0 or later.

This event is the same as the notification_clicked event for LINE campaigns.aiq_journey_map_exitAndroid

iOS

WebGenerated when the user is exited out of the journey map campaign. See how to segment audience using the Event Parameters of this event.

This event is only generated in journey maps created after August 2021.aiq_web_personalization_impressionWebGenerated when personalized content is loaded on the visited webpage.recommendation_impressionAndroid

iOS

WebGenerated when the recommended products of a recommendation scenario are shown to the user.

This event includes the following parameters which can be used for audience segmentation: scenario_id, model_id, and recommendation_id.

Supported versions: Android SDK 6.5.0 or later, iOS SDK 7.4.0 or later, React Native SDK 1.5.0.



Default Events and Attributes [4]

https://docs.aiqua.appier.com/docs/default-aiqua-parameters



Supported versions: Android SDK 6.5.0 or later, iOS SDK 7.4.0 or later, React Native SDK 1.5.0.

To track impressions for REST-API enabled scenarios, this event must be logged manually when using the iOS, Android, or React Native SDK methods.recommendation_clickedWebGenerated when a user clicks on a recommended product within the attribution window.

This event includes the following parameters which can be used for audience segmentation: scenario_id, model_id, recommendation_id, and product_id.

Must be logged manually in the iOS, Android, and React Native SDK.



Custom Events and Attributes [0]

https://docs.aiqua.appier.com/docs/custom-user-data



In addition to the default user data the Appier SDK automatically collects, you can collect custom user data on your website and app using the SDK logging methods. Custom user data consists of free-form attributes and events that you can define depending on your business needs.

Custom attributes are pieces of information that describe a user, such as their name, city of residence, or date of birth.

Custom events are user actions, such as viewing a product page or purchasing a product. Events can also contain event parameters, which are details about the event, such as the product name, image, and price. AIQUA retains event data for 180 days.

For example, when a user adds a product to their cart, you can log the product_added_to_cart event using an Appier SDK logging method. Events contain event parameters that describe the details of the event, such as product_name, product_id, product_category, and product_image_url.

Names for custom events, event parameters, and attributes must conform to AIQUA's naming standards; otherwise, features such as Dynamic Content and segmentation may not function properly.

Custom field names can only contain lowercase alphabetical letters (a-z), numbers (0-9), and underscores (_).

Custom field names must begin with an alphabetical character (a-z) or an underscore (_).

The following examples are valid custom field names because they begin with an alphabetical character (a-z) or underscore (_) and don't contain special characters other than underscores (_):

checkout_completed_1

product_purchased

_productprice_10

purchase_checkout_3

subscription_cancelled

The following table contains examples of invalid custom field names:

Invalid field nameReason1checkout.completedInvalid because it starts with a number and contains a period (.).



Custom Events and Attributes [1]

https://docs.aiqua.appier.com/docs/custom-user-data



Invalid field nameReason1checkout.completedInvalid because it starts with a number and contains a period (.).

The first letter of the field name must be an alphabetical letter (a-z) or an underscore (_). The period (.) is not an accepted special character.product-purchased%Invalid because it contains a dash (-) and a percent sign (%), which aren't accepted special characters._product price{10}Invalid because it contains a space and curly brackets ({}), which aren't accepted special characters.purchase+checkout(3)Invalid because it contains parentheses (()), which aren't accepted special characters.subscription: cancelledInvalid because it contains a space and a colon (:), which aren't accepted special characters.

👍TipYou can use the following regular expression to validate that a custom field name will be accepted by AIQUA without issues: [a-z_][a-z0-9_]*

Supported data types: Array, string, integer, float, boolean, object.

Arrays and objects cannot be nested, e.g. arrays nested in objects, objects nested in objects, and arrays nested in arrays are considered invalid.

Dates must be logged as strings with the proper date or datetime format.

Avoid unnecessarily setting a parameter or attribute to an empty value (e.g. a blank string) or null. Doing so may cause unexpected or undesirable behavior during segmentation.

Note: Using the exists segmentation condition without specifying a value will include users with parameters set to an empty value or null. For example, if you set the segment's include condition to phoneNo exists, users with an empty value or null for the phoneNo profile parameter will be included in the segment.

Whenever you log an attribute or parameter, ensure that the data type matches the data type you used the first time you logged it. If an attribute or parameter is logged with a data type different from the one it was initialized with, the value won't be saved. Instead, it will be set to null.

If you encounter any issues, please contact Appier Support (ess_support@appier.com) for assistance.



Custom Events and Attributes [2]

https://docs.aiqua.appier.com/docs/custom-user-data



If you encounter any issues, please contact Appier Support (ess_support@appier.com) for assistance.

If a transaction consists of multiple events, log each event separately. For example, when a user completes a checkout, two types of events should be logged: checkout_completed and product_purchased.

When logging an event that consists of multiple products, each event should only correspond to a single product. Each SDK method call should only contain one product_id. AIQUA features such as Recommendation 2.0, dynamic content inside creatives, and purchased product filtering (for recommendations and dynamic content) may not function optimally if a single event is associated with multiple products.

For common event types, follow the AIQUA Custom Event Reference. This reference enumerates common custom event types used by AIQUA features and the parameters they require to function properly.

In this situation, two types of events should be logged:

checkout_completed: Indicates that the user has successfully completed the checkout process. This can be used as the single conversion or goal event.

product_purchased: Indicates that a product was purchased. Log product_purchased separately for each product, so that each event corresponds to a single product_id. For example, if three products were purchased, this event should be logged three times, each with a different product_id.

For optimal feature performance, follow the requirements for predefined attributes. When logging one of these attributes, the name must match the name listed below. For details about which attributes are required for each feature, see Feature-specific requirements.

phoneNo: The user's phone number. The value should only contain digits 0-9, with no special characters or spaces. For example, "0123456789" is valid, while "+123-456-789-012" is invalid.

email: The user's email address.

line_uid: The user's LINE user ID.

user_id: The user's ID in your database or CRM.



Custom Events and Attributes [3]

https://docs.aiqua.appier.com/docs/custom-user-data



email: The user's email address.

line_uid: The user's LINE user ID.

user_id: The user's ID in your database or CRM.

You can log user attributes when events relating to user data occur, such as when a user adds payment information or completes an account registration. Use these events as triggers to provide AIQUA with new or updated user attribute data.

If your website has an auto-login feature, we recommend periodically logging the user_id attribute. Doing so allows AIQUA to remap the user to their third-party cookie if it expires before their login cookie. For example, you can log the user_id profile parameter on the user's first visit of the day.

Some AIQUA features require you to collect specific attributes, events, or event parameters. If you're using one of the features listed in the following table, ensure you log the required data:

Feature

Required data

Recommended data type

Email campaigns

email: The user's email address. Email addresses are not case-sensitive.



string



SMS/MMS campaigns

phoneNo: The user's phone number, including the country code.



string



Kakao campaigns

phoneNo: The user's phone number, including the country code.



string



Tracking attribution value

Include the "value to sum" parameter to track the total monetary value associated with an event.

Applicable to events such as product_purchased or checkout_completed.



See the Appier SDK docs for details on how to track "value to sum":



Web SDK

Android SDK

iOS SDK

React Native SDK

number

Recommendation 2.0

Include the product_idparameter when logging events required by recommendation models.

string

Uploading Offline Users

Include one of the following attributes for each user:

user_id: The user's unique ID in your system (e.g. your CRM system).

email: The user's email address.

phoneNo: The user's phone number.

line_uid: The user's LINE user ID.

string



Uploading Offline Events

user_id: The user's unique ID in your system (e.g. your CRM system).



string



(AIXON) Cookie sync



Custom Events and Attributes [4]

https://docs.aiqua.appier.com/docs/custom-user-data



Uploading Offline Events

user_id: The user's unique ID in your system (e.g. your CRM system).



string



(AIXON) Cookie sync

dmpid: The user's Data Management Platform (DMP) ID.



This is an additional field to collect a cookie-level ID.

If you're using AIXON, the user's dmpid can be used for ID syncing if you have a cookie-level ID that needs to map to the client-side first-party cookie assigned by the SDK.



string

📘Note for Recommendation 2.0Recommendation 2.0 requires you to onboard your product data feed with AIQUA. The product ID in the data feed must match the product_id event parameter for AIQUA to be able to match the event with the product in the data feed.

The type of user data you collect may differ based on your industry or marketing goals. Use the AIQUA Custom Event Reference as a guide when deciding what custom data to collect.

Once you've determined what type of data you want to collect, use the Appier SDK methods to log custom events and attributes: 

Web: Logging Data on the Web SDK

Native Android: Logging Android User Attributes and Logging Android User Events

Native iOS: Logging iOS User Attributes and Logging iOS User Events

React Native: Logging User Events and Attributes for React Native

📘NoteDon't log default events and attributes using the Appier SDK methods. This data is automatically tracked by Appier SDK.

To validate that events and attributes are being logged properly by the Appier SDK, go to the AIQUA Dashboard, click your account name in the lower-left corner, then select:

Recent Activity to see logged user events. 

Recent Users to see logged user attributes.

Logged user events and attributes are listed under the tab for each platform (e.g. Web, Android, iOS Production). You won't be able to select a platform if you haven't integrated the Appier SDK for that platform.

Updated over 1 year ago Launching Your First CampaignTable of Contents

Overview

Data logging guidelines

Field names for custom data

Event parameter and user attribute values

Logging events

Logging user attributes



Custom Events and Attributes [5]

https://docs.aiqua.appier.com/docs/custom-user-data



Field names for custom data

Event parameter and user attribute values

Logging events

Logging user attributes

Feature-specific requirements

Logging custom events and attributes via Appier SDK

Checkpoint: Validating the custom data is logged properly



Launching Your First Campaign [0]

https://docs.aiqua.appier.com/docs/launching-first-campaign



To help you get started, let's use a fashion brand as an example. Let's say you have a fashion e-commerce website and you want to send a Web Push notification about shoes discount to your website visitors who have recently viewed shoe-related pages on your site.

Web push notifications are notifications that can be sent to your website users who have opted-in, even when they're not on your website. When users visit your website, a prompt is shown asking for permission. Users who choose to allow notifications are considered opted-in.

Below are the typical steps for integrating your website with Appier SDK and launching your first web-push campaign. 

[Overview]

First, your website needs to be integrated with Appier SDK. This requires enabling the connection on AIQUA's dashboard, and then adding the required file and codes to your website. 

[Detailed Steps]

Login to AIQUA's dashboard and refer to the steps in Integrating with the Appier Web SDK. 

[Overview]

Next, set your website to record the action of users viewing webpages as an product_viewed event, which contains event parameters such as product_name, product_id, and product_category.

[Detailed Steps]

Add the following script to the shoes-related product pages of your website. Replace the 123, Brand Z shoes and shoes with the actual product ID, product name, and product category of the products viewed by the users.



For details, see Custom User Events and Logging Data on the Web SDK

[Overview]

On AIQUA dashboard, create an audience segment for users who have viewed shoes-related pages, and then create your web push campaign about the shoes discount.

[Detailed Steps] 

On AIQUA Dashboard, go to Audiences > Segment list, and click the + Create segment > Conditions in the top-right corner.

Enter a Segment Name. Adding a description is optional.

Under Include Users, click the Add New Condition button.



Launching Your First Campaign [1]

https://docs.aiqua.appier.com/docs/launching-first-campaign



Enter a Segment Name. Adding a description is optional.

Under Include Users, click the Add New Condition button.

Set Event as product_viewed and click the Add Filter button.

For the parameters, select product_category and equals, and then input "shoes".

Click Save. An audience segment is created.

Click Campaigns, select Regular Campaigns, and click the + Create campaign button.

Type a campaign name, and under Audience, set channel to Website.

Under Users to include, select the segment you just created. Then, click Next to continue.

Under Creative section, enter a Title and Message for your notification. Input the Destination URL and Icon image URL for your creative. You can also check the following boxes to:

Include image

Include action buttons

Include a "drip notification"

Keep the unclicked notification in the Notification Center (Pile up notifications)

On the right, you can preview the notifications on Windows 10, macOS and Android devices.

Click Test Your Creative. See here on how to receive a test creative on your device. 

Click Save. A regular campaign is created.

To send out the campaign, click the three vertical dots next to the campaign name in the campaign list, then select Send Now.

👍Tip:In the Title, Message, Icon, Image, and Destination URL fields, you can include dynamic content based on the actual event parameters. For example, you can include the product_name variable in the message, and show a "Get Brand Z Leather Boots at a discount!" message to users who have viewed "Brand Z Leather Boots".Type {{ in the text box to bring up a list of user attributes and events, and select product_viewed > product_name > of the latest event.Updated 3 months ago Table of Contents

1. Integrate Appier SDK with your website

2. Set website to send custom user data to AIQUA

3. Set up marketing campaigns via AIQUA dashboard

Create Audience Segment

Create Campaign



Web Push Quick Start [0]

https://docs.aiqua.appier.com/docs/web-push-quick-start



Web push notifications are pop-up messages that can be sent to users even when they're not actively browsing your website. These notifications are triggered by the Appier Web SDK and can only be sent to users who have subscribed by opted to web push notifications.

Once integrated with the Web SDK, a system prompt will appear in the user's browser asking if they want to allow notifications. Users who click Allow will be subscribed to your web push notifications.

Complete the following before creating your first web push campaign:

Integrate the Web SDK.

Configure prompt timing and custom prompts in your account's web pixel settings.

The table below lists the operating systems and browsers compatible with AIQUA's web push campaigns.

Operating systemSupported browsersWindows• Chrome

• FirefoxMacOS• Chrome

• Safari 16.4 or later (additional setup required)Android• Chrome

• FirefoxiOSSafari 16.4 or later (additional setup required)iPadOSSafari 16.4 or later (additional setup required)

📘Notes

Safari: Web push campaigns are only supported for web pages that have been added to the device’s home screen. 

Web push campaigns on Safari (iOS, macOS, iPadOS) require extra configuration which may involve code changes on your website. For detailed instructions, see Web Push for Safari.

Internet Explorer and Microsoft Edge: Web push campaigns are not supported, regardless of the operating system used.

Web push notifications might not be delivered in certain situations, such as when the browser isn't running or the device loses its network connection. See Web Push Known Issues for a list of known issues.

Follow these steps to set up your web push campaign: 

Add your device to the test segment

Create a regular web push campaign

Send the push notification

Before setting up your first web push campaign, add your device to the test segment:

Go to the AIQUA dashboard, click your account name in the bottom-left, click Recent users, then select the Web tab to find and copy your user ID.



Web Push Quick Start [1]

https://docs.aiqua.appier.com/docs/web-push-quick-start



Go to Audience > Segment list, then click the three vertical dots next to the Test segment and select Edit segment.

Under Include users, click + Add new condition. Create a condition with the following settings:

From the first dropdown, select userId.

Set the operator to =.

Set the value to the user ID you copied from the Recent users page.

Click Save to update your test segment.

Go to Campaigns > Regular campaigns, click + Create campaign, and select Push.

Enter a campaign name, and set channel to the Website.

Under Audience, go to Users to include, click + Add segment, and select "Test Segment". Then, click Next to proceed.

In the Creative section, select a type of creative and complete all the required fields. Refer to Creatives for details about each creative type and its settings.

Next, set up Schedule campaign and Campaign setting. 

Click Save to create the campaign.

On the campaign list page, click the three vertical dots next to the campaign name, then select Send now.

Monitor key metrics like subscriber engagement and delivery performance to evaluate your web push campaigns.

You can view your web push subscriber count from the segment list or analytics overview.

Segment list: To view the number of web push subscribers in a specific segment, go to Audience > Segment list and check the Web subscribers column.

Analytics overview: To view the overall number of current web push subscribers, go to Analytics > Overview and select the Web tab.

📘NoteUsers who previously subscribed but later blocked notifications or cleared cookies are not included in subscriber counts.

To view campaign performance, go to Campaigns > Regular campaigns and choose one of the following:

Campaign list: You can see the key performance metrics, including the number of users who received or clicked on the web push.

Campaign performance page: Click a campaign name to see detailed performance metrics for that specific campaign.

Updated about 2 months ago Web Push Creatives - StandardTable of Contents

Overview

Prerequisites



Web Push Quick Start [2]

https://docs.aiqua.appier.com/docs/web-push-quick-start



Updated about 2 months ago Web Push Creatives - StandardTable of Contents

Overview

Prerequisites

Browser compatibility

Limitations

Creating your first web push campaign

1. Add your device to the test segment

2. Create a regular web push campaign

3. Send the push notification

Tracking web push subscribers and campaign performance

View web push subscribers

View campaign performance



Standard Layout [0]

https://docs.aiqua.appier.com/docs/web-push-standard



Left: Web push on PC. Right: Web push on Android.

This is the title of the notification and can be entered as a text or emoji (click on the emoji icon). Keep the title short and eye-catching. Long titles are automatically trimmed depending on the user's screen size. The recommended length is 30 characters or less.

The text can either be static or personalized. 

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). The recommended length is 45 characters or less if you'll include an image in the web push, or 150 characters or less if you won't include an image.

The text can be either be static or personalized. 

Adding an icon is mandatory. See Image Types to upload the correct specifications.

Host your icon image on the web to enable adding its image URL in the field. It can also be personalized based on user activities.

Adding an image is optional. See Image Types to upload the correct specifications.

Host your image on the web to enable adding its image URL in the field. It can also be personalized based on user activities.

This is the URL where users are taken to after opening the web push. If left empty, the user will land on the default website.

The destination URL can be personalized based on user activity, like deep links.

If the user clicks on an action button, they'll be taken to its corresponding URL. If the web push has two action buttons, the user can be taken to separate URLs through these buttons. 

AIQUA lets you add up to two action buttons in a website push.

Action button text: Use this field to label an action button. 

Destination URL: This field carries the URL of the action button. 

Icon image URL: Host your icon image on the web to enable adding its image URL in this field. See Image Types to upload the correct specifications.



Standard Layout [1]

https://docs.aiqua.appier.com/docs/web-push-standard



A drip notification is a second notification that appears when the user dismisses the first notification you sent. When enabled, a Drip Creative editor is opened, allowing you to design the creative of the second notification.

Updated 9 months ago Table of Contents

Settings

Title

Message

Icon

Image

Destination URL

Include action buttons

Include a drip notification



2 Images Poster [0]

https://docs.aiqua.appier.com/docs/web-push-creatives-two-images-poster



📘NoteThis feature needs to be activated by Appier Support (ess_support@appier.com).

The 2 Images Poster creative consists of two images side by side. You can choose between two width proportions: 3:2 and 1:1.

Below are the recommended image sizes. 

Width ProportionImage on the LeftImage on the Right3:21094 x 900 px706 x 900 px1:1900 x 900 px900 x 900 px

If the size of the uploaded image does not match the recommended image size, the image will be resized to fit the width or length of the recommended image size.

If the image ratio does not match:

The aspect ratio will be maintained.

The empty space will be filled with white background color.

The image will be center-aligned.

This is title of the notification and can be entered as a text or emoji (click on the emoji icon). Keep the title short and eye-catching. Long titles are automatically trimmed depending on the user's screen size. The recommended length is 30 characters or less.

The text can either be static or personalized. 

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). The recommended length is 45 characters or less if you'll include an image in the web push, or 150 characters or less if you won't include an image.

The text can be either be static or personalized. 

Adding an icon is mandatory. See Image Types to upload the correct specifications.

Host your icon image on the web to enable adding its image URL in the field. It can also be personalized based on user activities.

Select the width proportion of the two images. The option on the left is 3:2, and the option on the right is 1:1.

Adding two images is mandatory. Host your image on the web to enable adding its image URL in the field. It can also be personalized based on user activities.

Image 1 URL: This is the image on the left. 

Image 2 URL: This is the image on the right.

This is the URL where users are taken to after opening the web push. If left empty, the user will land on the default website.



2 Images Poster [1]

https://docs.aiqua.appier.com/docs/web-push-creatives-two-images-poster



This is the URL where users are taken to after opening the web push. If left empty, the user will land on the default website.

The destination URL can be personalized based on user activity, like deep links.

If the user clicks on an action button, they'll be taken to its corresponding URL. If the web push has two action buttons, the user can be taken to separate URLs through these buttons. 

AIQUA lets you add up to two action buttons in a website push.

Action button text: Use this field to label an action button. 

Destination URL: This field contains the URL of the action button. 

Icon image URL: Host your icon image on the web to enable adding its image URL in this field. See Image Types to upload the correct specifications.

A drip notification is a second notification that appears when the user dismisses the first notification you sent. When enabled, a Drip Creative editor is opened, allowing you to design the creative of the second notification.

Updated 9 months ago Table of Contents

Settings

Title

Message

Icon

Image width proportion/Image layout

Image URL

Include action buttons

Include a drip notification



Setting Web Push Prompts (Web Pixel Settings) [0]

https://docs.aiqua.appier.com/docs/web-pixel-settings



Web push notifications can only be sent to desktop and Android users who have opted in to receive push notifications from your website. For websites integrated with Appier SDK, the browser shows a system prompt to site visitors to obtain their permission.

On AIQUA's Web Pixel Setting page, you can adjust the timing of the browser's system prompts, as well as create AIQUA's custom prompts to help increase the subscription rate. 

Go to AIQUA dashboard, click your account name in the lower-left corner and click Web Pixel Settings. This setting page is also shown during Web Integration. 

The following types of prompt are available:

System Prompt - Browser's native prompt to ask for user's permission.

Opt-in Prompt - AIQUA's custom prompt that precedes the system prompt.

Opt-in Tip - AIQUA's custom opt-in tips to show users how to manually allow notifications. 

Change Your Mind Prompt - AIQUA's custom prompt that encourages declined users to unblock. 

Pop-Up on Subscription - AIQUA's custom pop-up to welcome users who subscribed.

When a user visits your website, the browser pops up a system prompt that asks if the user wants to allow this website to send them push notifications. 

If the user clicks Allow, then the user is subscribed to your push notifications. 

If the user clicks Block, the browser will not show system prompts to this user again unless the user explicitly modifies the notification settings. 

If the user takes no action on the system prompt by ignoring or closing it, the browser will show system prompt again during the user's next visit. However, depending on the browser type, the browser may stop showing the system prompt if this happens too many times.

System prompt is the browser's native prompt, where the message and buttons cannot be modified.

Under General Settings, you can adjust the timing of the prompts. 

Time delay before the subscription prompt is shown - Delay the time when the system prompt is shown after the user visits your site.



Setting Web Push Prompts (Web Pixel Settings) [1]

https://docs.aiqua.appier.com/docs/web-pixel-settings



If opt-in prompt is enabled, this time delay is applied to opt-in prompt instead of system prompt.

If change your mind prompt (CYMP) is enabled, this time delay is applied to CYMP as well.

Delay between two subscription prompts - After a user is shown a system prompt, if the user visits the site again within the delay time specified here, AIQUA will not show the system prompt.

The same logic applies if you have enabled Opt-In Prompt. After the user is shown an opt-in prompt, AIQUA will not show another opt-in prompt during user's next visits if it is within the time delay specified.

This delay does not apply to Change Your Mind Prompt (CYMP).

📘Note:Delay between two subscription prompts cannot be set to 0. AIQUA will apply 3600 seconds when 0 is entered in this field. It is not recommended to set 0 delay between prompts as frequent prompts may have a negative impact on user experience.

Opt-in prompts, sometimes referred to as fake prompts, soft prompts, or pre-prompts, are custom prompts that you can display before the browser's native system prompt. If the user agrees to the opt-in prompt, then the system prompt is shown to ask for user's permission. If the user declines in the opt-in prompt, you have a chance to show the opt-in prompt again later at an appropriate time.

Some advantages for using opt-in prompts:

If the user blocks the system prompt, the browser doesn't allow you to display the system prompt again. So before displaying the system prompt, it's recommended to ask for approval first by displaying an opt-in prompt. 

Opt-in prompts are customizable. You can increase subscription rate by offering incentives to users if they subscribe.

Under Opt-In Prompt, select Use Opt-In Prompt to enable.

Title / Message - Type a custom title and message to encourage users to subscribe.

Icon Url - Change the default Bell icon on the top-left corner if needed.

Opt-In Button Text - You can adjust the text of the opt-in button.

Opt-In Button Color - You can adjust the color of the opt-in button.



Setting Web Push Prompts (Web Pixel Settings) [2]

https://docs.aiqua.appier.com/docs/web-pixel-settings



Opt-In Button Color - You can adjust the color of the opt-in button.

Close Button Text - You can adjust the text of the close button.

Prompt Message Location - The prompt can pop up on the left side or in the center.

Include an overlay - Select Yes to gray out the area outside of the prompt.

Opt-in tip, if enabled, is a pop-up designed to show Chrome users how to manually allow notifications. This tip is intended for users who no longer see system prompts because they are enrolled in Chrome's Quieter Permission UI. They will need to click the notification icon on the address bar to manually allow notifications.

Chrome users not enrolled in Quieter Permission UI will see both the system prompt and the opt-in tip.

If you have enabled Subscription Boost in in-web campaigns, the Subscription Boost notification also pops up with the opt-in tip when triggered.

Under Opt-In Tip, select Use Opt-in Tip to enable.

Title / Message - Type a custom title and message to encourage users to subscribe.

Background Color - You can adjust the color of the background.

Text Color - You can adjust the color of the text.

Location - Adjust the location of the prompt on the browser.

Include an overlay - Select Yes to gray out the area outside of the prompt.

📘Note:Opt-in tip is only supported in Chrome browsers.

For users who have selected Block in system prompt, you can show a Change Your Mind Prompt that instructs users how to modify their browsers' notification settings. 

Under Change Your Mind Prompt (CYMP), select Use CYMP to enable CYMP.

Message for Desktop Users / Message for Android Mobile Users: Type the prompt message for desktop users and Android mobile users. 

Background Color - Change the background color of the prompt.

Text Color - Change the text color of the prompt.

Duration to Prompt (days) - After the users block the system prompt, AIQUA will wait X days before showing the CYMP during the users' next site visit.



Setting Web Push Prompts (Web Pixel Settings) [3]

https://docs.aiqua.appier.com/docs/web-pixel-settings



You can display a pop-up once the user clicks Allow on system prompt. You can customize the design and the behavior of the pop-up message via HTML. 

For example, if you used opt-in prompt to promise the user a coupon if they subscribe, now you can provide the coupon code in the pop-up on subscription after they have subscribed.

Under Pop-Up on Subscription, select Use Pop-Up on Subscription to enable. 

Use the HTML editor to create what you want the users to see after they have subscribed. 

Next to Include an overlay, select Yes to gray out the background.

Updated over 1 year ago Table of Contents

System Prompt

Opt-In Prompt

Opt-In Tip

Change Your Mind Prompt (CYMP)

Pop-Up on Subscription



Web Push for Safari [0]

https://docs.aiqua.appier.com/docs/web-push-for-safari



Use web push notifications to increase your marketing reach and user engagement, now supported for Safari 16.4+ (MacOS, iPadOS, iOS). For users who opt in, web push notifications can be sent from Progressive Web Apps (PWAs) that have been added to the device's home screen.

After completing the setup steps for Safari web push, you'll be able to create and send web push campaigns from the AIQUA dashboard.

📘Note: Safari permission promptUnlike other browsers, Safari doesn't allow apps to directly send opt-in prompts. Instead, users must first agree to the AIQUA opt-in prompt before the system's web push permission dialogue can be sent.

The initial AIQUA web push opt-in prompt is displayed.

If the user accepts the AIQUA opt-in prompt, the Safari system dialogue requesting permission to send web push notifications is automatically sent.

After the user accepts both prompts (first the AIQUA opt-in prompt, then the Safari system dialogue), the user will become a web push subscriber and will be able to receive web push notifications.

📘PrerequisiteYour website must be integrated with the Appier Web SDK.

Your website must be an installable Progressive Web App (PWA). To be an installable PWA, i.e. having the ability to be added to the home screen, your website must be served alongside a web app manifest file.

Add or update your web app's manifest.json file with the following required members:

KeyDescriptionnameThe full name of your web app.short_nameAn abbreviated name that's displayed when there isn't enough space to display the full name.displayThe display mode that determines how much of the browser UI will be shown. For details on the possible values, refer to the Mozilla Development Network reference.



Web Push for Safari [1]

https://docs.aiqua.appier.com/docs/web-push-for-safari



We recommend setting this to standalone for a native app-like experience.theme_colorThe app's default theme color.background_colorThe placeholder background color used for the splash screen when launching the app, before its stylesheet is loaded.iconsAn array of icon image objects that can serve as app icons in different contexts. For more details about the icons objects, refer to the Mozilla Development Network reference.icons.srcThe path to the image file.icons.sizesA string containing space-separated image dimensions. icons.typeThe image's media type.

A manifest.json with all the required fields looks like this:

{

"name": "",

"short_name": "",

"display": "standalone",

"theme_color": "<#000000>",

"background_color": "<#000000>",

"icons": [

{

"src": "/path/to/file/icon.png",

"sizes": "256x256 512x512",

"type": "img/png"

}

]

}

In your web app's HTML, include the manifest using a element inside the tag. Every page in your app must be linked to the manifest.







Follow the instructions in Setting Web Push Prompts (Web Pixel Settings) to set up the initial AIQUA opt-in prompt.

The AIQUA opt-in prompt must be accepted by the user before the Safari system dialogue can be displayed, and the Safari system dialogue is automatically displayed after the AIQUA opt-in prompt is accepted. After accepting both prompts, the user will become a web push subscriber.

iOS and iPadOS users must manually add your website to their home screen before web push notifications can be sent. For example, you can send an in-web campaign guiding users browsing your website to add the website to their home screen.

After you've completed the setup steps, test your web push campaign to verify that you can receive web push notifications on your device.

If your users are unable to receive Safari web push notifications, please follow the troubleshooting steps below:

Check your operating system version



Web Push for Safari [2]

https://docs.aiqua.appier.com/docs/web-push-for-safari



Check your operating system version

Ensure that your web app has been installed (iOS, iPadOS)

Verify the user's web push subscription status

Verify your Appier Web SDK integration

👍Contact Appier SupportIf you encounter difficulties during the troubleshooting process, please contact Appier Support (ess_support@appier.com) for assistance.

Safari web push is only supported for the following operating systems:

macOS Big Sur, Monterey, Ventura, or later

iPadOS 16.4 or later

iOS 16.4 or later

Ensure that the web app has been successfully added to the receiving device's home screen. To be installable, your PWA must include a web app manifest file containing all of the required members.

Verify whether the has successfully subscribed to web push notifications. To check the web push subscription status:

Go to the AIQUA dashboard, click your account name in the bottom-left corner, then click Recent Activity and go to the Web tab.

In the event log, check if the user completed a subscribed_to_webpush event. If you see this event, it means the user successfully subscribed to web push notifications.

Confirm that you've successfully integrated the Appier Web SDK by checking if the AIQUA service worker is installed and active on your website.

Navigate to your website and accept both the AIQUA opt-in prompt and the Safari system dialogue requesting permission to send web push notifications.

If you don't see the Develop menu in the menu bar, follow the instructions in this Apple Support Guide to add it. 

In the menu bar, click Develop > Service Workers.

Verify that your website's URL is listed under Service Workers. If you can find your website, it means that the AIQUA service worker has been properly installed.

Updated about 1 year ago Table of Contents

Overview

User flow

Setup steps

1. Create or update your web app's manifest file

2. Link the manifest file to your web app

3. Set up the AIQUA opt-in prompt

4. Encourage users to add your website to their home screen (for iOS and iPadOS)

5. Test a web push campaign

Troubleshooting



Web Push for Safari [3]

https://docs.aiqua.appier.com/docs/web-push-for-safari



4. Encourage users to add your website to their home screen (for iOS and iPadOS)

5. Test a web push campaign

Troubleshooting

1. Check your operating system version

2. Ensure that your web app has been installed (iOS, iPadOS)

3. Verify the user's web push subscription status

4. Verify your Appier Web SDK integration



Web Push Known Issues

https://docs.aiqua.appier.com/docs/known-issues-web-push



Here are the known issues for Web Push.

Previously, some users using macOS 10.15 (Catalina) are not able to receive web push on Chrome. This issue has since been resolved by Chrome in version 78.0.3904.97. MacOS users experiencing problems with web push can upgrade their Chrome browser to the latest version.

Due to a Chrome update, Appier SDK can no longer support the web push feature in Incognito mode. 

Following this update, if you're sending a web push notification, these are the possible fake prompt scenarios when a user uses Chrome or Firefox for browsing. 

BrowserBrowsing ModeWeb ProtocolFake Prompt ScenarioChromeIncognitoHTTPFake prompt and dialog appear, but dialog gets automatically closedChromeIncognitoHTTPSNo fake promptChromeRegularHTTPFake prompt and system prompt with dialog appearChromeRegularHTTPSFake prompt and system prompt appearFirefoxPrivateHTTPNo fake promptFirefoxPrivateHTTPSNo fake promptFirefoxRegularHTTPFake prompt and system prompt with dialog appearFirefoxRegularHTTPSFake prompt and system prompt appear

DateStatus06/05/2019A Chrome browser, used on a macOS device, trims a subdomain name that exceeds 10 characters. This is a third-party system limitation.

DateStatus05/31/2019Due to a Chrome update, an HTTP-integrated Appier web SDK can't track if a domain was manually removed. The Appier web SDK isn't allowed to do permission checks via iFrame and can only get cache results from the notify domain.06/03/2019Won't fix.

DateStatus03/23/2019The issue was identified as happening across Chrome browsers running on Windows 10. We are currently tracking third-party updates and testing for a possible workaround.

For more details on this issue, see this reference.Updated over 1 year ago Table of Contents

Web push doesn't show on macOS 10.15 (Catalina) with Chrome

Web push is no longer supported in incognito or private browsing

HTTP web push limitation for macOS Chrome

HTTP-integrated sites can't identify if a site was removed

Web page doesn't load when clicking a web push from Action Center



Email Campaign Quick Start [0]

https://docs.aiqua.appier.com/docs/email-integration



You can integrate AIQUA with an email service provider to send targeted email campaigns to your users. AIQUA email campaigns allow you to utilize pre-built email templates for quick setup and leverage audience segmentation for effective targeting.

Before creating an email campaign, ensure the following:

Your account is integrated with an email service provider. To integrate AIQUA with an email service provider, contact Appier Support (ess_support@appier.com).

Email addresses are collected using the email custom user attribute.

Some third-party email service providers might not support the performance tracking, such as impressions, clicks, and conversions. In such cases, AIQUA cannot display these metrics.

AIQUA automatically converts uppercase email addresses to lowercase, which may affect segmentation.

IP warmup is an essential process to build up a good sender reputation and avoid being seen as a spam sender by email providers. To ensure better email deliverability, follow the instructions in the IP Warmup guide.

When email addresses are sent or uploaded to AIQUA using the email user attribute, AIQUA converts the uppercase letters in the email addresses into lowercase. The same email addresses with different capitalizations (such as Abc@email.com and abc@email.com) are treated as the same email address and they will be deduplicated in segments, reports, and the unsubscription list.

If you're using dynamic content in email campaigns, make sure to add a default value as fallback in case the dynamic content can't be generated successfully. 

Ensure that your email campaigns are only sent to users who consented to receive email and they have a clear way to unsubscribe to enhance the user experience.

Obtain user consent before sending them email campaigns.

Provide an easy opt-out option, such as an unsubscribe link in every email or an email preferences page. If users unsubscribe through your website, ensure their emails are added to AIQUA’s unsubscribed email list via API.



Email Campaign Quick Start [1]

https://docs.aiqua.appier.com/docs/email-integration



To learn more on handling email subscriptions, see Managing email subscriptions.

You can select from a variety of pre-built email templates, from your previously saved and customized templates, or add an email creatives with following editors:

Drag & Drop Editor 

HTML Editor

Follow these steps to set up a regular email campaign. 

Add your device to the test segment 

Create a regular email campaign

Before setting up your first email campaign, add your device to the test segment:

Go to Audience > Segment list, then click the three vertical dots on the Test Segment and select Edit segment.

Under Include users, click + Add new condition. Create a condition with the following settings:

From the first dropdown, select email.

Set the operator to equal.

Set the value to your email address.

Click Save to update your test segment.

Go to Campaigns > Regular campaigns, click + Create campaign, and select Email.

Enter a campaign name. In addition, add tags (optional) which can be used for filtering in the campaign list.

Under Audience section, select "Test Segment" from the Include Users of the Segment dropdown.

Next, set your Schedule campaign and the Campaign settings (optional).

In the Creative section, complete the required settings:

From Name: Enter the display name of the sender. This can only be static text.

Subject: Add a catchy subject line since this will appear as your email's subject title. The text can be static or dynamic text. 

Have users reply to a different Email address: Select if you want to use a different email address to receive any replies and bounces. This adds a "Reply To" field to the header of your email campaigns. When users click the Reply button, the "Reply To" email will be used instead of the "From" email. Reply-To Email Address and Reply-To Name can only be static text.

To design the body of your email campaign, click + Add Email Creative and select one of the tabs below:

Default templates: Start from a default template provided by Appier. See Email Templates.



Email Campaign Quick Start [2]

https://docs.aiqua.appier.com/docs/email-integration



Default templates: Start from a default template provided by Appier. See Email Templates.

My templates: Start from a template you have created previously.

Create Your Own: Create an email campaign from scratch by using Email Drag & Drop Editor or Email HTML Editor. 

Use the Test Your Creative button to send a test creative to the users in the test segment.

📘NoteWhen the message size exceeds 102 kb, Gmail clips the email and replaces the exceeded parts with a “View entire message” link. The message size is determined by the byte size of the email’s code (such as text, URLs, and tracking codes) rather than the size of images.

New email addresses logged via Appier SDK or uploaded via API are considered email subscribers by default. You can update users' email subscription status in the following ways:

Configure a custom unsubscribe URL in your account settings

Configure a custom unsubscribe URL in your account settings. After configuring a custom URL, a one-click unsubscribe button will be included at the top of your email for all email campaigns.

In addition, a POST request will be sent to the custom URL whenever a user clicks the one-click unsubscribe button.

Add unsubscribe links using the drag-and-drop email editor: Users who click the unsubscription links will be unsubscribed. See how to insert unsubscription links.

Update the unsubscription list via AIQUA API: When users update their email preferences, use these APIs to update their subscription status:

Add emails to the unsubscribed list.

Remove emails from the unsubscribed list.

When users are unsubscribed using the above methods:

Their user attribute email_unsubscribe will be set to true, and their email addresses are removed from the Email subscribers count in the segment List.



Email Campaign Quick Start [3]

https://docs.aiqua.appier.com/docs/email-integration



Their email addresses will be added to the AIQUA unsubscribed email list and your email campaigns will no longer be sent to these email addresses. The Test Segment is an exception. Users in this segment can still receive emails when you click Test Your Creative in the campaign creation page, even if they are on the unsubscribed list.

🚧ImportantDo not manually update the email_unsubscribe user attribute using:

Appier SDK attribute logging methods.

The Update User Profiles feature.

The Bulk Upload Offline Users API.

If you manually change email_unsubscribe to true, the user will be shown as unsubscribed in the profile, but the email will not be added to AIQUA's unsubscribed email list. As a result, the user will still continue receiving emails, and the email user count in the segment list will not match the sent number. The same issues occur if you try to subscribe a user by manually changingemail_unsubscribe to false.Updated about 1 month ago IP WarmupDrag & Drop EditorTable of Contents

Overview

Prerequisites

Limitations

Best practices

Creating your first email campaign

1. Add your device to the test segment

2. Create a regular email campaign

Managing email subscriptions



IP Warmup [0]

https://docs.aiqua.appier.com/docs/ip-warmup



IP warmup is the process of building up a good sender reputation for the IP address and domain that you are using to send email campaigns. To do this, start by sending a small number of emails to users and then gradually increase the volume over a period of time.

The goal is to show email service providers that this new IP is a legitimate email sender, which will increase the chance of your emails landing in the user's inbox instead of the spam folder. If you immediately start sending large volumes of emails without warming up, email providers might see your IP as a spam sender, resulting in your emails getting blocked or marked as spam in the future. 

In addition to sending volume, email providers also evaluate an IP based on how users interact with the emails, the number of invalid email addresses, and sending patterns.

IP warmup is needed:

If you are running email campaigns from this IP for the first time

If you have not sent email campaigns from this IP in a long time

If there will be a significant increase in the recipient size compared to your usual volume

Refer to the sections below to set up a warmup schedule, follow the best practices, and monitor the campaign performance.

Set a warmup schedule that starts with 500 or 1000 recipients on the first day. Gradually increase the number of emails sent per day until you reach the target volume. You can roughly double the volume each day or stretch it out a little more.

Before sending emails to your users, it is recommended to conduct an internal warmup by sending the emails to internal staff. Have your colleagues click on the links in the email to demonstrate user engagement. If the email ends up in the spam folder, have them mark the email as not spam, move the email back to the inbox, and click on the links.

Here's an example of a warmup schedule if the target volume is 400,000 emails.



IP Warmup [1]

https://docs.aiqua.appier.com/docs/ip-warmup



Here's an example of a warmup schedule if the target volume is 400,000 emails.

DayNumber of recipientsDay 1: Internal warmupInternal staff (up to 500)Day 21,000Day 32,000Day 45,000Day 510,000Day 620,000Day 740,000Day 880,000Day 9150,000Day 10250,000Day 11400,000

In addition to gradually increasing the volume, follow the best practices below.

Interactions from recipients are positive signs to email providers that this IP is not a spam sender, while emails that are blocked, hard-bounced, or marked as spam can hurt the sender reputation.

Use a "clean" email list. This list should consist of only real email addresses. Remove any invalid, bounced, or blocked email addresses.

Make sure the users have opted in to receive emails from you. This reduces the chance of getting reported as spam.

Include unsubscription links in the email to let users who do not want to engage opt out.

Target users who are likely to engage with your emails, especially in the first few days. You can create a segment to include the most active users, such as your premium members.

Make the email content interactive and relevant to the users.

Include interactive elements such as links and buttons. 

Include dynamic contents to tailor the content for each user. For example, include the user's actual name and images of the actual products they viewed on your website.

It is also recommended to place dynamic contents close to the start of the email body. Email providers are more likely to see each email as different and personalized.

When using regular campaigns to send your emails, it is recommended to set the campaign schedule as below:

Schedule the email campaigns to send at the end of an hour (e.g. 10:55 am). This allows email delivery to cross into two different hours so that your IP will have a lower hourly sent volume.



IP Warmup [2]

https://docs.aiqua.appier.com/docs/ip-warmup



Alternatively, you can run a trigger campaign where each email is sent at different times depending on when individual users complete a certain event. However, it might be more difficult to control the number of users who will receive the email per day.

📘BETASplit user is a Beta feature. Contact your customer success manager to enable it.

If you are sending emails using regular campaigns, you can split users into multiple segments. Skip this part if you are running trigger campaigns.

For example, if the goal is to send 20,000 emails on that day, you can split it into two split segments, each with 10,000 email users.

After the split segments are created, you can then create two regular campaigns and use different splits as the audience. Furthermore, you can slightly tweak the email content in one campaign so that the two campaigns consist of different content. You can also send the two campaigns at different hours to reduce the hourly sent volume.

After you start running IP warmup, be sure to monitor the performance of the campaigns.

In the campaign list, you can look at the Total Sent and the Delivered columns to monitor delivery rate, while Opens, Clicks, CTR (click-through rate), and Open Rate allow you to see whether your users are engaging with the content.

If you start seeing drops in the delivery rate or engagement rate:

Remove email addresses that bounced (qg_email_hard_bounced and qg_email_soft_bounced) and email addresses that reported your emails as spam (qg_email_spammed).

Do not increase the volume. You can try using the same volume as the previous day. For example, if you sent out 10,000 emails on day 5 and noticed a significant decline, keep the volume at 10,000 emails on day 6. 

Evaluate your email content again. 

Contact Appier Support for assistance if needed.Updated about 2 months ago Table of Contents

Overview

Set a warmup schedule

Example

Best practices

Send to a clean list of engaged users

Create engaging and tailored email content

Adjust the email schedule

Split users into multiple segments



IP Warmup [3]

https://docs.aiqua.appier.com/docs/ip-warmup



Create engaging and tailored email content

Adjust the email schedule

Split users into multiple segments

Monitor the campaigns



Drag & Drop Editor [0]

https://docs.aiqua.appier.com/docs/design-email



The Drag & Drop Editor allows you to create your own email creatives. You can use this editor in regular campaigns or trigger campaigns.

To access the Drag & Drop Editor, create an email campaign and click Add Email Creative under the Creative section. 

To start with an existing template, you can select a template under Default templates or My templates. 

To start from scratch, click the Create Your Own tab and click Drag & Drop Editor.

Inside the Drag & Drop Editor, three tabs are available: Content, Rows, Settings.

Start by clicking the Settings tab to adjust overall settings, including:

Content area width

Content area alignment

Background color

Content area background color

Default font

Link color

Optional properties: Set the preheader text for your email. The preheader appears next to the subject line in recipients' inboxes to provide a brief preview of your email campaign. Add dynamic content and emojis to the preheader to entice recipients to open your message.

Click the Rows tab to add different types of rows inside your email's body. Drag a row, and then drop it anywhere you see Drag it here.

To make adjustments, click the white space on the two sides of the row to see its Row Properties on the right.

Click the Content tab to add content blocks inside your email's body. 

Drag and drop. Drag an available feature block from the right, and drop it anywhere you see Drag it here. 

Click on the content block to access content properties on the right.

If you click on a text box or button you can customize the text options.

The following types of Content are available:

Text: This lets you add a static or dynamic text in the Design Email.

Image: This lets you add a static or dynamic image in the Design Email. 

Click Browse to select the type of image you want to add. 

You can select Upload to upload an image from your computer, or Search free photos to do an image search. Corresponding images are retrieved from available Creative Commons galleries.



Drag & Drop Editor [1]

https://docs.aiqua.appier.com/docs/design-email



Select the image you want to use and then click Insert. The image appears in the Image box you dropped in the editor. 

🚧IMPORTANT:It is suggested to not use Imgur to host your images, because Gmail tends to block emails that contain Imgur images.

Button: This lets you add an action button in your email.

Divider: Add this to separate the elements in your email with a horizontal line.

Social: This lets you add social media icons to your email message and link them to a corresponding social media account.

HTML: This lets you add your own HTML code to an email message. The HTML block you added turns into an HTML preview when you start adding your HTML code under Content Properties.

Video: This lets you add a video in your email using a url.

Icon: This lets you add an icon in your email. For example, a location icon in front of your business address.

👍One-click unsubscribeIf you're using AIQUA's default unsubscribe URL and you insert an unsubscription link in the editor, a one-click unsubscribe button (via list-unsubscribe header) is automatically included with the email.

There are a couple of ways to add unsubscribe links to your email. 

Click on the text box, click More, and select Insert unsubscription link.

Click on a button, go to Content Properties on the right, and click Insert unsubscription link under the Url field.

In the HTML block, insert {{ aiqua_unsub_url }} in the HTML tag.

In email campaigns, you can use dynamic content that changes based on each user's behaviors and attributes. For more details, see Dynamic Content.

Updated about 2 months ago Table of Contents

Accessing the Drag & Drop Editor

Using the Drag & Drop Editor

Settings

Rows

Content

Using Dynamic Content inside Email Editor



Email HTML Editor

https://docs.aiqua.appier.com/docs/email-html-editor



AIQUA's Email HTML Editor allows you to create and preview email templates made with custom HTML. You can choose to save your custom HTML as a template which can be reused in future campaigns.

To avoid unexpected differences between the in-editor preview, the thumbnail preview in the AIQUA Dashboard, and your final campaign email, make sure to:

Declare a character encoding scheme.

Check that the HTML used in your template is supported by the email client(s) you are targeting.

If your HTML template doesn't include a character encoding declaration, non-English text may not display properly in your campaign email. To prevent this issue, include an encoding declaration in your HTML's tag specifying an encoding scheme.

For example, an encoding declaration specifying the utf-8 scheme looks like this:







and a full HTML file using the utf-8 encoding looks like this:







AIQUA Email HTML Editor





The text on this page is encoded in UTF-8.







Not all email clients support all available HTML tags and CSS properties, so it's important to check if your custom HTML contains tags or properties unsupported by a particular email client.

Tools like www.caniemail.com allow you to search for specific HTML tags, CSS properties, or email clients to determine if your custom HTML will be fully supported, as seen below.

The background-color property is supported by all Apple Mail, Gmail, and Outlook email clients.

Searching by tag or property name returns columns of email providers (such as Gmail and Outlook) and sub-columns of email clients from that provider (such as iOS and Android). Email clients that support the tag or property you specified will contain a green box with a checkmark.Updated over 1 year ago Table of Contents

Usage Notes

Declare a Character Encoding Scheme

Check for Supported HTML Tags and CSS Properties



LINE Campaign Quick Start [0]

https://docs.aiqua.appier.com/docs/line-integration



You can integrate AIQUA with your LINE official accounts to send campaigns to followers in your LINE channel. Doing so allows you to use segments or creatives generated in AIQUA to better target your audiences.

There are several types of LINE account for businesses. Currently, the following types of LINE official account can be integrated with AIQUA. 

LINE Premium Official Account

LINE Verified Official Account

Follow the steps below to connect AIQUA with your LINE official account.

Log into your LINE official account, click Settings and select Messaging API in the left pane. Here you can find the channel info that needs to be entered on AIQUA dashboard.

On AIQUA dashboard:

a. Click your AIQUA account name in the lower-left corner and select Integration > Instant Messaging > LINE.

b. Click the Edit button and type a Channel Name.

c. Enter the Channel ID and Channel Secret of the LINE account retrieved in step 1.

d. Click Save. 

After setting up the connection, contact Appier Support (ess_support@appier.com). Appier Support will complete the configuration on Appier's end.

When configuration is done, the number of LINE followers is shown in the integration page.

📘Note:If you have integrated other messaging services (such as a third-party chatbot service) using the same LINE account credential, the LINE API rate limit is shared among AIQUA and these messaging services. More info about LINE's rate limit: https://developers.line.biz/en/reference/messaging-api/#rate-limits.You can use the account-level Notification Send Rate setting on AIQUA dashboard to control the send rate.

Once AIQUA is connected with the LINE account, a default LINE - All Followers segment will be automatically created. 

To understand how users are counted in the LINE segment, see LINE Segment FAQs.

You can send notifications to LINE followers using: 

Regular Campaigns

Trigger Campaigns

Start by running a regular campaign.

From the left menu, go to Campaigns > Regular campaigns, click + Create Campaign, then select LINE.

Enter a campaign name.



LINE Campaign Quick Start [1]

https://docs.aiqua.appier.com/docs/line-integration



From the left menu, go to Campaigns > Regular campaigns, click + Create Campaign, then select LINE.

Enter a campaign name.

Set the schedule and audience for the campaign.

Set up your creative. The following types of LINE creatives are available: Rich Message, Text, Photo, Video, Carousel Templates.

Click Add Message to add more creatives. You can deliver up to 5 creatives to followers each time a LINE campaign is sent. 

Use the Test Your Creative button to send a test creative to users in the Test Segment. You will need to first add your LINE account to the test segment.

You can enable Goal Events and select the events that will be shown as attributed events in the campaign performance.

Click Save.

In trigger campaigns, campaigns are triggered based on user events collected from your SDK-integrated website or app (for example, users viewed a product on your website). In order to send campaigns to LINE users based on web or app user events, AIQUA needs to be able to map the LINE users with the web or app users first.

LINE users are synced with web and app users when:

Users click on a link in AIQUA LINE campaigns (rich messages or carousel templates) and land on your SDK-integrated website or app. 

Users click on a LIFF URL you have set up. For details, see LINE LIFF URLs.

Before running a LINE trigger campaign, you should first collect enough synced LINE users via regular campaigns or LIFF URLs.

After LINE campaigns are created, you can manage them in the campaign list. The campaign list allows you to send out campaigns, download performance reports, set a campaign schedule, and edit campaign settings. Refer to the following guides for details.

Managing Regular Campaign

Managing Trigger Campaign

Downloading performance reports

When looking at the table in the campaign list, the following performance-related columns are applicable for LINE campaigns: 

Runs: The number of times LINE campaigns are sent to users.

Clicks: The number of times users click on your LINE campaign.



LINE Campaign Quick Start [2]

https://docs.aiqua.appier.com/docs/line-integration



Runs: The number of times LINE campaigns are sent to users.

Clicks: The number of times users click on your LINE campaign.

CONV COUNT / CONV VALUE: The number of conversion events achieved and the associated value.

Updated about 2 months ago LINE CreativesLINE User Profile SyncLINE Segment FAQsTable of Contents

Integrating AIQUA with LINE Accounts

LINE Segment

Creating LINE Campaigns

Creating Regular Campaigns

Creating Trigger Campaigns

Managing LINE Campaigns



LINE Creatives [0]

https://docs.aiqua.appier.com/docs/line-creatives



The following creatives types are available for LINE campaigns:

Rich message

Text

Photo

Video

Carousel templates

These are the available options:

Select Photo: This is the photo that will show up in your LINE notification. You can add up to 10 clickable areas by selecting Add clickable area and then adding the destination URL for each area. Only HTTPS/HTTP links are allowed.

Notification Message: The text users will see in the LINE chat list preview.

Message: The contents of the notification. 

Select Photo: The image file displayed in the notification.

Select Video: You can upload video here to deliver a video notification to users.

Select Cover Image: The image displayed to the user before the video is played.

You can create up to 10 sets of content (columns) for each carousel template. Users can see different columns by swiping left and right. There are two types of carousel templates: Carousel and Image Carousel. 

Left: Carousel

Right: Image Carousel

You can choose to include images for your carousel messages or make them text only. Up to three action buttons can be configured. The following options are available:

Thumbnail Image Aspect Ratio: Select the aspect ratio for your thumbnail image. Choose between square, rectangular, or no image.

Use Title: Choose whether or not to include a title for your message.

Number of Action Buttons: This option allows you to enable up to three action buttons.

Action Button Type: You can set the action button type to URI, Message, or Postback. 

URI: The action button will direct the user to the destination page you specified. Only https/http links are allowed.

Message: This is useful for LINE channels integrated with a bot. When user taps the action button, a text is sent in the channel as a message from the user. 

Postback: This is useful for LINE channels integrated with a bot. When user taps the action button, a postback event is returned to the server via webhook. 

Notification Message: The text users will see in the LINE chat list preview.



LINE Creatives [1]

https://docs.aiqua.appier.com/docs/line-creatives



Notification Message: The text users will see in the LINE chat list preview.

Under Column, the following options are available. You can click Add Carousel Column to create multiple sets of content for each carousel message.

Image: You can choose to upload an image or paste the link for the image.

Image Destination URI: This is the page users are taken to after tapping the image. Only https/http links are allowed.

Title: The title of the notification. 

Description: The main notification message.

Button Label: The button label text.

Button Destination URI: The page users are taken to after tapping the action button. Only https/http links are allowed. This field is available when Action Button Type is set to URI.

Button Description: The text displayed in the channel as a message sent by the user when the action button is tapped. This field is available when Action Button Type is set to Message.

Button Postback Data: The data that will be sent to the server when the action button is tapped. This field is available when Action Button Type is set to Postback.

In an image carousel, the image is used as a background and the action button is placed at the bottom of the image.

The following option is available:

Notification Message: The display text in the LINE chat list preview.

Under Column, the following options are available. You can click Add Carousel Column to create multiple sets of content for each carousel message.

Image: You can choose to upload an image or paste the link for the image.

Button Label: The button label text.

Button Destination URI: The page users are taken to after tapping the action button. Only https/http links are allowed.

Refer to the following table for specifications and limitations of LINE creatives.

🚧NoteText exceeding the stated character limits will be cropped when using dynamic content in text fields such as Notification Message, Message, Title, Description and Button Label.



LINE Creatives [2]

https://docs.aiqua.appier.com/docs/line-creatives



LINE CreativeSpecificationsSupported for Dynamic ContentSupported for LINE Desktop AppRich message• You can assign a maximum of 10 clickable areas for the image to be uploaded to the AIQUA dashboard

• Recommended image resolution: at least 1040 px in width

• Maximum file size: 10 MBNoYesText• Maximum length: 500 charactersYesYesPhoto• Maximum image resolution: 1024 px × 1024 px

• Maximum file size: 10 MBNoYesVideo• MP4 video format

• Maximum length: one minute

• Maximum file size: 100 MBNoYesCarousel templates• Maximum image resolution: 1024 px × 1024 px

• Maximum image file size: 10 MB

• Image aspect ratio: 1.51:1 for carousel - rectangle, 1:1 for carousel - square and image carousel

• Maximum title length: 40 characters

• Maximum description length: 120 characters

• Maximum of 20 characters for the button label for a carousel, and 12 characters for button label of image carousel

• Button Destination URI must be a valid HTTPS URLYesYes

Reference: LINE official documentationUpdated over 1 year ago Table of Contents

Rich Message

Text

Photo

Video

Carousel Templates

Carousel

Image Carousel

Specifications and Limitations



LINE User Sync [0]

https://docs.aiqua.appier.com/docs/line-user-profile-sync



📘PrerequisitesComplete the following before configuring LINE user sync:

Integrate your LINE account with AIQUA.

To sync LINE users with your website users, integrate your website with the Appier Web SDK.

To sync LINE users with your app users, integrate your app with the Appier Android or iOS SDK. 

Android SDK 7.12.0 or later

iOS SDK 7.20.0 or later

LINE user sync allows you to map a user's LINE profile to their web or mobile (Android, iOS) profile in AIQUA. After a user's LINE profile is synced, their events on your website or mobile app can be used as triggers in Journey Maps and trigger campaigns. You can sync users via:

LINE creatives (rich messages or carousel templates)

LINE Front-end Framework (LIFF) URLs

Android deep links

iOS deep links

Sync LINE users using LINE creatives (rich messages or carousel templates) by configuring a link to your Appier SDK-integrated website or mobile app in the creative's settings. Users who click on the creative that links to your website or mobile app will have their LINE profile synced with their AIQUA profile.

After you've integrated your website or mobile app with the Web or Android SDK, no additional setup is required. For instructions on implementing LINE user sync for iOS devices, see Syncing via iOS Deep Links.

📘NoteOnly HTTPS/HTTP links are supported in LINE creatives.

Sync LINE users by embedding LINE Front-end Framework (LIFF) URL that users can click to initiate the user sync flow. Users who complete the LIFF app user sync flow successfully will have their LINE profile synced with their AIQUA profile.

In addition to integrating the Appier SDK, you'll need to create a LIFF app to generate a LIFF URL.

📘NoteLIFF URLs can be used anywhere that a URL can be embedded, such as:

LINE rich menus

Your website or mobile app

LIFF URLs can be used wherever links can be embedded, including your website, app, or LINE rich menu. Depending on where the LIFF URL is embedded, certain steps may differ slightly.



LINE User Sync [1]

https://docs.aiqua.appier.com/docs/line-user-profile-sync



👍TipImplementing LINE user sync using a LIFF app gives users the option to add your LINE Official Account, if they haven't done so already.

The user clicks your LIFF URL.

The user is then prompted to:

i. Sign into their LINE account (if the user isn't currently logged in to their LINE account)

ii. Grant the LIFF app permission to access the user's LINE profile data

iii. Add your LINE Official Channel (if the user hasn't already done so)

After responding to the prompts, the user is redirected to the destination URL.

If the user granted permission to the LIFF app, the user's LINE user ID is passed to the Appier SDK which then syncs the user's LINE profile data with the user's web or mobile profile. If the user didn't grant permission to the LIFF app, their profile is not synced.

Complete the following steps to create a LIFF app and generate a LIFF URL.

Log in to the LINE Developers Console and select a provider.

Go to the Channels tab and click Create a new channel. Choose LINE Login for the channel type.

Enter a Channel name and Channel description. For App types, choose Web app. Agree to the LINE Developers Agreement and click Create.

In the LINE Login channel you just created, go to the LIFF tab and click Add.

Next, configure the following required settings for the LIFF app:

SettingDescriptionLIFF app nameYour LIFF app's name.SizeThe size of the blank LIFF browser the user temporarily sees before being redirected to an external browser.

We recommend choosing Compact, which ensures that the LIFF browser only covers the bottom half of the device's screen. See the LIFF docs for size references.Endpoint URLInput a placeholder URL for now, such as https://appier.com.

After you've finished creating the LIFF app, contact your customer success manager for your custom endpoint URL.ScopesChoose profile.Bot link featureChoose On (aggressive).

Contact your customer success manager for your custom Endpoint URL. Once you've received your custom URL, configure it in your LIFF app settings.



LINE User Sync [2]

https://docs.aiqua.appier.com/docs/line-user-profile-sync



From the LINE Developers Console, select the LINE Login channel you created for the AIQUA LIFF app.

Go to the LIFF tab, select the LIFF app you created, then do the following:

Set Endpoint URL to the URL provided by your customer success manager.

Copy the LIFF app's LIFF URL and provide this URL to your customer success manager.

Linking your LINE Official Account to the LIFF app allows you to request users to follow your account after they've logged in. This prompt is only presented to users who click the LIFF app URL.

Navigate to your LINE Login Channel's Basic Settings tab.

Under Linked OA, click Edit.

Select the LINE Official Account you want users to add, then click Update. 

📘NoteFor linking requirements, see LINE's documentation on how to link your LINE Official Account with your channel.

You'll need to construct your LIFF URL before being able to use it. The LIFF URL has the following format:

https://liff.aiqua.appier.com/v2/?dest=&openExternalBrowser=1&mode=aggressive

The URL can be divided into five parts:

URL portionDescription1https://liff.aiqua.appier.com/v2/The base URL.2Replace with your AIQUA app ID. Your app ID can be found in the AIQUA Dashboard on the Account Settings page.3?dest=Replace with an encoded version of your destination URL.4&openExternalBrowser=1Opens the destination URL in an external browser.5&mode=aggressiveGives users the option to add your LINE Official Account after clicking on a LIFF app URL and logging in to their LINE account.

A valid AIQUA LIFF URL might look like this:

https://liff.aiqua.appier.com/v2/0000?dest=https%3A%2F%2Fwww.example.com&openExternalBrowser=1&mode=aggressive

The AIQUA app ID is 0000

The destination URL https://www.example.com has been encoded to be https%3A%2F%2Fwww.example.com

LIFF URLs can be used wherever links can be embedded, including:

Websites

Apps

LINE rich menus



LINE User Sync [3]

https://docs.aiqua.appier.com/docs/line-user-profile-sync



LIFF URLs can be used wherever links can be embedded, including:

Websites

Apps

LINE rich menus

Users who click the LIFF URL and complete the user sync flow will have their LINE profiles synced with the web or mobile profile in AIQUA, meaning that their events on your website or mobile app can be used as triggers in Journey Maps and trigger campaigns.

The Android SDK automatically handles Android deep links and to sync LINE users. No additional setup or code modifications are required.

There are two ways to enable LINE user sync with iOS deep links:

Two types of URLs can be used to open your app: URLs using a custom iOS URL scheme and universal links.

To handle URLs using a custom iOS URL scheme: Call handleOpenUrl() in application(_:,open:,options:)

To handle universal links: Call handleUserActivity() in application(_:,continue:,restorationHandler:)

The following code sample demonstrates how to properly call handleOpenUrl() and handleUserActivity():

func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {

QGSdk.getSharedInstance().handleOpenUrl(url)

...

}

func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {

QGSdk.getSharedInstance().handleUserActivity(userActivity)

...

}

- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options {

[[QGSdk getSharedInstance] handleOpenUrl:url];

...

}

- (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray> * _Nullable))restorationHandler {

[[QGSdk getSharedInstance] handleUserActivity:userActivity];

...

}

When method swizzling is enabled in your app, the iOS SDK automatically handles LINE user syncing. For instructions on enabling method swizzling, see Method Swizzling in the iOS SDK.Updated about 1 year ago Table of Contents

Overview



LINE User Sync [4]

https://docs.aiqua.appier.com/docs/line-user-profile-sync



Overview

Syncing via LINE creatives

Syncing via LIFF URLs

LIFF app user sync flow

LIFF app setup guide

Syncing via Android deep links

Syncing via iOS deep links

Option 1: Handle iOS deep links in your app (Recommended)

Option 2: Enable method swizzling



LINE Segment FAQs [0]

https://docs.aiqua.appier.com/docs/line-segment-faqs



In the segment list, the LINE Subscribers count includes LINE users who are following your LINE channel, and excludes those who have unfollowed or blocked the channel. 

AIQUA detects for new LINE followers once a day.

The user and subscriber counts of non-default segments are only updated when the segment setting page is edited or resaved.

The user and subscriber counts of default segments are automatically updated once a day. Due to the different update time, the LINE Subscribers count listed under [LINE] All Followers may be slightly different from the count listed under All Users / All Audiences. You can see the update time under the segment name.

📘Note:Before 2021 April, the LINE Subscribers count of the All Users / All Audiences default segment and any created segments included LINE subscribers who have unfollowed or blocked the channel. This has been changed.

After your LINE channel is integrated with AIQUA, AIQUA automatically creates a default segment [LINE] All Followers. The number of followers in your LINE channel is listed under LINE Subscribers.

If you are running AIQUA LINE campaigns or are using LIFF URL, you will start seeing user counts listed under web, Android, iOS, Email, and SMS as shown below.

This is because AIQUA can sync LINE users with web, Android and iOS users if the LINE users click on links in your LINE campaigns (Rich messages and carousel templates) and are directed to your Appier SDK-integrated website or app.

If you have set up LINE LIFF URLs, users who click on the LIFF URLs can also be synced.

ChannelsReasonsWeb

Android

iOSThe LINE user is synced with web, Android, or iOS users as described above.EmailIf the synced LINE user has an email address in the user profile, the user will be counted in the Email Subscribers in the segment list. Users who have unsubscribed from email campaigns are not included.SMSIf the synced LINE user has a phone number in the user profile, the user will be counted in the SMS User segment list.



LINE Segment FAQs [1]

https://docs.aiqua.appier.com/docs/line-segment-faqs



AIQUA enables LINE user sync by default. To disable LINE user sync for web, please reach out to your customer success manager.Updated over 1 year ago Table of Contents

How are LINE subscribers counted in the segment list?

Why do LINE segments include web, mobile, email, and SMS users?

Disable automatic LINE user sync (Web)



Kakao Campaign Quick Start

https://docs.aiqua.appier.com/docs/kakao-quick-start



AIQUA offers two types of Kakao campaign types, giving you the flexibility to create and manage a diverse set of campaigns to meet your marketing goals.

Kakao Moment: Leverage Kakao Moment's diverse and flexible creative templates for advanced targeting and detailed analytics.

Kakao: Send Chingu Talk messages for direct, personalized communication and ongoing customer engagement.

For AIQUA to be able to deliver Kakao campaigns: 

AIQUA needs to be integrated with your KakaoTalk Channel. See Integrating AIQUA with a KakaoTalk Channel.

AIQUA needs to have the user's phone number (phoneNo). You can upload phone numbers to AIQUA on the AIQUA dashboard or via API.

The user needs to opt in to your KakaoTalk channel.

To learn more, refer to the guide corresponding to the Kakao campaign type you'd like to create:

Kakao Moment

Kakao

After Kakao campaigns are created, you can manage them in the campaign list using the action buttons. In the table, the following columns are applicable for Kakao campaigns: 

Runs: A run refers to the instance of sending the regular campaign to users. This indicates the number of runs of the campaign, until its end date.

Total sent: This is the total number of notifications sent by AIQUA during the entire campaign duration.

Delivered: The number of campaigns successfully delivered to the user by the Kakao service provider. 

Last sent time: Last sent time is the time when the last notification arrives at the notification service provider.

Updated about 2 months ago Table of Contents

Overview

Requirements

Creating Kakao campaigns

Managing Kakao campaigns



Kakao Moment Campaigns [0]

https://docs.aiqua.appier.com/docs/kakao-moment-campaigns



Create a Kakao Moment campaign to leverage Kakao Moment's diverse and flexible creative templates for advanced targeting and detailed analytics. To get started with AIQUA's Kakao Moment campaigns, complete the following steps:

Add Appier as a Kakao channel manager. 

Create a Kakao moment campaign.

👍TipRefer to the Kakao Moment creative specifications and dynamic content variable specifications when creating your campaign to ensure your campaign content meets all the requirements.

Blackout window: Kakao Moment campaigns can't be sent from 9 PM to 8 AM KST.

Phone number region restrictions: Kakao Moment campaigns can only be sent to Kakao accounts linked to a Korean phone number.

Real-time preview: Real-time previews of creative content is not supported.

Log in to the Kakao business console and go to Manage channel > Manager, click Invite new manager.

Invite the following account: kakao@appier.com, then click Invite.

Appier will create a Kakao Moment account on your behalf (this process may take several days), after which you'll receive an invitation under advertisement > Moment in the Requesting/Invited Advertising Accounts tab. 

After accepting the invitation to the Kakao Moment account, pre-load your account with ad credits. Ad credits are required to run Kakao Moment campaigns from AIQUA.

Next:

If your company doesn't have Kakao developer app yet, Appier will handle the creation of the Kakao developer app for you—no additional effort required.

If your company already has a Kakao developer app, invite Appier to onboarding your Kakao developer app.

📘Skip this section if your company doesn't have Kakao developer app yet. Appier will handle the creation of the Kakao developer app for you—no additional effort required.

Log in to Kakao Developers and select the app to be onboarded.

Go to Team Management.

Invite kakao@appier.com with the Editor role to enable Appier to onboard your developer app.

If you're to invite kakao@appier.com, please contact Appier Support (ess_support@appier.com) for assistance.



Kakao Moment Campaigns [1]

https://docs.aiqua.appier.com/docs/kakao-moment-campaigns



If you're to invite kakao@appier.com, please contact Appier Support (ess_support@appier.com) for assistance.

Go to Campaigns > Regular campaigns, click + Create campaign, then select Kakao Moment.

Enter a campaign name.

Choose how you'd like to send the campaign.

Send Manually: Select this option to send the campaign by manually clicking the Send Now button on the campaign list page.

One-Time Schedule: Schedule the campaign to be sent at a specific date and time. 

Recurring Schedule: Specify the first campaign send time and the time interval (in days) for resending the campaign.

Set the audience for your campaign by selecting which segments should be included or excluded.

Select a creative type, then add creative content, such as a message, images, and action buttons. 

📘Creative specificationsEnsure that your creative confirms to the Kakao Moment creative specifications to ensure successful campaign delivery.

(Optional) Add dynamic content to the creative's Message field to ensure that messages are tailored to each recipient. To add dynamic content, click {...} in the bottom right corner of the input field.

From the Dynamic content dropdown, select the attribute or event that should replace the dynamic content variable.

From the Variable type dropdown, select one of the supported Kakao variables to personalize your promotional text. Refer to Dynamic content variable specifications to learn more about dynamic content variables.

Enter fallback text for dynamic content variables to handle cases where the selected variable is empty. If a variable is empty, a fallback mechanism will send the fallback text to prevent delivery issues.

Under Frequency Cap Settings, choose whether this campaign should ignore or apply your account setting's frequency cap.

Apply Frequency Cap: Use the frequency cap settings configured in account settings. This applies to the minimum interval for regular campaigns.

Ignore Frequency Cap: Override all frequency caps for important messages by ignoring the minimum interval.



Kakao Moment Campaigns [2]

https://docs.aiqua.appier.com/docs/kakao-moment-campaigns



Ignore Frequency Cap: Override all frequency caps for important messages by ignoring the minimum interval.

📘Frequency cap behaviorNote that frequency cap settings apply independently to both standard Kakao campaigns and Kakao Moment campaigns.For example, if the frequency cap has a minimum interval setting of 60 seconds, you can send still send one Kakao campaign and one Kakao Moment campaign in the same 60-second period.

Review your campaign settings to ensure everything is correct, and when you're ready, click Save to finalize and launch your campaign.

Refer to the sections below for a list of specifications for each Kakao Moment creative type. To ensure successful campaign delivery, please adhere to the creative specifications.

Carousel commerce 

Carousel feed 

Text 

Wide image 

Wide list 

A carousel commerce creative can contain:

One optional intro card.

Up to five standard carousel commerce cards, for a total six cards (including the intro card). 

ComponentSpecificationsImage• Supported file formats: JPG, JPEG, PNG. Images must be RGB color mode.

• Maximum file size: 10 MB.

• Recommended image sizes: 800 x 400 (2:1 aspect ratio), 800 x 800 (1:1 aspect ratio), 800 x 600 (4:3 aspect ratio).Destination URL• Must be set using dynamic content.Title• Character limit: Up to 20 characters after dynamic content substitution.Message• Character limit: Up to 50 characters after dynamic content substitution.

• URLs must begin with http:// or https://.

ComponentSpecificationsImage• File format: JPG, JPEG, PNG. Images must be RGB color mode.

• Maximum size: 10 MB.

• Recommended image sizes: 800 x 400 (2:1 aspect ratio), 800 x 800 (1:1 aspect ratio), 800 x 600 (4:3 aspect ratio).Title• Character limit: Up to 25 characters after dynamic content substitution.Price information• Accepted values for Won (₩) and Yen (￥): Only integers can be entered (0 to 99,999,999).



Kakao Moment Campaigns [3]

https://docs.aiqua.appier.com/docs/kakao-moment-campaigns



• Accepted values for Dollars ($) and Euro (€): Values with up to two decimal places are supported.Discount price information• Accepted values for Won (₩), Yen (￥): Only integers can be entered (0 to 99,999,999).

• Accepted values for Dollar ($), Euro (€): Displayed to 2 decimal places (rounded down to 3 or fewer)

• The discounted price must be at least 1% lower than the value entered for price information.Destination URL• Can be set by specifying a static URL or using dynamic content.Buttons• Button text character limit: Up to eight characters after dynamic content substitution.

• Destination URL: Must be set using dynamic content.

ComponentSpecificationsImage• Supported file formats: JPG, JPEG, PNG. Images must be RGB color mode.

• Maximum file size: 10 MB

• Recommended image sizes: 800 x 400 (2:1 aspect ratio), 800 x 600 (4:3 aspect ratio)

Except for the first required card, the aspect ratio for all additional carousel feed cards must be identical.Title• Character limit: Up to 20 characters after dynamic content substitution.Buttons• Button text character limit: Up to eight characters after dynamic content substitution.

• Destination URL: Must be set using dynamic content.Message• Character limit: Up to 180 characters after dynamic content substitution.

• URLs must begin with http:// or https://.

ComponentSpecificationsImage• File format: JPG, JPEG, PNG. Images must be RGB color mode.

• File size: Up to 10MB.

• Recommended image sizes: 800 x 300 (2:1 aspect ratio), 800 x 800 (1:1 aspect ratio), 800 x 600 (4:3 aspect ratio).Message• Character limit: Up to 400 characters after dynamic content substitution, if no image is attached. If an image is attached, the character limit is 300 character.

• URLs must begin with http:// or https://.Buttons• Destination URL: Must be set using dynamic content.

ComponentSpecificationsImage• File format: JPG, JPEG, PNG. Images must be RGB color mode.

• File size: Up to 10 MB.



Kakao Moment Campaigns [4]

https://docs.aiqua.appier.com/docs/kakao-moment-campaigns



ComponentSpecificationsImage• File format: JPG, JPEG, PNG. Images must be RGB color mode.

• File size: Up to 10 MB.

• Recommended image size: 800 x 600 (4:3 aspect ratio).Message• Character limit: Up to 76 characters after dynamic content substitution.

• URLs must begin with http:// or https://.Buttons• Destination URL: Must be set using dynamic content.

ComponentSpecificationsTitle• Character limit: Up to 20 characters after dynamic content substitution.List item 1: Image• File format: JPG, JPEG, PNG.

• File size: 10 MB.

• Recommended image size: 800 x 400 (2:1 aspect ratio).List item 1: Text• Character limit: Up to 25 characters after dynamic content substitution.List items 2~4: Image (Minimum 2, maximum 3)• File format: JPG, JPEG, PNG.

• File size: 10 MB.

• Recommended image size: 800 x 800 (1:1 aspect ratio).List items 2~4: Text (Minimum 2, maximum 3)• Character limit: Up to 30 characters after dynamic content substitution.Buttons• Button text character limit: Up to eight characters after dynamic content substitution.

• Destination URL: Must be set using dynamic content.

When adding variables in dynamic content, you need to map the field to a Kakao variable type.

You can only use dynamic content that maps to an existing Kakao variable type (any option in the Variable type dropdown). Incorrect mappings, such as including dynamic content that doesn't match any Kakao variable type or mapping dynamic content to a Kakao variable type that doesn't match its type, can result in account penalties. 

The corresponding dynamic content must conform to Kakao's variable specifications to avoid account penalties from Kakao. Please pay special attention to the following requirements and limitations:

Number available: This Kakao variable type can only be used a certain number of times in a single campaign.

Length: The dynamic content must fit the length requirements of the Kakao variable type.

Data type: The dynamic content must be of the same data type as the Kakao variable type.



Kakao Moment Campaigns [5]

https://docs.aiqua.appier.com/docs/kakao-moment-campaigns



Data type: The dynamic content must be of the same data type as the Kakao variable type.

🚧ImportantTo avoid account penalties from Kakao:

Ensure that the dynamic content maps to the correct Kakao variable type selected from the Variable type dropdown.

Ensure that your dynamic content conforms to the specification of the Kakao variable it's mapped to.

For dynamic content variables whose format aligns with our AIQUA's suggested data format AIQUA automatically maps the variable with the corresponding Kakao variable. For event parameter and attribute data that isn't automatically mapped, you can choose the mapping when setting up the campaign creative.

The following table provides the automatic mapping that AIQUA sets for dynamic content variables.

Dynamic content variables are event parameters or attributes.

The Variable type is the Kakao variable type that maps to the dynamic content variable.

Dynamic content variable (attribute)Preset variable typeuser_idUser IDbirthdayDatenameUser name

Dynamic content variable (event parameter)Preset variable typeproduct_idProduct IDproduct_pricePrice - regularproduct_nameProduct nameuser_idUser IDratingUser ratingUpdated 3 months ago Table of Contents

Overview

Notes and limitations

Adding Appier as a Kakao channel manager

Invite Appier to onboard your Kakao developer app (for existing apps only)

Creating a Kakao Moment campaign

Kakao Moment creative specifications

Carousel commerce

Carousel feed

Text

Wide image

Wide list

Dynamic content variable specifications

Automatic variable mapping

Attributes

Event parameters



Kakao Campaigns [0]

https://docs.aiqua.appier.com/docs/kakao-campaigns



Kakao offers two types of messages. You can only send Chingu Talk messages via AIQUA's Kakao campaigns. 

Chingu Talk (supported by AIQUA): For sending promotional messages such as an annual sale announcement. 

Alim Talk (not supported by AIQUA): For sending transactional messages such as a reservation confirmation. 

For AIQUA to be able to deliver Kakao campaigns: 

AIQUA needs to be integrated with your KakaoTalk Channel. See Integrating AIQUA with a KakaoTalk Channel.

AIQUA needs to have the user's phone number (phoneNo). You can upload phone numbers to AIQUA via AIQUA dashboard or via API.

The user needs to opt in to your KakaoTalk Channel.

Kakao only allows you to send messages between 8:00 AM and 8:00 PM (Korea Standard Time zone).

Dynamic content is not supported in Kakao campaigns.

To integrate AIQUA with your KakaoTalk Channel, follow the instructions below.

Make sure your KakaoTalk Channel is connected to a Kakao business account and this channel is verified by Kakao. 

Contact Infobip, the service provider of KakaoTalk, to create an Infobip account. Infobip will assist you in connecting this Infobip account with your Kakao account, and provide a Kakao Sender Key to you. See Infobip's documentation for the contact information.

You will receive the following from Infobip:

Access to Infobip portal: https://portal.infobip.com/

Access to WiseMOKA dashboard for uploading Kakao images: https://moka.carrym.com

Your Kakao Sender Key

Contact Appier support and provide the following information. Appier support will complete the configuration on the Appier side.

Sender Key: This is the Kakao Sender Key obtained from Infobip in the previous step.

Base URL: You can find this information by visiting Infobip Portal > Home.

API Key: You can find this information by visiting Infobip Portal > Home > Manage API Keys.

After configuration is done, go to the AIQUA dashboard, click your account name in the lower-left corner, and select Integration > Instant Messaging > Kakao to make sure your Kakao account is connected.



Kakao Campaigns [1]

https://docs.aiqua.appier.com/docs/kakao-campaigns



Before creating Kakao campaigns, you must first upload the images to the Kakao server using the WiseMOKA dashboard if you want to include images in your campaigns. Make sure the images follow the specifications listed in Kakao's official guides. There are two types of image: normal image and wide image.

Normal imageWide imageBody Text400 characters76 charactersRecommended size720 px * 720 px800 px * 600 pxSize limitIf the width is less than 500 px, or if the aspect ratio is either less than 2:1 or exceeds 3:4, upload is not allowed.If the aspect ratio exceeds 4:3, upload is not allowedFile format.jpg, .png.jpg, .pngFile size (Maximum)500 KB2 MB

Follow the steps below to generate the image URL:

Log in to the WiseMOKA dashboard using the login credentials provided by Infobip: https://moka.carrym.com

In the left menu, select Chingutalk Image (친구톡 이미지) and click Registration (등록).

In the pop-up window, fill out the required information and click Save.

Kakao Channel ID (카카오채널ID): Select your KakaoTalk channel.

Image type (이미지 유형): Select Normal (친구톡 이미지) or Wide (친구톡 와이드).

Image code (이미지 코드): Type a unique value that includes only letters, numbers, -, and _.

Image name (이미지명): Type any value for image name.

Image upload (이미지 업로드): Click Upload (업로드) and choose the image file.

Copy the generated image URL. Later, you will need to paste it into the AIQUA Dashboard > Kakao Campaign > Image URL field.

Go to Campaigns > Regular campaign or Campaigns > Trigger campaign.

Regular campaign: Click + Create campaign, then select Kakao.

Trigger campaign: Click + Create New Campaign. In the settings page, set Campaign Type to Instant Messaging, and select Kakao.

Next, set a schedule or a trigger, depending on whether you're creating a regular campaign or trigger campaign.

Regular campaign: Set a campaign schedule.

Trigger campaign: Create a trigger rule.

Select the audience you want to target.

Set up your creative.



Kakao Campaigns [2]

https://docs.aiqua.appier.com/docs/kakao-campaigns



Trigger campaign: Create a trigger rule.

Select the audience you want to target.

Set up your creative. 

Select Label content as advertising if this campaign contains promotional content. This is required by law in some countries.

Select Insert Image if you want to include an image in the campaign. 

Under Image URL, paste the URL generated via WiseMOKA. 

Under Image Type, choose the option you have set on WiseMOKA. 

If you enter a URL for Destination web URL, the users will be redirected to this page if they click on the image. Only web URLs are supported.

Under Notification Message, type the message. The character limit changes based on the image type selected. To track clicks on this campaign, you can add an AIQUA short URL.

If you want to include action buttons, select Include Action Buttons. You can add up to five action buttons.

Under Action Button Text, type the text to be shown on the button.

Under Web URL, enter the destination page that the users will be redirected to when they click the button. Only web URLs are supported.

📘NoteThe creative preview on the right is just an example. The layout and appearance of the actual notification may be different based on the settings you have configured.

Use the Test Your Creative button to send a test creative to users in the Test Segment. You will need to first add your Kakao phone number to the test segment.

Click Save.

Using dynamic content, an AIQUA short URL can be inserted into a campaign creative to track message clicks, allowing for click-through attribution for Kakao campaigns. 

AIQUA short URLs are generated by appending a unique URL parameter to the destination URL that you specified, e.g. a page on your website, so that each user's clicks can be uniquely identified.

The total length of the generated short URL may be up to 13 characters, and will have a base URL of aiq.is. An example AIQUA short URL looks like this: aiq.is/abc123.

Go to the Creative section. In the Notification Message field, click the dynamic variable icon ({...}), then click Short URL.



Kakao Campaigns [3]

https://docs.aiqua.appier.com/docs/kakao-campaigns



Go to the Creative section. In the Notification Message field, click the dynamic variable icon ({...}), then click Short URL.

In the message, click the {...} Short URL variable, then input the destination URL. Please note the following requirements and limitations: 

The destination URL must be an HTTP/HTTPS URL.

The destination URL can't be an AIQUA short URL.

📘Using a shortened URL as the destination URLAlthough setting the destination URL to a short URL generated by a third-party URL shortening service is supported, doing so may increase loading times for users due to the need for multiple redirects before reaching the final destination page.

Set the default message. Under Default message, enter the message you'd like to send if the URL can't be loaded in the message.

The AIQUA short URL will replace the {...} Short URL variable in your final message. The destination URL can be modified at any time by clicking the variable and editing the Destination URL field.Updated 3 months ago Table of Contents

Overview

Limitations

Integrating AIQUA with a KakaoTalk channel

1. Prepare your KakaoTalk Channel and account

2. Set up Infobip account and obtain a Sender Key

3. Contact Appier

4. Verify your integration

Generating image URLs for Kakao campaigns

Creating a Kakao campaign

Tracking clicks for Kakao campaigns

Adding an AIQUA short URL



SMS/MMS Campaign Quick Start [0]

https://docs.aiqua.appier.com/docs/sms-integration



You can integrate AIQUA with an SMS/MMS service provider and send text or multimedia messages to your users. You can use AIQUA's audience segmentation and dynamic content features to better target your users.

📘BetaMMS is a beta feature that's only available in Taiwan. Contact your customer success manager to enable it.

To integrate AIQUA with an SMS/MMS service provider, contact your customer success manager for assistance.

SMS/MMS campaigns can only be sent to users who have a phoneNo parameter in their profiles containing the user's phone number. See the Custom Events and Attributes Guidelines for more details. 

Two types of campaigns are supported for sending SMS/MMS campaigns: Regular campaigns and trigger campaigns.

Follow the steps below to create SMS/MMS campaigns.

Go to Campaigns, select Regular Campaigns or Trigger Campaigns, and click the Create New Campaign button.

Enter your campaign name and select SMS/MMS as the Campaign Type.

For regular campaigns, set the schedule. 

For trigger campaigns, set the trigger rule.

Under audience, select the audience segments you want to include and exclude. 

In the Creative section, select SMS or MMS.

Message: Enter the SMS message. You can include dynamic content in your message by clicking {...} to create more personalized message content.

Default message: If you've added dynamic content in your message, set the default message that will be displayed if the content can't be loaded.

👍Tracking clicksTo track clicks on this message, e.g. for campaign attribution, add an AIQUA short URL.

📘SMS limitations and credit usage

Messages that exceed 160 characters will be split into multiple SMS parts.

When there are multiple SMS parts, each part can include up to 153 characters. 

Up to 6 SMS parts are allowed. Each SMS part uses 1 SMS credit. It is recommended to keep the message under 4 SMS parts since some carriers only support up to 4 SMS parts.



SMS/MMS Campaign Quick Start [1]

https://docs.aiqua.appier.com/docs/sms-integration



If you include any Unicode characters in the entire message, the maximum limit is lowered to 70 characters per part when there is only 1 SMS part, or 67 characters per part when there are multiple SMS parts.

If you have dynamic content in the message, the number of characters in the dynamic content is not reflected in the counter displayed, because the character length will be different for each user.

An MMS includes a subject, media files, and a message.

Subject: Type the subject line of the MMS. 

When the subject and message are the same, only the message will be displayed on some devices (e.g. iPhone).

Avoid using these special characters in the subject: &, <, >, “, ‘. These characters might not be displayed correctly for some users. Alternatively, you can use the equivalent characters in full width.

Media: Add the media files you want to include in the MMS. 

Supported file types: GIF, JPG, JPEG, PNG. 

Depending on the device and carrier, some users might need to tap the media file to see the image.

Message: Type the main message of the MMS. You can include dynamic content in your message by clicking {...} to create more personalized message content.

Default message: If you've added dynamic content in your message, set the default message that will be displayed if the content can't be loaded. 

📘MMS limitations and credit usage

The size of the subject, media files, and message combined cannot exceed 256K.

MMS credit usage is based on the file size of the creative. Credits are charged if MMS is sent successfully. 

< 50K: uses 3 MMS credits

50K - 256K: uses 5 MMS credits

If you have dynamic content in the message, the number of characters in the dynamic content is not reflected in the counter displayed, because the character length will be different for each user. If the creative size exceeds the limitations due to dynamic content, MMS sending will fail for that user and credits will not be charged.

On average, up to 25000 MMS messages can be delivered per hour.



SMS/MMS Campaign Quick Start [2]

https://docs.aiqua.appier.com/docs/sms-integration



On average, up to 25000 MMS messages can be delivered per hour.

You can use the Test Your Creative button to send a test creative to the users in the Test Segment.

An AIQUA short URL can be inserted into a campaign creative to track message clicks, allowing for click-through attribution for SMS campaigns. 

AIQUA short URLs are generated by appending a unique URL parameter to the destination URL that you specified, e.g. a page on your website, so that each user's clicks can be uniquely identified.

The total length of the generated short URL may be up to 13 characters, and will have a base URL of aiq.is. An example AIQUA short URL looks like this: aiq.is/abc123.

Go to the Creative section. In the Message field, click the dynamic variable icon ({...}) and select Short URL.

Click the {...} Short URL variable, then input the destination URL. Please note the following requirements and limitations: 

The destination URL must be an HTTP/HTTPS URL.

The destination URL can't be an AIQUA short URL.

📘Using a shortened URL as the destination URLAlthough setting the destination URL to a short URL, i.e. generated via third-party URL shortening service, is supported, doing so may increase loading times for users due to the need for multiple redirects before reaching the final destination page.

Set the default message. Under Default message, enter the message you'd like to send if the URL can't be loaded in the message.

The AIQUA short URL will replace the {...} Short URL variable in your final message. The destination URL can be modified at any time by clicking the variable and editing the Destination URL field.Updated 3 months ago Usage InformationTable of Contents

Requirements

Creating SMS/MMS Campaigns

1. Create a campaign

2. Set the campaign name and campaign type

3. Set the schedule or trigger rule

4. Select your audience

5. Add the creative

6. Test your creative

Tracking clicks for SMS campaigns

Adding an AIQUA short URL



Account Overview

https://docs.aiqua.appier.com/docs/account-overview



Go to the bottom left corner of the AIQUA Dashboard and click on your account name to access the following pages containing account-wide settings and information:

Account Settings: Account details (e.g. app ID, API key) and account-wide settings.

Usage Information: Delivery statistics for each paid channel in AIQUA (email and SMS).

Updated over 1 year ago



Account Settings [0]

https://docs.aiqua.appier.com/docs/user-settings



Account Settings page is where you can find your account information such as your API Token and APP ID. On this page, you can also configure settings at an account level such as setting frequency caps and defining conversion events.

On AIQUA dashboard, click on your account name in the lower-left corner of the screen and select Account Settings.

You can set a maximum number of notifications that can be sent per second. Usually, AIQUA tries to send notifications as fast as possible, but in some cases, you may want to set a limit to slow down the send rate. 

For example, if you send a notification that contains a link to your website to all your users at once, too many users may access your website at the same time, overloading your website. This issue can be avoided by setting a notification send rate to space out the notifications.

The values that can be entered fall in the range of 100 to 100000 notifications per second. This setting only applies to regular campaigns and trigger campaigns. Notification send rate is not applied to legacy Journey Maps campaigns.

Blackout Window allows you to set a time period when AIQUA will not send campaigns to your users. For example, if you set a 10:00 PM to 8:00 AM blackout window for Email campaigns, no email campaigns will be sent out during this period every day.

This blackout window is based on the actual sent time instead of the campaign's scheduled run time. For example, let's say you scheduled the campaign to run at 3:00 PM and the blackout window starts at 3:01 PM. If the campaign is targeting a large number of users and delivery cannot be completed within 1 minute, notifications that did not finish sending at 3:01 PM will be blocked and cleared by the blackout window. 

Note that there are some scenarios where users may receive notifications during blackout window:

While AIQUA does not send notifications during a blackout window, users may still receive a notification during a blackout window due to delayed notifications.



Account Settings [1]

https://docs.aiqua.appier.com/docs/user-settings



The blackout window is ignored for users in the Test Segment when you click the Test Your Creative button. 

To set up blackout window:

Select Enable Blackout Window.

Select the channels you want to enable blackout window for. 

Clear push messages queued in push server (FCM or APNs) during blackout window: If the user's device is turned off or not connected to network at the time of the campaign delivery, the message will queue up in the server of the service provider (e.g. APNs) and be delivered after the user's device is online again, even if it's during blackout window.

For push campaigns, you can select this option to avoid the situation described. If selected, queued push messages will be removed from the server once blackout window begins.

Set the Start Time and End Time. 

This is based on the time zone setting of your account.

The blackout window does not include the end time. In the image below, campaigns scheduled exactly at 08:00 will be sent.

Click Save.

You can select the conversion events and the attribution models for online events tracked by Appier SDK.

Conversion Events: You can indicate the events that represent conversion for your business, such as product_purchased. 

Attribution Models: Attribution models determine whether an event is attributed to a campaign. The attribution models selected here affect the Conv. Count and Conv. Value shown in the campaign list for that campaign type. 

For details on conversion events and attribution models, see Understanding Event Attribution. 

📘Note:A conversion event cannot be a default event that is triggered by an AIQUA campaign. Here are some examples of campaign-related default events: notification_clicked, qg_inapp_received, and qg_inweb_closed.

📘Note

This feature needs to be activated by Appier Support. 

To see the channels that support offline conversion attribution, see Attribution models by channels.

Offline conversion events need to be uploaded through the Offline Event API V2.



Account Settings [2]

https://docs.aiqua.appier.com/docs/user-settings



Offline conversion events need to be uploaded through the Offline Event API V2.

AIQUA calculates the offline conversion count once a day using offline events with a timestamp within 90 days.

If you have enabled offline event attribution, you can select the attribution model and attribution window for offline events.

Conversion Events: You can select up to five offline conversion events. Note that changes to offline conversion events aren't applied retroactively to previously uploaded event data.

Offline Attribution Models: For a conversion event to be attributed to a campaign, the user needs to complete the event within a certain time period after viewing or clicking the campaign.

Conversion Attribution: The different models determine whether the attribution is based on campaign clicks or views, and whether the attribution is only counted for the last campaign. For more details, see Understanding Attribution Models.

Attribution Window: You can set an attribution window between 1 to 30 days. For an offline conversion event to be attributed to a campaign, the timestamp of the uploaded event must be within this window after the user clicks or views the campaign. Changes to the attribution window aren’t applied retroactively to previously uploaded data. For more details, see Setting Attribution Window.

AIQUA provides two types of frequency caps to help you limit the number of notifications sent to users to avoid bombarding users with too many campaigns. 

Daily Limit 

Minimum Interval

In regular campaigns, you can choose to override both frequency caps for important messages when creating the campaign. See Overriding the Frequency Cap.

📘Capping for push notificationsFor push notifications, the frequency cap is counted separately for Android push, iOS push, and web push, and it is based on the user's device as defined below:



Account Settings [3]

https://docs.aiqua.appier.com/docs/user-settings



Web push: Each web browser is counted as one device. For example, if a person is subscribed to your web push from the Chrome browser on their laptop, the Firefox browser on their laptop, and the Chrome browser from their Android mobile device, this is counted as three separate devices. If the browser cookie is cleared, this web browser is treated as a new device.

Android push: An Android device that has your Android app installed.

iOS push: An iOS device that has your iOS app installed.

🚧Exceptions

The frequency cap is ignored for users in the Test Segment when you click the Test Your Creative button. Notifications sent via the Test Your Creative button do not count toward the frequency cap. 

Notifications that are blocked (e.g. due to blackout window) may sometimes still count toward the frequency cap. As a result, users may receive fewer notifications than the settings indicated in the frequency cap.

This setting allows you to set the maximum number of push notifications that can be sent to a device per day, regardless of the campaign type. 

Push notifications sent from regular campaigns, trigger campaigns, journey maps, and API calls are all limited by this frequency cap.

The notification count of each device is reset to 0 at midnight (00:00) based on the timezone set in your Account Settings page.

To set the daily limit:

Click the Enable notification limits (per day per device) checkbox.

Enter the maximum number of push notifications that can be sent to each device each day. 

Click Update Frequency Cap to apply.

If you update the daily limit, campaigns that are already running will still use the previous setting. The new limit will be applied, starting from the next campaign run.

For regular campaigns and trigger campaigns, you can set a minimum time interval in seconds between two notifications for each channel. If you don't want to set a minimum interval for a channel, set the value to 0.



Account Settings [4]

https://docs.aiqua.appier.com/docs/user-settings



In the example below, the frequency cap is set to 100 seconds for emails in regular campaigns. This means that after a user receives an email through regular campaigns, they won't receive another one from regular campaigns in the next 100 seconds.

For trigger campaigns, the interval is counted separately for each type of triggering rule. This means that a user can receive up to three notifications from that channel during the interval, one from each triggering rule.

by User Action

by Date/Time 

by Feed Changes

Legacy Journey Maps and regular campaigns share the same interval settings, but the interval is counted separately. 

In summary, the minimum interval is counted separately for each bullet point below.

Campaign typeInterval is counted separately for each bulletRegular campaign• Web Push (regular campaign)

• Web Push (legacy journey map)

• Android Push (regular campaign)

• Android Push (legacy journey map)

• iOS Push (regular campaign)

• iOS Push (legacy journey map)

• SMS (regular campaign)

• MMS (regular campaign)

• Email (regular campaign)

• Email (legacy journey map)

• LINE (regular campaign)

• LINE (legacy journey map)

• Kakao (regular campaign)Trigger campaign• Web Push, Trigger by User Action (trigger campaign)

• Web Push, Trigger by Date/Time (trigger campaign)

• Web Push, Trigger by Feed Changes (trigger campaign)

• Android Push, Trigger by User Action (trigger campaign)

• Android Push, Trigger by Date/Time (trigger campaign)

• Android Push, Trigger by Feed Changes (trigger campaign)

• iOS Push, Trigger by User Action (trigger campaign)

• iOS Push, Trigger by Date/Time (trigger campaign)

• iOS Push, Trigger by Feed Changes (trigger campaign)

• SMS, Trigger by User Action (trigger campaign)

• SMS, Trigger by Date/Time (trigger campaign)

• SMS, Trigger by Feed Changes (trigger campaign)

• MMS, Trigger by User Action (trigger campaign)

• MMS, Trigger by Date/Time (trigger campaign)

• MMS, Trigger by Feed Changes (trigger campaign)

• Email, Trigger by User Action (trigger campaign)



Account Settings [5]

https://docs.aiqua.appier.com/docs/user-settings



• MMS, Trigger by Feed Changes (trigger campaign)

• Email, Trigger by User Action (trigger campaign)

• Email, Trigger by Date/Time (trigger campaign)

• Email, Trigger by Feed Changes (trigger campaign)

• LINE, Trigger by User Action (trigger campaign)

• LINE, Trigger by Date/Time (trigger campaign)

• LINE, Trigger by Feed Changes (trigger campaign)

• KaKao, Trigger by User Action (trigger campaign)

• KaKao, Trigger by Date/Time (trigger campaign)

• KaKao, Trigger by Feed Changes (trigger campaign)

If you update the minimum interval, users who were previously capped will take on the new interval setting after their original interval expires.

For example, the original interval for SMS is 600 seconds, and a user has received an SMS campaign based on this interval setting. If you update the interval to 60, this user will not receive any SMS until the original 600-second interval is up.

If you want to override the frequency cap for an important notification, you can do so in regular campaigns by selecting Ignore frequency cap in the Create Regular Campaign page. 

When this option is selected, both the daily limit and the minimum interval set for regular campaigns will be ignored. 

The notifications sent from this campaign still count toward both types of frequency caps. For example, if you are sending push from a campaign with the Ignore frequency cap option selected, a device that has already received two notifications will now be counted as having received three notifications. 

Use Appier's default unsubscribe URL: By default, email campaigns use Appier's default unsubscribe URL. Select this option if you don't need to maintain your own list of unsubscribed users.

Use a custom URL: Specify a custom URL, which can include dynamic content variables (user attributes or events). A POST request is made to your custom URL whenever a user unsubscribes by clicking the one-click unsubscribe link at the top of the email (list-unsubscribe header). Note that using a custom URL requires additional implementation steps.



Account Settings [6]

https://docs.aiqua.appier.com/docs/user-settings



Unsubscription link at the top of the email (list-unsubscribe header)

When a user clicks unsubscribes from email campaigns:

That user's email_unsubscribe attribute set to true, and their email address is excluded from the Email Subscribers count shown in the segment list.

That user's email address is added to AIQUA's unsubscribed user email list. Email campaigns will no longer be sent to users on this list.

When a user unsubscribes from email campaigns by clicking the one-click unsubscribe button at the top of the email, a POST request is made to your custom unsubscribe URL. Custom unsubscribe URLs can contain dynamic content such as user identifiers.

If you choose to use a custom URL to unsubscribe from email campaigns, you'll need to complete additional steps to ensure the unsubscription is processed correctly:

Implement a handler in your system to receive the unsubscribe POST request and process the user's unsubscription. The POST request will be sent to the custom URL configured in your account settings. The request looks like this:

"POST /unsubscribe/custom/url HTTP/1.1

Host: example.com

Content-Type: application/x-www-form-urlencoded

Content-Length: 26

List-Unsubscribe=One-Click"

Update AIQUA's unsubscribed user email list using the email unsubscribe API. Until this step is completed, AIQUA email campaigns will continue to be sent to the user.

Insert dynamic content (user attributes or events) into your custom URL by clicking the dynamic content button ({...}), then selecting the attribute or event you'd like to use.

This section allows you to update your password information. The password needs to contain 8 or more characters, with at least 1 number, 1 uppercase letter, and 1 lowercase letter.

For better security:

Use a strong password. Do not use a password that can be easily guessed, such as your birthday, phone number, name, login ID, employee ID...etc.

Do not use the same password that you are already using for other services.



Account Settings [7]

https://docs.aiqua.appier.com/docs/user-settings



Do not use the same password that you are already using for other services.

Do not use an old password that you have used for other services in the past.

You can grant access to the AIQUA dashboard to your team. There are four types of roles for accessing AIQUA dashboard. 

Administrator: Administrators have access to all features and user data including PII.

Developer: Developers can create and execute campaigns. They can access Recent Users and Recent Activity pages to verify integration.

Operator: Operators can create and execute campaigns, but cannot access user data or any reports that include user data.

Viewer: Viewers can only edit campaigns and view the campaign performance pages.

To see detailed access rights of each role, refer to the Access Control List below.

📘Note:

Administrator accounts have access to end users' Personally Identifiable Information (PII), such as emails collected in lead generation forms.

If you want to mask Personally Identifiable Information (PII) in Recent Users and Recent Activity pages for developer accounts, contact Appier Support and indicate the fields you want to mask, such as email, phoneNo, line_uid, IDFA, IDFV, advertiserId, and ip.

To grant access to the AIQUA dashboard:

Under Invite User, click Add User.

Type their email addresses, select a role, and click Invite. 

You can add multiple email addresses at a time with the same role.

If you have multiple AIQUA accounts, you have to send invitations from each AIQUA account to provide access to each.

To edit the role or delete an existing user, click the menu button, and select Edit Role or Remove.

This action only applies to the current AIQUA account. If you have multiple AIQUA accounts, you'll need to repeat the step for each AIQUA account.

👍Tip:A dashboard user is automatically logged out after 24 hours of inactivity. This default 24-hour timeout period can be shortened if needed.

See the following tables for the access rights of each type of role.

O: Have access

X: No access

(M): PII masked if masking is enabled



Account Settings [8]

https://docs.aiqua.appier.com/docs/user-settings



O: Have access

X: No access

(M): PII masked if masking is enabled

📘Note:To enable PII data masking, contact Appier Support.

FunctionsAdministratorDeveloperOperatorViewerSample UsersOO (M)XXExport Segment ReportsOXXXOther FunctionsOOOO

[A] Sample Users, [B] Export Segment Reports

FunctionsAdministratorDeveloperOperatorViewerAPI Token & APP SecretOXXXUser Role Management

(Invite User)OXXXOther FunctionsOOOO

FunctionsAdministratorDeveloperOperatorViewerExecute CampaignOOOXSchedule CampaignOOOXExport Campaign User ReportOXXXDownload Click Report (Regular Campaigns)OXXXDownload Form Data (Lead Generation)OXXXExport Campaign Performance ReportOOOOOther FunctionsOOOO

[A] Execute campaign, [B] Schedule Campaign, [C] Export Campaign User Report

[D] Download Click Report, [E] Export Campaign Performance Report

[A] Execute Campaign, [C] Export Campaign User Report, [F] Download Form Data

FunctionsAdministratorDeveloperOperatorViewerAnalytics PagesOOOO

Updated about 2 months ago Table of Contents

General Settings

Notification Send Rate

Blackout Window

Conversion and Attribution

Offline Conversion and Attribution

Notification Frequency Cap

Daily Limit

Minimum interval

Overriding the frequency cap

Email list-unsubscribe header

Use Appier's default unsubscribe URL

Use a custom URL

Update Password

Account User Role Management

Access Control List (ACL)



Usage Information [0]

https://docs.aiqua.appier.com/docs/account-usage-information



📘NoteThis feature is only available if you're subscribed to AIQUA's email or SMS services. Contact your customer success manager for more information.

Your account's usage information page details the total volume of messages your campaigns deliver, which can be used to estimate the potential delivery expenses incurred. For details on which usage metrics incur costs, see the usage definitions. Total and daily usage within a specified date range are visible for each supported channel.

Currently, usage information is supported for the following channels:

Email

SMS

To view your account's usage information, click on your account name in the lower left corner of the AIQUA Dashboard, then click Usage Information.

Select the channel and date range you want to view usage data for (date range limitations apply). You can also export the usage report to a CSV file.

Refer to the following definitions of usage to understand which metric is used to calculate costs for each channel. For detailed definitions of each metric, see Usage metrics.

Email usage is defined by the Email Sent metric.

SMS usage is defined by the SMS Credits Used metric.

Usage metricDefinitionEmail Sent The total number of email sent by all campaigns associated with this account. Determines email channel costs.Sent (Credits Charged)The total number of SMS delivered by all campaigns associated with this account.SMS Credits UsedThe total number of SMS credits used by all campaigns associated with this account. Determines SMS channel costs.

Note that SMS Credits Used may be greater than Sent (Credits Charged). Actual SMS credit usage is based on message length, language, and character encoding scheme.

Export a CSV file containing a report with your account's usage data by selecting the Email or SMS tab, then clicking the Export Report button.

In the Export Usage Report modal that appears, complete the following:

Specify a date range. Usage data is unavailable for dates before April 1, 2022.



Usage Information [1]

https://docs.aiqua.appier.com/docs/account-usage-information



Specify a date range. Usage data is unavailable for dates before April 1, 2022.

Enter up to 10 emails that you want the report download link to be sent to.

Click Export. When the report is ready, an email containing the download link for the report will be sent to the email(s) you specified. It takes one to two days for the download link to be sent.

The email containing your usage report's download link also includes your business name, the channel type, and date range of the data.

Usage data is only available starting from April 1, 2022.

Only data from the past 12 months can be viewed on the AIQUA Dashboard. This means that the start date cannot be more than 12 months before the current date. This limitation doesn't apply to usage report exports.

Usage data for each date is based on the time zone configured in your account settings.

Updated over 1 year ago Table of Contents

Overview

Usage definitions

Usage definition by channel

Usage metrics

Exporting the usage report

Date range notes and limitations



February 2025

https://docs.aiqua.appier.com/docs/aiqua-release-notes-february-2025



📘NoteContact your customer success manager to learn more about AI Copilot.

We've upgraded AI Copilot with a more intuitive workflow, making it easier to create campaigns while ensuring AI-assisted content generation adapts to your brand’s style and tone:

Generate AI-assisted content that adapts to your brand’s voice. 

Refine and customize AI-generated content with prompt suggestions.

Automatically generates content in the selected input language.

We've enhanced template management in Creative Studio, allowing you to find, organize, and customize templates more efficiently:

Filtering default template by Goal, Format, or Device.

Search for templates by name or ID.

Sort templates by Last edited or Template name.

Improve browsing performance with enhanced pagination.

We've introduced three user-based models to recommend up to 20 of the most recent products based on user behaviors, improving personalized shopping experiences:

Recently viewed

Recently purchased

Recently added to cart

For more details, see Recommendation model reference.

To prevent users from receiving duplicate messages in a journey campaign, journey maps now ensure each LINE UID receives only one message per campaign node per run.

📘NoteContact your customer success manager to learn more about webhook node.

We've introduced batching support for the webhook node, allowing you to enable batch requests, set a batch size, and define a minimum interval window for more efficient data processing. For more details, see webhook node. 

Updated 25 days ago Table of Contents

New features and enhancements

Campaign AI Copilot: Enhanced AI-driven campaign creation

Creative Studio: Enhanced template browsing and management

Recommendation: New user-based models

Journey maps: Prevent duplicate messages

Journey maps: Webhook processing with batching support



January 2025

https://docs.aiqua.appier.com/docs/aiqua-release-notes-january-2025



We’ve started rolling out an enhanced navigation bar, which will soon be available to all AIQUA users. This enhancement introduces a new organization dropdown, making it easier to switch between organizations, projects, and products. To learn more, see Enterprise resource center.

We’ve introduced new enhancements that make it easier to organize and manage in-web and in-app campaigns. These updates help you browse, filter, and prioritize campaigns more efficiently.

New tagging system: Create and manage both custom and system-generated tags to simplify campaign browsing and data review. These tags help simplify decision-making when adjusting campaign priorities.

Campaign list with more details and filters: Get a clearer view of campaign targeting with audiences, trigger rules, and performance metrics. Use filters for status, device type, tags, and trigger rules to find campaigns faster.

You can now select from all segments when creating merged push campaigns, instead of only being able to select segments active in the last 180 days.Updated about 2 months ago Table of Contents

New features and enhancements

Enhanced navigation bar for Enterprise products

In-web and In-app campaign: Campaign list enhancements

Merged push campaign: Segment selection enhancement



December 2024

https://docs.aiqua.appier.com/docs/aiqua-release-notes-december-2024



We've improved error detection for dynamic content on the Drag & Drop Editor and HTML Editor. Clear error messages help you identify and fix issues during email campaign creation.

We've introduced 10 new prebuilt templates to journey maps to help you accelerate campaign creation on common marketing scenarios:

Churn user engagement

Update user attribute

Sync LINE profiles with web profiles (Webchat)

Browse abandonment (short cycle)

Audience sync (retargeting)

Audience sync (first purchase incentive)

Audience sync (retargeting suppression)

Member birthday reminder

Drive offline user to online purchase

Product launch (long cycle)

We've improved Creative Studio templates loading performance by 95% for smoother user experience.Updated 3 months ago Table of Contents

New features and enhancements

Email Editor: Improved error detection for dynamic content

Journey maps: Additional templates

Creative Studio: Faster performance



November 2024

https://docs.aiqua.appier.com/docs/aiqua-release-notes-november-2024



We’ve introduced new enhancements on the regular campaign list to improve usability and optimize campaign management. The key improvements include:

New tag display: Tags are visible under the campaign name for easier identification.

Campaign statuses: Campaign statuses are directly displayed in the campaign list, enabling you to quickly filter and locate campaigns. To learn more, see Searching and filtering campaigns.

Campaign list details: Include segments, Exclude segments, and Next scheduled time are now displayed in the campaign list. To learn more, see Campaign list metrics.

Journey maps have been updated to improve offline data management, enabling you to distinguish between online data collected via SDK and offline data uploaded through the API. The key enhancements include:

Offline tags: Automatically identify offline events with an Offline tag, simplifying the process of tracking and setting conversion goals in your customer journeys.

Separate offline metrics: Gain comprehensive visibility into offline performance by tracking conversion counts and revenue independently. View online and offline conversion separately in the Journey map list and detailed performance in the Journey analytics tab.

Updated 4 months ago Table of Contents

New features and enhancements

Regular campaign: Campaign list enhancements

Journey maps: Offline conversion tagging and metrics



October 2024

https://docs.aiqua.appier.com/docs/aiqua-release-notes-october-2024



We’ve expanded our support for Kakao Moment with three additional creative templates enhancing the flexibility and design options for your campaigns to better reach your audience: 

Wide list

Carousel commerce

Carousel feed

You can now view Recommendation performance metrics for up to 180 days, enabling better analysis of long-term trends and campaign effectiveness.

We've added two new custom English fonts, available in the email drag & drop editor:

Inter

Poppins

User profiles deleted using the Delete Users API are now removed from segmentation immediately after the API call.Updated 5 months ago Table of Contents

New features and enhancements

Kakao Moment campaigns: New creative templates added

Recommendation: Performance date range extended

New custom fonts for the email drag & drop editor

Fixes and changes

Improved Delete Users API performance



September 2024

https://docs.aiqua.appier.com/docs/aiqua-release-notes-september-2024



You can now choose whether to display a background overlay in your in-app campaigns designed with Creative Studio. Disabling the background overlay allows users to interact with the app in areas not covered by the creative, providing a more flexible user experience.

We've introduced Kakao Moment campaigns in AIQUA, allowing you to leverage diverse and flexible creative templates, personalized dynamic content, and comprehensive data tracking for advanced targeting and detailed performance analytics.

For a complete overview and more details on setting up Kakao Moment campaigns, see Kakao Moment campaigns.

📘NoteContact your customer success manager to learn more about Onsite Experience.

We've added a new template for Onsite Experience campaigns that allows you to display a single image banner that redirects users to a specified URL when clicked. This offers a streamlined design for driving engagement through visual content.

Updated 4 months ago Table of Contents

New features and updates

In-app campaigns (Creative Studio): Background overlay settings

Kakao Moment campaign integration

Onsite Experience: New single image template



August 2024

https://docs.aiqua.appier.com/docs/aiqua-release-notes-august-2024



📘NoteContact your customer success manager to learn more about Onsite Experience.

We’ve introduced new enhancements that allow you to search, filter, sort, and archive Onsite Experience campaigns. These updates are designed to simplify the process of locating and managing your campaigns, streamlining your workflow.

Increase your email open rates with our new preheader support feature. Email preheaders appear next to the subject line and provide a brief preview of your email content, grabbing your audience’s attention right from the inbox. Please note that preheader support is only available when using Drag & Drop Editor. In addition, preheaders:

Can contain dynamic content and emojis, allowing you to customize your pre-headers for maximum impact. 

Are compatible with the “Test Your Creative” feature, making it easier than ever to optimize your email campaigns.

We've expanded the user search capabilities during journey testing, allowing you to search for users by LINE UID, in addition to the existing searchable attributes (email, phone number, and user ID).Updated 5 months ago Table of Contents

New features and updates

Onsite Experience: Enhanced campaign management

Email Drag & Drop Editor: Preheader support

Journey maps: Searching for users by LINE UID during journey testing



July 2024 [0]

https://docs.aiqua.appier.com/docs/aiqua-release-notes-july-2024



AIQUA recommendations now support OMO mode, enriching model training data with both online and offline events to provide even more precise product recommendations!

Previously, standard recommendation models were based only on online events, i.e. events logged via Appier SDK. Now, you can upload offline events, e.g. a user's purchase history at a physical location and activate OMO mode in your account settings to use both online and offline events for recommendation model training. Contact your customer success manager to enable OMO mode in your account. 

📘Note: Models supporting OMO mode

All standard models support OMO mode, except for Recommended for You (Advanced). 

Professional Service custom models can support all modes (online, offline, and OMO).

The Campaign performance data source now contains the Offline Conversions and Offline Conversion Value metrics.

In addition to a brand-new look and feel, we've completely overhauled the creation flow for regular campaigns, allowing you to create a single push campaign that supports multiple channels, including Android, iOS, and Web. The new, streamlined process allows you to configure creative types and campaign messages for each channel from a single screen.

Performance data for regular push campaigns is available for aggregated metrics (all channels) and channel-specific metrics on the performance page on the AIQUA dashboard as well as downloadable CSV reports.

👍TipSee Push (Web and App) to learn how to create regular push campaigns using the new user interface.

To improve Appier's cross-product synergy and optimize the Web SDK, we've revamped the project structure of the source code, allowing us to reduce the SDK file size from 501.5 KB to 399.8 KB. No behavior changes were introduced, so you don't need to make any changes to your integration.

We've added the following custom fonts for multiple languages, now available in the email drag & drop editor:

微軟正黑 (Mandarin)

Georgia (English)

Verdana (English)

Tahoma (Thai)

Arial (Vietnamese)



July 2024 [1]

https://docs.aiqua.appier.com/docs/aiqua-release-notes-july-2024



微軟正黑 (Mandarin)

Georgia (English)

Verdana (English)

Tahoma (Thai)

Arial (Vietnamese)

Noto Sans Japanese (Japanese)

Noto Serif Japanese (Japanese)

Updated 5 months ago Table of Contents

New features and updates

Recommendation: Online-merge-offline (OMO) support

Analytics Studio: Offline conversion support in the campaign performance data source

Regular campaigns: Merged push campaigns

Web SDK optimizations

New custom fonts for the email drag & drop editor



June 2024 [0]

https://docs.aiqua.appier.com/docs/aiqua-release-notes-june-2024



We've enhanced the campaign list loading experience by introducing segmented loading and a skeleton screen for campaign metrics. The campaign information and actions will be loaded and displayed as soon as they're ready, without needing to wait for metrics to finish loading.

Previously, the recommendation model used by a scenario couldn't be edited after the scenario was enabled. Now, you can edit the recommendation model settings at any time, giving you the flexibility to seamlessly adjust the scenario to suit your marketing goals.

During the training period for the new settings, the scenario will continue using the previous settings to ensure uninterrupted service. While the update is in progress, the scenario status will be set to Updating.

📘NoteFor scenarios using the Autopilot or Professional Service - Custom Model recommendation model, the model setting can't be edited.

In addition, we've improved the look and feel of the scenario list page and made some changes to make it easier to find the information you're looking for.

Filtering and sorting: You can now filter and sort scenarios by status, placement, and model type, making it easier to find exactly what you need.

Improved date picker: We've updated the date picker for a smoother experience, and the default date range is now set to This Month for your convenience.

The winning variant feature allows you to optimize push notifications by testing different variants of messages and automatically selecting the best performer. You can choose the traffic allocation, winning metric, and test duration, and the winning variant will be automatically selected.

This feature ensures the most effective push notification reaches your audience, enhancing campaign success and user engagement.

👍To learn more about push campaign experiments with winning variants, see Experiments: Push.

View-through attribution (VTA) attributes conversions to campaign impressions even when a user:

Doesn't click on the notification.

Views other notifications during the attribution window.



June 2024 [1]

https://docs.aiqua.appier.com/docs/aiqua-release-notes-june-2024



Doesn't click on the notification.

Views other notifications during the attribution window. 

When a user views the notification and completes the goal event within the attribution window, the goal event will be counted as a conversion.

Please note that goal events in the view-through attribution window will be attributed across all campaigns. For example:

A user views "Campaign A".

The same user views "Campaign B".

The user completes a goal event (converts) within the attribution window.

As a result, the conversion will be attributed to both "Campaign A" and "Campaign B".

If any segment daily refresh data is missing in the selected date range, linear interpolation will be used to plot a line between the known data points to ensure a clear trend chart and smooth lines. If you hover over the date with missing data, no dialog is displayed.

New API rate limits have been implemented for some AIQUA API endpoints. For details, please refer to the API documentation:

Create an Offline User Upload Job

Upload Offline Event Data (v2)

Updated 4 months ago Table of Contents

New features and updates

Campaign list loading enhancements

Recommendation: Editable scenarios and scenario list redesign

Regular campaigns: Push campaign experiments with winning variants

Regular campaigns: Support for view-through attribution

Segment trend: Handling missing data

Fixes and changes

New API rate limits



May 2024

https://docs.aiqua.appier.com/docs/aiqua-release-notes-may-2024



All email campaigns now include a one-click unsubscribe button (via email list-unsubscribe header) at the top of the email. By default, AIQUA's default unsubscribe URL is used for the unsubscribe button, but if you'd like to process email unsubscriptions in your system, go to your account settings to configure a custom email unsubscribe URL.

Unsubscribe link at the top of the email (list-unsubscribe header)

Unsubscribe URL configuration in account settings

We've added three new custom Korean fonts, available in the email drag & drop editor:

Gowun Dodum (고운돋움)

Jua (배달의민족 주아체)

Do Huron (배달의민족 도현체)

Previously, the product_purchased event was the only supported offline conversion event. Now, you can select up to five offline conversion events in the account settings page, allowing for more precise and comprehensive performance metrics for regular and trigger campaigns.

The Send Campaign Notifications API now supports sending SMS campaigns. You can send SMS campaigns via API by specifying the campaign recipients' phone numbers or selecting an existing segment.

The Create an Offline User Upload Job (Bulk Upload Offline Users API) now returns a 400 Bad Request with the following error message if the uploaded file is not UTF-8 encoded: “Data file without UTF-8 encoded is invalid”.

Faulty logic for calculating iOS uninstall counts has been fixed. As a result, you may observe an increase in iOS app uninstall counts. For details on how the number of app uninstalls is calculated, see Uninstall Analytics.Updated 9 months ago Table of Contents

New features and updates

Email campaigns now support one-click unsubscribe

New custom Korean fonts for the email drag & drop editor

Set up to five offline conversion events

Send SMS campaigns via API

Fixes and changes

Bulk Upload Offline Users API: UTF-8 encoding error response

Fixes to iOS uninstall analytics



Appier Enterprise Solution Status [0]

https://status.appier.com/



All Systems Operational



AIQUA Services



Operational



AIQUA Web UI Service



?

Operational



AIQUA API Service



Operational



AIQUA Campaign Service



?

Operational



AIQUA Recommendation Service



Operational



AIXON Services



Operational



AIXON Web UI Service



Operational



AIXON API Service



Operational



BotBonnie Services



Operational



BotBonnie Web UI Service



?

Operational



BotBonnie API Service



Operational



AIRIS Service



Operational



AIRIS Web UI Service



?

Operational



AIRIS API Service



Operational



AIRIS Data Collection Service



Operational



AiDeal Services



Operational



AiDeal Web UI Service



Operational



AiDeal API Response Time



Operational



AiDeal Campaign Service



Operational



Retail Media Network Services



Operational



Retail Media Network Web UI Service



Operational



Retail Media Network API Service



Operational



Auth0 User Authentication



Operational



Auth0 Machine to Machine Authentication



Operational



Operational



Degraded Performance



Partial Outage



Major Outage



Maintenance



Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:000100200300400

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:00050010001500

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:00200300400500

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:0005001000

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:002505007501000

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:00200300400500

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:00050010001500

Created with Highcharts 10.3.112:0015:0018:0021:0011. Apr03:0006:0009:000200400600

Past Incidents

Apr 11, 2025

No incidents reported today.

Apr 10, 2025

No incidents reported.

Apr 9, 2025

No incidents reported.

Apr 8, 2025

No incidents reported.

Apr 7, 2025

No incidents reported.

Apr 6, 2025

No incidents reported.

Apr 5, 2025



Appier Enterprise Solution Status [1]

https://status.appier.com/



Apr 8, 2025

No incidents reported.

Apr 7, 2025

No incidents reported.

Apr 6, 2025

No incidents reported.

Apr 5, 2025

No incidents reported.

Apr 4, 2025

No incidents reported.

Apr 3, 2025

No incidents reported.

Apr 2, 2025

No incidents reported.

Apr 1, 2025

No incidents reported.

Mar 31, 2025

No incidents reported.

Mar 30, 2025

No incidents reported.

Mar 29, 2025

No incidents reported.

Mar 28, 2025

No incidents reported.



Creating a Segment

https://docs.aiqua.appier.com/docs/audiences



Audience segmentation is the process of dividing users who share the same user events and/or attributes into subgroups based on the criteria you've defined. Creating audience segments allows you to send relevant messages to each group of users, instead of indiscriminately sending the same campaigns to all users.

👍TipBefore you create audience segments, see User Data Collection to read about how user data is tracked and used in AIQUA.

There are three ways to create an audience segment: Conditions, Mapping with User List, and Offline events.

This method allows you to segment the audience based on the user attributes or events tracked by Appier SDK. For example, you can create a segment of users who have purchased within a week.

After you create a segment by condition, users who meet the segmentation condition will continue to be added to the segment. Similarly, users may be removed from the segment once they no longer meet the criteria. Note that in in-web campaigns, users are added to the segment 24 hours after they meet the segment conditions. The same applies when users are removed from the segment.

This method allows you to segment the audience by uploading a list of user attributes, such as a list of emails. AIQUA will look for existing users in the database with matching user attributes and include those users in the segment. In other words, only users who already exist in AIQUA's database will be included in the segment.

This method allows you to segment audience based on the offline events you have uploaded. You will need to first upload the offline events via API, and then you can use these offline events as conditions to create a segment.Updated 3 months ago Table of Contents

Creating Audience Segments

Conditions

Mapping with User List

Offline events



Conditions [0]

https://docs.aiqua.appier.com/docs/defining-segments



You can divide your users into smaller groups using user events or user attributes as segmentation conditions. 

👍Tip:Appier SDK automatically collects these Default Events and Attributes.

Make sure any Custom Events and Attributes you want to use as segmentation condition are already set up during SDK integration.

Go to Audience > Segment list, and click the + Create segment > Conditions in the top-right corner.

Type a name for the segment.

Select Set the Condition.

There are two sections. 

Include Users: This section allows you to include users who have the specified user attributes or have performed the specified user events. 

And Exclude: This section allows you to define the criteria to remove certain users already included in the "Include Users" section. 

If no Include users condition is set, the segment will include all audiences. If you didn't set an Include condition, but set an Exclude condition, the segment will include all audiences minus the users who meet the Exclude condition.

You can add one or multiple conditions. If you select ​Any, users who match any of the conditions will be considered a match. If you select All, users need to match all conditions to be considered a match.

To add conditions, click the Add New Condition button. 

When creating a condition based on a user attribute, you must select an operator, and type the value. See the Operators section below.

When creating a condition based on a user event, you can select an event without choosing an event parameter.

Optionally, if you want to further narrow down on the condition, click Add Filter to specify the event parameter, operator, and value. See the Operators section below.

You can specify a time range for user events using Events in the last X days. 

This setting applies to all the user events set as condition EXCEPT for events where you have set Lifetime Count as the event parameter. 

This setting does NOT apply to user attributes that are set as condition.



Conditions [1]

https://docs.aiqua.appier.com/docs/defining-segments



This setting does NOT apply to user attributes that are set as condition.

If the number entered exceeds the data retention period (180 days by default), the data retention period will be applied.

Do not set the number to 0. 

For some of the default events collected by Appier SDK, you might see the following event parameters.

Event ParametersDescriptionnotificationIdThis is the ID of the notification you have sent. This parameter is available for some default events that are related to campaigns, such as notification_clicked.

See How do I segment by notification ID?Campaign NameThis is the name of the campaign. Campaigns from the last 7 days will be shown in the drop-down list.Lifetime CountThis feature needs to be activated by Appier Support.

This is the number of times the event is completed in the user's lifetime based on events collected by the Appier SDK. The Lifetime Count is not subjected to the time range specified in the Events in the last X days option.referrerThis is the url of the webpage that sends visitors to your site using a link. This parameter is available for some default events that are related to website visits, such as page_viewed.urlThis is the url of the current webpage the user is accessing. This parameter is available for some default events that are related to website visits, such as page_viewed.

Below are the event parameters of the default event aiq_journey_map_exit, an event that is generated when the user is exited out of a journey map campaign. 

📘Note:The event aiq_journey_map_exit is only generated in journey maps created after August 2021.

Event ParametersDescriptionexit_timesThe number of times the user is exited out of a single journey map campaign.



Conditions [2]

https://docs.aiqua.appier.com/docs/defining-segments



Event ParametersDescriptionexit_timesThe number of times the user is exited out of a single journey map campaign.

Here's an example of how to segment users who are exited out of a journey map campaign more than 3 times:aiq_journey_map_exit exit_times Once > "3"exit_reasonexit_node: Users are exited out of the journey map campaign after entering an exit node.exit_criteria: Users are exited out of the journey map campaign after meeting the overall exit criteria.excluded_after_segment_refresh: Users are exited out of the journey map campaign because they no longer fulfill the conditions of the audience segment selected.journey_map_idThe campaign ID of the journey map. To find the campaign ID, go to Campaign List, click the Edit button of the campaign, and find the campaign ID in the URL.

Here's an example of how to segment users who are exited out of a journey that has the campaign ID "12345":aiq_journey_map_exit journey_map_id Once = "12345"journey_map_nameThe campaign name of the journey map.

After you have selected an attribute or an event parameter, you will see the operator drop-down list. Depending on the data type of the attribute or event parameter, different operators or filters will be available. 

String

Number

Boolean

Date / Time

If the data type of the attribute or the event parameter is set to string (i.e. text), you will see the following operators in the drop-down list. The value entered is not case-sensitive.

OperatorsDescriptionequalsThe value has to be exactly the same to be considered a match.Example

If condition is product_name equals "Blue Jeans"

• "Blue Jeans" >> Match

• "Classic Blue Jeans" >> Not a match

• "Jeans" >> Not a matchis any ofThe value has to be an exact match with at least one of the values you have entered. You can directly paste a list of comma-separated values or a list from a spreadsheet.Example

If the condition is product_name is any of "apple" or "juice" or "banana cake"

• "apple" >> Match

• "apple juice" >> Not a match



Conditions [3]

https://docs.aiqua.appier.com/docs/defining-segments



• "apple" >> Match

• "apple juice" >> Not a match

• "banana" >> Not a matchcontainsIf the parameter value collected contains the value you have entered, it will be considered a match.Example

If condition is product_name contains "Blue Jeans"

• "Classic Blue Jeans" >> Match

• "Blue Denim Jeans" >> Not a match

***If condition is product_name contains "Jean"

• "JeanS" >> MatchexistsIf you choose exists, you don't need to input a value.

When the operator is set to exists, note that users with empty string or null value for this parameter are considered as meeting the condition.

For example, if you set the include condition to phoneNo exists, this segment will include users with an empty value for the phoneNo profile parameter.

If the data type of the attribute or the event parameter is set to number you will see the following operators in the drop-down list. 

OperatorsDescription=Equal to!=Not equal toGreater than<=Less than or equal to>=Greater than or equal to

If the data type of the attribute is set to boolean, you will see the operator is and you can select true or false. The following default attributes in the condition drop-down list are boolean.

aiq_push_enabled

email_hard_bounced

email_unsubscribe

Currently, the date / time related filters are only supported for the following default attributes:

line_first_sync_time: The date when the user is detected as a follower of the LINE channel. 

line_unfollow_time: The date when the user is detected as no longer following the LINE channel. 

You can use the above LINE-related user attributes to segment users based on the date they follow or unfollow your LINE channel. 

🚧ImportantAIQUA detects for new LINE followers and unfollowers once a day. The detected date may be one day later than users’ actual followed or unfollowed date.

When line_first_sync_time or line_unfollow_time is selected, the following filters are available:



Conditions [4]

https://docs.aiqua.appier.com/docs/defining-segments



When line_first_sync_time or line_unfollow_time is selected, the following filters are available:

FiltersDescriptionIn the last X daysIncludes today.In the next X daysIncludes today.BeforeDoes not include today or the selected date.AfterDoes not include today or the selected date.

For example, you can send a campaign with welcoming message to your new LINE users. To do this, create a segment of users with line_first_sync_time = "in the last 1 day".

Below are some examples on how to segment audience.

Segment users who added jeans-related products to cart, but didn't purchase.

IncludeExcludeproduct_added_to_cart, category contains "jeans"product_purchased, category contains "jeans"

Segment users who have clicked on a particular campaign with the campaign name "ABC".

IncludeExcludenotification_clicked, Campaign Name = "ABC"--

👍Tip:If you do not see the campaign name listed in the dropdown list, you can also segment based on notification ID. See How do I segment by notification ID?

Segment VIP users who have purchased in the last 30 days, but not in the past 7 days.

IncludeExcludemember_status equals "VIP"--product_purchasedproduct_purchasedEvents in the last 30 daysEvents in the last 7 daysUpdated 3 months ago Table of Contents

Overview

Segmenting by conditions

Include and Exclude Users

Adding Conditions

User Attributes

User Events

Event Parameters

Data Type and Operators

String

Number

Boolean

Date / Time

Segmentation Examples

Example 1: Reduce cart abandonment

Example 2: Target interested users

Example 3: Re-engage inactive users



Offline Events [0]

https://docs.aiqua.appier.com/docs/segment-by-offline-events



📘NoteOffline event segmentation is a beta feature.

You can segment audiences based on API-uploaded offline event data from your own files, CRM, or other data sources. A typical example of offline event data is transaction data from your physical stores. 

First, your developer needs to create an offline segment source and upload an offline event file using the Offline Event API v2. An offline segment source serves as the underlying data source for offline segmentation.

Next, on the AIQUA dashboard, select an offline segment source and set segmentation conditions to create the final offline event segment.

📘Note

Offline event segments can only be used in:

Regular campaigns: Push, Email, SMS, LINE, and Kakao.

Journey maps

Up to three offline source segments can be created. 

Each offline event entry must have a user_id. If the uploaded user_id does not match with any existing user_id in the AIQUA database, the entry will be stored in the database, but cannot be used in segmentation and campaigns until it has been matched with a user.

Offline event segments cannot be used when creating campaigns via API or sending notifications via API.

Go to Audience > Segment list, and click the + Create segment > Offline events in the top-right corner.

Enter a segment name.

Under Segment Source, select an offline segment source from the dropdown. The dropdown will only show offline segment sources with valid data.

Select Set the Condition and click + Add New Condition to start creating a segmentation condition. For example, you can create a condition to include users who have completed product_purchase events with the product_name parameter containing "shoes" in the past day.

👍TipTo include every user from the offline segment source in the segment, select All Audiences.

If needed, you can set Exclude conditions to explicitly exclude users who have specified offline events.

Click Save. 

In the segment list, you'll be able to see the segment with the Source set to Offline event.



Offline Events [1]

https://docs.aiqua.appier.com/docs/segment-by-offline-events



Click Save. 

In the segment list, you'll be able to see the segment with the Source set to Offline event.

Users who matched with a user_id in the uploaded offline events are tallied in the segment list table based on the channels they can receive campaigns from. For example, if a matched user has an email address and phone number recorded in the database, the user will be counted in the Email subscribers and Phone numbers columns.Updated 3 months ago Getting Started with the Offline Event API v2Table of Contents

Overview

Segmenting by offline events



Test Segment [0]

https://docs.aiqua.appier.com/docs/test-segment



When creating campaigns, you can send a test creative to yourself to preview the campaign using the Test Your Creative button.

To receive test creatives, you need to first add your devices to the Test Segment. 

The test segment’s purpose is to receive test campaigns, which have different settings than standard campaigns. When sending test campaigns using the Test Your Creative button:

The unsubscribed email list and user consent settings for push notifications are ignored

Blackout window settings are ignored

Frequency caps don't apply

Refer to the sections below to see how to add your device to the test segment for different campaign types.

Web Push

App Push and In-App Campaigns

LINE Campaigns

Kakao and SMS Campaigns

Email Campaigns

👍TipFor In-Web Campaigns, you can use the Preview on Website feature to preview the creatives.

Add your web profile to the test segment using your userId.

📘PrerequisiteMake sure your website is integrated with Appier Web SDK

Go to the website on your test device. 

Windows desktops and Android devices: Use a Chrome or Firefox browser.

MacOS desktops: Use a Chrome browser.

iOS devices: Web push is not supported on iOS devices.

In the browser's address bar, enter your website URL, and append a "?" followed by a unique identifier. For example, if your website is https://www.appier.com/en/index.html, you can use https://www.appier.com/en/index.html?xyz as your unique url.

📘Note:Tags entered in a URL after a ‘?’ does not affect the landing page. For example, all of the URLs listed below direct the user to the same landing page. https://www.appier.com/en/index.html

https://www.appier.com/en/index.html?abcdef

https://www.appier.com/en/index.html?tag=abcdef

https://www.appier.com/en/index.html?utm_source=ads123

Visit the unique URL at least twice. Each time, wait for the page to completely load. The AIQUA pixel will capture your test device in this step. 

On the AIQUA dashboard, click your account name in the lower-left corner, and select Recent Activity.



Test Segment [1]

https://docs.aiqua.appier.com/docs/test-segment



On the AIQUA dashboard, click your account name in the lower-left corner, and select Recent Activity. 

Find the event with your unique URL and copy the User ID.

👍Tip:If you do not see your event, you may need to wait a few minutes or click Refresh. You can also enter the unique url in the search bar to search.

Go to Audience > Segment List and click the edit icon of the Test Segment.

Under User who match conditions > Include Users, click + Add New Condition.

In the new field that appears, select userId, select =, and paste the id you previously copied.

Click Save.

The Web Users and Web Push Subscribers count should increase by one.

Add your Android device to the Test Segment using the device's advertiserId.

📘PrerequisitesMake sure your app is integrated with Appier Android SDK.

On your Android test device, go to Menu > Settings > Google > Ads > Advertiser ID to find your Advertiser ID.

Go to Audience > Segment List and click the edit icon of the Test Segment.

Under User who match conditions > Include Users, click + Add New Condition.

In the new field that appears, select to advertiserId, select equals, and enter the Advertiser ID.

Click Save.

Add your iOS device to the Test Segment using the userId.

📘Prerequisites

Make sure your app is integrated with Appier iOS SDK.

Log a uniquely identifying attribute, like email or phoneNo, so that you can use this attribute to identify your test device later. User attributes can be logged using these methods via iOS SDK.

Launch your app and allow notifications. 

From the AIQUA dashboard, click your account name in the lower-left corner and select Recent Users.

After a few minutes, your profile should appear under iOS Production or iOS Development (select the environment you are using).

Search for your device using the uniquely identifying attribute you have logged.

Copy the value under USER ID column.

Go to Audience > Segment List and click the edit icon of the Test Segment.

Under User who match conditions > Include Users, click + Add New Condition.



Test Segment [2]

https://docs.aiqua.appier.com/docs/test-segment



Under User who match conditions > Include Users, click + Add New Condition.

In the new field that appears, select userId, select =, and paste the USER ID you previously copied.

Click Save.

Add your LINE account to the Test Segment using your account's line_uid. 

You need to be able to access LINE Developers console. Your developer can grant access to you by clicking Invite by email in the Roles tab of the channel. 

Log in to LINE Developers console, select your business under Providers and click your LINE channel.

Under the Basic Settings tab, scroll down to find and copy your user ID.

On the AIQUA dashboard, go to Audience > Segment List and click the edit icon of the Test Segment.

Under User who match conditions > Include Users, click + Add New Condition.

In the new field that appears, select line_uid, select equals, and paste your LINE user ID.

Click Save.

📘Prerequisites

The phone number needs to be in AIQUA's database already. You can add the phone number to AIQUA using one of these methods:

Upload User Attributes via AIQUA dashboard

Uploading Offline Users via API

For Kakao, make sure you have opted in to your Kakao Talk Channel so that you can receive notifications.

Add your phone number to the Test Segment using phoneNo as the user attribute. 

On the AIQUA dashboard, go to Audience > Segment List and click the edit icon of the Test Segment.

Under User who match conditions > Include Users, click + Add New Condition.

In the new field that appears, select phoneNo, select equals, and type your phone number with the country code (for example, 886912345678 where 886 is the country code).

Click Save.

Add your email address to the Test Segment using email as the user attribute.

📘PrerequisitesThe email address needs to be in AIQUA's database already. You can add the email address to AIQUA using one of these methods:

Upload User Attributes via AIQUA dashboard

Uploading Offline Users via API

On the AIQUA dashboard, go to Audience > Segment List and click the edit icon of the Test Segment.



Test Segment [3]

https://docs.aiqua.appier.com/docs/test-segment



On the AIQUA dashboard, go to Audience > Segment List and click the edit icon of the Test Segment.

Under User who match conditions > Include Users, click + Add New Condition.

In the new field that appears, select email, select equals, and then type your email address. Use lowercase letters in the email address.

Click Save.

Updated 3 months ago Table of Contents

Web Push

App Push and In-App Campaigns

Android Devices

iOS Devices

LINE Campaigns

Kakao and SMS Campaigns

Email Campaigns



Upload User Attributes [0]

https://docs.aiqua.appier.com/docs/updating-user-profiles



📘Note:This is a BETA feature.

The Upload User Attributes feature on the AIQUA dashboard allows you to add and update user attributes to AIQUA by uploading a CSV file. For example, you can upload offline user data from your CRM system or upload email lists you have collected from marketing events.

Once uploaded, AIQUA will try to match the uploaded user attributes with existing Android, iOS, and web users onboarded via SDK. If an identifier matched (based on user_id, email, or phoneNo), AIQUA merges the uploaded offline user with the SDK-collected online users.

This merging enriches your user data and allows you to reach previously offline users through other marketing channels such as push notifications.

🚧IMPORTANT:Each user record must have one of the following identifiers: user_id, email, phoneNo. The assigned value must be a string (text).If more than one identifier presents in a record, only one identifier is used to match users based on the following priority:

first priority - user_id

second priority - email

third priority - phoneNo

In case the identifiers of the offline user do not match with any Android, iOS, or web users, the uploaded user is stored in a common database for offline users. They can be segmented, based on their user attributes, and used only for email and SMS campaigns.AIQUA will try to match the remaining unmatched offline users once per day since new online users will continue to be onboarded through SDK.

Here's an example of how the merging process works after an upload.

The following SDK-collected user profile exists in the Android database:

Then, an CRM offline user profile is uploaded. This CRM user shares the same email address with the above Android user. 

After a batch job, the Android and CRM user profiles are merged as an online user in the Android database into the following profile. 

An uploaded user profile updates a matching SDK-collected user only once. This uploaded user profile is archived once done updating each SDK user profile.



Upload User Attributes [1]

https://docs.aiqua.appier.com/docs/updating-user-profiles



To access this feature, go to AIQUA dashboard, select Audience > Segment list and click on the three vertical dots and select Upload user attributes. 

On the Upload user attributes page, click Download Example CSV to see how your CSV file must look like before uploading it to AIQUA. 

Follow these formats and standards when creating your CSV file:

Include a header record. The first record is treated as a header and skipped for the import. 

Include one of these required fields: user_id, email, phoneNo.

Use a comma (,) to separate values.

Each record must have the same number of comma-separated fields. 

Fields that have a line break, double quote, or commas must be enclosed by quotes. If they're not, the file might not get processed correctly. 

The supported encoding is UTF-8 without BOM. DO NOT use UTF-8 BOM or other encodings.

The maximum CSV file size is 100 MB. 

After preparing your CSV file, refer to the following steps to upload. 

Click Upload CSV File and choose the CSV file you'd like to upload.

You'll see a preview of the user profiles you uploaded, as below:

COLUMN TITLE: This indicates the entries you included in the first row of your CSV file. 

CONTENT EXAMPLE: This displays all the entries you included under each column title. 

Under ATTRIBUTES, assign an existing attribute for the values. The DATA TYPE of this existing attribute is shown.

If the attribute is not an existing attribute in AIQUA, click Create new attribute to create a new attribute and set the Data Type to either Text or Number.

If you do not wish to update this attribute to AIQUA, click Skip this column. 

When you're done setting up your attributes, click Save.

🚧Important:Submitted attributes may no longer be edited.

Copy and save the tracking number displayed upon submission. 

Using an API call, you can check the status of your upload by using the tracking number shown above as the job_id. See details in this guide.Updated 3 months ago Table of Contents

How it works

Step 1: Prepare a CSV file for your user profiles



Upload User Attributes [2]

https://docs.aiqua.appier.com/docs/updating-user-profiles



How it works

Step 1: Prepare a CSV file for your user profiles

Step 2: Upload the CSV file



Export Segment Reports [0]

https://docs.aiqua.appier.com/docs/export-segment-reports



From the segment list on AIQUA dashboard, you can export the users included in a segment. Segment report can be exported in two ways:

Export via AIQUA dashboard (segment list page)

Export via Report API

📘NoteSegments containing more than 1.2 million users can't be exported.

A separate CSV file will be exported for each platform (e.g. web, Android, iOS) that has at least one user. The following platforms are available:

Web users: Lists all web users in the segment, including those who are no longer active or have unsubscribed from push notifications.

Android users: Lists all Android users, including those who are no longer active or have unsubscribed from push notifications. Users who have uninstalled the app are not included.

iOS users: Lists all iOS users of your production app, including those who are no longer active or have unsubscribed from push notifications. Users who have uninstalled the app are not included.

iOS dev users: Lists all iOS users of your development app, including those who are no longer active or have unsubscribed from push notifications. Users who have uninstalled the app are not included.

Email users: Lists all users with an email address in the segment, including those who have unsubscribed from email campaigns.

Phone users: Lists all users with a phone number in the segment.

LINE users: Lists all users with a LINE UID in the segment, including those who have unfollowed or blocked the LINE channel.

Go to Audience and select Segment List.

Next to the segment name, click the menu icon and click Export Reports.

When the report is ready, an email containing the download links for the reports will be sent to the email address associated with your login account. 

In addition to exporting segment reports from the AIQUA dashboard, you can also programmatically export reports using the Report API. To export segment reports via API, you'll need to provide the following details:

The segment ID of the segment you'd like to export the report for



Export Segment Reports [1]

https://docs.aiqua.appier.com/docs/export-segment-reports



The segment ID of the segment you'd like to export the report for

The reports are based on user information retrieved at the time of the export. As a result, the number of users in the reports might be different from the user counts shown in the segment list due to different data update times, depending on the segment type.

For app users who are using the following SDK versions, the unsubscribed column will be FALSE regardless of the actual opt-in status:

Android SDK 5.5.2 or earlier

iOS SDK 4.4.1 or earlier

The columns included in the report are different based on the platform. Refer to the following tables for the columns included in the reports.

Column NamePlatformsDescriptionFirst SeenWeb

Android

iOSFor web users, this is the date when the user first visits your website.

For app users, this is the date when the user first installs the app or when the user reinstalls the app.Last SeenWeb

Android

iOSThis indicates the date when the user last completed an event, or an attribute is updated for the user.Install TypeAndroid

iOSFor app users, first install indicates whether this is the user's first time installing the app.User IdWeb

Android

iOS

Email

SMS

LINEThis is the custom user ID used by your company (e.g. member ID from your CRM system). The data needs to be stored using the parameter name user_id.Email IDWeb

Android

iOS

EmailThis is the user's email address. The data needs to be stored using the parameter name email.LINE UIDLINEThis is the user's LINE UID.Lifecycle StageWeb

Android

iOSThis feature has been deprecated.Total Days ActiveWeb

Android

iOSThe total number of days the user is active since the user's "First Seen" date.

The user is considered active in a day if the user has at least one event activity that day (excluding some system events such as notification_received).Days Active In Last 30 DaysWeb

Android

iOSThe number of days the user is active in the past 30 days.



Export Segment Reports [2]

https://docs.aiqua.appier.com/docs/export-segment-reports



Android

iOSThe number of days the user is active in the past 30 days.

The user is considered active in a day if the user has at least one event activity that day (excluding some system events such as notification_received).Install SourceAndroid

iOSTo have data under this column, AppsFlyer or Adjust needs to be integrated.First NameWeb

Android

iOSThis is the user's first name. The data needs to be stored using the parameter key first_name.Last NameWeb

Android

iOSThis is the user's last name. The data needs to be stored using the parameter key last_name.Phone NumberWeb

Android

iOS

SMSThis is the user's phone number. The data needs to be stored using the parameter key phoneNo.CityWeb

Android

iOSThis is the user's city. The data needs to be stored using the parameter key city.DOBWeb

Android

iOSThis is the user's date of birth. This data needs to be stored using the parameter keys day_of_birth, month_of_birth, and year_of_birth.Device TokenWeb

Android

iOSThe FCM token in Android and Web, or the APNS device token in iOS.Advertising IdAndroid

iOSThis is the advertising ID.UnsubscribedWeb

Android

iOS

Email

LINEA TRUE value indicates that:

The web user has denied permission to push notifications.

The Android or iOS user has denied permission to push notifications. See limitations in the note above the table.

The email user has unsubscribed from email campaigns or the email address has hard bounced.

The LINE user has unfollowed the LINE channel.

The following columns in the report are related to the device, app, or browser used by the user.

Column NamePlatformsDescriptionDevice VendorWebThis is the device vendor.Device ModelWeb

Android

iOSThis is the device model.Device TypeWebThis is the device type.OS VersionWeb

Android

iOSThis is the version of the operating system used.OS NameWebThis is the operating system used.Browser nameWebThis is the browser name.Browser versionWebThis is the browser version.App VersionAndroid

iOSThis is the app version.Device BrandAndroid

iOSThis is the brand of the mobile device.LanguageAndroid



Export Segment Reports [3]

https://docs.aiqua.appier.com/docs/export-segment-reports



iOSThis is the app version.Device BrandAndroid

iOSThis is the brand of the mobile device.LanguageAndroid

iOSThis is the detected language.QG SDK VersionAndroid

iOSThis is the version of the Appier Android or iOS SDK in the app.

The following columns in the report depend on the user events and attributes available in this AIQUA account.

Column NamePlatformsDescription_countWeb

Android

iOSThis is the number of times the user has completed this event._first_occurrenceWeb

Android

iOSThis is the timestamp when the user completed this event for the first time._last_occurrenceWeb

Android

iOSThis is the timestamp when the user last completed this event.CustomField_Web

Android

iOSThis is the value of the user attribute.Updated 3 months ago Table of Contents

Overview

Exporting via AIQUA dashboard

Exporting via Report API

How to read the reports

Report columns



Campaigns [0]

https://docs.aiqua.appier.com/docs/campaigns



👍Tip:In AIQUA, creating audiences is essential before starting a campaign. If you want to know more about Audiences, check out these guides:User Data Collection

Audience Segmentation

Using AIQUA, you can create various types of campaigns and use them to send creatives to your customers. The following types of campaigns are available:

Regular Campaigns - Regular campaigns allow you to reach users via Push, Email, SMS, and Instant Messaging. In regular campaigns, notifications are sent based on the schedule you specified.

Trigger Campaigns - Trigger campaigns allow you to reach users via Push, Email, SMS, and Instant Messaging. In trigger campaigns, notifications are sent based on trigger conditions.

In-Web Campaigns - In-web campaigns are popups that are displayed on your websites to your website visitors when the trigger condition is met.

In-App Campaigns - In-app popup campaigns are popups that are displayed inside your app to your app users when the trigger condition is met.

Different AIQUA campaign types are made up of different components to help meet various marketing needs. 

However, every AIQUA campaign contains the following key components to specify the WHO, WHAT, WHEN, WHERE of the campaign. 

Audience is WHO will be receiving your campaign. An audience segment is a group of users segmented based on the criteria you have defined. In some campaigns, you can use multiple segments as your audience. 

This is WHEN the campaign will be sent or displayed. Depending on the campaign type, notifications can be sent based on a schedule or trigger conditions, or a combination of both.

This is WHERE you will be reaching your users. AIQUA offers these channels for reaching users: Push, SMS, Email, instant messaging, in-app notifications, and in-web notifications.



Campaigns [1]

https://docs.aiqua.appier.com/docs/campaigns



Creatives are WHAT you will be showing to your users. A creative is essentially the message to be sent to your users. Using AIQUA, you can make various types of creatives that go beyond the traditional. AIQUA's creatives can be personalized using variables that change based on each user's behaviors and attributes. For more details, see Dynamic Content.Updated 11 months ago Table of Contents

Campaign Types

Key Components of AIQUA Campaigns

Audience

Schedule and Trigger Conditions

Channel

Creative



Regular Campaigns

https://docs.aiqua.appier.com/docs/regular-campaigns



AIQUA's regular campaigns allow you to send messages to your user manually or based on a schedule. The message can be sent using the following channels:

Push (Web, Android, iOS)

SMS

Email

Instant Messaging (LINE, Kakao)

Updated about 2 months ago What’s NextCreating Regular CampaignsManaging Regular CampaignsDid this page help you?



Creating Regular Campaigns

https://docs.aiqua.appier.com/docs/creating-regular-campaigns



Regular campaigns are campaigns that can be scheduled or sent manually. Regular campaigns are supported for the following channels types:

Push (web, mobile)

SMS

Email

Messaging app (LINE, Kakao)

Refer to the following guides to learn how to create a regular campaign, depending on which channel you'd like to use:

Creating push (web, mobile) campaigns 

Creating SMS, email, or messaging (LINE, Kakao) campaigns 

In addition, regular campaign experiments allow you to conduct A/B testing and identify which campaign creatives are the most effective and maximize the impact of your campaigns. Experiments are supported for the following campaigns types:

Push (web, mobile)

Email

See Experiments: Regular Campaigns to learn more about regular campaign experiments.Updated 9 months ago Table of Contents

Overview

Supported channels

Campaign experiments



Push (Web and App) [0]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-push



Follow the steps below to create push (web, mobile) regular campaigns:

Select your audience 

Add campaign creatives 

Configure campaign settings 

Review and launch your campaign 

From the left menu, go to Campaigns > Regular campaigns, click + Create Campaign, then select Push.

Enter a campaign name and select the channels you want to send this campaign to. In addition, you have the option to add:

Tags which can be used for filtering in the campaign list.

A campaign description.

Under the Audience section, select which segments to include and exclude from the campaign.

Users to include: Users in this segment will receive the campaign. If no segment is selected, the value will All users, and every user will receive the campaign. You can select up to 10 segments.

Users to exclude: Users in this segment won't receive the campaign. You can select up to 10 segments.

For example, to send a campaign to users who didn't open your mobile app in the last 30 days:

Users to include: Keep the default value of All users—don't select any segment.

Users to exclude: Select a segment that contains users who have opened the app in the last 30 days.

Next, set up an experiment to analyze creative performance and add campaign creatives.

In push campaigns, you can run experiments. For more details, see Experiments: Push.

The available creatives vary based on the campaign type and audience platform you selected. In the Creative section, select a type of creative and complete all the required fields. Refer to Creatives for details about each creative type and its settings.

A creative preview is available for:

All web campaign creatives.

Android standard push notifications.

iOS standard push notifications.

Note that the actual notification may look different on each user’s device depending on the receiving device’s screen size, settings, and OS version.



Push (Web and App) [1]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-push



You can configure the title, subtitle (only for Android, iOS), message, and destination URL once and apply to all selected channels. You can break down the destination URL by Android, iOS, and website if needed. 

In addition, different advanced settings are available depending on the channel and creative type you select.

👍Content assistantAIQUA's campaign content assistant leverages generative AI to automatically create written content for you campaign creatives. For more details, see Content Assistant.

In the Schedule section, select one of the following options for delivering your campaign.

Send Manually: Send the campaign by manually clicking the send now button on the campaign list page.

One-Time Schedule: Send the campaign at a specific date and time.

You can also select Enable send time optimization, which will send the campaign within 24 hours after the date you specify (based on your account's time zone configurations in Account settings > General settings), but the actual send time is based on when each user is most likely to engage.

Recurring Schedule: Specify the first campaign send time as well as the time interval (in days) for resending the campaign.

The Campaign setting section contains additional settings for goal events, time to live, and frequency cap.

SettingDescriptionSet goal events as conversionsEnabling this setting allows you to select events that will override the account-level conversion events for this campaign.

In the campaign performance page of this campaign, conversion-related metrics will be calculated based on goal events instead of the account-level conversion events.Define time to live (in sec)Set a lifespan for your Android, iOS, and web push campaign notifications. Setting a time to live (TTL) is useful for time-sensitive campaigns, i.e. limited time sales. If no value is specified, the TTL is set to that maximum length of 28 days.



Push (Web and App) [2]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-push



For example, if a campaign is sent at 5PM with a TTL of 7200 seconds (2 hours), only users whose devices are connected to the notification service between 5PM and 7PM will receive the notification. Possible reasons that could prevent a device from connecting to the notification service include:

• The device being powered off

• The device being in power saving mode

• The device having no network connection

Note that a blackout window will override the TTL. For example, if you’ve configured a blackout window starting at 10PM and sent a campaign at 9PM with a TTL of three hours, the campaign's TTL would be reduced from three hours to one hour due to the blackout window.Frequency Cap Settings• Apply frequency cap configured in account settings: Both the daily limit and minimum interval for regular campaigns will be applied.

• Ignore frequency cap: Both the daily limit and minimum interval will be ignored. Select this option to override all frequency caps for important messages.

Learn more about the notification frequency cap in Account Settings.

Finally, review and confirm your campaign settings. When you're ready to launch the campaign, click Publish.

Updated about 2 months ago Table of Contents

Overview

1. Select your audience

2. Configure creatives

Set up an experiment

Add creatives

3. Configure campaign settings

Schedule campaign

Campaign setting

4. Review and launch your campaign



Email and Instant Messaging [0]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-email-and-instant-messaging



Follow the steps below to create email and instant messaging regular campaigns:

Go to the regular campaigns page 

Choose a campaign name and select your campaign type 

Select your audience 

Schedule your campaign 

(Optional) Set campaign settings 

(Optional) Perform an experiment or A/B test 

Add a creative 

(Optional) Configure advanced settings 

Save and send your campaign 

From the left menu, go to Campaigns > Regular Campaigns, and then click Create New Campaign.

📘NoteThe campaign type you select determines the available audience, creative, and advanced options.

In the Campaign section, create a Campaign Name and select your Campaign Type. Adding tags is optional.

Push (web push or app push)

SMS 

Email 

Instant messaging (LINE and Kakao)

👍TipTags can be used to search for your campaign on the campaign list page.

If you selected Push for the campaign type, select a platform to indicate whether you want to send an Android, iOS, or web push campaign. The available creative settings and advanced settings will vary based on the platform selected. Define your campaign the audience using the following options:

Include Users of the Segment: The users in this segment should receive this campaign

Exclude Users of the Segment: The users in this segment shouldn't receive this campaign

For example, to send a campaign to users who didn't open the app in the last 30 days:

Under Include Users of the Segment, select All users

Under Exclude Users of the Segment, select a segment that contains users who have opened the app in the last 30 days

📘NoteUnder default settings, AIQUA will start to pre-calculate the audience and creatives 1 hour before the scheduled run time of regular campaigns. As a result, users who meet the segmentation conditions within 1 hour of the scheduled run time will not be considered. 

If the regular campaign is created within 30 minutes or updated within 1 hour of the scheduled run time, AIQUA will not pre-calculate.



Email and Instant Messaging [1]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-email-and-instant-messaging



If the segment condition is changed from the segment list during pre-calculation, AIQUA will continue with pre-calculation and the changes will not be applied to that campaign.

In the Schedule section, select one of the following options for delivering your campaign:

Send Manually: Send the campaign by manually clicking the send now button on the campaign list page

One-Time Schedule: Send the campaign on a specific time and day

Recurring Schedule: Specify the first campaign send time as well as the time interval (in days) for resending the campaign

One-Time Schedule

Recurring Schedule

👍TipFor web push, SMS, and instant messaging, the corresponding options are located under Advanced Settings.

SettingDescriptionSet goal events as conversionsEnabling this setting allows you to select events that will override the account-level conversion events for this campaign.

In the campaign performance page of this campaign, conversion-related metrics will be calculated based on goal events instead of the account-level conversion events.Define time to live (in sec)Set a lifespan for your Android, iOS, and web push campaign notifications. Setting a time to live (TTL) is useful for time-sensitive campaigns, i.e. limited time sales. If no value is specified, the TTL is set to that maximum length of 28 days.

For example, if a campaign is sent at 5PM with a TTL of 7200 seconds (2 hours), only users whose devices are connected to the notification service between 5PM and 7PM will receive the notification. Possible reasons that could prevent a device from connecting to the notification service include:

• The device being powered off

• The device being in power saving mode

• The device having no network connection



Email and Instant Messaging [2]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-email-and-instant-messaging



• The device being powered off

• The device being in power saving mode

• The device having no network connection

Note that a blackout window will override the TTL. For example, if you’ve configured a blackout window starting at 10PM and sent a campaign at 9PM with a TTL of three hours, the campaign's TTL would be reduced from three hours to one hour due to the blackout window.Frequency Cap Settings• Apply frequency cap configured in account settings: Both the daily limit and minimum interval for regular campaigns will be applied.

• Ignore frequency cap: Both the daily limit and minimum interval will be ignored. Select this option to override all frequency caps for important messages.

Learn more about the notification frequency cap in Account Settings.

The following options let you show different variations of a creative to a portion of your users and test what works best for your audience.

In email campaigns, you can run experiments. For more details, see Experiments.

In push campaigns, you can perform A/B tests. Select Perform an A/B test and add two creatives for A/B testing. Configure the following settings for the A/B test:

The percentage of users in the segment who will receive each creative. For example, if you choose 5%, it means that 5% of users will receive Creative A and another 5% will receive Creative B.

The time it takes before the better performing creative gets sent to the remaining percentage of your user segment.

📘NoteThe available creatives vary based on the Campaign Type and Audience Platform you selected.

👍TipUse content assistant to automatically generate content for your creative. Content assistant can generate options for the creative's Title, Subtitle, and Message.

In the Creative section, select a type of creative and complete all the required fields.

A creative preview is available for the Standard creative for web, Android, and iOS push notifications. The actual notification may look different on each user’s device depending on the screen size, settings, and OS version.



Email and Instant Messaging [3]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-email-and-instant-messaging



Click Test Your Creative to receive a test notification. See Test Segment to see how to add your device to the test segment.

Different options are available based on the campaign type and audience platform you selected.

Web push

Android push

iOS push

👍TipFor more information on Time to Live, Goal Events, and Frequency Cap Settings, see Step 5. Set campaign settings.

SettingDescriptionEnable heads-up notificationsHeads-up notifications allow you to send a notification that briefly appears as a floating window in unlocked Android devices.

Requirements:

• Your app must be using Appier Android SDK version 5.5.4 or later

• The receiving device must be running Android 5.0 (Lollipop) or laterMessage Settings in the Notification Center• Pile Up: All notifications from this campaign will remain in the device's Notification Center until the user clicks on them.

• Replace: An unclicked notification will be removed from Notification Center when the next notification arrives.Customize notification soundAllows you to insert a sound file in your Android or iOS push campaign. Sound files must meet the requirements specified for each platform:

• Android sound file requirements

• iOS sound file requirements

For Android, Message Settings in the Notification Center > Pile Up must be selected for this feature to be supported.Include Key-Value PairsAllows you to include custom data in Android and iOS push campaigns.

For details on how to receive key-value pairs in your app, see the guides for Android and iOS.Keep the unclicked notification in the Notification Center (Pile up notifications)This is a web push feature.

• If this option is selected, all notifications from this campaign will remain in the device's Notification Center until the user clicks on them.

• If this option is not selected, an unclicked notification will be removed from Notification Center when the next notification arrives.

Click Save to save your settings and create the campaign.



Email and Instant Messaging [4]

https://docs.aiqua.appier.com/docs/creating-regular-campaigns-email-and-instant-messaging



Click Save to save your settings and create the campaign.

After being created, your campaign will be visible from the campaign list page. Depending on the setting you selected under the Schedule section, you'll either be able to send the campaign or view the next campaign run time.

Schedule settingDescriptionSend ManuallyIf you selected Send Manually, you'll need to manually click the Send Now icon to send the campaign.One-Time Schedule or Recurring ScheduleIf you selected One-Time Schedule or Recurring Schedule, you'll see the next run time in the campaign list under the Schedule Run column.Updated 7 months ago Table of Contents

Overview

1. Go to the regular campaigns page

2. Choose a campaign name and select your campaign type

3. Select your audience

4. Schedule your campaign

5. (Optional) Set campaign settings

6. (Optional) Perform an experiment or A/B test

Experiment

A/B test

7. Add a creative

8. (Optional) Configure advanced settings

9. Save and send your campaign



Managing Regular Campaigns [0]

https://docs.aiqua.appier.com/docs/managing-regular-campaigns



After creating a regular campaign, you can view and manage it in the regular campaign list (Campaigns > Regular campaigns). In addition to searching and filtering existing campaigns, you can perform operations such as manually sending campaigns, viewing the campaign's performance page, and exporting reports.

Search and filter campaigns 

Perform campaign operations

Viewing campaign performance 

From the campaign list, you can find campaigns using the search box and apply various filters to display a more focused set of campaigns.

Enter search terms to find campaigns by name or ID.

Use the provided filter options to streamline searches in the regular campaign list.

Filter optionDescriptionChannelSelect a campaign channel like Push or Email.StatusSelect one of the following campaign statuses:

• Draft: The campaign hasn't been manually sent yet. Not applicable to campaigns on a one-time or recurring schedule. Select this option to quickly identify campaigns ready for manual sending.

• Scheduled: One-time: The campaign is scheduled to run in the future.

• Scheduled: With STO: The campaign is scheduled for the future with send-time optimization enabled.

• Scheduled: Recurring: This campaign is scheduled to run on a recurring schedule.

• Completed: The campaign has finished sending.

• Archived: The campaign has been archived.TagSelect one or more tags from the dropdown.

From the campaign list, you can access the campaign's edit screen and campaign actions by clicking the buttons next to the campaign's name.

To edit the campaign, click the pencil icon.

To see a list of other available operations, click the three vertical dots and select a campaign operation to perform.

The following table describes the operations available for regular campaigns.



Managing Regular Campaigns [1]

https://docs.aiqua.appier.com/docs/managing-regular-campaigns



The following table describes the operations available for regular campaigns.

Campaign operationDescriptionScheduleSet a campaign delivery schedule.DuplicateDuplicate the campaign. The duplicated campaign's name will be the original campaign's name with "-copy" appended.Send nowManually send the campaign.Modify tagsAdd and remove tags for this campaign.View Activity LogsView logs detailing operations performed on this campaign.Export user reportExport a user report containing data about users who interacted with or received this campaign.ArchiveArchive the campaign. Archived campaigns aren't displayed in the campaign list unless the status filter is set to include campaigns with the Archived status.

You can view performance data using:

Campaign list metrics 

The campaign performance page 

Exportable reports 

The following table lists the metrics and campaign details visible from the campaign list.

MetricDescriptionRunsThe number of campaign runs. Each run refers to a single instance of sending the campaign.Total sentThe total number of notifications sent by AIQUA.DeliveredThe number of times this campaign has been delivered via email, SMS, and Kakao, as reported by their respective vendors.ImpressionsAn impression is counted when a user receives a push (app or web), in-web, or in-app campaign notification on their device. This is based on the number of notification_received events.



Managing Regular Campaigns [2]

https://docs.aiqua.appier.com/docs/managing-regular-campaigns



For example, if the campaign is sent to an audience with 50K users, and only 30K users receive it on their devices, then the number of impressions is 30K.OpensThe number of times the email was opened.Open rateThe open rate for email campaigns.ClicksThe number of times users click on the campaign based on the number of notification_clicked events.CTRThe clickthrough rate of the campaign until its end date. Calculated using (Clicks / Impressions) x 100%.CONV. countThe count of online conversion events until the campaign's end date. This is based on the attribution settings and conversion events you selected in your account settings.CONV. valueThe monetary value associated with online conversion events.

For example, if the conversion event is checkout_completed, the CONV. value represents the sum of the conversion values of all checkout_completed events attributed to the campaign.Offline CONV. countThe count of offline conversion events uploaded through Offline Event API V2. This is based on the attribution settings you selected in your account settings.Offline CONV. valueThe monetary value of all offline conversion events attributed to the campaign.Include segmentsSegments selected to receive this campaign. Hover over this column to view the full list of included segments.Exclude segmentsSegments excluded from receiving this campaign. Hover over this column to view the full list of excluded segments.Next scheduled timeIf the campaign has been scheduled for the future, this column displays the date and time of the run, otherwise, this column will be empty.Last sent timeThe last time the campaign was run.Last editedThe last time the campaign was edited.

Click on the campaign's name to open its performance page. For more details, see View Performance.

Campaign performance report

User report



Managing Regular Campaigns [3]

https://docs.aiqua.appier.com/docs/managing-regular-campaigns



Campaign performance report

User report 

Campaign performance reports contain campaign details and performance metrics, and can be exported to a CSV file and downloaded via URL sent to your email address. For details about what data the campaign performance report includes, see Exporting Campaign Performance Reports.

To export a campaign performance report, click Export report.

User reports contain data about users who interacted with or received this campaign, including their user ID, email address, and whether they performed certain actions, such as opens and clicks. The report can be exported to a CSV file and downloaded via URL sent to your email address. For more details about the data contained in user reports, see Export Campaign User Reports.

To export this report, click the three vertical dots to open the list of available campaign actions, then click Export user report.

Updated 5 months ago Table of Contents

Overview

Searching and filtering campaigns

Searching

Filtering

Performing campaign operations

Viewing campaign performance

Campaign list metrics

Campaign performance page

Exportable reports
