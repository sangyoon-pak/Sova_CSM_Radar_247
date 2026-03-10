---
source: notebooklm_export
file_id: "064"
filename: "064_aiqua_rc_part_4.txt.txt"
doc_type: "reference_card"
product: "AIQUA"
content_type: "txt"
language: "en"
guide_summary: "This documentation serves as a practical guide for integrating the AIQUA platform across web and mobile applications, focusing on developer setup and marketing optimization. It details the essential requirements for **conversion value tracking**, such as setting events and including the necessary `valueToSum` parameter, alongside mechanisms for managing **event attribution** across multiple domains. Crucially, the text provides robust strategies for overcoming push notification delivery challeng"
guide_keywords: "Log User Events, SDK Installation, Push Notifications, Track Monetary Value, User Data Permissions"
---

# 064 aiqua rc part 4

How do I segment by notification ID? [1]

https://docs.aiqua.appier.com/docs/how-do-i-segment-by-notification-id



If the campaign execution has been triggered, you can also open the Experiment analysis tab on the performance page. Click the copy icon corresponding to a variant from Performance analysis section to copy its notification IDs.

After retrieving the notification ID, refer to the Segment by Condition (User Events) guide to create a segment. Follow the steps provided to add new conditions with the notification ID:

In the event drop-down list, select a notification-related event, such as notification_received or notification_clicked.

Click Add Filter, set the event parameter to notificationId, and then enter the notification ID.

Use each variant's campaign ID to generate a notification ID that can be used for segmentation. This method of retrieving the notification ID is applicable to the following campaign types:

Regular push (non-merged) campaigns

Regular email campaigns

In-app campaigns

In-web campaigns

Go to the campaign list, click the Edit button for the campaign, and find the variant's campaign ID by hovering over the variant name. 

Next, convert the variant's campaign ID to a notification ID using the following formula:Notication ID = Campaign ID x 10,000.

For example, if the variant's campaign ID is 111111, then its notification ID would be 1111110000 (111111 x 10,000).

After retrieving the notification ID, refer to Segment by Condition (User Events) for guidance on creating a segment. Follow the steps provided to add new conditions with notification ID:

In the event drop-down list, select a notification-related event, such as:

qg_inweb_displayed

qg_inweb_clicked

qg_inapp_displayed

qg_inapp_clicked

qg_email_opened

Click Add Filter, set the event parameter to notificationId, and then enter the notification ID.

📘NotesNot applicable for non-experiment merged push campaign.

For non-experiment campaigns, go to campaign list, click the Edit button of the campaign, and find the campaign ID in the URL.

Next, convert the campaign ID to a notification ID as described below.



How do I segment by notification ID? [2]

https://docs.aiqua.appier.com/docs/how-do-i-segment-by-notification-id



Next, convert the campaign ID to a notification ID as described below.

If Campaign ID >= 188800, then the Notification ID = Campaign ID * 10000

e.g. campaign ID is 198765, the notificationId will be 1987650000.

If Campaign ID < 188800, then the `Notification ID = Campaign ID * 1000

e.g. campaign ID is 87654, the notificationId will be 87654000.

After retrieving the notification ID, refer to Segment by Condition (User Events) for guidance on creating a segment. Follow the steps provided to add new conditions with the notification ID:

In the event drop-down list, select a notification-related event, such as:

notification_received

notification_clicked

qg_inweb_displayed

qg_inweb_clicked

qg_inapp_displayed

qg_inapp_clicked

qg_email_opened

Click Add Filter, set the event parameter to notificationId, and then enter the notification ID.

Updated about 2 months ago Table of Contents

Overview

Regular merged push campaigns

1. Retrieve the notification IDs

2. Segment by notification ID

Experiment campaigns

1. Retrieve the variant's campaign ID

2. Convert the variant's campaign ID to a notification ID

3. Segment by notification ID

Non-experiment campaigns

1. Retrieve the campaign ID

2. Convert the campaign ID to a notification ID

3. Segment by notification ID



How do I see conversion value in campaign performance?

https://docs.aiqua.appier.com/docs/faq-conversion-value-in-campaign-performance



Let's say you are tracking checkout_completed events on your website or app, and you want to be able to see the conversion value in the campaign performance page and downloaded performance reports.

To have the monetary value of events tracked under Conv. Value:

Requirement 1: You need to select the events you want to use as conversion events in the Account Settings page.

Requirement 2: The conversion events need to be attributed to the campaign. See Understanding Event Attribution. 

Requirement 3: You need to include the event's monetary value with valueToSum parameter when tracking the events.

The following example demonstrates how to log a checkout_completed event with valueToSum using the Appier Web SDK, where the purchase value is 4000:

appier("event", "product_purchased", {"product_id": "p123", "product_name": "Brand Z shoes"}, 4000);

If the valueToSum parameter is not added, the event will still be tracked, but without a conversion value. You don't need to include valueToSum when tracking event that aren't associated with monetary value. The following example shows how you might log such as event:

appier("event", "product_purchased", {"product_id": "p123", "product_name": "Brand Z shoes"});

For more details on how to track valueToSum, refer to the links below:

Web SDK: Tracking User Events for Web

Android SDK: Tracking User Events for Android

iOS SDK: Tracking User Events for iOS

React Native SDK: Tracking Events and Attributes for React Native

Updated over 1 year ago



How do I track clicks with shortened URLs? [0]

https://docs.aiqua.appier.com/docs/how-do-i-track-clicks-with-shortened-url



If you use shortened URLs as campaign destination URLs, clicks and click-based attribution data to the URL won't be tracked by AIQUA. This is because URL-shortening services remove AIQUA's URL tracking parameters.

To work around this limitation, you can manually append AIQUA's tracking parameter aiqua_attr=.click to the URL before shortening the URL. You'll need to obtain the notification ID of each campaign and replace with the actual notification ID. 

Follow the steps below. 

👍SMS and Kakao campaign click trackingTo track clicks for SMS and Kakao campaigns, you can add an AIQUA short URL to your campaign creative on the AIQUA dashboard.

AIQUA short URL for SMS 

AIQUA short URL for Kakao

To get the notification ID, you will need to obtain the campaign ID first. 

For non-experiment campaigns, go to Campaign List, click the Edit button of the campaign, and find the campaign ID in the URL.

For campaigns with the Experiment feature enabled, each variant has a different campaign ID.

Go to Campaign List, click the Edit button of the campaign, and find the campaign ID by hovering over the variant name.

Next, convert the campaign ID to notification ID as described below.

If Campaign ID >= 188800, then the Notification ID = Campaign ID * 10000

e.g. If the campaign ID is 198765, the notification ID will be 1987650000.

If Campaign ID < 188800, then the Notification ID = Campaign ID * 1000

e.g. If the campaign ID is 87654, the notification ID will be 87654000.

If Campaign 190000 is an A/B campaign, then the 

The notification ID of Creative A is 1900001000

The notification ID of Creative B is 1900002000

Use the notification ID you obtained in the previous step to replace in AIQUA's tracking parameter aiqua_attr=.click. For example, aiqua_attr=12345670000.click.



How do I track clicks with shortened URLs? [1]

https://docs.aiqua.appier.com/docs/how-do-i-track-clicks-with-shortened-url



Next, append the tracking parameter to your destination URL as the query string. A query string is the part of the URL that begins with a question mark, such as ?lang=en in https://www.example.com/product?lang=en.

If your destination URL doesn't have an existing query string, append a question mark ?, followed by aiqua_attr=.click. Example:

Original destination URL: https://www.example.com/products

Parameter appended: https://www.example.com/products?aiqua_attr=12345670000.click

If your destination URL already has existing query parameters, append &aiqua_attr=.click to the URL. Example:

Original destination URL: https://www.example.com/products?lang=en

Parameter appended: https://www.example.com/products?lang=en&aiqua_attr=12345670000.click

🚧ImportantBe sure to change the notification ID for each campaign.

Now you can shorten the URL and use it in AIQUA campaign. 

Updated 7 months ago Table of Contents

Step 1. Obtain the campaign ID

Step 2. Convert the campaign ID to a notification ID

Step 3. Append AIQUA's tracking parameter to the URL

Step 4. Shorten the URL



Why Do I See Discrepancies between AIRIS and AIQUA Reports?

https://docs.airis.appier.com/docs/faq-airis-aiqua-data-discrepancies



At times, you may notice slight data differences between AIRIS reports and AIQUA Analytics Studio reports. The discrepancies are primarily due to inherent differences in how each system processes data and structures its reports.

Here are the three main factors that may cause data discrepancies.

AIRIS and AIQUA both utilize Appier SDK to capture user events but have different data ingestion frequencies. AIRIS focuses on real-time tracking and sends user events to the server instantaneously. AIQUA, on the other hand, sends and aggregates user events in small batches in order to optimize data transmission. The different data processing frequencies can result in small data inconsistencies.

Starting from July 2023, we have removed the batching behavior in AIQUA accounts that are connected with an AIRIS account. After the change, we observed that the data discrepancies have been reduced to under 0.5%.

The data collected by Appier SDK goes through two different data pipelines, one catering to AIRIS and the other to AIQUA. Consequently, even a minor network disturbance can result in small data discrepancies between the two systems.

AIRIS reports are user-centric while AIQUA reports are device-based. If the same person visits your website or app from multiple devices (for example, two iOS devices or multiple web browsers), AIRIS uses a user unification process to merge multiple devices based on the identifiers and ID hierarchy defined in AIRIS. AIQUA, on the other hand, treats each device as a different user. As a result, you might see different results if you compare the user-centric reports (such as Journey, Attribution, and Cohorts) in AIRIS with AIQUA reports.Updated 20 days ago



Why are users receiving delayed notifications?

https://docs.aiqua.appier.com/docs/why-are-users-receiving-delayed-notifications



Due to external factors, it's possible for users to receive delayed notifications, potentially leading to issues such as receiving notifications during a blackout window. Possible reasons for delayed notifications include:

Misconfigured device network settings (for example, DNS or VPN settings).

The mobile device can't receive the notification when it is initially sent (for example, if the device is offline or powered off).

Updated over 1 year ago



Why can't I find some of my past campaigns?

https://docs.aiqua.appier.com/docs/faq-past-campaigns



Only campaigns that have been updated within the past 180 days are shown on AIQUA dashboard. 

If it's an archived campaign, make sure the Show archived campaigns checkbox is selected.

Updated over 1 year ago Why are users receiving delayed notifications?App Push FAQsDid this page help you?



Why do my app push campaigns have low delivery rates? [0]

https://docs.aiqua.appier.com/docs/why-do-my-app-push-campaigns-have-low-delivery-rates



This FAQ describes how AIQUA delivers mobile app push notifications, discusses several reasons which may cause undelivered app push notifications, and provides a solution to mitigate low delivery rates for app push campaigns:

Factors that can affect push notification delivery rates

Factors that don't affect push notification delivery rates

Improving delivery rate: Segmenting by active users

The delivery rate for push campaigns can be calculated using Impressions / Total Sent, where:

Total sent: The total number of push notifications sent

Impressions: The total number of push notifications received on mobile devices, determined by the number of notification_received events which are automatically logged by the Appier SDK upon receiving a push notification

👍Both the Total sent and Impressions metrics are visible from the campaign list page.

Push campaign audience: When an AIQUA app push campaign is run, a push notification is sent to Android or iOS subscribers in the campaign audience, depending on which platform the campaign is targeting. Users satisfying the following conditions are considered subscribers:

The app is installed on the user's device

The user has opted in to your app's push notifications (aiq_push_enabled)

The user has a valid push token (gcmId)

Push notification delivery: AIQUA delivers push notifications using Firebase Cloud Messaging (FCM) or Apple Push Notification service (APNs). After the notification is delivered by AIQUA to the notification service, AIQUA only knows if the notification has been successfully delivered if the Appier SDK logs a push impression event (notification_received). The SDK automatically logs a notification_received event for each push notification that is received.

📘NoteDelivery issues occurring at the notification service level, i.e. due to FCM or APNs, can't be prevented by AIQUA.



Why do my app push campaigns have low delivery rates? [1]

https://docs.aiqua.appier.com/docs/why-do-my-app-push-campaigns-have-low-delivery-rates



📘NoteDelivery issues occurring at the notification service level, i.e. due to FCM or APNs, can't be prevented by AIQUA.

Push notification priority level: To ensure that notifications can be received consistently across platforms and device state (e.g. when your app is killed or running in the background), AIQUA sends notifications to the notification service (FCM or APNs) with the following priority levels: 

FCM message priority: High priority

APNs notification priority (apns-priority): 10

The following factors can affect your campaign's push delivery rate:

Blackout windows (account settings)

Time to live expired (campaign settings)

Delay in uninstalled app token deletion

FCM message overwrite (Android)

Background service restrictions (Android)

Battery optimization

If you've set a blackout window in your account settings to avoid disturbing users or to comply with local regulations, your campaign notifications may go undelivered. When a blackout window is active:

AIQUA strictly avoids sending any notifications to users

If the notification's time to live (TTL) has expired, the notification won't be delivered

If your campaign has a notification time to live (TTL) configured, and the device can't establish a network connection within the specified TTL, the notification will expire and go undelivered.

Notification services, such as FCM or Apple Push Notification service, are unable to deliver push notifications to users who aren't connected to the internet. Notifications are only sent after the connection is re-established, which can result in delayed delivery or TTL-expired (undelivered) messages.

📘NoteAlthough a short TTL may reduce delivery rates to offline devices, notifications with a TTL of 0 seconds are sent by notification services (FCM, APNs) without throttling, allowing for the lowest notification delivery latency.

There is a delay between the time a user uninstalls an app and when the app registration token is removed by notification service, i.e. FCM/APNs.



Why do my app push campaigns have low delivery rates? [2]

https://docs.aiqua.appier.com/docs/why-do-my-app-push-campaigns-have-low-delivery-rates



During this interim period, the notification service will still recognize the app as installed on that user's device (due to the registration token still being present) and will give these notifications a valid message ID even though it's undeliverable, as the user has already uninstalled the app. Since the app has already been uninstalled and the user has no way of receiving the notification, the notification will go undelivered.

AIQUA delivers notifications to offline devices using "collapsible" messages with a single collapse key. When FCM receives more than one "collapsible" message destined for a single device, only the latest message is queued, causing all previous messages to be deleted. This means that messages that haven't yet been delivered by FCM will be deleted if a new message is add to the queue.

For example, if FCM receives two messages from AIQUA, one after the other, destined for a single device, and the device is offline (hence unable to receive notifications), the device will only receive the latest message upon reconnecting to the network.

The first message is queued by FCM, but can't be delivered since the destination device is offline

The second message is queued, but since messages share a single collapse key, the first message is deleted

When the device reconnects to the network, only the latest message is delivered

Apps that the Android operating system determines are not frequently used may be placed in the "Rare" priority bucket. The operating system imposes strict limitations to apps in this priority bucket—they're subject to certain restrictions (e.g. running jobs, triggering alarms) in addition to power management restrictions, which reduce the apps ability to connect to the internet.

👍To learn more about Android's priority buckets, see App Standby Buckets.

When battery optimization features are enabled on a device, background processes can be stopped or restricted, which may limit device connectivity with notification services and potentially impacting push notification delivery.



Why do my app push campaigns have low delivery rates? [3]

https://docs.aiqua.appier.com/docs/why-do-my-app-push-campaigns-have-low-delivery-rates



"Do Not Disturb" mode

Notification frequency cap (account settings)

When "Do Not Disturb" (Android, iOS) is enabled on a device, all notifications are hidden from the user's view. Although users don't see notifications when "Do Not Disturb" mode is enabled, notifications are still delivered in the background, and delivery rate is unaffected.

📘NoteAlthough your campaign's delivery rate may not be affected by devices with "Do Not Disturb" enabled, conversion rates may decrease if fewer users see and interact with the notifications that have been delivered.

Setting a notification frequency cap in your account settings prevents campaign notifications from being sent if your account has exceeded the cap. Although this setting prevents the sending of notifications exceeding the frequency cap, it has no effect on your campaign's delivery rate since AIQUA doesn't send the notifications in the first place.

To reach users more effectively, you can segment by active app users (e.g. users who launched the app in the past seven days). Active app users are more likely to have a higher delivery rate, since your app is less likely to be subject to background service restrictions by the device operating system if your app is frequently used. Reserve app push campaigns for these users.

For the inactive users segment, you can try to use other channels to motivate them to launch your app in order to prevent your app from becoming labeled as "inactive" by the device operating system.Updated over 1 year ago Table of Contents

Overview

Push notification delivery rate

Understanding AIQUA's push notification mechanism

Factors that can affect push notification delivery rates

Blackout windows (account settings)

Time to live expired (campaign settings)

Delay in uninstalled app token deletion

FCM message overwrite (Android)

Background service restrictions (Android)

Battery optimization

Factors that don't affect push notification delivery rates

"Do Not Disturb" mode

Notification frequency cap (account settings)



Why do my app push campaigns have low delivery rates? [4]

https://docs.aiqua.appier.com/docs/why-do-my-app-push-campaigns-have-low-delivery-rates



Factors that don't affect push notification delivery rates

"Do Not Disturb" mode

Notification frequency cap (account settings)

Improving delivery rate: Segmenting by active users



Can I also trigger a fake prompt for users who aren’t opted-in?

https://docs.aiqua.appier.com/docs/can-i-also-trigger-a-fake-prompt-for-users-who-arent-opted-in



Yes. You can do this by calling appier("prompt-push") in the Appier web SDK. 

📘Note:Unsubscribed users, or users who disabled web notifications on their device, wouldn’t get the fake prompt.Updated over 1 year ago Why do my app push campaigns have low delivery rates?How do I disable Web push and system prompts?



How do I disable Web push and system prompts?

https://docs.aiqua.appier.com/docs/faq-disable-web-push-prompts



If you do not want to use the Web push function and wish to stop showing system prompts to request user permission, you can disable the Web push on AIQUA dashboard.

Click your account name in the lower-left corner, go to Integration > Website, and clear the selection for Enable Web Push. 

Click Next to apply the change. 

Visit the website from a new browser to make sure the system prompt does not pop up anymore.

Updated over 1 year ago Can I also trigger a fake prompt for users who aren’t opted-in?How can users opt out of web push?



How can users opt out of web push?

https://docs.aiqua.appier.com/docs/how-can-users-opt-out-of-web-push



If users do not wish to receive web push anymore, they can change the notification settings on their browsers to block web push. Note that the notification settings are only available when the browser is NOT under incognito mode.

Users can follow the instructions below to opt out of web push. 

Opting Out on Desktop Chrome

Opting Out on Desktop Firefox

Opting Out on Android Devices

On the browser, click the lock icon next to the website URL, and select Site settings.

Under the Permissions section, find Notifications in the list to check the the current subscription status.

To opt out of Web push notification from this website, select Block.

On the browser, click the menu icon and select Options or Preferences.

On the left, click Privacy & Security, and under the Permissions section, click the Settings button next to Notifications.

Find the website to check the the current subscription status.

To opt out of Web push notification from this website, select Block and click Save Changes.

On the browser, tap the menu icon next to the website URL and select Settings.

Under the Basics section, select Notifications. 

Find the website to check the current subscription status.

To opt out of Web push notification from this website, turn off the notifications switch.

Updated over 1 year ago Table of Contents

Desktop Chrome

Desktop Firefox

Android Devices



What's Quieter Permission UI? [0]

https://docs.aiqua.appier.com/docs/whats-quieter-permission-ui



Chrome introduced "Quieter Permission UI" for Web push in Chrome 80, where some users will no longer see the system prompts that ask for permission to send Web push notifications. 

There are several situations where Quieter Permission will be applied to Chrome users:

Manual Enrollment - Users can manually enroll in Quieter Permission by going to Chrome's Settings page > Privacy Security > Site Settings > Notifications, and then enabling "Use quieter messaging".

Automatic Enrollment for Users Who Frequently Opt-Out - Chrome automatically enrolls users who frequently decline notification permission across various websites in Quieter Permission.

Automatic Enrollment for Websites with Low Opt-in Rates - Chrome automatically enrolls websites with low opt-in rates in Quieter Permission. 

Users enrolled in Quieter Permission now need to manually click the notification icon in the browser's address bar if they want to subscribe to web push. This is expected to lower your opt-in rate. 

On the upside, however, users who do choose to subscribe probably have higher intent and are more likely to engage.

📘Note:Existing subscribers are not affected.

With the new Quieter Permission UI, it is now even more crucial for marketers to carefully consider user experience. Instead of indiscriminately showing system prompts to all users immediately upon site visit, AIQUA offers several features that help you ask for users' permission at the appropriate time with relevant messages. 

The following feature can be configured in In-Web Campaign:

Subscription Boost - Subscription boost notifications are customizable messages that can pop up inside your website to encourage users to opt-in. Using triggering rules based on user's behavior, Subscription Boost can be shown at the contextually relevant moments in a user’s journey.

The following features can be configured in Web Pixel Settings:

Opt-In Tip - A tip message to show users how to manually opt-in even if they do not see the browser's native system prompt.



What's Quieter Permission UI? [1]

https://docs.aiqua.appier.com/docs/whats-quieter-permission-ui



Opt-In Tip - A tip message to show users how to manually opt-in even if they do not see the browser's native system prompt.

Opt-In Prompt (fake prompt) - This customizable opt-in prompt asks whether the users want to receive notification and only shows the actual system prompt if users agree. This lowers the chance of users declining the system prompt and the chance of your website being considered as having "low opt-in rate" by Chrome.

Delay the timing of the system prompts - You may want to delay the time to show system prompt and space out the time between two system prompts.

The following feature can be configured by contacting Appier Support:

Custom timing for system prompt - Instead of showing system prompt upon users' site visit, you can set the system prompt to only pop up after specific conditions (e.g. after the user completed a purchase). You need to contact Appier Support to enable this feature, and then use appier("prompt-push") to call the function in Appier web SDK.

Updated over 1 year ago Table of Contents

Who will experience Quieter Permission?

What are the impacts?

What are AIQUA's solutions?



How can I manage the traffic coming from my web push campaign?

https://docs.aiqua.appier.com/docs/how-can-i-manage-the-traffic-coming-from-my-web-push-campaign



We recommend these options for you to manage this. 

Option 1: In the AIQUA web UI, go to Account Settings > Notification Send Rate to input the value which corresponds to the number of messages you’d like to send per second. The value must be between 100 to 100,000.

Option 2: If your web push uses a number of images, we recommend hosting these images on your CDN.Updated over 1 year ago What's Quieter Permission UI?Why do some users have different userId and wUserId?



Why do some users have different userId and wUserId?

https://docs.aiqua.appier.com/docs/faq-userid-wuserid



On AIQUA Dashboard, click your account name in the lower-left corner, go to Recent Users and select the Web tab. You will see the userId listed under the USER ID column and the wUserId listed under OTHER FIELDS column. 

This FAQ explains why some web users have the same ID for both userId and wUserId, while other web users have a userId that is different from their wUserId.

userId is the ID for third-party cookie. 

This is used by AIQUA as the unique ID to identify users. 

When the user visits a website integrated with Appier Web SDK for the first time, a userId is generated.

The user will be assigned the same userId across websites, meaning that when this user visits other websites integrated with Appier Web SDK, AIQUA will use the same userId for this user. 

wUserId is the first-party cookie ID. 

For each Appier SDK-integrated website the user visits, Appier Web SDK generates a new wUserId.

The user will have a different wUserId on each websites.

As a result, if your website is the first Appier SDK-integrated website visited by the user, you may see these users having the same ID for userId and wUserId. If the users have previously visited other Appier SDK-integrated websites, they will have a wUserId that is different from their userId.Updated over 1 year ago Table of Contents

userId

wUserId



If I switch to AIQUA from another service, will my users be prompted to allow web push notifications again?

https://docs.aiqua.appier.com/docs/if-i-switch-to-aiqua-from-another-service



The notification prompt's behavior is unchanged after you integrate your website with AIQUA, as long as your website's domain is the same and the user hasn't manually changed their browser's notification settings.

Before integrating with AIQUAAfter integrating with AIQUA*The user allowed web push notificationsThe notification prompt won't display and notifications will continue to be allowed.The user blocked web push notificationsThe notification prompt won't display and notifications will continue to be blocked.The user hasn't allowed or blocked web push notificationsThe notification prompt will continue to display until the user has provided a response.

This scenario occurs under the following conditions:

The user always dismissed the prompt without selecting a response

The user uses a browser that delivers the notification prompt quietly and the user never responded to the prompt

* Only if your domain hasn't changed and the user hasn't changed their browser's notification settings.

Updated over 1 year ago



Journey Maps FAQs [0]

https://docs.aiqua.appier.com/docs/journey-faq



❗️This page is no longer maintained. Please refer to the Enterprise Resource Center instead.

What counts as one user in a journey?

Are re-entered users counted again in node stats?

Why is "Opens" under Performance much higher than "Opened" in node stats?

Is "Arrived" the number of users who received the message?

In journey maps, users across different channels are unified based on the unique identifier user_id, which is the custom user ID used by your company. 

For example, if a person logs in to your website, this web user is no longer an anonymous visitor and can be linked to a user_id. If this person has installed your Android app and logged in on the app, this web user can then be unified with the Android user based on the same user_id. 

If two different devices with the same user_id arrive at a node, they will be deduplicated and count as one user in the node statistics. 

Yes. The user counts are counted based on the number of entries. For example, if a user exited the journey and then re-entered one time, this user is counted 2 times under Entered.

You may find the message metrics count under the Performance tab to be much higher than the metrics count under Moved forward to. 

This is because users might still interact (e.g. opens, clicks) with the messages after being moved to the no-interaction path. This can often happen If you set a short timeout duration.

In the example below, users are moved to the "Not opened" path if they didn't open the email in one hour. But if they open the email while they are still in the journey, the open will be counted in the Performance tab. 

In message nodes, Arrived is the number of users the system has tried to send or show the message to. This is not the number of users who received the message. 

To see the actual sent, views, delivered, and clicks metrics, open the message node and see the Performance tab instead.Updated 8 months ago Table of Contents

Performance and Analytics

What counts as one user in a journey?

Are re-entered users counted again in node stats?



Journey Maps FAQs [1]

https://docs.aiqua.appier.com/docs/journey-faq



Performance and Analytics

What counts as one user in a journey?

Are re-entered users counted again in node stats?

Why is "Opens" under Performance much higher than "Opened" in node stats?

Is "Arrived" the number of users who received the message?



Where is AIQUA's data center located?

https://docs.aiqua.appier.com/docs/where-is-aiquas-data-center-located



AIQUA's data center is located in Singapore.

Updated over 1 year ago



Web SDK Integration Overview

https://docs.aiqua.appier.com/docs/web-sdk-overview



Integrating your website with Appier Web SDK is required if you want to:

Log user data for your website visitors

Send Web Push notifications 

Show In-Web Campaigns to users on your website

Generate and show a list of recommended products on your website

📘Note:Microsoft has announced that Windows 10 will no longer support Internet Explorer 11 after June 2022.

Features provided by Appier Web SDK are not guaranteed to work for users who are using Internet Explorer.

There are four main parts to Web SDK integration. Parts III and IV are for sending Web Push notifications. To begin integration, proceed to Integrating Appier Web SDK.

Part I: Website Info - On AIQUA dashboard, enable Web push notification and In-Web Campaigns.

Part II: Integrate SDK - Add qg-service-worker.js file and snippets of Javascript code to your website.

Part III: Send Notifications - Send a test push notification to yourself.

Part IV: Web Pixel Settings - It is highly recommended to configure the permission prompts that ask users to subscribe to web push using Web Pixel Settings.

👍TipIf your website is a Shopify store, refer to Integrating Shopify Stores with Appier Web SDK.Updated 21 days ago Integrating Appier Web SDKTable of Contents

Integration Overview



Integrating the Appier Web SDK [0]

https://docs.aiqua.appier.com/docs/integrating-with-the-aiqua-web-sdk



👍Alternative integration methods

To integrate the Web SDK using Google Tag Manager, refer to Using Google Tag Manager to Install the Appier Web SDK.

If your website is a Shopify store, refer to Integrating Shopify Stores with Appier Web SDK.

To begin integration, click on your account name in the lower-left corner of the AIQUA dashboard and select Integration > Website.

You will see the four main parts for Web SDK integration. 

Part I: Website Info

Part II: Integrate SDK

Part III: Send Notifications

Part IV: Web Pixel Settings

If your website uses an HTTPS protocol, refer to these steps for integration.

Input your HTTPS website URL.

Tick Enable Web Push if you want to send Web push notifications.

Restrict web push in specific websites only: If you want to restrict web push to specific urls only, select and type the websites you want to allow web push. 

👍TipRestrict web push in specific websites only feature is useful If you have multiple subdomains, but do not want to enable Web push on all subdomains. For more details, see here.

Tick Enable In-Web Notification if you want to show pop-ups inside your website via AIQUA's in-web campaigns, and then click Next.

If you enabled web push in the previous step, install the Appier service worker by adding qg-sw..js file to the website's root directory.

a. Click the Download button next to qg-sw..js.

b. Add this downloaded file to the root directory of your website.

c. To check if you've done so correctly, click the link to see if you can access it.

d. Click the Check button. You should see a success message. 

📘NoteIf your website is built using a third-party service, follow that service's instructions for installing service workers instead.

📘Note

If clicking the Check button produces the error message "qg-sw..js is not available", make sure the downloaded .js file is placed under the website's root directory.



Integrating the Appier Web SDK [1]

https://docs.aiqua.appier.com/docs/integrating-with-the-aiqua-web-sdk



If you prefer to place the qg-sw..js file under another directory, contact Appier Support (ess_support@appier.com).

If you are testing on your staging environment, the "All file checks passed successfully" message may not appear since access to the staging environment is often restricted. In this case, you can ignore the "qg-sw..js is not available" error message and proceed to the next step.

👍TipStep 2 can also be done using Google Tag Manager.

Copy the JavaScript provided under Install General SDK and add it to the or tag of each page on your website that will use the Web SDK.

You should see "SDK is connected" in green.

If you have enabled Web push, open your website in the browser, and you should see a prompt requesting for push permission. Click Allow.

Click Next.

If you have enabled Web push, this page allows you to send a test Web push notification to devices that have allowed push permission prompt.

If needed, adjust the Title, Message, Icon Image, Big Image, Action Buttons of the test notifications.

Click Send. 

📘Note

You can only send test push notifications here when your website has less than 10 subscribers. If you have more than 10 subscribers, you can add yourself to the Test Segment and then create a campaign to test using the Test Your Creative button.

If you didn't receive a Web push, see troubleshooting steps below.

It is highly recommended to customize the permission prompt for Web push. This can help improve the Web push subscription rate, as well as the user experience for your site visitors. See Web Pixel Settings for details.

AIQUA recommends using an HTTPS website for web SDK integration. If you use an HTTP protocol for your website:

Extra steps are needed to enable Web push

Change Your Mind Prompt (CYMP) is not supported

Web Push can only be sent from HTTPS websites. To work around this issue, Web push needs to be sent through an alternative HTTPS domain or subdomain.



Integrating the Appier Web SDK [2]

https://docs.aiqua.appier.com/docs/integrating-with-the-aiqua-web-sdk



When setting Website Info, if you have entered an HTTP website and enabled Web Push, the following settings become available:

I will use AIQUA's Domain - Web push is sent through AIQUA's HTTPS subdomain. Type a subdomain name that represents your company. For example, if you type companyxyz, users will see a notification sent from https://companyxyz.aiqua.io.

I have my own Domain - You can prepare your own HTTPS domain and send Web push through this domain.

If you didn't receive your test Web push, here's how you can troubleshoot:

Make sure you are subscribed to Web push. Go to your website and click the lock or bell icon on the browser to make sure the notification status is set to Allow. 

Wait a few minutes, go to Recent Users on AIQUA dashboard, and look for your user profile.

👍TipYou can find your user profile by searching your userId. Here's how you can find your userId.

If you see permission: granted under "Other Fields" column and "Copy GCMID" under "Push Token" column, send a test Web push to yourself again.

If no Web push is received, check your profile in Recent Users and see if there's an uninstallTime field with a date under "Other Fields".

AIQUA marks a user with uninstallTime when it detects the user's push token as no longer valid. If marked with uninstallTime, continue to the steps below to regenerate a new push token.

Go to your website again, set the notification status to Block, and reload the webpage. This step clears the push token.

Resubscribe to Web push by setting the notification status to Allow on your browser, and reload the webpage. A new push token is generated.

Wait about 5 minutes, and send a test Web push to yourself again.

Updated over 1 year ago Table of Contents

For HTTPS sites

Part I: Website Info

Part II: Integrating the SDK

Part III: Send Notification

Part IV: Web Pixel Settings

For HTTP sites

Enabling web push for HTTP sites

Troubleshooting



Using Google Tag Manager to Install the Appier Web SDK

https://docs.aiqua.appier.com/docs/installing-the-aiqua-web-sdk-using-google-tag-manager



You can install the Appier web SDK in your website’s pages via GTM. Doing this also enables you to check if tags are being fired from your website.

📘Note:Before adding web SDK code via GTM, you need to go to AIQUA Dashboard to complete the following steps:

Enter website information.

Add qg-sw..js file to the website's root directory. See here.

Skip this section if you have already implemented GTM on your website.

Sign in to Google Tag Manager and click Create Account.

Under Add a New Account, input all the needed details and select Web as the location of your container setup.

Click Create.

Go through the Google Tag Manager Terms of Service Agreement, tick the box to agree, then click Yes to proceed.

Follow the onscreen instructions on Install Google Tag Manager and install the GTM code in all of your website pages.

On GTM, go to Workspace to create a custom tag.

Click Tags > New. 

Do the following in the pop-up screen:

a. Click Untitled Tag and rename it.

b. Click the edit icon in Tag Configuration then select Custom HTML.

c. In the HTML body, copy and paste the Appier Web code.

📘Note:Retrieve this code by going to the AIQUA Dashboard > Your account name > Integration > Web. If your website info is already entered, click Next then scroll down to 3. ADD FOLLOWING LINES TO INDEX.HTML.

d. Click the edit icon in Triggering then select All Pages to implement personalization features in your website. This also allows you to set up different rules for firing tags according to your use case.

e. Click Save.

Click Preview and go to your website. The debug mode appears on the bottom of the browser window to let you check if tags are firing properly from your website.

When you’re done checking, click Submit > Publish. 

Updated over 1 year ago Table of Contents

Implementing GTM on Your Website

Adding Appier Web SDK Code via GTM



Integrating Shopify Stores with the Appier Web SDK [0]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



Integrate the Web SDK with your Shopify store to begin leveraging AIQUA features such as collecting user events and attributes, sending campaigns, and displaying product recommendations.

Supported features: View the list of supported AIQUA features.

User data collection: Understand what type of data the Web SDK can collect from your Shopify store.

🚧Integration using checkout.liquidIf you've previously integrated the Web SDK using checkout.liquid, please follow these steps:

Follow the instructions in Shopify’s Checkout Extensibility upgrade guide. 

Proceed directly to Install the purchase tracking code (checkout events) for instructions on replacing the checkout.liquid event tracking code with a custom pixel.

The following table summarizes AIQUA features supported in Shopify stores. Note that the scope of support differs between the sandbox environment for pixels and unsandboxed environments, due to Shopify's sandbox environment limitations.

📘Sandbox environment for pixelsOn August 13, 2024, checkout.liquid will be deprecated for Information, Shipping, and Payment pages, and will be replaced with Checkout Extensibility.After this change, the Information, Shipping, and Payment pages will run in a sandboxed environment, limiting third-party access to page data, including user events, and will require pixels to track event data.

FeatureSupported (unsandboxed environments)Supported (sandboxed environment for pixels)Audience segmentationYesYesCampaign-related features• Regular campaigns: Yes (excluding app push)

• Trigger campaigns: Yes (excluding app push)

• In-Web Campaigns: Yes

• Creative Studio: Yes

• Journey Maps: Yes

• Experiment: YesNoPerformance and analyticsYesNoRecommendationsYesNoDynamic contentYesNo

After installing the general tracking code, the Web SDK automatically collects default events and attributes—no additional code changes are required. In addition, the following custom events and attributes will automatically be collected as well:



Integrating Shopify Stores with the Appier Web SDK [1]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



TypeNameDescriptionAttributeemailThe email address of the user who logged in.AttributephoneNoThe phone number of the user who logged in.Attributefirst_nameThe first name of the user who logged in.Attributelast_nameThe last name of the user who logged in.EventsearchedGenerated when the user searches a keyword on the website.Eventcategory_viewedGenerated when the user views a product category page on the website.Eventproduct_viewedGenerated when the user views a product page on the website.Eventproduct_added_to_cartGenerated when the user adds a product to the shopping cart on the website.

👍TipTo collect custom data not listed in the table above, you can implement your own custom event collection using the Web SDK logging methods in the general tracking code. Refer to the following guides to learn more about logging custom data:

Guidelines for Logging Custom Events and Attributes 

Logging User Attributes for Web 

Logging User Events for Web

Click on your account name in the lower-left corner of the AIQUA dashboard and select Integration > Website.

Enter the URL of your Shopify store and configure the following options.

Check Enable Web Push to enable web push notifications. If you want to restrict web push to specific URLs only, select Restrict web push in specific websites only and enter the websites you want to allow web push notifications for.

Check Enable In-Web Notification if you want to enable AIQUA's in-web campaigns.

Click Next to save your settings.

Log in to Shopify dashboard and copy the ".myshopify.com" URL of your shop.

Share your Shopify URL with Appier Support (ess_support@appier.com), who will provide you with a link where you can install the AIQUA Notify app.

After installing the AIQUA Notify app, contact Appier Support (ess_support@appier.com) to complete the setup process.

Next, install the general tracking code and purchase tracking code:

Installing the general tracking code will begin collection of default data and the specified custom data.



Integrating Shopify Stores with the Appier Web SDK [2]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



Installing the general tracking code will begin collection of default data and the specified custom data.

Installing the purchase tracking code (checkout events) will begin collecting checkout events. 

On Shopify dashboard, go to Online Store > Themes, click the actions button (three horizontal dots) on the theme you want to use, and select Edit code.

In the code editor, select Snippets and click Add a new snippet.

Name the snippet "aiqua-track" and click Done.

Go to aiqua-track.liquid in the menu, and paste the following code:



{% unless appierRtAddToCartSelector %}

{% assign appierRtAddToCartSelector = 'YOUR-ADD-TO-CART-BUTTON-SELECTOR' %}

{% endunless %}









{% if customer %} 



{% endif %}





{% if request.page_type == 'search' %}

{% if search.performed == true %}





Integrating Shopify Stores with the Appier Web SDK [3]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



appier("event", "searched", {

searched_keyword: appierRtSearch

});



{% endif %}

{% endif %}





{% if request.page_type == 'collection' %}



{% endif %}





{% if request.page_type == 'product' %}



{% endif %}











👍Custom dataTo collect other custom events and attributes, you can implement your own custom event collection using the Web SDK logging methods in the general tracking code. Refer to the following guides to learn more about logging custom data:

Guidelines for Logging Custom Events and Attributes 

Logging User Attributes for Web 

Logging User Events for Web



Integrating Shopify Stores with the Appier Web SDK [4]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



Guidelines for Logging Custom Events and Attributes 

Logging User Attributes for Web 

Logging User Events for Web

In aiqua-track.liquid, search for {{ YOUR-ADD-TO-CART-BUTTON-SELECTOR }} and replace it with the class name of the add-to-cart button. Since Shopify offers different kinds of buttons, this step identifies which buttons are the add-to-cart buttons on your Shopify site. To find the button's class name:

Right-click the add-to-cart button and select Inspect or Inspect Elements.

Find the class name of the button, and copy a unique part of the class name.

Replace all instances of {{ YOUR-ADD-TO-CART-BUTTON-SELECTOR }} in the code snippet with the class name you copied.

Click Save.

In the left menu of the code editor, select Layout and click theme.liquid.

Add the following code snippet into the element of theme.liquid, replacing {{ YOUR_APP_ID }} with your AIQUA app ID, then click Save.

{% render 'aiqua-track' , appid: '{{ YOUR_APP_ID }}' %}

Repeat steps 1-8 for each theme you want to use.

The Web SDK uses custom pixels to track events. The following section provides instructions on creating a custom pixel for the checkout event and its associated tracking code.

👍TipTo learn more about managing your custom pixels, see Shopify's custom pixel guide.

On Shopify dashboard, go to Settings, click Customer events in the left menu, then Add custom pixel.

Enter a name for the custom pixel, then click Add pixel.

Next, install code snippets in the Code section to:

Initialize the JavaScript Pixel SDK.

Subscribe to customer events. 

Initialize the pixel SDK. Replace {app_id} with your AIQUA app ID.

// Step 1. Initialize the JavaScript pixel SDK (make sure to exclude HTML)

!(function (q, g, r, a, p, h, js) {

// Initialize Appier SDK only in the checkout process

const isCheckoutProcess = /\/checkouts(?:\/|$)/.test(

window.location.pathname

);

if (!isCheckoutProcess) return;

q.appier = q.qg;

if (q.qg) return;

js = q.appier = q.qg = function () {



Integrating Shopify Stores with the Appier Web SDK [5]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



);

if (!isCheckoutProcess) return;

q.appier = q.qg;

if (q.qg) return;

js = q.appier = q.qg = function () {

js.callmethod ? js.callmethod.call(js, arguments) : js.queue.push(arguments);

};

js.queue = [];

p = g.createElement(r);

p.async = !0;

p.src = a;

h = g.getElementsByTagName(r)[0];

h.parentNode.insertBefore(p, h);

})(window,document,'script','https://cdn.qgr.ph/qgraph.{app_id}.js');

// Helper function for normalizing price format

function fixPriceForAiqua(price) {

let appierRtPrice = price.toString();

const appierRtPriceCommas = appierRtPrice.match(/,/g);

if (

appierRtPriceCommas &&

appierRtPriceCommas.length === 1 &&

/,[0-9]{0,2}$/.test(appierRtPrice)

) {

appierRtPrice = appierRtPrice.replaceAll('.', '').replace(',', '.');

} else {

appierRtPrice = appierRtPrice.replace(',', '');

}

return parseFloat(appierRtPrice);

}

Subscribe to customer events with analytics.subscribe() and add tracking code for the checkout event (checkout_completed). After installing the following code snippet, checkout events and their properties will be logged to AIQUA. 

// Step 2. Subscribe to customer events with analytics.subscribe(), and add tracking

// analytics.subscribe("all_standard_events", event => {

// console.log("Event data ", event?.data);

// });

// checkout_completed

analytics.subscribe('checkout_completed', (event) => {

const checkout = event.data.checkout;

const lineItems = checkout.lineItems;

lineItems.forEach((item) => {

const itemPrice = item.variant.price.amount;

// Log event `product_purchased` to Appier

appier?.('event', 'product_purchased', {

order_id: checkout.order.id,

product_id: item.id,

product_url: `${event.context.document.location.origin}${item.variant.product.url}`,

product_name: item.title,

product_price: fixPriceForAiqua(itemPrice),

quantity: item.quantity,

}, fixPriceForAiqua(itemPrice));

});

const orderPrice = fixPriceForAiqua(event.data.checkout.subtotalPrice.amount);

// Log event `checkout_completed` to Appier

appier?.('event', 'checkout_completed', {



Integrating Shopify Stores with the Appier Web SDK [6]

https://docs.aiqua.appier.com/docs/integrating-shopify-stores-with-appier-web-sdk



// Log event `checkout_completed` to Appier

appier?.('event', 'checkout_completed', {

order_id: event.data.checkout.order.id,

order_price: orderPrice,

},

orderPrice

);

});

Follow the steps below to verify that events and attributes are being collected by the Web SDK.

On the AIQUA dashboard, click your account name in the lower-left corner, and select Recent Activity to see collected user events or select Recent Users to see collected user attributes.

Click the Web tab to see events or attributes collected from your Shopify site.

Updated 8 months ago Table of Contents

Overview

Supported features

User data collection

1. Register your website on the AIQUA dashboard

2. Install AIQUA Notify on Shopify

3. Install the Appier Web SDK

Install the general tracking code

Install the purchase tracking code (checkout events)

4. Verify the integration



Logging User Data for Web

https://docs.aiqua.appier.com/docs/logging-data-on-the-web-sdk



The Appier Web SDK provides a way to send user data to AIQUA, which allows you to segment audience based on that data. For example, you can send relevant images to a user based on the products they viewed on your website.

After web SDK integration, the SDK starts collecting data about your web users. For the list of user data the Web SDK can collect by default, see Default Events and Attributes.

In addition to default user data, you can collect Custom Events and Attributes about your users.

To collect custom user events and attributes, you need to set the website to send user attributes and user events to the web SDK. See below for instructions:

Logging Custom User Attributes

Logging Custom User Events

Updated 10 months ago Table of Contents

Default user data

Custom user data



Logging Custom User Attributes

https://docs.aiqua.appier.com/docs/logging-profile-information-on-the-web-sdk



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

User attributes are pieces of information that describe a user, such as their name, city, or date of birth. Logging user attributes to allow marketers to segment and filter users based on their attributes.

To log custom user attributes using the Appier Web SDK, call appier('identify') as shown in the following code sample, where attributes is the object containing the custom user attributes you're logging:

appier('identify', attributes);

The following code sample demonstrates how to use appier("identify") to log the following custom user attributes:

email

first_name

last_name

const custom_attributes = {

'email': 'appier@example.com',

'first_name': 'Foo',

'last_name': 'Bar'

}

appier('identify', custom_attributes);

Follow the steps below to validate that your website is logging attributes properly.

Open your website and complete the action that logs the attribute.

On the AIQUA Dashboard, click your account name in the lower-left corner and go to Recent Users.

Under the Web tab, you should see the event. It may take several minutes for the logged data to display on the AIQUA Dashboard.

Updated over 1 year ago Logging Event Information on the Web SDKCustom User DataTable of Contents

Overview

Attribute logging example

Checkpoint: Validating that custom attributes are correctly logged



Logging Custom User Events [0]

https://docs.aiqua.appier.com/docs/logging-event-information-on-the-web-sdk



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

User events are actions that users perform on your app, such as viewing a product or completing a checkout. Logging user events allow marketers to create segments by filtering users based on their events.

To log custom events using the Web SDK, call appier('event'):

appier('event', eventName, parameters, valueToSum);

ParameterTypeDescriptioneventNameStringSee the guidelines on field names for custom data for limitations on eventName.parametersObjectOptional.parameters must be a flat JSON object; it can't contain any nested JSON objects or arrays. See the Data Logging Guidelines for more details and limitations.valueToSumNumberOptional. The monetary value associated with this event. Used to calculate conversion value in campaign performance reports.

🚧Logging page_viewed for single-page applicationsIf you website is a single-page application, you'll need to manually log the page_viewed default AIQUA event.

The following example logs the registration_completed event without any additional parameters.

// Log the `registration_completed` event without parameters

appier('event', 'registration_completed');

The following example logs the product_viewed event with the following parameters:

product_name: "Brand A Computer"

category: "electronics"

// Log a `product_viewed` event with the following parameters: `product_name`, `category`

appier('event', 'product_viewed', {'product_id': 'E0238','product_name': 'Brand A Computer', 'category': 'electronics'});

The following example logs the product_purchased event with the following parameters:

product_id: "E0238"

product_name: "Brand A Computer"

category: "electronics"

product_price: 1000.0

In addition, valueToSum is set to 1000.0 (no currency specified).

// Log a `product_viewed` event with the `product_name` and `category` parameters and a `valueToSum` of 1000.0



Logging Custom User Events [1]

https://docs.aiqua.appier.com/docs/logging-event-information-on-the-web-sdk



// Log a `product_viewed` event with the `product_name` and `category` parameters and a `valueToSum` of 1000.0

appier('event', 'product_purchased', {'product_id': 'E0238', 'product_name': 'Brand A Computer', 'category': 'electronics', 'product_price': 1000.0}, 1000.0);

Follow the steps below to validate that your website is logging events properly.

Open your website and complete the action that logs the event.

On the AIQUA Dashboard, click your account name in the lower-left corner and go to Recent Activity.

Click the Web tab. You should see a list of logged events on this page. It may take several minutes for the event to display on the AIQUA Dashboard.

If your website is a single-page application (SPA), you'll need to manually log the default AIQUA event page_viewed. For non-SPA websites, this default event is automatically logged by the Appier SDK.

appier('event', 'page_viewed', { url: window.location.href });

If you've installed Google Tag Manager (GTM) on your website, log a page_viewed event when the browser's history object is updated. Create a GTM tag with the trigger type set to History Change, then use code snippet provided above to log the event.Updated 11 months ago Table of Contents

Overview

Event logging examples

Logging events (event name only)

Logging events with parameters

Logging events with valueToSum

Checkpoint: Validating that events are correctly logged

Logging page_viewed for single-page applications (SPA)

Using Google Tag Manager



Cross-Domain Integration [0]

https://docs.aiqua.appier.com/docs/cross-domain-integration



Refer to the following sections for notes and limitations regarding cross-domain integration with the Appier Web SDK:

Businesses using multiple domains

Websites using multiple subdomains

Event attribution across domains or subdomains

📘NoteUser segmentation can be done across domains or subdomains as long as the user is using the same device and same browser.

In general, if you use multiple domains, for example, "www.abc.com", "www.abc2.com", and "www.abc-blog.com", you should have a separate AIQUA account for each domain. 

If you have multiple domains under one AIQUA account, the following features are affected:

Filtering audience based on events within 24 hours does not work across multiple domains. See here for more details.

A user's subscription to push notifications does not carry across domains.

As a result, users who have already allowed or blocked notifications will see the system prompt again when they visit a different domain. If the user allows or blocks notifications in the second system prompt, the user's latest push subscription status will be applied.

If your website has multiple subdomains, for example, "shop.abc.com", "m.shop.abc.com", and "blog.abc.com", the following features are affected:

In-web campaigns: Events within 24 hours

Web push subscriptions

Filtering audience based on events within 24 hours does not work across multiple subdomains. See here for more details.

Under default settings, a user's push subscription also does not carry across subdomains, but you can follow the steps below to avoid having users opt-in for each subdomain. 

Scenario 1

Let's say you have multiple subdomains, but only want to enable web push on one subdomain "shop.abc.com". Simply restrict web push to that subdomain only.

On AIQUA dashboard, click on your account name in the lower-left corner and select Integration > Website. 

Under Enable Web Push, select Restrict web push in specific websites only, and type "shop.abc.com".



Cross-Domain Integration [1]

https://docs.aiqua.appier.com/docs/cross-domain-integration



Under Enable Web Push, select Restrict web push in specific websites only, and type "shop.abc.com". 

In this example, web push will be enabled on "shop.abc.com" but not on subdomains that are not listed here, such as "m.shop.abc.com" or "job.abc.com".

Scenario 2

Let's say there are three subdomains, and you want to enable web push on two of them: "shop.abc.com" and "blog.abc.com". 

Contact Appier Support (ess_support@appier.com) to enable cross-domain SDK functionality for the following domains: "shop.abc.com" and "blog.abc.com". 

Make sure Appier Web SDK is integrated on "shop.abc.com" and "blog.abc.com".

Because there is a third subdomain that doesn't need web push, you need to restrict web push to "shop.abc.com" and "blog.abc.com" only on AIQUA dashboard. Refer to instructions listed for scenario 1.

Under default settings, events that happened on a different domain are not attributed to the campaign. This means that if the user receives an AIQUA notification on domain A and completes an event on domain B, the event will not be properly attributed to the AIQUA notification in the performance report. A common scenario is when the main website has a different domain from the checkout pages because the payment flow is on a separate site. 

If you want to track event attribution across domains, you can use one of the methods below. Note that both domains have to be integrated with the same Appier Web SDK.

Method 1

You can call the navigateWithAttributions method in any element which will navigate to the next domain. Using this method, we'll automatically append attribution data in the target URL and navigate to that page.



Navigate



Method 2

Alternatively, you can retrieve attribution data directly by calling Appier Web SDK's getAttributions method. The returned attribution data can then be appended to the next domain's URL as a list of query parameters, as demonstrated in the following example:



Cross-Domain Integration [2]

https://docs.aiqua.appier.com/docs/cross-domain-integration





Navigate

<https://www.NEXT-DOMAIN.com>



Updated over 1 year ago Table of Contents

Overview

Multiple domains

In-web campaigns: Events within 24 hours

Web push subscription

Multiple subdomains

In-web campaigns: Events within 24 hours

Web push subscriptions

Event attribution across domains and subdomains



Android SDK Overview [0]

https://docs.aiqua.appier.com/docs/android-sdk-overview



Integrate your app with Appier Android SDK to take advantage of features such as sending push notifications, logging custom user data, and delivering in-app campaigns. This page summarizes the setup steps required to begin using the Android SDK and all the features the SDK supports.

We recommend using the latest Android SDK for continual updates and feature support. See the Android SDK release notes for details about the latest releases.

Latest Appier Android SDK versionSupported Android versions8.2.4Android 5.0 or later (API level 21).Recommendation 2.0 requires Android 7.1.1 or later.

VersionsNotesv7.20.0 to v7.24.2Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ',", \n, or any HTML tags (such as 

).v7.15.0 to v7.18.0This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using this combination of incompatible versions breaks core SDK features, e.g. data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.v7.15.0 to v7.17.1Using event parameters in trigger conditions for in-app pop-up campaigns caused app crashes. If your campaigns use event parameters in trigger conditions, please use version 7.17.2 or later.v7.11.0 to v7.17.3Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.v7.8.0 or earlierTapping in-app campaign deep links would occasionally cause the app to crash. To avoid this issue, please use version 7.8.1 or later.v7.7.0 or earlierNotifications on apps targeting Android 12 (targetSdkVersion: 31) may not function properly. To avoid issues with notification behavior, please choose one of the following solutions:

• Upgrade your Appier Android SDK to version 7.8.0 or later.



Android SDK Overview [1]

https://docs.aiqua.appier.com/docs/android-sdk-overview



• Upgrade your Appier Android SDK to version 7.8.0 or later.

• Use targetSdkVersion: 30 instead.v7.3.0 or earlierApps on devices running Android 11 or later which also target API level 30 or later may experience unexpected crashes if the READ_PHONE_STATE permission isn't granted. To avoid this issue, please upgrade your app to use Android SDK 7.3.1 or later.v6.10.0 or earlierIf you're upgrading from this SDK version, update your build.gradle file to use com.appier:appier-android instead of com.quantumgraph.sdk:QG.

Before integrating your app with the Android SDK, complete the following:

Prepare your Appier app ID. Find your app ID on the AIQUA dashboard under the Account Settings page.

Prepare your app's Google Play Store URL.

Add Firebase to your Android project. This step is required even if your app doesn't use push notifications.

If you're using your own Firebase Cloud Messaging (FCM) credentials, prepare your FCM API Key and Sender ID.

Complete the required setup before using the Android SDK. Once the required setup is complete, the Android SDK will begin logging default user events and attributes and you'll be able to start using all of the SDK's features.

📘If you encounter dependency conflicts during the SDK installation process, check if your issue is addressed in the dependency troubleshooting notes.

After completing the required setup, you can begin using all the features supported by the Android SDK.

Updated 7 months ago Table of Contents

Overview

Latest Android SDK version

Version notes

Integration overview

Prerequisites

Required setup

Supported features



Development Android SDK Versions [0]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes



Added logic to map incorrectly regenerated Appier IDs to their original correct IDs, enabling data recovery efforts initiated due to the known issue present in versions 8.2.0, 8.2.1, and 8.2.2.

The Appier ID (userId) is no longer incorrectly regenerated on the first app launch (either in the foreground or background). This issue is present in versions 8.2.0, 8.2.1, 8.2.2.

The following configuration APIs weren't successfully applied if they were called before the SDK finished initializating in SDK versions 8.0.0 to 8.2.1:

QG.addJavaScriptInterface

QG.enablePushNotificationStorage

QG.setMaxNumStoredNotifications

QG.updateInboxRecordLimit

QG.setDataTrackingConfig

Campaign creative changes for active in-app campaigns weren't applied after reopening the app from the background.

The Appier ID (userId) is incorrectly regenerated on the first app launch (either in the foreground or background) after upgrading to this SDK version. These regenerated Appier IDs were treated as new users, impacting related metrics and segments.

Apps unexpectedly crashed when users clicked on non-hierarchical URLs, such as mailto:[user@example.com]or tel:+123456789.

The Appier ID (userId) is incorrectly regenerated on the first app launch (either in the foreground or background) after upgrading to this SDK version. These regenerated Appier IDs were treated as new users, impacting related metrics and segments.

Optimized data transmission process to the server.

Improved campaign stability to ensure that custom HTML campaigns remain active and uninterrupted when the campaign is expanded or collapsed, or when switching app pages.

The exit push notification was incorrectly sent again after the first exit push and the subsequent 10 push campaigns. Affected versions: v8.0.0 and later.

In-app campaigns failed to display when the system time was changed.



Development Android SDK Versions [1]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes



In-app campaigns failed to display when the system time was changed.

The Appier ID (userId) is incorrectly regenerated on the first app launch (either in the foreground or background) after upgrading to this SDK version. These regenerated Appier IDs were treated as new users, impacting related metrics and segments.

Added app ID validation for app web views. If your app and website use different app IDs, contact Appier Support (ess_support@appier.com ) to modify the SDK's app ID allowlist to ensure web data is logged to the correct app ID.

Extracted the geofencing feature as a standalone library. For details about this beta feature, contact your customer success manager.

Removed the following SDK dependencies:

com.google.android.gms:play-services-location:21.3.0

org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.4.1

com.google.firebase:firebase-iid:20.0.1

The model_id parameter's data type (included in recommendation_clicked events) is now sent as a string. If you're logging this event, you'll need to modify your implementation. Please refer to Android SDK: Recommendation 2.0 for details.

qg_inapp_toggled events are now correctly logged in the following scenarios: 

Closing a HTML in-app campaign.

Clicking the action button of an in-app campaign with Persist until the notification is clicked is enabled.

Apps no longer experience occasional crashes due to an improperly configured google-service.json or using an incorrect sender ID.

In-app campaign floating icons no longer flicker due to unexpected rendering behavior.

Support for Retail Media Network features (beta). To learn more, contact your customer success manager.

Support for AiDeal features (beta). To learn more, contact your customer success manager.

Banner creatives are now fully expandable, displaying the title, message, and banner image simultaneously.

Updated to several SDK dependencies.

Upgraded the firebase-messaging dependency from version 20.0.1 to 23.0.0.

Removed the deprecated firebase-iid dependency.

Updated 15 days ago Table of Contents



Development Android SDK Versions [2]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes



Removed the deprecated firebase-iid dependency.

Updated 15 days ago Table of Contents

v8.2.4 - March 12, 2025

v8.2.3 - March 11, 2025

v8.2.2 - February 24, 2025 (Deprecated)

v8.2.1 - February 7, 2025 (Deprecated)

v8.2.0 - January 17, 2025 (Deprecated)

v8.1.0 - December 20, 2024

v8.0.1 - November 15, 2024

v8.0.0 - October 31, 2024



Troubleshooting Dependency Issues [0]

https://docs.aiqua.appier.com/docs/resolving-dependency-conflicts



The Appier Android SDK has the following dependencies:

implementation 'androidx.appcompat:appcompat:1.4.2'

implementation "androidx.recyclerview:recyclerview:1.2.1"

implementation 'androidx.lifecycle:lifecycle-livedata-core:2.3.1'

implementation "com.android.installreferrer:installreferrer:2.2"

implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1'

implementation 'com.google.firebase:firebase-messaging:23.0.0'

implementation('io.socket:socket.io-client:1.0.2') {

// excluding org.json which is provided by Android

exclude group: 'org.json', module: 'json'

}

implementation 'org.jetbrains.kotlin:kotlin-stdlib:1.8.22'

implementation "org.jetbrains.kotlin:kotlin-reflect:1.8.22'

implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.5.0'

implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.0'

If your app uses Android SDK 5.9.5 or earlier, you must use Glide version 4.9.0 or later.

To resolve conflicts with your app's dependencies, the Appier SDK's dependencies can be explicitly excluded in your build.gradle file.

🚧Only exclude libraries that cause dependency conflicts with your app.

For example, if the version of firebase-messaging used by the Appier SDK is causing a dependency conflict, update your project's build.gradle file to exclude this dependency from the Appier SDK and specify a different version instead:

implementation('com.appier:appier-android:8.2.4') {

exclude group: 'com.google.firebase'

}

// your libraries & dependencies

implementation 'com.google.firebase:firebase-messaging:'

Appier SDK versions 5.10.0 and earlier indirectly use com.squareup.okhttp through the com.github.nkzawa:socket.io-client dependency. Exclude com.squareup.okhttp in your project's build.gradle if it causes a dependency conflict:

implementation('com.quantumgraph.sdk:QG:5.10.0') {

exclude group: 'com.squareup.okhttp'

}



Troubleshooting Dependency Issues [1]

https://docs.aiqua.appier.com/docs/resolving-dependency-conflicts



implementation('com.quantumgraph.sdk:QG:5.10.0') {

exclude group: 'com.squareup.okhttp'

}

If you receive a ClassNotFoundException while building your project, check the following, ensure that you've included Maven properly in project/build.gradle.

allprojects {

repositories {

google()

mavenCentral()

jcenter() // sunset on 2022/02/01

}

}

If you get a DuplicatePlatformClasses error while building your project, refer to Gradle's guide on viewing and debugging dependencies to resolve the version conflict.

The following error means your project is missing the runtime dependency of com.google.firebase:firebase-iid:

java.lang.NoClassDefFoundError: Failed resolution of: Lcom/google/firebase/iid/FirebaseInstanceId;

To resolve this error, explicitly declare the com.google.firebase:firebase-iid dependency in your project's build.gradle:

com.google.firebase:firebase-iid:20.0.1

Updated 4 months ago Table of Contents

Appier Android SDK dependencies

Apps using Glide

Resolving dependency conflicts

Conflicts with com.squareup.okhttp

Common errors and exceptions

ClassNotFoundException

DuplicatePlatformClasses

NoClassDefFoundError



Required Setup

https://docs.aiqua.appier.com/docs/using-the-android-sdk



Complete the required setup before using the Appier Android SDK. Once the required setup is complete, the SDK will begin logging default user events and attributes and you'll be able to start using all of the SDK's features.

StepDescription1. Registering Your App with AIQUAConfigure app information, such as your app's Google Play Store URL and FCM details, on the AIQUA Dashboard.2. Installing the Android SDKInstall the Android SDK in Android Studio.3. Initializing the Android SDKInitialize the Android SDK in the onCreate() method of your app's main activity.Updated over 1 year ago



Registering Your App with AIQUA [0]

https://docs.aiqua.appier.com/docs/entering-app-info-on-aiqua-dashboard



Prepare your Google Play Store URL in the proper format. Remove the language setting (the hl query parameter) from the URL before entering it on the AIQUA dashboard.

Original URLFormatted URLhttps://play.google.com/store/apps/details?id=com.appier.aiqua.app&hl=tw_zhAfter removing the hl query parameter (&hl=tw_zh):https://play.google.com/store/apps/details?id=com.appier.aiqua.app

If you'd like to use your own service account private key or FCM key to register your app instead of AIQUA's default push credentials, follow the instructions below to create the credentials:

Service account private key

FCM key (Please note that the use of FCM keys will be retired in June 2024, and service account private keys will be required instead.)

👍AIQUA's default credentialsIf you want to use AIQUA's default push credentials, no additional setup is needed, and you can continue with registering your app on the AIQUA dashboard.

If you'd like to use your own service account private key rather than using the private key provided by AIQUA, complete the following steps before registering your app on the AIQUA dashboard.

Go to the Firebase console and select a project or create a new project. Create a service account if you don't have one already.

Go to the Project settings page and click the Cloud Messaging tab.

If Firebase Cloud Messaging API (V1) isn't enabled for your project, enable it by clicking Manage API in Google Cloud Console, then clicking Enable.

Generate your service account private key. From the Project settings page, go to the Service accounts tab. Click Generate new private key, then in the modal that appears, click Generate key to begin downloading your private key.

🚧NoteSave your private key in a secure location—this key can't be recovered if it's lost.

Your private key will be downloaded as a JSON file. Save this file and upload it when registering your app on the AIQUA dashboard.



Registering Your App with AIQUA [1]

https://docs.aiqua.appier.com/docs/entering-app-info-on-aiqua-dashboard



🚧FCM keys retiringPlease note that the use of FCM keys will be retired in June 2024, and service account private keys will be required instead.

If you have your own Firebase Cloud Messaging (FCM) key, have your FCM server key and FCM sender ID ready to upload to the AIQUA Dashboard.

Log in to the Firebase Console.

Go to the Project settings page and click the Cloud Messaging tab.

Enable Cloud Messaging API (Legacy). Click the three-dot vertical menu, click Manage API in Google Cloud Console, and on the Google Cloud Console, click Enable.

Once you've enabled the Cloud Messaging API, your FCM server key and sender ID will be visible under Cloud Messaging API (Legacy):

On the AIQUA dashboard, click on your account name in the lower-left corner of the screen, click Integration, then select Android.

On the Android integration page, enter your app's Google Play Store URL without the language settings (the hl query parameter).

Select I use FCM in my app. GCM has been deprecated by Google.

Under Key Type, select one of the following options:

I will use AIQUA's FCM Key: If you'd like to use AIQUA's FCM key, select this option.

I have my own key:

If you have your own FCM key, select this option and enter your FCM Key and Sender ID.

If you have your own service account private key, upload the JSON key by going to Service Account Private Key and clicking Upload key.

🚧FCM keys retiringPlease note that the use of FCM keys will be retired in June 2024. If you'd like to continue using your own push credentials, service account private keys will be required instead.

To enable heads-up notifications by default for all new campaigns, select Enable heads-up notifications.

👍TipIf you don't want to enable heads-up notifications by default, you can manually enable heads-up notifications for specific campaigns instead.

Click Next to finish registering your app with AIQUA. 

After you've finished registering your app, use Android Studio to install the Appier Android SDK.



Registering Your App with AIQUA [2]

https://docs.aiqua.appier.com/docs/entering-app-info-on-aiqua-dashboard



After you've finished registering your app, use Android Studio to install the Appier Android SDK.

📘NoteHeads-up notifications are only supported for apps using Android SDK 5.6.1 or later.

Heads-up notifications (HUNs) are notifications that briefly appears as a floating window on unlocked Android devices running Android 5.0 (Lollipop) or later. You can use HUNs with the following AIQUA features:

Regular campaigns

Trigger campaigns

Edit the regular campaign you want to enable HUNs for, and under the creative's Advanced Settings, select Enable heads-up notification.

Edit the trigger campaign you want to enable the HUNs for, and under the Advanced section, select Heads-up message style.

Updated 7 months ago Table of Contents

Prerequisites

Prepare your Google Play Store URL

Using your own key

Registering your app on the AIQUA dashboard

Heads-up notifications

Enabling heads-up notifications for specific campaigns



Installing the Android SDK [0]

https://docs.aiqua.appier.com/docs/installing-in-android-studio



After you've registered your app on the AIQUA Dashboard, install the Appier Android SDK.

📘SDK versions earlier than 7.0.0Starting from version 7.0.0, the Appier Android SDK is distributed on mavenCentral() instead of jcenter().If you're upgrading from an earlier version, make sure mavenCentral() is added to repositories in the project-level build.gradle.

allprojects {

repositories {

...

mavenCentral()

...

}

}

Or in the app module (app/build.gradle):

repositories {

...

mavenCentral()

...

}

If your app uses Java 7 or below, add the following to your app/build.gradle to specify the Java version.

android {

compileOptions {

sourceCompatibility JavaVersion.VERSION_1_8

targetCompatibility JavaVersion.VERSION_1_8

}

}

Add the Appier SDK and Firebase Core and Messaging Services (firebase-iid) to app/build.gradle.

// Appier SDK

implementation 'com.appier:appier-android:8.2.4'

// Add other necessary dependencies

// Firebase

implementation 'com.google.firebase:firebase-iid:17.0.4'

Apps using firebase-bom 8.0.0+ or firebase-messaging 22.0.0+： If you're using Appier Android SDK 7.1.0 or earlier, you need to declare com.google.firebase:firebase-iid:17.0.4 in your build.gradle file. 

Apps using com.quantumgraph.sdk:QG: When upgrading from Android SDK 6.10.0 or earlier, change the package name from com.quantumgraph.sdk:QG to com.appier:appier-android.

👍TipIf you encounter dependency conflicts, check the dependency troubleshooting notes to see if your issue is addressed.

Add the following ProGuard rules to app/proguard-rules.pro:

-keep class com.appier.** { *; }

-keep class com.quantumgraph.** { *; }

-keep class androidx.core.app.Aiqua* { *; }

Adding these ProGuard rules is mandatory for apps enabling shrinking, obfuscation, and optimization. These rules won't have any affect on apps that don't enable shrinking, obfuscation, and optimization.



Installing the Android SDK [1]

https://docs.aiqua.appier.com/docs/installing-in-android-studio



❗️Incompatible Android Gradle Plugin (AGP) versionsAppier Android SDK versions 7.15.0 to 7.18.0 are incompatible with AGP versions 7.0.0 to 7.0.4.Using this combination of incompatible versions breaks core Android SDK features, such as data logging and in-app campaigns, and you may encounter app crashes. To prevent these issues, please upgrade the Appier SDK or AGP to a later version to support compatibility.

First, follow the steps provided in the Android developer's guide to implement runtime permission checking. 

Next, update your app's manifest file to specify which permissions your app will request:

Request the notification permission (apps targeting API level 33+)

(Optional) Request location and network permissions

(Optional) Remove the advertising ID permissions (apps targeting API level 33+)

🚧ImportantThe notification permission is required for apps targeting API level 33+ (for devices running Android 13 or later).

Add the POST_NOTIFICATIONS permission to AndroidManifest.xml as shown below. You must implement runtime permission checking, then include the POST_NOTIFICATIONS permission in your app’s AndroidManifest.xml for Android devices running Android 13 or later to receive push notifications. 



To access device location data, add one of the following permissions to AndroidManifest.xml:

ACCESS_COARSE_LOCATION: Uses network for location tracking

ACCESS_FINE_LOCATION: Uses network and GPS for location tracking







To access the device's network type (e.g. 2G, 3G, 4G), add the READ_PHONE_STATE permission to AndroidManifest.xml.



📘The advertising ID permission (AD_ID) is only available for apps targeting Android 13 (API level 33) or higher.



Installing the Android SDK [2]

https://docs.aiqua.appier.com/docs/installing-in-android-studio



📘The advertising ID permission (AD_ID) is only available for apps targeting Android 13 (API level 33) or higher.

By default, the Android SDK declares the Google Play services permission which allows access to the advertising ID for apps targeting Android 13 (API level 33) or higher. If your app doesn't need to access the advertising ID, remove the AD_ID permission by adding the following line in AndroidManifest.xml:

tools:node="remove"/>

Starting from version 7.22.0, the Android SDK declares RECEIVE_BOOT_COMPLETED permission by default to support geofencing. If your app isn't using geofencing and doesn't require this permission, you can remove it by adding the following line in AndroidManifest.xml:



Updated over 1 year ago Table of Contents

1. Declare the mavenCentral() repository

2. Specify Java 8 in app/build.gradle

3. Add dependencies to app/build.gradle

4. Add ProGuard rules to app/proguard-rules.pro

5. Update AndroidManifest.xml permissions

Request the notification permission (for apps targeting API level 33+)

(Optional) Request location and network permissions

(Optional) Remove the advertising ID permission

(Optional) Remove the RECEIVE_BOOT_COMPLETED permission



Initializing the Android SDK

https://docs.aiqua.appier.com/docs/initializing-the-android-sdk



After installing Appier Android SDK in Android Studio, import and initialize the SDK.

Prepare your Appier app ID. You can find your app ID on the AIQUA Dashboard by clicking on your account name in the lower-left corner and going to the Account Settings page.

(Optional) If you're using your own Firebase Cloud Messaging (FCM) key, prepare your FCM sender ID. Find your FCM sender ID in the FCM console under the Cloud Messaging tab of the project settings page.

In all the classes using the Android SDK, include the following import:

import com.quantumgraph.sdk.QG;

import com.quantumgraph.sdk.QG

📘User data permissionsBy default, the Android SDK automatically collects the device's AAID upon initialization.If your app requires limitations on user data collection for data privacy regulation compliance, see Android User Data Permissions to learn how to configure data collection settings before initializing the SDK.

In the onCreate() method of your app's main activity, call QG.initializeSDK().

If you're using AIQUA's FCM key, pass your app ID into QG.initializeSDK():

QG.initializeSdk(getApplication(), );

QG.initializeSdk(application, )

If you're using your own FCM key, pass your FCM sender ID and app ID into the method call:

QG.initializeSdk(getApplication(), , );

QG.initializeSdk(application, , )

🚧ImportantWhen calling QG.initializeSdk(), the first parameter must be an Application instance, not a Context instance.Updated 7 months ago Table of Contents

Prerequisites

1. Import the Appier SDK into your activity

2. Initialize the SDK



Android User Data Permission Controls [0]

https://docs.aiqua.appier.com/docs/android-user-data-permissions



📘Required SDK versionUser data permissions controls are only available on Android SDK 7.23.0 or later.

To allow your app to comply with data privacy policies and regulations, the Appier Android SDK allows you to manage user data permissions for the following types of data:

Google Advertising ID (AAID): Collection is enabled by default.

Location data: Collection is disabled by default.

You can enable or disable collection for this data at any point in your app's lifecycle, even before the Appier SDK is initialized, and the changes will be effective immediately. For example, you may want to update user data collection settings in the following scenarios:

After the app is launched

After a user has responded to a data collection consent prompt

After regenerating the user's Appier ID

After a user logs in or logs out of their account

val collectAaid = QG.getInstance(context).dataTrackingConfig.collectAaid

boolean collectAaid = QG.getInstance(context).dataTrackingConfig.getCollectAaid();

AAID collection is enabled by default. To disable AAID collection, set collectAaid to false.

QG.getInstance(context).dataTrackingConfig.collectAaid = false

QG.getInstance(context).dataTrackingConfig.setCollectAaid(false);

📘NoteBy default, the Appier SDK automatically collects the device's AAID upon initialization. If you want to avoid this scenario, we strongly recommend disabling AAID collection before initializing the Appier SDK.

Location data collection is disabled by default. To enable location data collection, set collectLocation to true.

QG.getInstance(context).dataTrackingConfig.collectLocation = true

QG.getInstance(context).getDataTrackingConfig().setCollectLocation(true);

The following sample demonstrates how to configure data collection settings for multiple data types simultaneously:

val trackingConfig = DataTrackingConfig(collectLocation = false, collectAaid = false)

trackingConfig.collectAaid = true // The settings won't be applied since they're not assigned to QG.



Android User Data Permission Controls [1]

https://docs.aiqua.appier.com/docs/android-user-data-permissions



trackingConfig.collectAaid = true // The settings won't be applied since they're not assigned to QG.

QG.getInstance(context).dataTrackingConfig = trackingConfig // The settings takes effect.

DataTrackingConfig trackingConfig = new DataTrackingConfig(false, false);

trackingConfig.setCollectAaid(true); // The settings won't be applied since they're not assigned to QG.

QG.getInstance(context).setDataTrackingConfig(trackingConfig); // The settings takes effect.

Updated over 1 year ago Table of Contents

Overview

AAID

Retrieving the current user data collection settings

Disabling AAID collection

Location data

Enabling location data collection

Sample data collection configuration



Logging Custom User Data for Android

https://docs.aiqua.appier.com/docs/event-tracking-and-attribution-for-android



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

Custom user data consists of free-form attributes and events that you can define depending on your business needs. Custom data isn't collected by the Appier SDK by default; instead, these custom events and attributes must be manually logged using the SDK logging methods as described in the following pages:

Logging Custom User Attributes for Android 

Logging Custom User Events for Android 

To understand how campaign events are attributed under default settings, and how to adjust the default attribution window, see the Event Attribution for Android.Updated over 1 year ago Android User Data Permission ControlsLogging Custom User AttributesTable of Contents

Overview

Event attribution



Logging Custom User Attributes [0]

https://docs.aiqua.appier.com/docs/logging-user-profiles-for-the-android-sdk



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

User attributes are pieces of information that describe a user, such as their name, city of residence, or date of birth. Logging user attributes allows marketers to segment and filter users based on their attributes.

The Android SDK provides the following built-in methods for logging user attributes:

public void setUserId(String userId)

public void setName(String name)

public void setFirstName(String firstName)

public void setLastName(String lastName)

public void setCity(String city)

public void setEmail(String email)

public void setDayOfBirth(int day)

public void setMonthOfBirth(int month)

public void setYearOfBirth(int year)

public void setPhoneNumber(String phoneNo)

// Methods for logging UTM data

public void setUtmSource(String utmSource)

public void setUtmMedium(String utmMedium)

public void setUtmTerm(String utmTerm)

public void setUtmContent(String utmContent)

public void setUtmCampaign(String utmCampaign)

fun setUserId(userId: String?)

fun setName(name: String?)

fun setFirstName(firstName: String?)

fun setLastName(lastName: String?)

fun setCity(city: String?)

fun setEmail(email: String?)

fun setDayOfBirth(day: Int)

fun setMonthOfBirth(month: Int)

fun setYearOfBirth(year: Int)

fun setPhoneNumber(phoneNo: String?)

// Methods for logging UTM data

fun setUtmSource(utmSource: String?)

fun setUtmMedium(utmMedium: String?)

fun setUtmTerm(utmTerm: String?)

fun setUtmContent(utmContent: String?)

fun setUtmCampaign(utmCampaign: String?)

Use the method corresponding to the attribute you want to log. For example, to log the user's email attribute, call setEmail():

// Sets the user's `email` attribute to "email@example.com"

QG qg = QG.getInstance(getApplicationContext());

qg.setEmail("email@example.com");

// Sets the user's `email` attribute to "email@example.com"

val qg = QG.getInstance(applicationContext)

qg.setEmail("email@example.com")

📘NoteSetting an attribute to null may result in unexpected segmentation behavior.



Logging Custom User Attributes [1]

https://docs.aiqua.appier.com/docs/logging-user-profiles-for-the-android-sdk



qg.setEmail("email@example.com")

📘NoteSetting an attribute to null may result in unexpected segmentation behavior.

To clear the value of a user attribute with a built-in method that accepts a string, log null.

You can't clear the values of user attributes using built-in methods that accept integer values.

// Resets the user's `name` attribute by logging an empty string

QG qg = QG.getInstance(getApplicationContext());

qg.setName(null);

// Resets the user's `name` attribute by logging an empty string

val qg = QG.getInstance(applicationContext)

qg.setName(null)

In addition using the built-in methods, you can also specify which user attributes to log by using setCustomUserParameter() and specifying a custom key, where key is the user attribute you want to log:

public void setCustomUserParameter(String key, E value)

fun setCustomUserParameter(key: String, value: E?)

In the following example, setCustomUserParameter() is used to set the user's current rating:

// Sets the value of the `rating` attribute to 5

QG qg = QG.getInstance(getApplicationContext());

qg.setCustomUserParameter("rating", 5);

// Sets the value of the `rating` attribute to 5

val qg = QG.getInstance(applicationContext)

qg.setCustomUserParameter("rating", 5)

📘NoteSetting an attribute to null may result in unexpected segmentation behavior.

To clear the value of a user attribute with setCustomKey(), log a null value.

// Clears the user's `rating` attribute by logging a null value

QG qg = QG.getInstance(getApplicationContext());

qg.setCustomUserParameter("rating", null);

// Clears the user's `rating` attribute by logging a null value

val qg = QG.getInstance(applicationContext)

qg.setCustomUserParameter("rating", null)

Follow the steps below to validate that attributes are being logged properly.

Launch your app and complete the action that logs the user attribute.

On the AIQUA dashboard, click your account name in the lower-left corner and go to Recent Users.



Logging Custom User Attributes [2]

https://docs.aiqua.appier.com/docs/logging-user-profiles-for-the-android-sdk



On the AIQUA dashboard, click your account name in the lower-left corner and go to Recent Users.

Under the Android tab, you should be able to see the logged user attribute(s). It can take several minutes for the attribute to show on the AIQUA Dashboard.

Updated over 1 year ago Table of Contents

Using built-in methods

Example: Built-in method

Clearing attributes using built-in methods

Using custom keys

Example: Custom keys

Clearing attributes using setCustomUserParameter()

Checkpoint: Validating that events are properly logged



Logging Custom User Events [0]

https://docs.aiqua.appier.com/docs/logging-user-events-for-the-android-sdk



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

User events are actions that users perform on your app, such as viewing a product or completing a checkout. Logging user events allow marketers to create segments by filtering users based on their events.

The Android SDK provides the following overloaded logEvent() methods, which allow you to log custom events and event parameters associated with that event:

public void logEvent(String eventName)

public void logEvent(String eventName, JSONObject parameters)

public void logEvent(String eventName, JSONObject parameters, double valueToSum)

public void logEvent(String eventName, JSONObject parameters, double valueToSum, String valueToSumCurrency)

fun logEvent(eventName: String)

fun logEvent(eventName: String, parameters: JSONObject?)

fun logEvent(eventName: String, parameters: JSONObject?, valueToSum: Double?)

fun logEvent(eventName: String, parameters: JSONObject?, valueToSum: Double?, valueToSumCurrency: String?)

ParameterDescriptioneventNameRequired. See the guidelines on field names for custom data for limitations on eventName.parametersOptional. parameters must be a flat JSON object; it can't contain any nested JSON objects or arrays. See the Data Logging Guidelines for more details and limitations.valueToSum and valueToSumCurrencyOptional. The monetary value associated with this event. See valueToSum and valueToSumCurrency

Include valueToSum when logging an event to track the monetary value associated with the event (e.g. the total conversion value associated with a checkout_completed event), and log valueToSumCurrency to specify an ISO 4217 currency code.

👍If the event is attributed to a campaign, valueToSum will be included in the total attributed value of the campaign's performance report.

See the following sections for examples on how to include valueToSum and valueToSumCurrency when logging custom events:

Logging events with parameters, valueToSum

Logging events with parameters, valueToSum and valueToSumCurrency



Logging Custom User Events [1]

https://docs.aiqua.appier.com/docs/logging-user-events-for-the-android-sdk



Logging events with parameters, valueToSum

Logging events with parameters, valueToSum and valueToSumCurrency

The following example logs the registration_completed event without any additional parameters.

// Log the `registration_completed` event without parameters

QG.getInstance(context).logEvent("registration_completed");

// Log the `registration_completed` event without parameters

QG.getInstance(context).logEvent("registration_completed")

The following example logs the product_viewed event with the following parameters:

product_name: "Brand A Camera"

category: "electronics"

// Log a `product_viewed` event with the following parameters: `product_name`, `category`

try {

JSONObject productDetails = new JSONObject();

productDetails.put("product_id", "E0238");

productDetails.put("product_name", "Brand A Camera");

productDetails.put("category", "electronics");

QG.getInstance(context).logEvent("product_viewed", productDetails);

} catch (JSONException e) {

// Handle the exception

}

// Log a `product_viewed` event with the following parameters: `product_name`, `category`

try {

val productDetails = JSONObject()

productDetails.put("product_id", "E0238") 

productDetails.put("product_name", "Brand A Camera")

productDetails.put("category", "electronics")

QG.getInstance(context).logEvent("product_viewed", productDetails)

} catch (e: JSONException) {

// Handle the exception

}

The following example logs the checkout_completed event with the following parameters:

product_name: "Brand A Camera"

category: "electronics"

In addition, valueToSum is set to 1000 (no currency specified).

// Log a `checkout_completed` event with the `product_name` and `category` parameters and a `valueToSum` of 1000.0

try {

JSONObject productDetails = new JSONObject();

productDetails.put("product_id", "E0238");

productDetails.put("product_name", "Brand A Camera");

productDetails.put("category", "electronics");

QG.getInstance(context).logEvent("checkout_completed", productDetails, 1000.0);

} catch (JSONException e) {



Logging Custom User Events [2]

https://docs.aiqua.appier.com/docs/logging-user-events-for-the-android-sdk



QG.getInstance(context).logEvent("checkout_completed", productDetails, 1000.0);

} catch (JSONException e) {

// Handle the exception

}

// Log a `checkout_completed` event with the `product_name` and `category` parameters and a `valueToSum` of 1000.0

try {

val productDetails = JSONObject()

productDetails.put("product_id", "E0238") 

productDetails.put("product_name", "Brand A Camera")

productDetails.put("category", "electronics")

QG.getInstance(context).logEvent("checkout_completed", productDetails, 1000.0)

} catch (e: JSONException) {

// Handle the exception

}

The following example logs the checkout_completed event with the following parameters:

product_name: "Brand A Camera"

category: "electronics"

In addition valueToSum is set to 1000.0 and valueToSumCurrency is set to "USD", meaning that the monetary value associated with this event is $1000 USD.

// Log a `checkout_completed` event with the `product_name` and `category` parameters and a `valueToSum` of 1000.0 with `valueToSumCurrency` set to "USD"

try {

JSONObject productDetails = new JSONObject();

productDetails.put("product_name", "Brand A Camera");

productDetails.put("category", "electronics");

QG.getInstance(context).logEvent("checkout_completed", productDetails, 1000.0, "USD");

} catch (JSONException e) {

// Handle the exception

}

// Log a `checkout_completed` event with the `product_name` and `category` parameters and a `valueToSum` of 1000.0 with `valueToSumCurrency` set to "USD"

try {

val productDetails = JSONObject()

productDetails.put("product_name", "Brand A Camera")

productDetails.put("category", "electronics")

QG.getInstance(context).logEvent("checkout_completed", productDetails, 1000.0, "USD")

} catch (e: JSONException) {

// Handle the exception

}

Follow the steps below to validate that your app is logging events properly.

Launch your app and complete the action that logs the event.

On the AIQUA Dashboard, click your account name in the lower-left corner and go to Recent Activity.



Logging Custom User Events [3]

https://docs.aiqua.appier.com/docs/logging-user-events-for-the-android-sdk



On the AIQUA Dashboard, click your account name in the lower-left corner and go to Recent Activity.

Under the Android tab, you should see the event. It may take several minutes for the event to display on the AIQUA Dashboard.

Updated over 1 year ago Table of Contents

Overview

valueToSum and valueToSumCurrency

Event logging examples

Logging events (event name only)

Logging events with parameters

Logging events with parameters and valueToSum

Logging events with parameters, valueToSum, and valueToSumCurrency

Checkpoint: Validate that events are logged properly



Event Attribution [0]

https://docs.aiqua.appier.com/docs/event-attribution-android-sdk



Event attribution allows you to determine how your campaigns are contributing to user conversions. Events attributed to campaign notifications are listed as attributed events in the Campaign Performance page. 

AIQUA uses two types of attribution models:

Attribution modelDescriptionView-through attributionBy default, events occurring within one hour of the user receiving a campaign notification are attributed as view-throughs.

The one hour view-through attribution window can be modified using setAttributionWindow().Click-through attributionBy default, events occurring within 24 hours of the user clicking a campaign notification are attributed as click-throughs.

The 24 hour click-through attribution window can be modified using setClickAttributionWindow().

For more details on how event attribution works, see Understanding Event Attribution.

The event attribution window is the period of time after a campaign is viewed or clicked in which a conversion event can be attributed to that campaign. Attribution windows apply to both push campaigns and in-app campaigns, and can be modified using the Android SDK:

Modifying the click-through attribution window

Modifying the view-through attribution window

📘NoteStarting from Android SDK 6.8.0, attribution windows can't be set to 0. If you set the attribution window to 0, the SDK will reset it to its default value of 86,400 seconds (24 hours).

By default, the view-through attribution window is set to 3,600 seconds (one hour). To update the view-through attribution window, use setAttributionWindow(), where CUSTOM_WINDOW is the length of the desired attribution window in seconds.

public void setAttributionWindow(long seconds)

fun setAttributionWindow(seconds: Long)

The following example sets the view-through attribution window to 7200 seconds (two hours):

QG.getInstance(context).setAttributionWindow(7200);

QG.getInstance(context).setAttributionWindow(7200)



Event Attribution [1]

https://docs.aiqua.appier.com/docs/event-attribution-android-sdk



QG.getInstance(context).setAttributionWindow(7200);

QG.getInstance(context).setAttributionWindow(7200)

By default, the click-through attribution window is set to 86,400 seconds (24 hours). To update the click-through attribution window, use setClickAttributionWindow(), where CUSTOM_WINDOW is the length of the desired attribution window in seconds.

public void setClickAttributionWindow(long seconds)

fun setClickAttributionWindow(seconds: Long)

The following example sets the click-through attribution window to 43,200 seconds (12 hours):

QG.getInstance(context).setClickAttributionWindow(43200);

QG.getInstance(context).setClickAttributionWindow(43200)

Updated 11 months ago Table of Contents

Overview

Attribution windows

Modifying the view-through attribution window

Modifying the click-through attribution window



Android In-App Campaigns

https://docs.aiqua.appier.com/docs/in-app-campaigns-for-android



In-app campaigns, unlike push notifications which are delivered outside of your app, are delivered to your users while they're using your app. You can use AIQUA to send two types of in-app campaigns:

Pop-up campaigns send notifications that immediately pop up inside of your app. You can use following creative types with in-app pop-up campaigns: Floating text, Small, Medium, Full screen, and Custom creatives.

From left to right: Floating Text, Small Content Box, Medium Image, Full screen

Inbox campaigns (Beta) notifications can be fetched from AIQUA and saved on local device storage. Choose how and when to display locally-stored notifications to app users without having to rely on more obtrusive push or pop-up notifications.

📘In-app inbox campaigns are a beta feature. While this feature is currently available for use, you may encounter occasional bugs or stability issues.Updated over 1 year ago



In-App Pop-Up Campaigns

https://docs.aiqua.appier.com/docs/in-app-popup-notifications-for-android



The Android SDK provides methods for clearing foreground in-app pop-ups and disabling pop-ups.

To clear all the foreground in-app pop-ups, call hideInAppCampaigns().

public void hideInAppCampaigns()

fun hideInAppCampaigns()

QG qg = QG.getInstance(context);

qg.hideInAppCampaigns();

val qg = QG.getInstance(context)

qg.hideInAppCampaigns()

To display in-app campaign pop-ups in the foreground again, log the trigger event. Frequency cap limitations apply.

To disable in-app pop-up notifications for a specific activity, call hideInApp().

public void hideInApp(Activity activity)

fun hideInApp(activity: Activity)

Pass the name of the activity into your call to hideInApp(). hideInApp() should be called before onStart() in the activity where you want in-app pop-ups to be disabled.

QG qg = QG.getInstance(context);

qg.hideInApp(activity);

val qg = QG.getInstance(context)

qg.hideInApp(activity)

Updated over 1 year ago Table of Contents

Clearing all foreground in-app pop-up notifications

Using hideInAppCampaigns()

Disabling in-app pop-up notifications

Using hideInApp()



In-App Inbox Campaigns [0]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-android



🚧NoteIn-app inbox campaigns are a beta feature. While this feature is currently available for use, you may encounter occasional bugs or stability issues.

📘Prerequisites

Complete the required setup for the Appier Android SDK.

Create an in-app campaign on the AIQUA Dashboard with the campaign type set to Inbox.

In-app inbox campaigns allow you to fetch notifications from AIQUA and store them on local device storage. You can choose how and when to display locally-stored notifications to app users without having to rely on push notifications or pop-up campaigns.

Use the following classes in the Android SDK to implement inbox campaigns:

QG class methods: Operations for the entire inbox, such as setting the inbox's maximum capacity.

AiqInbox class methods: Operations on individual inbox campaign notifications, such as logging an event for a single notification or setting a notification's status.

Inbox campaign notifications differ from pop-up campaign notifications and push notifications in several ways. Namely, inbox campaign notifications are:

Fetched using an SDK method: Fetch new notifications using fetchInboxMessages(). Other notification types can't be fetched with SDK methods; instead, they are sent directly to the device after AIQUA delivers the campaign.

Retrieved silently: Other notification types are displayed to the user as soon as the campaign is delivered. With inbox campaigns, you can silently retrieve notifications and choose how and when to display the locally-stored notifications to app users. 

Stored on the device: Use fetchInboxMessages() to fetch and store the latest notifications in the inbox using local device storage. Stored notifications can then be retrieved at any time using getInboxes().

The Android SDK doesn't automatically log impression and click events for inbox campaign notifications. To view in-app inbox campaign performance data on the AIQUA Dashboard and in campaign user reports, notification impression and click events must be logged manually using logEvent().



In-App Inbox Campaigns [1]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-android



Using inbox campaigns, we'd like to implement a message center in our app. The message center will contain messages notifying our users of app updates and product announcements. We're using inbox campaigns for this feature so that:

We can retrieve new notifications without interrupting the user, since inbox campaign notifications are retrieved silently by default.

Messages are stored in the inbox, using local device storage, so we can give users the ability to view messages at any time by navigating to the app's message center.

To use the Android SDK methods to implement the message center described above, follow these steps:

StepDescription1Set the notification capacity of the in-app inbox using updateInboxRecordLimit(). By default, the inbox capacity is set to 50.2When the app is launched, call fetchInboxMessages() to retrieve the latest campaign notifications.3When a user navigates to the message center, get a list of all unread messages by calling getInboxes() and display a list of all the new messages.4(Optional) Log a qg_inapp_displayed event for each displayed message.

Logging this event will allow you to view this campaign performance metric on the AIQUA Dashboard and in campaign user reports.5• When a user clicks on a message in the message center, retrieve any additional message content from the array returned by getInboxes() and display it to the user.

• After a message has been read, update the message's status to READ using setStatus().6(Optional) Log a qg_inapp_clicked event for the clicked message.

Logging this event will allow you to view this campaign performance metric on the AIQUA Dashboard and in campaign user reports.

In our message center, we want to include a force refresh button that a user can click to fetch the latest messages. To accomplish this, we'll employ the following SDK methods:

fetchInboxMessages(): Fetches new messages from AIQUA's servers and saves them locally.

getInboxes(): Returns a list of all locally-saved messages and their metadata.



In-App Inbox Campaigns [2]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-android



getInboxes(): Returns a list of all locally-saved messages and their metadata.

The following code sample demonstrates how to implement a force refresh:

QG.fetchInboxMessages(context, new AiqInbox.FetchCallback() {

@Override

public void onInboxFetched(boolean success, String errMsg) {

if (!success) {

Log.d(LOG_TAG, "onInboxFetched inbox error:" + errMsg);

return;

}

// Get all inbox campaigns

AiqInbox[] inboxes = QG.getInboxes(true, true, true);

}

});

QG.fetchInboxMessages(context) { success, errMsg ->

if (!success) {

Log.d(LOG_TAG, "onInboxFetched inbox error:$errMsg")

return@fetchInboxMessages

}

// Get all inbox campaigns

val inboxes = QG.getInboxes(true, true, true)

}

Operations for the entire in-app inbox — such as setting the inbox's notification capacity, or fetching new notifications — can be done using the following QG class methods:

Sets the inbox's maximum notification capacity. 

By default, the inbox capacity is 50.

If fetching the latest notifications from AIQUA by calling fetchInboxMessages() results in a locally-stored list of notifications exceeding the inbox capacity, the notifications with the smallest notificationId(see AiqInbox properties) will be deleted from local storage so that the number of notifications doesn't exceed the maximum capacity.

// Signature

public static void updateInboxRecordLimit(int limit)

// Usage

// Sets the inbox capacity to 10 messages

QG.updateInboxRecordLimit(10);

// Signature. This is a static method.

fun updateInboxRecordLimit(limit: Int)

// Usage

// Sets the inbox capacity to 10 messages

QG.updateInboxRecordLimit(10)

Fetches the latest inbox notifications from AIQUA. For a usage example, see In-App Message Center: Force Refresh Function.

/**

* To fetch the inbox messages from server and store them locally

* @param context the android context

* @param fetchCallback an instance of AiqInbox.FetchCallback

*/

public static void fetchInboxMessages(Context context, AiqInbox.FetchCallback fetchCallback)

// AiqInbox.FetchCallback



In-App Inbox Campaigns [3]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-android



*/

public static void fetchInboxMessages(Context context, AiqInbox.FetchCallback fetchCallback)

// AiqInbox.FetchCallback

public interface FetchCallback {

/**

* Will be triggered after the inbox notifications are fetched from the server

* @param success true if the fetching is successful fetched; false if failed.

* @param errMsg "" if the fetching is successful; "Response Code: ###" if failed.

*/

void onInboxFetched(boolean success, String errMsg);

}

/**

* To fetch the inbox notifications from server and store them locally

* @param context the android context

* @param fetchCallback an instance of AiqInbox.FetchCallback

*/

fun fetchInboxMessages(context: Context, fetchCallback: AiqInbox.FetchCallback)

// AiqInbox.FetchCallback

interface FetchCallback {

/**

* Will be triggered after the inbox notifications are fetched from the server

* @param success true if the fetching is successful fetched; false if failed.

* @param errMsg "" if the fetching is successful; "Response Code: ###" if failed.

*/

fun onInboxFetched(success: Boolean, errMsg: String)

}

Returns a list of all locally-stored inbox notifications. For a usage example, see In-App Message Center: Force Refresh Function.

/**

* To get the inbox messages from local storage

* @param getUnread get unread messages

* @param getRead get read messages

* @param getDeleted get deleted messages

* @return an array of AiqInbox

*/

public static AiqInbox[] getInboxes(boolean getUnread, boolean getRead, boolean getDeleted)

/**

* To get the inbox messages from local storage

* @param getUnread get unread messages

* @param getRead get read messages

* @param getDeleted get deleted messages

* @return an array of AiqInbox

*/

fun getInboxes(getUnread: Boolean, getRead: Boolean, getDeleted: Boolean): Array

Each inbox notification is an instance of the AiqInbox class. Operations on individual inbox notifications can be done using the AiqInbox class methods.

/**

* the read-only members

*/

public final String notificationId;



In-App Inbox Campaigns [4]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-android



/**

* the read-only members

*/

public final String notificationId;

public final String image;

public final String deepLink;

public final String title;

public final String text;

public final JSONObject qgPayload;

public final long startTime;

public final long endTime;



/**

* the writable member

*/

public Status status;

/**

* AiqInbox.Status enumeration

*/

public enum Status {

UNREAD,

READ,

DELETED

}

📘Receiving key-value pairsIf you're sending key-value pairs with your inbox notifications, you can access them in the qgPayload object.

Sets the status of an individual notification to one of the statuses listed in the AiqInbox.Status enumeration.

// Signature

public void setStatus(Context context, Status status)

// Usage

// Set the message's status to `READ`

inbox.setStatus(context, AiqInbox.Status.READ);

// Signature

fun setStatus(context: Context, status: AiqInbox.Status)

// Usage

// Set the message's status to `READ`

inbox.setStatus(context, AiqInbox.Status.READ)

Use logEvent() to log the following types of event for inbox notifications:

Custom events

Campaign performance events (clicks and impressions) that you want to view on the AIQUA Dashboard

// Signature

public void logEvent(Context context, String eventName, JSONObject eventInfo, Double valueToSum, String valueToSumCurrency)

// Signature

fun logEvent(context: Context, eventName: String, eventInfo: JSONObject?, valueToSum: Double?, valueToSumCurrency: String?)

📘NoteWhen logging any event for an inbox notification, the notification's notificationId is automatically added as an event parameter by the Appier SDK.

When using logEvent() to log custom events, include any additional event parameters as defined in your custom event schema.

The following code sample retrieves all read inbox messages, then logs a custom event with a parameter for the first message:

try {

AiqInbox[] readInboxes = QG.getInboxes(false, true, false);

JSONObject param = new JSONObject();

param.put("parameter", "parameter_value");



In-App Inbox Campaigns [5]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-android



JSONObject param = new JSONObject();

param.put("parameter", "parameter_value");

readInboxes[0].logEvent(context, "custom_event", param, 0.0, null);

} catch (JSONException e) {

Log.e(LOG_TAG, "Failed to log event with an inbox", e);

}

try {

val readInboxes = QG.getInboxes(getUnread = false, getRead = true, getDeleted = false)

val param = JSONObject().apply {

put("parameter", "parameter_value")

}

readInboxes[0].logEvent(context, "custom_event", param, 0.0, null)

} catch (e: JSONException) {

Log.e(LOG_TAG, "Failed to log event with an inbox", e)

}

To track and view campaign performance data (impressions and clicks) on the AIQUA Dashboard, you need to manually log the following events using logEvent():

qg_inapp_displayed (impressions)

qg_inapp_clicked (clicks)

👍TipYou don't need to add event parameters when logging qg_inapp_displayed or qg_inapp_clicked.

// Log the `qg_inapp_displayed` event for this notification

inbox.logEvent(context, "qg_inapp_displayed", new JSONObject(), 0.0, "");

// Log the `qg_inapp_displayed` event for this notification

inbox.logEvent(context, "qg_inapp_displayed", new JSONObject(), 0.0, "")

Although these events are default events, the SDK doesn't automatically log them for inbox campaigns. When properly logged, these campaign performance metrics will be displayed in the in-app campaign list on the AIQUA Dashboard.

Updated 10 months ago Table of Contents

Overview

Inbox campaigns vs pop-up and push campaigns

Logging events for inbox campaign notifications

Example use case: In-app message center

Message center implementation

Message center force refresh feature

QG methods

updateInboxRecordLimit()

fetchInboxMessages()

getInboxes()

AiqInbox class

AiqInbox properties

AiqInbox methods



Implementing Deep Links

https://docs.aiqua.appier.com/docs/implementing-deep-links-for-android



Push campaigns and in-app campaigns can include deep links which, when clicked by a user, brings them directly to a specific location in your app or website.

To use deep links in a campaign:

In your project's AndroidManifest.xml, declare an intent filter for the deep link.

On the AIQUA dashboard, input the deep link when configuring the regular (push) campaign creative or in-app campaign creative.

On the AIQUA dashboard, input the deep link in the campaign creative's settings.

In your project's AndroidManifest.xml, declare an intent filter for the destination of the deep link.

For example, to create a deep link that redirects to MyActivity via myapp://myactivity, declare the following intent filter in AndroidManifest.xml:











android:scheme="myapp"

android:host="myactivity"/>





Once the intent filter is created:

MyActivity will be able to recognize a deep link intent with the data specification myapp://myactivity.

When a user clicks the campaign, an intent with this specification will be generated and caught by MyActivity, resulting in the user being redirected to that location in the app.

For more details on the intents and intent filters, refer to the Android Developer guides below:

Intents and Intent Filters



Updated 10 months ago Table of Contents

Overview

Declaring an intent filter for a deep link



Android Push Notifications [0]

https://docs.aiqua.appier.com/docs/push-notifications-for-android



Push notifications can be used to deliver important or useful information to your users, even when your app is running in the background or inactive.

For apps targeting API level 33 or higher: Your app's AndroidManifest.xml must include the POST_NOTIFICATIONS permission for devices running Android 13 or later to receive push notifications.

For apps targeting API level 32 or lower: The Appier Android SDK automatically handles push notifications from Firebase Cloud Messaging (FCM).

You can also customize your FirebaseMessagingService implementation depending on your app's specific needs (e.g. if your app requires the use of multiple FCM services, custom FCM services, or needs to disable push AIQUA push notifications).

🚧Notifications from non-FCM servicesImpressions and clicks for notifications sent by notification services other than FCM are not tracked.

You can use a custom implementation of FirebaseMessagingService if you want to:

Support behaviors that aren't supported by the default implementation provided by the Android SDK (e.g. using multiple FCM services).

Disable AIQUA push notifications.

First, define a class that extends FirebaseMessagingService.

In the following examples, we'll use a class named MyFcmListener to demonstrate a custom implementation:

import com.google.firebase.messaging.FirebaseMessagingService;

import com.google.firebase.messaging.RemoteMessage;

public class MyFcmListener extends FirebaseMessagingService {

// Implement any required class methods

}

import com.google.firebase.messaging.FirebaseMessagingService

import com.google.firebase.messaging.RemoteMessage

class MyFcmListener : FirebaseMessagingService() {

// Implement any required class methods

}

Depending on what functionalities you need, implement the following methods in the class you defined:

onMessageReceived(): Required for receiving or blocking AIQUA push notifications.

onNewToken(): Required for receiving AIQUA push notifications.

import com.google.firebase.messaging.FirebaseMessagingService;



Android Push Notifications [1]

https://docs.aiqua.appier.com/docs/push-notifications-for-android



onNewToken(): Required for receiving AIQUA push notifications.

import com.google.firebase.messaging.FirebaseMessagingService;

import com.google.firebase.messaging.RemoteMessage;

import com.quantumgraph.sdk.QG;

public class MyFcmListener extends FirebaseMessagingService {

@Override

public void onMessageReceived(RemoteMessage message) {

// If the message is from AIQUA, handleRemoteMessage() returns true

// and processes it. Otherwise, the method returns false.

if (!QG.getInstance(this).handleRemoteMessage(message)) {

// handle FCM message from other services

}

}

@Override

public void onNewToken(String token) {

super.onNewToken(token);

QG.logFcmId(getApplicationContext());

// handle FCM token for other services

}

}

import com.google.firebase.messaging.FirebaseMessagingService

import com.google.firebase.messaging.RemoteMessage

import com.quantumgraph.sdk.QG

class MyFcmListener : FirebaseMessagingService() {

override fun onMessageReceived(message: RemoteMessage) {

// If the message is from AIQUA, handleRemoteMessage() returns true

// and processes it. Otherwise, the method returns false.

if (!QG.getInstance(this).handleRemoteMessage(message)) {

// handle FCM message from other services

}

}

override fun onNewToken(token: String) {

super.onNewToken(token)

QG.logFcmId(applicationContext)

// handle FCM token for other services

}

}

import com.google.firebase.messaging.FirebaseMessagingService;

import com.google.firebase.messaging.RemoteMessage;

import com.quantumgraph.sdk.QG;

public class MyFcmListener extends FirebaseMessagingService {

@Override

public void onMessageReceived(RemoteMessage message) {

if (QG.getInstance(getApplicationContext()).isAppierPush(message.getData())) {

// Do nothing to block AIQUA message

}

}

}

import com.google.firebase.messaging.FirebaseMessagingService

import com.google.firebase.messaging.RemoteMessage

import com.quantumgraph.sdk.QG

class MyFcmListener : FirebaseMessagingService() {

override fun onMessageReceived(message: RemoteMessage) {



Android Push Notifications [2]

https://docs.aiqua.appier.com/docs/push-notifications-for-android



class MyFcmListener : FirebaseMessagingService() {

override fun onMessageReceived(message: RemoteMessage) {

if (QG.getInstance(applicationContext).isAppierPush(message.data)) {

// Do nothing to block AIQUA message

}

}

}

After you've defined the class and implemented the required methods, declare the class as a service in AndroidManifest.xml. 











Updated over 1 year ago Table of Contents

Overview

Custom FirebaseMessagingService implementation

1. Define a class

2. Implement class methods

3. Add the class to AndroidManifest.xml



Sending Test Notifications [0]

https://docs.aiqua.appier.com/docs/test-notification-for-android



Follow the steps below to send a campaign from the AIQUA Dashboard to see if your test device can successfully receive a push notification.

🚧Devices running Android 13 or laterTo send push notifications to devices running Android 13 or later, your app's AndroidManifest.xml must include the POST_NOTIFICATIONS permission for devices running Android 13 or later to receive push notifications.

Open your project in Android Studio and run the app on your device. If your device is running Android 13 or later, accept the app's request to send push notifications.

On the AIQUA Dashboard, click your account name in the lower-left corner, select Recent Users, and go to the Android tab. You should see a new user at the top of the user list. Under Other fields, aiq_push_enabled should be equal to true.

Wait for Copy GCMID text to become visible under the Push token (APNS token / GCM ID) column, then copy the user ID. If Copy GCMID doesn't appear, continue waiting and refreshing the page until it does. 

📘The Copy GCMID text is only visible on the dashboard when AIQUA's servers receive the device's push token. Until the device's push token is received, that device can't receive AIQUA push notifications.

From the navigation bar, go to Audience > Segment list, and click the + Create segment > Conditions in the top-right corner.

Enter a name. You'll need the name of this segment when you create the campaign.

Under Include Users, click + Add New Condition and set userId to the value you obtained from the app_launched event.

Click Save. 

On the segment list page, (Audience > Segment List) the segment you just created should have a single user under Android Subscribers.

From the navigation bar, go to Campaigns > Regular Campaigns, then click Create a New Campaign.

Set the following fields:

SectionSettingsCampaignCampaign Type: PushScheduleSend ManuallyAudience• Platform: Android

• Include Users of the Segment: 

Replace with the name of the segment you created.Creative• Type: Standard



Sending Test Notifications [1]

https://docs.aiqua.appier.com/docs/test-notification-for-android



Replace with the name of the segment you created.Creative• Type: Standard

• Title: Hello Push

• Message: Hello Push 👍

• Big Image URL: https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg

Click Save.

Find the campaign you just created on the regular campaign list page (Campaigns > Regular Campaigns), and click the three vertical dots next to the campaign name, then select Send Now.

Your Android device should receive a push notification. Tap the notification to log a notification_clicked event.

In the regular campaign list page, the counts for Impressions and Clicks should have been incremented, indicating that the impression and clicks were properly tracked for the push notification you just sent.

If you didn't receive the push notification on your test device, ensure that the following conditions have been met:

The segment contains the test device you are using

The mobile device has a stable network connection

All required setup steps have been completed

If you're using a customized implementation of FirebaseMessagingService, ensure it has been implemented correctly

See the sections below for solutions to specific issues you may encounter while sending test push notifications.

Check for dependency conflicts. See Troubleshooting Dependency Issues for a list of Appier SDK dependencies and solutions for common issues

Check for a NoClassDefFoundError in your system log and follow the steps provided in Troubleshooting Dependency Issues to resolve the error.

On your test device, go to your app's notification channel settings and ensure that all notification channels have been enabled:

Updated 3 months ago Table of Contents

1. Generate a user ID

2. Create a segment

3. Create an Android push campaign

4. Send the campaign

Troubleshooting

The Android Studio error logs show "Duplicate class..."

The Copy GCMID option doesn't appear on the AIQUA Dashboard after thirty minutes

On the Recent Users page, the aiq_push_enabled setting is false



(Optional) Storing Push Notifications [0]

https://docs.aiqua.appier.com/docs/storing-push-notifications-for-android



The Appier Android SDK allows you to enable push notification storage and provides APIs for the following operations:

Setting the maximum notification storage limit

Retrieving stored notifications

Deleting stored notifications

Your app must be using Android SDK 5.9.4 or later.

The Appier SDK can only store notifications sent by AIQUA.

Push notification storage is disabled by default. To enable it, call enablePushNotificationStorage().

QG.getInstance(context).enablePushNotificationStorage();

QG.getInstance(context).enablePushNotificationStorage()

By default, the notification storage limit is set to 20. Messages that exceed the storage limit are deleted, with the oldest messages being deleted first.

Use setMaxNumStoredNotifications() to change the storage limit. In the following example, the storage limit is set to 100:

QG.getInstance(context).setMaxNumStoredNotifications(100);

QG.getInstance(context).setMaxNumStoredNotifications(100)

getStoredNotifications() returns a JSONArray of the notifications and their fields.

JSONArray storedNotifications = QG.getInstance(context).getStoredNotifications();

val storedNotifications: JSONArray = QG.getInstance(context).storedNotifications

Different types of notifications may include different fields. However, all of them have a title and a message. They may also have imageUrl, bigImageUrl, deepLink and other fields depending on the notification type. For details on image specifications, see Image Specifications.

You can delete a single notification by retrieving it's position in the array returned by getStoredNotifications() and passing it into deleteNotificationAtIndex(). The following example deletes the first stored notification (at position 0) in the array:

// Delete the first notification locally stored by the SDK

QG.getInstance(context).deleteNotificationAtIndex(0);

// Delete the first notification locally stored by the SDK

QG.getInstance(context).deleteNotificationAtIndex(0)



(Optional) Storing Push Notifications [1]

https://docs.aiqua.appier.com/docs/storing-push-notifications-for-android



// Delete the first notification locally stored by the SDK

QG.getInstance(context).deleteNotificationAtIndex(0)

For example, you can use deleteNotificationAtIndex() to delete a notification from the app's notification history after a user reads or clicks it.

Delete all locally stored AIQUA notifications using deleteStoredNotifications():

QG.getInstance(context).deleteStoredNotifications();

QG.getInstance(context).deleteStoredNotifications()

Updated 6 months ago Table of Contents

Overview

Requirements and limitations

Enabling push notification storage

Setting the notification storage limit

Retrieving stored notifications

Deleting stored notifications

Deleting a single notification

Deleting all notifications



(Optional) Receiving Key-Value Pairs [0]

https://docs.aiqua.appier.com/docs/setting-up-notifications



In addition to the default AIQUA campaign fields such as the title, message, and icon URL, you can send custom data to your app by including key-value pairs in your Android push campaigns.

For example, if you're using an in-house analytics tool to measure campaign performance, you can include key-value pairs in your push campaigns to pass any additional parameters required by your analytics tool.

On the AIQUA Dashboard, navigate to Campaigns > Regular Campaigns, then go to the campaign creation or settings page for the campaign you want to add key-value pairs for.

Under Advanced Settings, check Include Key-Value Pairs, then add the key-value pairs you'd like to include.

Key-value pairs are sent via the push notification's deep link intent filter. When the notification is clicked and the redirection to the deep link occurs, the key-value pairs are passed to your app as well.

Follow the instructions in Implementing Deep Links to create a filter for the activity in your app that will handle these key-value pairs.

Finally, implement two callbacks in your app: onNewIntent() and onCreate(). These methods will catch and process the deep link intents when a user clicks on the campaign.

When the activity is in the foreground, any caught intents will be sent to onNewIntent().

The following example demonstrates how to implement an intent handler and retrieve the value of myKey from the intent in onNewIntent():

@Override

public void onNewIntent(Intent intent) {

super.onNewIntent(intent);

processIntent(intent);

}

private void processIntent(Intent intent) {

if (intent != null && intent.hasExtra("myKey")) {

String value = intent.getStringExtra("myKey");

// Do anything to the value

}

}

override fun onNewIntent(intent: Intent) {

super.onNewIntent(intent)

processIntent(intent)

}

private fun processIntent(intent: Intent?) {

intent?.apply {

if (hasExtra("myKey")) {

val value = intent.getStringExtra("myKey")

// Do anything to the value

}

}

}



(Optional) Receiving Key-Value Pairs [1]

https://docs.aiqua.appier.com/docs/setting-up-notifications



intent?.apply {

if (hasExtra("myKey")) {

val value = intent.getStringExtra("myKey")

// Do anything to the value

}

}

}

If the activity hasn't been created, onCreate() will be invoked instead of onNewIntent(), so you'll also need to override onCreate() to process caught intents.

The following example demonstrates how to implement an intent handler and retrieve the value of myKey from the intent in onCreate():

@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

processIntent(getIntent());

}

private void processIntent(Intent intent) {

if (intent != null && intent.hasExtra("myKey")) {

String value = intent.getStringExtra("myKey");

// Do anything to the value

}

}

override fun onCreate(savedInstanceState: Bundle?) {

super.onCreate(savedInstanceState)

processIntent(intent)

}

private fun processIntent(intent: Intent?) {

intent?.apply {

if (hasExtra("myKey")) {

val value = intent.getStringExtra("myKey")

// Do anything to the value

}

}

}

Updated 8 months ago Table of Contents

Overview

Setup steps

1. Add key-value pairs in your campaign

2. Create an intent filter

3. Receive key-value pairs in an activity



(Optional) Customizing Notification Previews [0]

https://docs.aiqua.appier.com/docs/customizing-push-notification-images



Refer to the following sections to learn about how to customize the appearance of your push notification previews, i.e. collapsed push notifications.

Small icon

Color defaults

When a user receives an Android push notification, the notification icon is displayed in two locations:

The status bar at the top of the device

The top of the push notification

When users receive your push, this image is displayed as the status bar notification image at the top of the screen and the small icon on the push notification.

Customized notification icons are only supported for apps using Android SDK 5.5.4 or later

This feature doesn't apply to notification icons on the status bar

Make sure that you have an image called ic_notification.png in your drawable/ folder.

This image should be: 

72 x 72 px or larger, with an aspect ratio of 1:1

A white image on a transparent background

Use a transparent background for the small icon's background to ensure the accent color is shown. The accent color feature is dependent on the Android version and devices

👍TipWe recommend creating notification icons using Android Studio's Asset Studio Tool.

The status bar notification image is shown in white against a transparent background, while the small icon uses the accent color, which is grey by default. 

Using accent_color_notification, you can customize the color of the small icon and app name when shown on the notification. For more details on accent color, see this Google guide.

For additional reference, this link can be followed.

🚧Important

This feature is supported in Appier Android SDK 5.5.4 or later

This feature doesn't apply to notification icons on the status bar

Use a transparent background for the small icon's background to ensure the accent color is shown

The accent color feature is dependent on the Android version and devices

In your Android app, create a color resource named accent_color_notification. If accent_color_notification isn't set, the system's default color is used.



(Optional) Customizing Notification Previews [1]

https://docs.aiqua.appier.com/docs/customizing-push-notification-images



For example, in src > main > res > values > color.xml, add a default accent color hex, as shown below.





#ffff0000



You can configure the following color settings to control the appearance of your app's push notifications in the collapsed state. If no custom colors are set on the AIQUA dashboard (campaign creative settings), the following default colors will be used.

🚧ImportantColor defaults are overridden by custom colors set from the AIQUA dashboard (creative settings).

ModeSettingLight mode• Title color: ?android:attr/textColorPrimary

• Message color: ?android:attr/textColorSecondaryDark mode• Title color: ?android:attr/textColorPrimaryInverse

• Message color:?android:attr/textColorSecondaryInverseUpdated over 1 year ago Table of Contents

Overview

Small icon

Limitations

Icon image requirements

Changing the small icon color (accent color)

Notification preview color defaults



(Optional) Customizing Notification Sounds

https://docs.aiqua.appier.com/docs/custom-push-notification-sound-for-android



Android supports using custom sounds when sending push notifications. AlQUA lets you enable this for Android users via a compatible sound file URL added on the AIQUA dashboard.

Before adding the sound file, make sure that it meets the following requirements:

The file URL must be in HTTPS.

It must be in a supported sound file format:

3GPP (.3gp)

MPEG-4 (.mp4, .m4a)

ADTS raw AAC (.aac, decode in Android 3.1+, encode in Android 4.0+, ADIF not supported)

MPEG-TS (.ts, not seekable, Android 3.0+)

FLAC (.flac) only

GSM(.gsm)

Type 0 and 1 (.mid, .xmf, .mxmf)

RTTTL/RTX (.rtttl, .rtx)

OTA (.ota)

iMelody (.imy)

MP3 (.mp3)

WAVE (.wav)

For more details on the supported audio formats and codecs, see this Android Audio Support guide.

Add the sound file URL with its file extension under the ADVANCED section of the Campaign creation page. 

🚧Important:

If the Sound File URL field is empty, the default sound is played when your notification reaches the user's device.

If the Sound File URL field is present, Pile up notifications is automatically selected and cannot be changed. 

Updated over 1 year ago Table of Contents

Configuring the Sound File URL

Adding the Sound File in a Campaign



Android SDK Web View Support [0]

https://docs.aiqua.appier.com/docs/android-webview-support



Track custom user events and attributes logged from a Appier SDK-integrated web page displayed inside a web view (via the Android WebView class) by establishing a JavaScript bridge between the Appier Web SDK and the Appier Android SDK. If the web-to-mobile SDK bridge is not established, your mobile app users will be tracked in AIQUA as web users rather than Android users.

When a web page is integrated with the Web SDK and web view logging has been properly implemented:

Custom user events and attributes logged by the Web SDK are passed to the Android SDK.

The Web SDK's default user events and attributes (such as page_viewed and visited) aren't tracked from websites displayed in a web view.

FeatureRequired Android SDK versionWeb view loggingRequires Android SDK 5.4.2 or later.Recommendation 2.0Requires Android SDK 6.10.0 or later.Filtering out purchased products by user_id from recommendation results in web pages inside a web view requires Android SDK 7.2.0 or later.Multiple app IDs (Android SDK 8.1.0 or later)If your app and website use different app IDs, contact Appier Support (ess_support@appier.com ) to modify the SDK's app ID allowlist to ensure web data is logged to the correct app ID.

To establish the JavasScript bridge, use addJavaScriptInterface() to inject a JavaScript interface into the WebView.

public void addJavaScriptInterface(WebView webView)

fun addJavaScriptInterface(webView: WebView)

Once the JavaScript bridge is established, custom user events and attributes logged from your website displayed in a web view (via the Web SDK) are passed to the Android SDK and can be collected by AIQUA. 

The following example demonstrates how to enable JavaScript for a WebView and inject AIQUA's JavaScript interface into it:

WebView webView = findViewById(R.id.webview);

WebSettings webSettings = webView.getSettings();

webSettings.setJavaScriptEnabled(true);

// Inject AIQUA's JavaScript interface

QG.getInstance(this).addJavaScriptInterface(webView);

webView.loadUrl("http://www.example.com");



Android SDK Web View Support [1]

https://docs.aiqua.appier.com/docs/android-webview-support



QG.getInstance(this).addJavaScriptInterface(webView);

webView.loadUrl("http://www.example.com");

val webView: WebView = findViewById(R.id.webview)

val webSettings = webView.settings

webSettings.javaScriptEnabled = true



// Inject AIQUA's JavaScript interface

QG.getInstance(this).addJavaScriptInterface(webView)

webView.loadUrl("http://www.example.com")

Updated 4 months ago Table of Contents

Overview

Version requirements

Implementing WebView logging



Android SDK Batching

https://docs.aiqua.appier.com/docs/configuring-batching-for-android



To optimize network usage, the Appier SDK batches its network requests to AIQUA's server when ever one of the following conditions are met:

15 seconds have passed since data was last sent to AIQUA's servers

The number of user events stored by the SDK exceeds 100

The flush() API is called, forcing the SDK to upload all stored data

Unless one of the conditions stated above are met, the SDK will continue to collect and store data, including user events and attributes, without uploading it to AIQUA's servers.

You can force the SDK to flush all stored data to AIQUA's servers at any time by calling flush():

QG.getInstance(context).flush();

QG.getInstance(context).flush()

Updated over 1 year ago Table of Contents

Appier Android SDK batching

Force-flushing stored data



Managing Android Users

https://docs.aiqua.appier.com/docs/managing-android-users



AIQUA Android users are identified using the Appier SDK-generated userId. 

Retrieving userId

Deleting and regenerating Android users

📘Retrieving userId is only available in Android SDK 7.18.0 and later.

To retrieve the value of userId, use appierId (Android SDK 7.21.0 or later) or getAppierId() (Android SDK 7.18.0 to 7.20.0):

// Android SDK 7.21.0 or later

QG.getInstance(context).appierId

// Android SDK 7.18.0 to 7.20.0

QG.getInstance(context).getAppierId()

QG.getInstance(context).getAppierId();

To delete an Android user's data and regenerate userId, for example, when a user modifies their data tracking consent settings, you'll need to complete two steps:

Delete the user's data with the Delete Users API using their unique identifier from your CRM (user_id).

Regenerate userId using the Android SDK. In addition to generating a new userId, calling this method will delete all locally cached data, including events, attributes, and campaigns.

Android SDK 7.18.0 and later: Use renewAppierId()

Android SDK 6.8.0 to 7.17.3: Use renewUserId()

Android SDK 6.7.1 and earlier: Regenerating userId is not supported

📘NoteWhen regenerating userId:

The Android SDK won't renew the app's push token. This prevents users from receiving campaigns before cached data (deleted using the Delete Users API) is purged from AIQUA's servers.

User data permissions will remain unchanged. Reconfigure the relevant user data permissions after regenerating the user if needed.

// Android SDK 7.18.0 and later

QG.getInstance(context).renewAppierId()

// Android SDK 6.8.0 to 7.17.3

QG.getInstance(context).renewUserId()

// Android SDK 7.18.0 and later

QG.getInstance(context).renewAppierId();

// Android SDK 6.8.0 to 7.17.3

QG.getInstance(context).renewUserId();

Updated over 1 year ago Table of Contents

Overview

Retrieving userId

Deleting and regenerating Android users



iOS SDK Overview [0]

https://docs.aiqua.appier.com/docs/ios-sdk-integration-overview



Integrate your app with Appier iOS SDK to take advantage of features such as sending push notifications, logging custom user data, and delivering in-app campaigns. This page summarizes the setup steps required to begin using the iOS SDK and all the features it supports.

We recommend using the latest iOS SDK for continual updates and feature support. See the iOS SDK release notes for details about the latest releases.

Latest Appier iOS SDK versionSupported iOS versionsSupported Xcode versionSDK download (for manual installation only)8.2.2iOS 9 to iOS 18Xcode 12+Objective-C and Swift

Refer to the following notes for known issues and notable behaviors in certain iOS SDK versions.

VersionNotesv7.27.0 to v7.32.2Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ',", \n, or any HTML tags (such as 

).v7.20.0 to v7.25.0Method swizzling is enabled by default to support LINE user sync. Apps using these versions may encounter app crashes due to method swizzling conflicts with third-party SDKs. To avoid crashes, please upgrade to the latest SDK version or disable method swizzling.



iOS SDK Overview [1]

https://docs.aiqua.appier.com/docs/ios-sdk-integration-overview



To support LINE user sync without method swizzling, set up iOS deep link handling.v8.0.0 or laterThe original AppierFramework will no longer be supported for rich push notifications.v7.10.0 or laterAppierExtensionFramework is used in the Notification Service Extension and the Notification Content Extension for rich push notifications. The main app target still uses the AppierFramework introduced in version 7.0.0. See Migrating to iOS SDK 7.10.0 or Above to upgrade from an earlier version.v7.0.0 to v7.9.0Apps using these versions will receive the following Xcode warning, which can be safely ignored: ld: linking against a dylib which is not safe for use in application extensions. This is caused by the Appier iOS SDK using a single framework for both the main application target and extension targets. Despite the warning, apps can be successfully submitted to the App Store and safely released.

Before integrating the iOS SDK with your app, prepare the following:

Your Appier app ID. Find your app ID on the AIQUA Dashboard under the Account Settings page.

A MacOS device with the Xcode 12 installed.

A physical iOS device running an iOS version supported by the iOS SDK to test push notifications with.

Complete the following required setup before using the Appier iOS SDK. Once completed, the SDK will begin logging default user events and attributes and you'll be able to start using all of the SDK's features.

After completing the required setup, you can begin using all the features supported by the iOS SDK.

Review the following notes and requirements when you're ready to submit your app to the App Store.

If your app allows for account creation, ensure that your app also allows users to initiate deletion of their account from within the app by June 30, 2022. See Apple's announcement for detailed requirements.

See Apple App Privacy for information required to answer Apple's app privacy questions.



iOS SDK Overview [2]

https://docs.aiqua.appier.com/docs/ios-sdk-integration-overview



See Apple App Privacy for information required to answer Apple's app privacy questions.

The following flags can be set in your project's Info.plist file. Please refer to the following table for the default values in each SDK version. Note that if a flag isn't explicitly configured or is incorrectly configured, the default value for the SDK version used by the app will apply.

ConfigurationDefault valueNotesAppierAppDelegateProxyEnabled• v7.20.0 to v7.25.0: true

• All other SDK versions: falseSet to true to enable method swizzling.AppierSceneDelegateDeeplinkHandlingEnabled• v7.30.0 and v7.30.1: true

• All other SDK versions: falseSet to true to enable universal link handling using the scene delegate.

When submitting your app to the App Store, you must provide information describing how your app uses the Advertising Identifier (IDFA). If your app is only using the Appier iOS SDK, select the following options on the IDFA review form:

Select Yes for Does this app use the Advertising Identifier (IDFA)?

Select Attribute an action taken within this app to a previously served advertisement. Note that AIQUA doesn't track attribution for app installations.

Select Limit Ad Tracking setting in iOS.

Updated about 2 months ago Table of Contents

Latest iOS SDK version

Version notes

Integration overview

Prerequisites

Required setup

Supported features

Publishing your app

Account deletion

App privacy

SDK configuration options

IDFA for iOS 14.4 and earlier



Development iOS SDK Versions [0]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes



📘Apple app privacy changes (v7.32.0 or later)In December 2023, Apple introduced new privacy updates for App Store submissions. If you're upgrading to iOS SDK 7.32.0 or later and haven't reviewed the updates, please review Apple App Privacy to learn more about how to complete your app's Privacy Nutrition Label.

Clicks on custom HTML in-app campaigns caused campaigns to close unexpectedly. Affected versions: 8.0.0 to 8.2.1.

The following events were occasionally duplicated for custom HTML in-app campaigns: qg_inapp_toggled (when closing campaigns) and qg_inapp_clicked. Affected versions: 7.34.0 to 7.35.0, 8.0.0 to 8.2.1.

In-app campaigns using Creative Studio incorrectly opened universal links in an external browser instead of opening the corresponding page in the app.

In-app campaigns using Creative Studio didn't display for apps using SceneDelegate.

Optimized data transmission process to the server.

In-app campaigns being displayed would freeze when the SDK was reinitialized.

Added app ID validation for app web views. If your app and website use different app IDs, contact Appier Support (ess_support@appier.com ) to modify the SDK's app ID allowlist to ensure web data is logged to the correct app ID.

The model_id parameter's data type (included in recommendation_clicked events) is now sent as a string. If you're logging this event, you'll need to modify your implementation. Please refer to iOS SDK: Recommendation 2.0 for details. 

Apps no longer encounter unexpected crashes due to an occasional race condition that occurred when displaying in-app campaigns. Affected versions: 8.0.0 and 8.0.1.

Improved debug logging for in-app Creative Studio campaigns.

The default flushInterval was incorrectly set to 0 seconds instead of 15 seconds. Affected version: v8.0.0.

Support for Retail Media Network features (beta). To learn more, contact your customer success manager.

Support for AiDeal features (beta). To learn more, contact your customer success manager.



Development iOS SDK Versions [1]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes



Support for AiDeal features (beta). To learn more, contact your customer success manager.

In-app pop-up campaign floating icons are no longer pushed off-screen when the campaign text is too long.

Long in-app pop-up floating campaign messages are no longer cut off when the device orientation changes.

qg_inapp_toggled events are no longer logged when in-app campaign action buttons are clicked. Affected versions: 7.27.0 to 7.34.0.

qg_inapp_closed events are no longer logged when collapsing an in-app pop-up campaign to a floating icon.

In-app pop-up campaigns disabled via SDK are no longer displayed upon app launch or when the campaign is disabled after a delay setting is configured. Affected version: 7.34.0.

Creative Studio campaigns now display every time the trigger event is detected. Previously, campaigns displayed only after the first instance of the trigger event and failed to display after subsequent events. Affected version: 7.34.0.

Deep links in Creative Studio campaigns are no longer incorrectly encoded. Affected versions: 7.32.2 to 7.34.0.

Updated 15 days ago Table of Contents

v8.2.2 - February 21, 2025

v8.2.1 - February 7, 2025

v8.2.0 - January 17, 2025

v8.1.0 - December 19, 2024

v8.0.1 - November 15, 2024

v8.0.0 - October 31, 2024



Apple App Privacy [0]

https://docs.aiqua.appier.com/docs/apple-app-privacy



Starting from December 2020, Apple requires developers to disclose the privacy practices of the app: https://developer.apple.com/app-store/app-privacy-details/. 

When submitting your app to the App Store, you'll need to answer a series of questions about the data collected by you and your third-party partners, includes the data collected by the Appier iOS SDK. Refer to the data collection and usage table for a list of all the data collected by the Appier iOS SDK.

📘NoteYou may need to provide additional disclosures based on your app's data collection practices and any other third-party partners you are using.

Starting from iOS SDK 7.32.0, the Appier SDK provides a privacy manifests which allows you to automatically generate an App Privacy Report. The App Privacy Report summarizes the data collected and used by your app, including the third-party SDKs your app uses.

The Appier SDK's privacy manifest only includes the required data (✅) as listed in the data collection and usage table.

For optional data (▵), you should complete Apple's Privacy Nutrition Labels based on your app's specific usage requirements.

Under "General > App Privacy" in App Store Connect, click Get Started and select Yes, we collect data from this app.

You'll see a list of data types, and you'll need to select the types of data collected from your app. Refer to the Part I column in the table below for the data collected by Appier iOS SDK.

For each data type you select, you'll need to select from the list below to indicate how the data is being used in your app. Refer to the Part II column in the data collection and usage table below for how the data is used by Appier iOS SDK.

Next, you will have to answer some Yes/No questions such as:

Are the collected from this app linked to the user's identity?

Do you or your third-party partners use for tracking purposes?

Refer to the Part III column in the data collection and usage table below for how the data is used by Appier iOS SDK.



Apple App Privacy [1]

https://docs.aiqua.appier.com/docs/apple-app-privacy



Refer to the Part III column in the data collection and usage table below for how the data is used by Appier iOS SDK.

✅ = Always required when using the Appier iOS SDK

▵ = May be required when using the Appier iOS SDK

❌ = Not required when using the Appier iOS SDK

Part I: What Data Is CollectedPart II: How Is It Used?Part III: Yes/No Questions[Contact Info]

▵ Name

▵ Email Address

▵ Phone Number

▵ Physical Address

▵ Other User Contact Info

(▵ = Select if you collect these data via Appier iOS SDK)✅ Developer's Advertising or Marketing

✅ Analytics

▵ Product Personalization

(▵ = Select if you are using Recommendation or Personalization features)• Linked to the user's identity? YES ✅

• Tracking purposes? YES ✅❌ [Health and Fitness]❌ [Financial Info][Location]

▵ Precise Location

▵ Coarse Location

(▵ = Select if you enabled location collection)✅ Analytics• Linked to the user's identity? YES ✅

• Tracking purposes? YES ✅❌ [Sensitive Info]❌ [Contacts]❌ [User Content]❌ [Browsing History]❌ [Search History][Identifiers]

✅ User ID

✅ Device ID✅ Developer's Advertising or Marketing

✅ Analytics

▵ Product Personalization

(▵ = Select if you are using Recommendation or Personalization features)• Linked to the user's identity? YES ✅

• Tracking purposes? YES ✅▵ [Purchases]

(▵ = Select if you collect purchase-related events via Appier iOS SDK)✅ Developer's Advertising or Marketing

✅ Analytics

▵ Product Personalization

(▵ = Select if you are using Recommendation or Personalization features)• Linked to the user's identity? YES ✅

• Tracking purposes? YES ✅[Usage Data]

✅ Product Interaction

❌ Advertising Data

❌ Other Usage Data✅ Developer's Advertising or Marketing

✅ Analytics

▵ Product Personalization

(▵ = Select if you are using Recommendation or Personalization features)• Linked to the user's identity? YES ✅

• Tracking purposes? YES ✅[Diagnostics]

✅ Crash Data

❌ Performance Data

❌ Other Diagnostic Data✅ App Functionality• Linked to the user's identity? YES ✅

• Tracking purposes? NO ❌❌ [Other Data]



Apple App Privacy [2]

https://docs.aiqua.appier.com/docs/apple-app-privacy



❌ Other Diagnostic Data✅ App Functionality• Linked to the user's identity? YES ✅

• Tracking purposes? NO ❌❌ [Other Data]

After you are done, you will see a preview of your app's privacy practices that will be shown to users in the app store.

Updated 8 months ago Table of Contents

Overview

App privacy manifest (iOS SDK 7.32.0 or later)

Data Collection

Part I: Select the Data Types Collected

Part II: Select How Each Data Type is Used

Part III: Answer Yes/No Questions

Data collection and usage



Production and Development Environments [0]

https://docs.aiqua.appier.com/docs/ios-production-and-development-environment



When integrating your app with the iOS SDK, it's important to take note of which environment you're using for push notification to be sent properly.

In the following diagram, we see that depending on the Debug/Release build configurations you have for your app, user data – including push permission tokens – are stored in separate databases on AIQUA and Apple Push Notification service (APNs).

The following sections describe points in the SDK integration process when you'll need to ensure that your environment configuration is correct.

The code for initializing the iOS SDK already includes a flag that conditionally sets the value of the setDevProfile parameter based on the app's build configuration. If you choose to not use the flag, note that:

If setDevProfile is true/YES, the user data will only be sent to the Dev DB. 

If setDevProfile is false/NO, the user data will only be sent to the Prod DB. 

When configuring iOS push certificates, if you're using .p12 files, you need to upload separate .p12 certificates for the two environments. If you're using .p8 files, only one certificate is

needed for both environments.

The APS environment key specifies which Apple Push Notification service (APNs) environment to use when registering for push notifications.

In your project's root directory, open the .entitlements file and verify that the value of APS environment corresponds to the environment you're developing for – either production or development.

See Apple's docs on the APS Environment Entitlement for details.

When you're ready to build and run your app, go to Xcode, click the build scheme, and select Edit Scheme. Use the Build Configuration drop-down list to select Debug or Release mode.

When sending iOS campaign from the AIQUA dashboard, you need to select whether you're using the Production Profile or Development Profile based on the app's build configuration. If the wrong profile is selected, the push notification won't be delivered.



Production and Development Environments [1]

https://docs.aiqua.appier.com/docs/ios-production-and-development-environment



The following pages on the AIQUA Dashboard list production and development environment data separately:

Account Name > Recent Users

Account Name > Recent Activity

Audiences > Segment List

Analytics 

Data sent to the Dev DB can be seen under the iOS Development, while data sent to the dev Prod DB can be seen under iOS Production. 

Updated 8 months ago Table of Contents

Overview

Initializing the SDK

Generating a Push Certificate

Configuring Xcode Project Settings

APS Environment Entitlement

Build Configuration

Sending Campaigns

Accessing Data on AIQUA Dashboard



Migrating to iOS SDK 7.10.0 or Later

https://docs.aiqua.appier.com/docs/migrating-to-ios-sdk-700



If you are using Appier iOS SDK 7.0.0 - 7.9.0 and you are upgrading to the latest SDK version, you need to follow the rich push migration instructions below to migrate. 

From SDK VersionsTo SDK Versions7.0.0 - 7.9.07.10.0 or above

In Appier iOS SDK 7.0.0, the dynamic framework AppierFramework was introduced to make integration easier. 

Starting from Appier iOS SDK 7.10.0:

For rich push, the Appier iOS SDK uses AppierExtensionFramework in Notification Service Extension and Notification Content Extension. The AppierFramework introduced in version 7.0.0 will no longer be supported in both extension targets starting from version 8.0.0.

The AppierFramework introduced in version 7.0.0 will only be used for the main app target.

To migrate your app to Appier iOS SDK 7.10.0, update the following parts of your project:

The Notification Service Extension

The Notification Content Extension

Your project's Podfile (if you use CocoaPods for package management)

Update the contents of the NotificationService.* files.

Remove Appier.framework or Appier.xcframework from AppierNotificationServiceExtension target > General tab > Frameworks and Libraries. 

Update the contents of the NotificationViewController.* files.

Remove Appier.framework or Appier.xcframework from AppierNotificationContentExtension target > General tab > Frameworks and Libraries. 

If your project uses CocoaPods for package management, update your Podfile to include AppierExtensionFramework, AppierNotificationServiceExtension , and AppierNotificationContentExtension .Updated over 1 year ago Table of Contents

Rich Push Migration

Notification Service Extension

Notification Content Extension

Podfile (CocoaPods only)



Troubleshooting and FAQs

https://docs.aiqua.appier.com/docs/ios-troubleshooting-faqs



When the user's Apple Push Notification service (APNs) token is invalid, APNs returns a 400 badDeviceToken error, meaning that the push notification can't reach the user. As a result, the following attribute may appear in the user's profile: reason: badDeviceToken.

This error can be caused by one of the following reasons:

An incorrect profile was selected in the Xcode build configuration settings.

An incorrect profile was selected when sending campaigns from the AIQUA Dashboard.

Invalid p8 or p12 push credentials.

To remove the reason attribute, the user must re-install the app to regenerate the APNS token.Updated over 1 year ago Table of Contents

Where does the user attribute "reason: badDeviceToken" come from?



Required Setup

https://docs.aiqua.appier.com/docs/ios-sdk-required-setup



Complete the following required setup before using the Appier iOS SDK. Once completed, the SDK will begin logging default user events and attributes and you'll be able to start using all of the SDK's features.

StepDescription1. Install the iOS SDKImport the Appier iOS SDK into your iOS project.2. Enable CapabilitiesAdd the Background Modes and App Groups capabilities to your app.3. Initialize the iOS SDKInitialize the iOS SDK in your project's AppDelegate file.4. App Tracking Transparency (iOS 14.5+)Request user permission to use their Advertising Identifier (IDFA) for improved data tracking with the AppTrackingTransparency framework.Updated over 1 year ago Troubleshooting and FAQsInstalling the iOS SDKDid this page help you?



Installing the iOS SDK [0]

https://docs.aiqua.appier.com/docs/installing-the-appier-ios-sdk-v2



Install the Appier iOS SDK using one of the following methods:

Installing with Swift Package Manager

Installing with CocoaPods

Manual installation (Not recommended)

📘Note

iOS apps using Firebase Cloud Messaging (FCM): You must integrate the Firebase SDK to your app in addition to the Appier iOS SDK.

Using a new notification service: If your app is already integrated with Apple Push Notification service (APNs), all of your existing iOS push subscribers will be lost if you switch to FCM. The same applies when switching your notification service from FCM to APNs.

Location tracking: AIQUA only tracks location if you properly initialize location services. Remember to add any key(s) required for requesting authorization for location services in info.plist.

Open your Xcode project and select File > Swift Packages > Add Package Dependency.

Input the following repository URL: https://github.com/appier/appier-ios-framework, then click Next.

For Rules, select Version and choose Up to Next Major and set the version number to 7.17.0 or later. We recommend using the latest version of the Appier iOS SDK, version 8.2.2.

In the next screen, under Package Product, select AppierFramework. If you plan to use push notifications, select AppierExtensionFramework as well.

Click Finish to complete the installation. 

For more details about adding dependencies, see Apple's documentation on Adding Package Dependencies to Your App.

Open your Xcode project and select File > Add Packages.

In the search bar, enter the following package URL: https://github.com/appier/appier-ios-framework

For Dependency Rule, choose Up to Next Major and set the version number to 7.17.0 or later. We recommend using the latest version of the Appier iOS SDK, version 8.2.2.



Installing the iOS SDK [1]

https://docs.aiqua.appier.com/docs/installing-the-appier-ios-sdk-v2



🚧artifact not found for target "AppierFramework"This error may occur for apps using iOS SDK 7.17.0 or earlier and developing on Xcode 13.3 or later because Swift Package Manager (SPM) requires the artifact name to match the target name.If you encounter this error, set appier-ios-framework's Dependency Rule to Branch with the branch name set to master.

In the next screen, under Package Product, select AppierFramework. If you plan to use push notifications, select AppierExtensionFramework as well.

Click Add Package to complete the installation.

Install CocoaPods version 1.10.0 or later

Create a Podfile

For instructions on completing these steps, see the CocoaPods Getting Started guide.

Add the AppierFramework dependency to your Podfile. We recommend using the latest version of the Appier SDK, version 8.2.2.

target 'PROJECT_TARGET' do

...

# Add the pod for the Appier SDK

pod 'AppierFramework', '8.2.2'

end

In the project directory, run the following commands to install the dependencies and create a new workspace:

$ pod repo update

$ pod install

Open the PROJECT_TARGET.xcworkspace file created by CocoaPods.

(For Objective C only): Go to Build Settings > Build Options and make sure Always Embed Swift Standard Libraries is set to Yes.

Import the following header to use the Appier Framework:

import Appier

#import 

📘NoteFor React Native or Flutter projects, you don't need to install the Appier iOS SDK in the main app target.

Download the SDK file listed on the AIQUA iOS SDK Integration Overview page.

Add the downloaded Appier.xcframework folder to your main app target. Go to Build Phases > Link Binary With Libraries, click +, then select Add Other... > Add Files... and choose the Appier.xcframework folder.

(For Objective-C only) Go to Build Settings > Build Options and make sure Always Embed Swift Standard Libraries is set to Yes.

Go to General > Frameworks, Libraries, and Embedded Content, select Appier.xcframework and set the Embed option to Embed & Sign.



Installing the iOS SDK [2]

https://docs.aiqua.appier.com/docs/installing-the-appier-ios-sdk-v2



Import the following header to use the Appier Framework:

import Appier

#import 

Updated over 1 year ago Table of Contents

Installing with Swift Package Manager

Xcode 12.5.1 or earlier

Xcode 13 or later

Installing with Cocoapods

Prerequisites

1. Add the Appier SDK pod to your Podfile

2. Create your workspace

Usage

Manual installation (Not recommended)



Enabling Capabilities

https://docs.aiqua.appier.com/docs/enabling-capabilities



After installing the iOS SDK, you need to follow the steps to enable the capabilities required for user tracking and the APNS token and enable App Group to initialize the SDK.

🚧ImportantOnly do this for the main application target. Do not do this for Service Extension or Content Extension.

Go to Project > Main Target > Signing & Capabilities.

Click + Capability, enable Background Modes, and select the following checkboxes:

Background fetch

Remote notifications

Click + Capability and enable Push Notifications.

You will see that the following capabilities are enabled.

Under the All tab, click + Capability, add an App Group and enter the App Group ID (hereby referred to as APPIER_APP_GROUP_ID). 

👍What is my APPIER_APP_GROUP_ID (App Group ID)?The APPIER_APP_GROUP_ID is "group.YOUR_BUNDLE_ID.notification". For example, if your iOS Bundle Identifier is "com.appier.docs.SampleProject", your APPIER_APP_GROUP_ID is "group.com.appier.docs.SampleProject.notification".

🚧Important:

If you want to change your App Group ID, make sure you are using iOS SDK 7.7.0 or above. In earlier SDK versions, changing the App Group ID will result in iOS users being duplicated.

This App Group ID will later be used when setting up SDK initialization and rich push notifications. Be sure to use the same App Group ID you've entered here.

Updated over 1 year ago



Initializing the iOS SDK [0]

https://docs.aiqua.appier.com/docs/initializing-the-ios-sdk



To initialize the SDK, have your Appier APP ID and App Group ID ready.

The APPIER_APP_ID of your AIQUA account can be found in the Account Settings page.

The APPIER_APP_GROUP_ID is the APP Group ID entered when enabling App Group.

To get started with the Appier iOS SDK, you can check APIs in QGSdk.h. All the APIs are documented in this file.

📘User data permissions

iOS SDK 7.31.0 and earlier: The device's IDFA is collected by default.

iOS SDK 7.32.0 or later: The device's IDFA is not collected by default.

If your app uses an SDK version prior to 7.32.0 and requires limitations on user data collection for data privacy regulation compliance, see iOS User Data Permissions to learn how to configure data collection settings before initializing the SDK.

Open your AppDelegate file.

Be sure to import the Appier headers:

Swift: import Appier

Objective-C (for SDK 7.0.0 or above): #import 

📘Note:If you are using Objective-C with SDK 5.x.x or below, use #import "QGSdk.h".

Add the code snippets below to initialize the SDK. It initializes the SDK using the onStart method. It is recommended to do this inside your app launch didFinishLaunchingWithOptions method. The SDK initialization will request for a push notification token using registerForRemoteNotifications. 

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {



// Override point for customization after application launch

let QG = QGSdk.getSharedInstance()

#if DEBUG

QG.onStart("APPIER_APP_ID", withAppGroup:"APPIER_APP_GROUP_ID", setDevProfile: true)

#else

QG.onStart("APPIER_APP_ID", withAppGroup:"APPIER_APP_GROUP_ID", setDevProfile: false)

#endif

return true

}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

// Override point for customization after application launch.

QGSdk *qgsdk = [QGSdk getSharedInstance];

#ifdef DEBUG



Initializing the iOS SDK [1]

https://docs.aiqua.appier.com/docs/initializing-the-ios-sdk



// Override point for customization after application launch.

QGSdk *qgsdk = [QGSdk getSharedInstance];

#ifdef DEBUG

[qgsdk onStart:@"APPIER_APP_ID" withAppGroup:@"APPIER_APP_GROUP_ID" setDevProfile:YES];

#else

[qgsdk onStart:@"APPIER_APP_ID" withAppGroup:@"APPIER_APP_GROUP_ID" setDevProfile:NO];

#endif

return YES;

}

The code also includes the parameter setDevProfile that sets the development and production profiles to avoid confusion while uploading your app to the App Store.

🚧Important:

The APP Group ID must be the same ID used when you enabled the App Group.

If you want to use a new App Group ID, make sure you are using iOS SDK 7.7.0 or above. In earlier SDK versions, changing the App Group ID will result in iOS users being duplicated.

After finishing the initialization steps above, you can test if the iOS SDK can be initialized successfully.

Build your app and make sure it builds without error.

On AIQUA dashboard, click your account name in the lower-left corner, select Recent Activity. Under iOS Production or iOS Development, you should see an app_launched event. 

📘Note:Events from your development build (for debug and testing) should be seen under the iOS DEVELOPMENT tab, while events from your production build (for release) should be seen under the iOS PRODUCTION tab. For more details about productions and development environments, see iOS Production and Development Environment.

If you do not see an app_launched event, here are some possible reasons. 

It may take up to 5 minutes for the event to show up on AIQUA dashboard. Check again in 5 minutes.

Make sure the APPIER_APP_ID and APPIER_APP_GROUP_ID are correct.

Updated about 1 year ago Table of Contents

Initializing the iOS SDK

Checkpoint

Troubleshooting



App Tracking Transparency (iOS 14.5+) [0]

https://docs.aiqua.appier.com/docs/app-tracking-transparency



📘Note:Support for App Tracking Transparency requires iOS SDK 7.9.0 or above.

Starting with iOS 14.5, Apple now requires app to ask for permission to track users using the device's advertising identifier (IDFA). See https://developer.apple.com/app-store/user-privacy-and-data-use/.

To do this, you will need to use the App Tracking Transparency framework provided by Apple. Once the App Tracking Transparency framework is integrated, users will see a dialog box that asks for permission to track them.

Below is a brief summary on how to integrate the AppTrackingTransparency framework, but be sure to go through Apple's official documents on AppTrackingTransparency framework for more details.

In your project’s info.plist file, add an NSUserTrackingUsageDescription key. Write a message describing the purpose for tracking user data that is specific to your use case. ​The message shown below is just an example. 

NSUserTrackingUsageDescription

This allows us to serve personalized contents and ads based on your browsing pattern across apps and websites.

This message will be displayed on the dialog box to request user permission.

To request user's permission for tracking, add the AppTrackingTransparency framework to your app. Below is an example of requesting for user's permission at app launch.

import AppTrackingTransparency

@available(iOS 14, *)

func askATTPermission() {

ATTrackingManager.requestTrackingAuthorization { _ in

...

}

}

#import 

- (void)askATTPermission API_AVAILABLE(ios(14)) {

[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:^(ATTrackingManagerAuthorizationStatus status) {

...

}];

}

If the user chooses to allow tracking, an ATTrackingManagerAuthorizationStatusAuthorized value will be returned. See Apple's documentation for details on the authorization values available.



App Tracking Transparency (iOS 14.5+) [1]

https://docs.aiqua.appier.com/docs/app-tracking-transparency



If you want Appier SDK to collect IDFA only when an "Authorized" status is returned, call the setIDFAConsent method and set it to true for Swift or YES for Objective-C.

If setIDFAConsent is set to false or NO, Appier SDK will collect IDFA regardless of user's authorization status. However, depending on the user's authorization status, the IDFA collected may be valid or invalid (e.g. 00000000-0000-0000-0000-000000000000). The same applies if setIDFAConsent is not set.

import Appier

func sendingIDFAWhenAuthorized() {

let qgsdk = QGSdk.getSharedInstance()

// If true, IDFA is sent ONLY if the user authorizes tracking

// If false or not set, IDFA is sent regardless of user's authorization status

qgsdk.setIDFAConsent(true)

}

#import 

- (void)sendingIDFAWhenAuthorized {

QGSdk *qgsdk = [QGSdk getSharedInstance];

// If true, IDFA is sent ONLY if the user authorizes tracking

// If false or not set, IDFA is sent regardless of user's authorization status

[qgsdk setIDFAConsent:YES];

}

Updated over 1 year ago Table of Contents

Integrate the AppTrackingTransparency framework

Add usage description to info.plist

Request authorization to track

Sending IDFA based on authorization status



iOS User Data Permission Controls [0]

https://docs.aiqua.appier.com/docs/ios-user-data-permissions



📘Required SDK versionUser data permission controls are only available on iOS SDK 7.30.0 or later.

To allow your app to comply with data privacy policies and regulations, the Appier iOS SDK allows you to manage user data permissions for the following types of data:

Identifier for Advertising (IDFA): Collection disabled by default starting from iOS SDK 7.32.0. In earlier SDK versions, IDFA collection is enabled by default.

Location data: Collection is disabled by default.

You can enable or disable collection for this data at any point in your app's lifecycle, even before the Appier SDK is initialized, and the changes will be effective immediately. For example, you may want to update user data collection settings in the following scenarios:

After the app is launched

After a user has responded to a data collection consent prompt

After regenerating the user's Appier ID

After a user logs in or logs out of their account

The dataTrackingConfig property contains the SDK's current data permissions settings. The default definition for dataTrackingConfig is defined as follows:

class AIQDataTrackingConfiguration: NSObject {

public var isCollectIDFA: Bool // IDFA collection disabled by default starting from v7.32.0

public var isCollectLocation: Bool // Location data collection disabled by default

}

// Get current settings for IDFA

let isCollectingIDFA: Bool = QGSdk.getSharedInstance().dataTrackingConfig.isCollectIDFA

// Get current settings for location data

let isCollectingLocation: Bool = QGSdk.getSharedInstance().dataTrackingConfig.isCollectLocation

// Get current settings for IDFA

BOOL isCollectingIDFA = [QGSdk getSharedInstance].dataTrackingConfig.isCollectIDFA;

// Get current settings for location data

BOOL isCollectingLocation = [QGSdk getSharedInstance].dataTrackingConfig.isCollectLocation;

let config = QGSdk.getSharedInstance().dataTrackingConfig

AIQDataTrackingConfiguration config = [QGSdk getSharedInstance].dataTrackingConfig;

// Enable IDFA collection permissions



iOS User Data Permission Controls [1]

https://docs.aiqua.appier.com/docs/ios-user-data-permissions



AIQDataTrackingConfiguration config = [QGSdk getSharedInstance].dataTrackingConfig;

// Enable IDFA collection permissions

QGSdk.getSharedInstance().dataTrackingConfig.isCollectIDFA = true

// Enable location data collection permissions

QGSdk.getSharedInstance().dataTrackingConfig.isCollectLocation = true

// Enable IDFA collection permissions

[QGSdk getSharedInstance].dataTrackingConfig.isCollectIDFA = YES;

// Enable location data collection permissions

[QGSdk getSharedInstance].dataTrackingConfig.isCollectLocation = YES;

To set all data permissions simultaneously, instantiate an AIQDataTrackingConfiguration instance and assign it to dataTrackingConfig:

let trackingConfig: AIQDataTrackingConfiguration = AIQDataTrackingConfiguration(isCollectIDFA: false, isCollectLocation: false) // Instantiate an AIQDataTrackingConfiguration instance

trackingConfig.isCollectIDFA = true // The settings won't be applied since they're not assigned to QG.

QGSdk.getSharedInstance().dataTrackingConfig = trackingConfig // Save the new settings.

AIQDataTrackingConfiguration *trackingConfig = [[AIQDataTrackingConfiguration alloc] initWithIsCollectIDFA:NO isCollectLocation:NO];

trackingConfig.isCollectIDFA = YES; // The settings won't be applied since it's not assiged to QG.

[QGSdk getSharedInstance].dataTrackingConfig = trackingConfig; // The settings takes effect.

Updated about 1 year ago Table of Contents

Overview

dataTrackingConfig property

Retrieving data permission settings

Retrieving individual permission settings

Retrieving all permission settings

Setting data permission settings

Setting individual permissions

Setting all permissions



Logging Custom User Data for iOS

https://docs.aiqua.appier.com/docs/event-tracking-and-attribution-for-ios



👍See the Custom Events and Attributes for detailed guidelines on defining and logging custom data.

Custom user data consists of free-form attributes and events that you can define depending on your business needs. Custom data isn't collected by the Appier SDK by default; instead, these custom events and attributes must be manually logged using the SDK methods described in the following pages:

Logging Custom User Attributes for iOS 

Logging Custom User Events for iOS 

To understand how campaign events are attributed under default settings and how to adjust the default attribution window, see Event Attribution for iOS.Updated over 1 year ago iOS User Data Permission ControlsLogging Custom User AttributesTable of Contents

Overview

Event attribution



Logging Custom User Attributes [0]

https://docs.aiqua.appier.com/docs/logging-user-profile-information-for-ios-sdk



👍See the Custom Events and Attributes for detailed guidelines on defining and logging custom data.

User attributes are pieces of information that describe a user, such as their name, city, or date of birth. Log user attributes to allow marketers to segment and filter users based on their attributes.

The Appier iOS SDK provides built-in methods to track common attributes such as name, email, and phoneNo, but you can also use custom keys to track other attributes that don't have a dedicated method (such as birthday or vip_level).

The iOS SDK provides the following built-in methods for logging user attributes:

(void)setUserId:(NSString *)userId; 

(void)setName:(NSString *)name; 

(void)setFirstName:(NSString *)name;

(void)setLastName:(NSString *)name;

(void)setCity:(NSString *)city;

(void)setEmail:(NSString *)email;

(void)setDayOfBirth:(NSNumber *)day;

(void)setMonthOfBirth:(NSNumber *)month;

(void)setYearOfBirth:(NSNumber *)year;

(void)setPhoneNumber:(NSString *)phoneNo; (This method is only supported on iOS SDK 7.8.0 or later)

In the following example, setName() is used to set a user's name attribute:

// Sets the user's `name` attribute to "John Doe"

QGSdk.getSharedInstance().setName("John Doe")

// Sets the user's `name` attribute to "John Doe"

[[QGSdk getSharedInstance] setName:@"John Doe"];

📘NoteSetting an attribute to null may result in unexpected segmentation behavior.

To clear the value of an attribute with a built-in method that accepts NSString *, log an empty string ("")

You can't clear the values of an attributes using built-in methods that accept NSNumber *

// Resets the user's `name` attribute by logging an empty string

QGSdk.getSharedInstance().setName("")

// Resets the user's `name` attribute by logging an empty string

[[QGSdk getSharedInstance] setName:@""];

Aside from the built-in methods, you can also specify which user attributes to log using custom keys using the following method:

(void)setCustomKey:(NSString *)key withValue:(id)value;



Logging Custom User Attributes [1]

https://docs.aiqua.appier.com/docs/logging-user-profile-information-for-ios-sdk



(void)setCustomKey:(NSString *)key withValue:(id)value;

In the following example, setCustomKey() is used to set the user's current rating:

// Sets the value of the `rating` attribute to "5"

QGSdk.getSharedInstance().setCustomKey("rating", withValue: "5")

// Sets the value of the `rating` attribute to nil

QGSdk.getSharedInstance().setCustomKey("rating", withValue: nil)

// Sets the value of the `rating` attribute to "5"

[[QGSdk getSharedInstance] setCustomKey:@"rating" withValue:@"5"];

// Sets the value of the `rating` attribute to nil

[[QGSdk getSharedInstance] setCustomKey:@"rating" withValue:nil];

📘NoteSetting an attribute to null may result in unexpected segmentation behavior.

To clear the value of a user attribute with setCustomKey(), log an empty string ("") or NSNull.

// Clears the user's `rating` attribute by logging NSNull

QGSdk.getSharedInstance().setCustomKey("rating", withValue: NSNull.init())

// Clears the user's `rating` attribute by logging an empty string

QGSdk.getSharedInstance().setCustomKey("rating", withValue: "")

// Clears the user's `rating` attribute by logging NSNull

[[QGSdk getSharedInstance] setCustomKey:@"rating" withValue:[NSNull null]];

// Clears the user's `rating` attribute by logging an empty string

[[QGSdk getSharedInstance] setCustomKey:@"rating" withValue:@""];

Follow the steps below to validate that attributes are being logged properly.

Launch your app.

On the AIQUA dashboard, click your account name in the lower-left corner, then click Recent Users.

Under the iOS Production or iOS Development section (depending on which environment your app is using) you should see the user attributes after a few minutes.

Updated over 1 year ago Table of Contents

Using built-in methods

Example: Built-in method

Clearing attribute values using built-in methods

Using custom keys

Example: Custom keys

Clearing attribute values using setCustomKey()

Checkpoint: Validating attributes have been logged



Logging Custom User Events [0]

https://docs.aiqua.appier.com/docs/logging-events-with-parameters-for-ios-sdk



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

User events are the actions users perform on your app. Logging user events enables marketers to create segments by filtering users based on their events.

The iOS SDK provides the following overloaded logEvent() methods, which allow you to log custom events, with or without any associated event parameters, valueToSum, or valueToSumCurrency:

(void)logEvent:(NSString *)name;

(void)logEvent:(NSString *)name withParameters:(NSDictionary *)parameters;

(void)logEvent:(NSString *)name withParameters:(NSDictionary *)parameters withValueToSum:(NSNumber *)valueToSum;

(void)logEvent:(NSString *)name withParameters:(NSDictionary *)parameters withValueToSum:(NSNumber *)valueToSum withValueToSumCurrency:(NSString *)vtsCurr;

ParameterDescriptionnameRequired. See the guidelines on field names for custom data for limitations on eventName.parametersOptional. parameters must be a flat JSON object; it can't contain any nested JSON objects or arrays. See the Data Logging Guidelines for more details and limitations.valueToSum and valueToSumCurrencyOptional. The monetary value associated with this event. See valueToSum and valueToSumCurrency.

Include valueToSum when logging an event to track the monetary value associated with the event (e.g. the total conversion value associated with a checkout_completed event), and log valueToSumCurrency to specify an ISO 4217 currency code.

👍If the event is attributed to a campaign, valueToSum will be included in the total attributed value of the campaign's performance report.

See the following sections for examples on how to include valueToSum and valueToSumCurrency when logging custom events:

Logging events with parameters, valueToSum

Logging events with parameters, valueToSum and valueToSumCurrency

QGSdk.getSharedInstance().logEvent("event_name")

[[QGSdk getSharedInstance] logEvent:@"event_name"];

var event: [String: Any] = [:]

event["num_products"] = "1"

event["my_param"] = "some_value"



Logging Custom User Events [1]

https://docs.aiqua.appier.com/docs/logging-events-with-parameters-for-ios-sdk



var event: [String: Any] = [:]

event["num_products"] = "1"

event["my_param"] = "some_value"

event["some_other_param"] = 123

event["another_param"] = 123.45

event["unknown_param"] = NSNull.init()

event["empty_param"] = ""

QGSdk.getSharedInstance().logEvent("event_name", 

withParameters: event)

NSMutableDictionary *event = [[NSMutableDictionary alloc] init];

[event setObject:@"1" forKey:@"num_products"];

[event setObject:@"some_value" forKey:@"my_param"];

[event setObject:[NSNumber numberWithInt:123] forKey:@"some_other_param"];

[event setObject:[NSNumber numberWithFloat:123.45] forKey:@"another_param"];

[event setObject:[NSNull null] forKey:@"unknown_param"];

[event setObject:@"" forKey:@"empty_param"];

[[QGSdk getSharedInstance] logEvent:@"event_name" 

withParameters:event];

var event: [String: Any] = [:]

event["my_param"] = "some_value"

QGSdk.getSharedInstance().logEvent("event_name", 

withParameters: event, 

withValueToSum: 123.45)

NSMutableDictionary *event = [[NSMutableDictionary alloc] init];

[event setObject:@"some_value" forKey:@"my_param"];

[[QGSdk getSharedInstance] logEvent:@"event_name" 

withParameters:event 

withValueToSum:[NSNumber numberWithFloat:123.45]];

var event: [String: Any] = [:]

event["my_param"] = "some_value"

QGSdk.getSharedInstance().logEvent("event_name", 

withParameters: event, 

withValueToSum: 123.45, 

withValueToSumCurrency: "USD")

NSMutableDictionary *event = [[NSMutableDictionary alloc] init];

[event setObject:@"some_value" forKey:@"my_param"];

[[QGSdk getSharedInstance] logEvent:@"event_name" 

withParameters:event 

withValueToSum:[NSNumber numberWithFloat:123.45] 

withValueToSumCurrency:@"USD"];

Follow the steps below to validate that your app is logging events properly.

Launch your app and complete the action(s) that log the event.

On the AIQUA Dashboard, click your account name in the lower-left corner and go to Recent Activity.

Under the iOS Development tab, you should see the event. It can take several minutes for the event to display on the AIQUA Dashboard.



Logging Custom User Events [2]

https://docs.aiqua.appier.com/docs/logging-events-with-parameters-for-ios-sdk



Updated over 1 year ago Table of Contents

Overview

valueToSum and valueToSumCurrency

Event logging examples

Logging events (event name only)

Logging events with parameters

Logging events with parameters and valueToSum

Logging events with parameters, valueToSum, and valueToSumCurrency

Checkpoint: Validate that events are logged properly



Event Attribution

https://docs.aiqua.appier.com/docs/event-attribution-ios-sdk



To track how notifications are affecting the metrics on your app, events attributed to campaign notifications are listed as attributed events in the Campaign Performance page. 

An event can be attributed to a campaign based on:

View-Through Attribution: If the event happens within 1 hour after the user receives a notification, AIQUA attributes it as a view-through. 

Click-Through Attribution: If the event happens within 24 hours after the user clicks on a notification, AIQUA attributes it as a click-through. 

For more details on how event attribution works, see Understanding Event Attribution.

By default, the click-through attribution window (time interval) is set to 86,400 seconds (24 hours) while the view-through attribution window is set to 3,600 seconds (1 hour). 

You can change this time window using the following APIs. The event attribution window will apply to both iOS app push campaigns and iOS in-app campaigns. 

// to set click through attribution window

(void)setClickAttributionWindow:(NSInteger)seconds;

// to set view through attribution window 

(void)setAttributionWindow:(NSInteger)seconds;

To set a custom attribution window interval, specify a value for seconds.

Below is an example of setting the click-through attribution window to 12 hours (43200 seconds):

QGSdk.getSharedInstance().setClickAttributionWindow(43200)

[[QGSdk getSharedInstance] setClickAttributionWindow:43200];

Below is an example of setting the view-through attribution window to 2 hours (7200 seconds):

QGSdk.getSharedInstance().setAttributionWindow(7200)

[[QGSdk getSharedInstance] setAttributionWindow:7200];

📘Note:Starting from iOS SDK v7.6.0, view-through and click-through attribution window CANNOT be set to 0. If set to 0, the attribution window will fall back to its default value.Updated over 1 year ago Table of Contents

Adjusting Attribution Window



iOS In-App Campaigns

https://docs.aiqua.appier.com/docs/in-app-campaigns-for-ios



An in-app campaign, unlike push notifications that are delivered outside of the app, is delivered to your users when they are using your app.

The Appier SDK supports two types of in-app campaigns: pop-up and inbox.

In-app pop-up notifications pop up inside your app. The Appier SDK supports various types of in-app popup creatives.

1 - Floating Text

2- Small Content Box

3- Medium Image

4- Fullscreen

In-app inbox notifications let you display offers and notify users of important updates in-app without sending them push notifications or showing pop-up notifications.

Updated over 1 year ago



In-App Pop-Up Campaigns [0]

https://docs.aiqua.appier.com/docs/in-app-popup-notifications-for-ios-sdk



The Appier SDK supports in-app notifications starting from the SDK version 2.0.0 and has two types: text and image. In-app campaigns can be created on the AIQUA dashboard.

These notifications are shown based on the log events the app sends through our SDK, and the matching conditions of the in-app campaigns. Make sure to send the appropriate log event, with a parameter or valueToSum if applicable, for in-app notifications to work.

📘NoteiOS in-app campaigns are only supported for apps provisioned with Apple's distribution (production) certificate.

In-app notifications are enabled by default. You can enable or disable it anytime using this method:

- (void)disableInAppCampaigns:(BOOL)disabled;

Here's an example for disabling in-app notifications:

QGSdk.getSharedInstance().disable(inAppCampaigns: true)

[[QGSdk getSharedInstance] disableInAppCampaigns:YES];

Disabling it restricts the device from getting any new in-app campaigns. It also disables in-app notifications from being drawn. To enable it again, pass NO or false as below:

QGSdk.getSharedInstance().disable(inAppCampaigns: false)

[[QGSdk getSharedInstance] disableInAppCampaigns:NO];

For all in-app notifications, you can configure a deep link URL from the dashboard while creating an in-app campaign.

There is a tap event defined on text and image in-app notifications. When the user taps on a text on or clicks on an image, and if there is a valid deep link, you'll get a call back in your AppDelegate.m using any of these methods:

func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool

- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options;

Here, you can implement a deep link with the URL.

To clear all the foreground in-app pop-ups, call hideInAppCampaigns():

- (void)hideInAppCampaigns;

The following example hides all in-app pop-ups:

QGSdk.getSharedInstance().hideInAppCampaigns()

QGSdk *qgsdk = [QGSdk getSharedInstance];

[qgsdk hideInAppCampaigns];



In-App Pop-Up Campaigns [1]

https://docs.aiqua.appier.com/docs/in-app-popup-notifications-for-ios-sdk



QGSdk.getSharedInstance().hideInAppCampaigns()

QGSdk *qgsdk = [QGSdk getSharedInstance];

[qgsdk hideInAppCampaigns];

To display the in-app campaign again, log the trigger event. Frequency cap limitations apply.Updated 8 months ago Table of Contents

Overview

Disabling in-app pop-up campaigns

Clearing all foreground in-app pop-up notifications



In-App Inbox Campaigns [0]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



🚧NoteIn-app inbox campaigns are a beta feature. While this feature is currently available for use, you may encounter occasional bugs or stability issues.

📘Prerequisites

Complete the required setup for the Appier iOS SDK.

Create an in-app campaign on the AIQUA dashboard with the campaign type set to Inbox.

In-app inbox campaigns allow you to fetch notifications from AIQUA and store them on local device storage. You can choose how and when to display locally-stored notifications to app users without having to rely on push notifications or pop-up campaigns.

Use the iOS SDK's QGInbox class to implement inbox notifications in your app.

Inbox notifications differ from pop-up notifications and push notifications in several ways. Namely, inbox notifications can be:

Fetched using an SDK method: Fetch new notifications using fetchInboxMessages(). Other notification types can't be fetched with SDK methods. Instead, they are received by the device after AIQUA delivers the campaign.

Delivered silently: Other notification types are displayed to the user as soon as the campaign is delivered. With inbox campaigns, you can silently retrieve notifications and choose how and when to display the locally-stored notifications to app users.

Stored on the device: On every app launch, the SDK fetches and stores the latest notifications in the inbox using the device's local storage. Stored inbox notifications can then be retrieved from local device storage using getInboxesWithStatusRead().

The iOS SDK doesn't automatically log impression and click events for inbox notifications. To view in-app inbox campaign performance data on the AIQUA Dashboard, inbox notification impression and click events must be logged manually using logEvent().

Using inbox notifications, we'd like to implement a message center in our app. The message center will contain messages notifying our users of app updates and product announcements. We're using inbox notifications for this feature so that:



In-App Inbox Campaigns [1]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



We can receive new messages without interrupting the user, since inbox notifications are retrieved silently by default.

Messages are stored in the inbox using local device storage, so users can choose to view the messages at any time by navigating to the app's message center.

To use the iOS SDK methods to implement the message center described above, follow these steps:

StepDescription1(Optional) Change the message capacity of the inbox in your app using updateInboxRecord().

By default, the inbox capacity is set to 50.2When the app is launched, new inbox notifications are automatically fetched from AIQUA. These notifications will be stored on the device for later retrieval.

You can a call fetchInboxMessages() at any time to retrieve the latest inbox notifications.3When a user navigates to the message center, get a list all locally-stored messages to display on the screen using getInboxesWithStatusRead().4(Optional) Log a qg_inapp_displayed event for each displayed message.

Logging this event will allow you to view this campaign performance metric on the AIQUA Dashboard.5

When a user clicks on a message in the message center, retrieve that message's contents from the array returned by getInboxesWithStatusRead() and display it to the user.

After a message has been read, update the message's status to READ using updateStatus().

6(Optional) Log a qg_inapp_clicked event for the clicked message.

Logging this event will allow you to view this campaign performance metric on the AIQUA Dashboard.

In our message center, we want to include a force refresh button that a user can click to fetch the latest messages. To accomplish this, we'll employ the following SDK methods:

fetchInboxMessages(): Fetches new messages from AIQUA's servers and saves them locally.

getInboxesWithStatusRead(): Returns a list of all locally-saved messages and their metadata.

The following code sample demonstrates how to implement a force refresh:

// Fetch the latest inbox notifications from AIQUA's servers



In-App Inbox Campaigns [2]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



// Fetch the latest inbox notifications from AIQUA's servers

QGSdk.getSharedInstance().fetchInboxMessages { (success, err) in

// Update UI views based on the status if needed

// Get the list of all the locally-saved messages

let list:[QGInbox] = QGSdk.getSharedInstance().getInboxesWithStatusRead(true, statusUnread: true, statusDeleted: true)

}

// Fetch the latest inbox notifications from AIQUA's servers

[[QGSdk getSharedInstance] fetchInboxMessages:^(BOOL success, NSError * _Nullable error) {

// Update UI views based on the status if needed

// Get the list of all the locally-saved messages

NSArray *inboxList = [[QGSdk getSharedInstance] getInboxesWithStatusRead:YES statusUnread:YES statusDeleted:YES];

}];

Each inbox notification is an instance of the QGInbox class and contains the following properties:

/*!

@abstract

An image url



@discussion

This is an image URL related to the inbox message

*/

@property (nonatomic, readonly, copy) NSString *image;

/*!

@abstract

The notification's title

*/

@property (nonatomic, readonly, copy) NSString *title;

/*!

@abstract

The content of the notification

*/

@property (nonatomic, readonly, copy) NSString *text;

/*!

@abstract

Deep link url

*/

@property (nonatomic, readonly, copy) NSString *deepLink;

/*!

@abstract

Custom parameters(Key, Value) for the inbox message

*/

@property (nonatomic, readonly, copy) NSDictionary *qgPayload;

/*!

@abstract

The inbox message's unique identifier

*/

@property (nonatomic, readonly, copy) NSNumber *notificationId;

/*!

@abstract

Expiration time of the inbox message. If current time exceed it, the inbox message should be removed

*/

@property (nonatomic, readonly) long long endTime;

/*!

@abstract

Starting time for the inbox message. It is supposed to be smaller than endTime

*/

@property (nonatomic, readonly) long long startTime;

/*!

@abstract

The current state of the notification. Ex: Unread (Default), Read, Deleted

*/

@property (nonatomic, readonly) QGInboxStatus status;



In-App Inbox Campaigns [3]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



*/

@property (nonatomic, readonly) QGInboxStatus status;

📘Receiving key-value pairsIf you're sending key-value pairs with your inbox notifications, you can access them in the qgPayload dictionary.

Use the following class methods to implement inbox notifications in your app:

updateInboxRecord(): Set the maximum number of notifications to store locally

fetchInboxMessages(): Fetch inbox notifications from AIQUA

getInboxesWithStatusRead(): Get locally-stored inbox notifications

updateStatus(): Update the status of an inbox notification

logEvent(): Logging impressions and click events for an inbox notification

Sets the maximum number of notifications to store locally. Please note that the following operations can potentially delete locally stored notifications:

If the number of stored notifications exceeds the storage limit while fetching new notifications, the oldest notification(s) will be deleted

If you change the storage limit to a size smaller than the number of currently stored notifications, the oldest notification(s) will be deleted

In the QGInbox class, use the enum QGInboxLimit to set the storage limit in the SDK. By default, the limit is set to QGInboxLimitSmall with a maximum capacity of 50 notifications.

QGInbox uses the following enumeration to define inbox capacities:

typedef NS_ENUM(NSInteger, QGInboxLimit) {

QGInboxLimitSmall = 50,

QGInboxLimitMedium = 120,

QGInboxLimitHigh = 300,

QGInboxLimitExtraHigh = 600

};

The following line limits the number of locally-stored inbox messages to 300.

QGSdk.getSharedInstance().updateInboxRecord(.high)

[[QGSdk getSharedInstance] updateInboxRecordLimit:QGInboxLimitHigh];

An asynchronous method that fetches new inbox notifications from AIQUA's servers and saves them locally as a list of QGInbox objects, then activates a completion handler notifying of the success or failure of the operation.

QGSdk.getSharedInstance().fetchInboxMessages({ success, error in

print("fetching inbox messages success: \(success)")

})

// new, added by Michael



In-App Inbox Campaigns [4]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



print("fetching inbox messages success: \(success)")

})

// new, added by Michael

[[QGSdk getSharedInstance] fetchInboxMessages:^(BOOL success, NSError * _Nullable error) {

NSLog(@"fetching inbox messages success: %d", success);

}];

QGSdk.getSharedInstance().getInboxesWithStatusRead(true, statusUnread: true, statusDeleted: false)

[[QGSdk getSharedInstance] getInboxesWithStatusRead:YES statusUnread:YES statusDeleted:NO];

A synchronous method that returns a list of QGInbox object representing locally-stored inbox notifications. The function parameters are described in the following table:

NameDescriptionstatusRead• true: Include inbox notifications with the status "Read"

• false: Exclude inbox notifications with the status "Read"statusUnread• true: Include inbox notifications with the status "Unread"

• false: Exclude inbox notifications with the status "Unread"statusDeleted• true: Include inbox notifications with the status "Deleted"

• false: Exclude inbox notifications with the status "Deleted"

👍TipAlthough the latest inbox messages are fetched whenever the app is launched, you should call fetchInboxMessages() before calling getInboxesWithStatusRead() if you want to retrieve the latest messages from AIQUA's servers.

You can return a list of inbox notifications depending on the notification's status.

For example, you can make the following method call to get list of all inbox notifications that have been read and deleted (both statusRead and statusDeleted are true).

let messages: [QGInbox] = QGSdk.getSharedInstance().getInboxesWithStatusRead(true, statusUnread: false, statusDeleted: true)

NSArray *messages = [[QGSdk getSharedInstance] getInboxesWithStatusRead:YES statusUnread:NO statusDeleted:YES];

func update(_ newStatus: QGInboxStatus)

- (void)updateStatus:(QGInboxStatus)newStatus;

Updates the notification's status to one of "Read", "Unread" or "Deleted", using the flags defined in the following enumeration:

typedef NS_ENUM(NSInteger, QGInboxStatus) {

QGInboxStatusUnread = 0,

QGInboxStatusRead,



In-App Inbox Campaigns [5]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



typedef NS_ENUM(NSInteger, QGInboxStatus) {

QGInboxStatusUnread = 0,

QGInboxStatusRead,

QGInboxStatusDeleted

};

For example, if the user reads, then deletes a message, the status flags can be updated using two calls to updateStatus():

let listInbox: [QGInbox] = QGSdk.getSharedInstance().getInboxesWithStatusRead(true, statusUnread: true, statusDeleted: true)

let first: QGInbox = listInbox[0]

first.updateStatus(.deleted) // Set status to "Deleted"

first.updateStatus(.read) // Set status to "Read"

NSArray *listInbox = [[QGSdk getSharedInstance] getInboxesWithStatusRead:NO statusUnread:NO statusDeleted:YES];

QGInbox *first = [listinbox objectAtIndex:0];

[first updateStatus:QGInboxStatusDeleted]; // Set status to "Deleted"

[first updateStatus:QGInboxStatusRead]; // Set status to "Read"

Use logEvent() to log the following types of event for inbox notifications:

Custom events

Campaign performance events (clicks and impressions) that you want to view on the AIQUA Dashboard

📘NoteWhen logging any event for an inbox notification, the notification's notificationId is automatically added as an event parameter by the Appier SDK.

func logEvent(_ name: String?, withParameters parameters: [AnyHashable : Any]?, withValueToSum valueToSum: NSNumber?, withValueToSumCurrency vtsCurr: String?)

- (void)logEvent:(NSString *)name withParameters:(nullable NSDictionary *)parameters withValueToSum:(nullable NSNumber *) valueToSum withValueToSumCurrency:(nullable NSString *)vtsCurr;

When using logEvent() to log custom events, include any additional event parameters as defined in your custom event schema.

The following code sample retrieves all read inbox messages, then logs a custom event with a parameter for the first message:

let listInbox: [QGInbox] = QGSdk.getSharedInstance().getInboxesWithStatusRead(true, statusUnread: false, statusDeleted: false)

let first: QGInbox = listInbox[0]

first.logEvent("CUSTOM_EVENT_NAME", withParameters: ["PARAMETER": "PARAMETER_VALUE"], withValueToSum: nil, withValueToSumCurrency: nil)



In-App Inbox Campaigns [6]

https://docs.aiqua.appier.com/docs/in-app-inbox-notifications-for-ios



NSArray *listInbox = [[QGSdk getSharedInstance] getInboxesWithStatusRead:NO statusUnread:NO statusDeleted:NO];

QGInbox *first = [listinbox objectAtIndex:0];

[first logEvent:@"EVENT_NAME" withParameters:@{@"PARAMETER_NAME": @"PARAMETER_VALUE"} withValueToSum:nil withValueToSumCurrency:nil];

To track and view campaign performance data (impressions and clicks) on the AIQUA Dashboard, you need to manually log the following events using logEvent():

qg_inapp_displayed (impressions)

qg_inapp_clicked (clicks)

👍TipYou don't need to add event parameters when logging qg_inapp_displayed or qg_inapp_clicked.

let first: QGInbox = listInbox[0]

first.logEvent("qg_inapp_clicked", withParameters: [], withValueToSum: nil, withValueToSumCurrency: nil)

QGInbox *first = [listinbox objectAtIndex:0];

[first logEvent:@"qg_inapp_clicked" withParameters:@{} withValueToSum:nil withValueToSumCurrency:nil];

Although these events are default events, the iOS SDK doesn't automatically log them for inbox campaigns. When properly logged, these campaign performance metrics will be displayed in the in-app campaign list on the AIQUA Dashboard.

Updated 11 months ago Table of Contents

Overview

Inbox vs pop-up and push notifications

Logging events for inbox notifications

Example use case: In-app message center

In-app message center: Implementation

In-app message center: Force refresh feature

QGInbox properties

QGInbox methods

updateInboxRecord()

fetchInboxMessages()

getInboxesWithStatusRead()

updateStatus()

logEvent()



Implementing Deep Links [0]

https://docs.aiqua.appier.com/docs/implementing-deep-links-for-ios



The Appier iOS SDK supports passing deep links to your app. Note that the iOS SDK doesn't resolve or handle deep links—the links are passed directly to the app for handling.

👍Deep links can be added in push campaigns and in-app pop-up campaigns from the AIQUA dashboard.

Deep links can be implemented using one of the following methods:

Option 1: Using a custom URL scheme

Option 2: Using universal links

All other types of links will be routed to the browser instead.

Define a custom URL scheme. See Defining a Custom URL Scheme for Your App for detailed instructions.

Implement URL handling in one of the following methods:

Swift: application(_:open:options:)

Objective-C: application:openURL:options:

func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool { 



// Code to change the page to specific page as per the url

...



return true

}

- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options 

{

// Code to change the page to specific page as per the url

...



return YES;

}

🚧React Native and FlutterIf you're using the Appier Flutter or React Native, please skip these instructions and refer to the guides below instead:

Flutter SDK

React Native SDK

To use universal links with the iOS SDK, refer to the following instructions.

Complete the required setup for supporting universal links. See Allowing Apps and Websites to Link to Your Content for detailed instructions.

Specify your universal links by calling setUniversalLinkDomains() in AppDelegate.swift (for Swift) or AppDelegate.m (for Objective-C). Doing so will allow the link to redirect to your app instead of the browser.

📘NoteIf setUniversalLinkDomains() isn't called with your universal link domains, these links will redirect to the browser instead of your app.

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

let QG = QGSdk.getSharedInstance()

#if DEBUG



Implementing Deep Links [1]

https://docs.aiqua.appier.com/docs/implementing-deep-links-for-ios



let QG = QGSdk.getSharedInstance()

#if DEBUG

QG.onStart("APPIER_APP_ID", withAppGroup:"APPIER_APP_GROUP_ID", setDevProfile: true)

#else

QG.onStart("APPIER_APP_ID", withAppGroup:"APPIER_APP_GROUP_ID", setDevProfile: false)

#endif



/* If your Universal Link domains are: 

* https://YOUR_DOMAIN_1/

* and 

* https://YOUR_DOMAIN_2/

* , please add this line below:

*/

QG.setUniversalLinkDomains(["YOUR_DOMAIN_1", "YOUR_DOMAIN_2"])



...



return true

}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions

{

QGSdk *qgsdk = [QGSdk getSharedInstance];

#ifdef DEBUG

[qgsdk onStart:@"APPIER_APP_ID" withAppGroup:@"APPIER_APP_GROUP_ID" setDevProfile:YES];

#else

[qgsdk onStart:@"APPIER_APP_ID" withAppGroup:@"APPIER_APP_GROUP_ID" setDevProfile:NO];

#endif



/* If your Universal Link domains are: 

* https://YOUR_DOMAIN_1/

* and 

* https://YOUR_DOMAIN_2/

* , please add this line below:

*/

[qgsdk setUniversalLinkDomains:@[@"YOUR_DOMAIN_1", @"YOUR_DOMAIN_2"]];



...



return YES;

}

If your app uses the scene delegate, follow the instructions for implementing universal link handling using the scene delegate.

If your app isn't using the scene delegate, follow the instructions for implementing universal link handling using the app delegate.

In your app's Info.plist file, add the flag AppierSceneDelegateDeeplinkHandlingEnabled and set it to YES (boolean value). 

Next, implement universal link handling in the one of the following methods in the scene delegate:

Swift: func scene(_:continue:)

Objective-C: scene:continueUserActivity:

func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {

// Retrieve the URL

if let url = userActivity.webpageURL {

// then handle the URL

}

}

- (void)scene:(UIScene *)scene continueUserActivity:(NSUserActivity *)userActivity { 

// Retrieve the URL

NSURL *url = userActivity.webpageURL;

// then handle the URL

}

Implement universal link handling in the one of the following methods in the app delegate:



Implementing Deep Links [2]

https://docs.aiqua.appier.com/docs/implementing-deep-links-for-ios



// then handle the URL

}

Implement universal link handling in the one of the following methods in the app delegate:

Swift: application(_:continue:restorationHandler:

Objective-C: application:continueUserActivity:restorationHandler:

func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {

// Retrieve the URL

if let url = userActivity.webpageURL {

// then handle the URL

}

return true

}

- (BOOL) application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray * _Nullable))restorationHandler {

// Retrieve the URL

NSURL *url = userActivity.webpageURL;

// then handle the URL

return YES;

}

Updated 1 day ago Table of Contents

Overview

Option 1: Using a custom URL scheme

1. Define a custom URL scheme

2. Implement custom URL handling

Option 2: Using universal links

1. Complete the universal link setup

2. Specify your universal links

3. Implement universal link handling



iOS Push Notifications

https://docs.aiqua.appier.com/docs/push-notification-guide-for-ios



Push notifications can be used to deliver important or useful information your users, even when your app is running in the background or inactive. Note that push notifications are opt-in — users who opt out won't receive any push notifications from your app.

After completing the required setup, you'll be able to send push notifications — including rich push notifications (notifications containing images, GIFs, or videos) and notifications with embedded deep links — from the AIQUA Dashboard.

StepDescription1. Configuring Push CredentialsConfigure a .p8 key or .p12 certificate with Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM).2. Registering for Push NotificationsRegister your app for remote notifications, request permission to send notifications to your users, and send your push token to AIQUA.3. Handling Push NotificationsDetermine how your app responds to notifications.4. Adding Required ExtensionsAdd app extensions required by the Appier SDK to enable:

• Impression tracking for push notifications

• Support for rich push notifications (notifications containing images, videos, or GIFs)5. Configuring Deep LinksConfigure deep links inside your notification. Users who tap a deep link will be sent to the specified app or website location.6. Sending Test NotificationsValidate that campaign push notifications can be delivered properly by sending yourself a push notification to your test device.

Refer to the following guides to learn about optional push notification features and customizations.

Updated over 1 year ago Table of Contents

Required setup

Optional features and customization



Configuring Push Credentials [0]

https://docs.aiqua.appier.com/docs/creating-push-certificates



Create push credentials to allow your iOS app to send push notifications using Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM). There are two types of push credentials you can use:

Option 1: Using a .p8 key (Recommended)

Option 2: Using a .p12 certificate

We recommend using a .p8 key, which doesn't expire and can be used for both your production and development apps, as long they share the same Bundle ID.

📘NoteIf your development and production apps use different Bundle IDs, you need to create a separate .p8 key for each app.

Log in to your Apple developer account and navigate to the Certificates, Identifiers & Profiles section.

Select Keys and click + to add a new key. 

Enter a Key Name, select Apple Push Notifications service (APNs), then click Continue.

Click Register.

Click Download to download the .p8 file. Save your Key ID. If your app uses Apple Push Notification service, you'll need to provide both the .p8 key file and key ID to Appier Support.

🚧CautionSave your .p8 file in a safe location - this file can only be downloaded once.

Follow the instructions corresponding to the notification service (APNs or FCM) your app is using.

Log in to your Apple developer account and navigate to the Certificates, Identifiers & Profiles section.

Go to the Identifiers page.

If you already have an existing app you want to use, skip to step 8. If you don't have an existing app, create one. Click +, choose App IDs, then click Continue.

Select the App identifier type, then click Continue.

Set a Description. For the Bundle ID, choose Explicit, enter your app's Bundle ID, then click Continue.

Under Capabilities, enable Push Notifications.

Click Continue, then click Register.

Search for and click on the app ID you just created. In the Push Notifications row, click Edit.

Select Create Certificate under Development SSL Certificate or Production SSL Certificate, depending on which profile you're creating this certificate for.



Configuring Push Credentials [1]

https://docs.aiqua.appier.com/docs/creating-push-certificates



Open Keychain Access on your Mac and go to Certificate Assistant > Request a Certificate From a Certificate Authority.

Input an email address as well as a descriptive name for Common Name.

Choose Saved to disk then click Continue to save the .certSigningRequest file. In Keychain Access > Keys, a new private and public key will appear with the common name you specified.

Go to your Apple developer account. In the Certificates, Identifiers & Profiles section, click Choose File and upload the .certSigningRequest file you generated.

Click Continue, then click Download to download the certificate.

Double-click the downloaded certificate to add it to your private login keychain in Keychain Access.

In Keychain Access > My Certificates, select both certificate and its key, then right-click and select Export 2 items.

You'll be prompted to enter a password to protect the certificate. You can either set a password or click OK to skip this step. If you set a password, you'll need to input it into the AIQUA Dashboard when you upload the certificate.

Input your system admin password in the next prompt to save the .p12 file.

Follow the instructions corresponding to the notification service (APNs or FCM) your app is using.

Notification ServiceInstructionsAPNsOn the AIQUA Dashboard, click on your name in the lower left corner and select Integration. Select the iOS platform, then upload your .p12 certificate file and enter your passphrase, if you configured one. If you didn't configure a password, leave the password field blank.FCMUpload your .p12 file to the Firebase console.

Then, provide your Firebase Server Key and Sender ID to Appier Support (ess_support@appier.com).Updated over 1 year ago Table of Contents

Using a .p8 key (Recommended)

1. Create the .p8 Key

2. Configure Your Push Credentials with AIQUA or FCM

Using a .p12 certificate

1. Create the .p12 certificate

2. Create a Certificate Signing Request

3. Configure Your Push Credentials with AIQUA or FCM



Registering for Push Notifications [0]

https://docs.aiqua.appier.com/docs/registering-push-notifications-for-ios



To be able to send push notifications, you need to request permission from the user. After the user grants permissions to receive notifications, a push notification token will be generated by the Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM) servers, then the token must be passed to Appier's servers.

In the main app target, go to Build Phases and add the framework UserNotifications. 

In your class where you will handle the push notifications, preferably in the AppDelegate class,

For Swift, import UserNotifications.

For Objective-C, import .

You also need to add UNUserNotificationCenterDelegate to the class interface.

// Import UserNotifications

import UserNotifications

// Add UNUserNotificationCenterDelegate to the class interface

class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {

...

}

#import 

#import "QGSdk.h"



// Add UNUserNotificationCenterDelegate to the class interface

@interface AppDelegate ()

@end



@implementation AppDelegate

...

@end

Request users to grant permission to your app to send push notification by displaying a permission prompt. Users will be able to receive your app's push notifications after viewing the permission prompt and authorizing your app to send push notifications. 

Include the code sample below somewhere within your app. You need to register for userNotificationSettings (for iOS 8 and iOS 9) or requestAuthorization (for iOS 10 and above).

// Registering Push Notification 

if #available(iOS 10.0, *) {

let center = UNUserNotificationCenter.current()

center.delegate = self

center.requestAuthorization(options: [.badge, .carPlay, .alert, .sound]) { (granted, error) in

print("Granted: \(granted), Error: \(String(describing: error))")

}

} else {

// Fallback on earlier versions - iOS 8 & 9

let settings = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories: nil)
