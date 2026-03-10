---
source: notebooklm_export
file_id: "062"
filename: "062_aiqua_rc_part_2.txt.txt"
doc_type: "reference_card"
product: "AIQUA"
content_type: "txt"
language: "en"
guide_summary: "This extensive documentation details the sophisticated marketing campaign features available within the AIQUA platform, focusing on **regular, trigger, and in-web campaigns**. A central theme is the emphasis on **personalization and automation**, facilitated by tools like the Content Assistant, which uses generative AI to create marketing messages, and Dynamic Content, which customizes creatives based on user data, recommended products, or feed changes. The document comprehensively outlines the "
guide_keywords: "Campaign Management, Trigger Campaigns, Dynamic Content, In-Web Campaigns, Creative Studio"
---

# 062 aiqua rc part 2

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



Content Assistant [0]

https://docs.aiqua.appier.com/docs/content-assistant



📘Content assistant is a beta feature. While this feature is currently available for use, you may encounter occasional bugs or stability issues.

AIQUA's campaign content assistant leverages generative AI to automatically create written content for you campaign creatives.

Automatically generate multiple marketing messages in seconds

Reduce or entirely eliminate manual effort required to create marketing content for A/B testing

Instantly get inspiration and ideas for marketing copy

Content assistant is supported for the following types of regular push campaigns:

Push (Android, iOS, and web)

Instant messaging (LINE, Kakao)

To open content assistant, open the campaign's edit page, go to the Creative section, then click Content assistant. 

In the Describe your campaign field, enter one of the following:

A content generation prompt (keywords, descriptions, marketing scenarios)

Content that you want to modify, e.g. content that must be shortened to fit a target length, or modified to match a certain tone

Next, set the settings for content length, language, and tone that best suit your campaign:

SettingDescriptionTarget message lengthThe number of characters in the generated content.

• Includes content for all applicable fields, e.g. the combined length of the generated Title, Subtitle, and Message.

• Maximum length is 500 charactersLanguageThe desired language of the generated content. ToneThe conversational style that the generated content should be written in. 

Once you've selected the desired settings, click Generate content, and three options for suggested content will be generated.

To browse between the three options, click the arrows on either side of the suggested content.

Once you've decided on the option you want to use, click Apply suggestion to automatically populate the campaign settings with the content suggestion.

If none of the options are satisfactory, click Regenerate to generate a brand new set of suggestions, or click Edit settings to modify your content settings before regenerating new suggestions.



Content Assistant [1]

https://docs.aiqua.appier.com/docs/content-assistant



Updated 10 months ago Table of Contents

Overview

How to use content assistant

1. Open content assistant

2. Enter a description for your campaign

3. Set the length, language, and tone for generated content

4. Generate and apply the content to your campaign



Trigger Campaigns

https://docs.aiqua.appier.com/docs/trigger-campaigns



Trigger campaigns are campaigns that are sent to a user when the user meets the trigger condition. Trigger campaigns can be sent to the following types of channels:

Push (Web, Android, iOS)

SMS

Email

Instant Messaging (LINE, Kakao)

Go to Campaigns > Trigger Campaigns, and then select Create New Campaign.

In trigger campaigns, the campaign is not sent in bulk to the entire audience. It is automatically sent to a user when they meet the conditions used to define a trigger. The following types of conditions are available:

This condition can be used to trigger a message based on a user event. For example, you can set the campaign to be sent to users when they make a purchase.

This condition can be used to trigger a message based on a date or time parameter. For example, you can have a reminder sent to users a day before their flight departure date.

There are two important factors that make up a trigger rule based on feed changes. The trigger rule must indicate:

A change in the value of the data feed parameter (e.g. price drop for a product)

The user events that define the scope of the feed change (e.g. product added to cart)

For example, you can set the campaign to trigger when there is a price drop in the product added to cart by the user.

Trigger campaigns based on date or time:

This feature needs to be activated by Appier Support.

The event or attribute parameters to be used as the trigger condition need to follow the Date format or Datetime format.

Trigger campaigns based on feed changes: 

This feature needs to be activated by Appier Support.

Make sure you have onboarded your product feed to AIQUA.

Updated over 1 year ago Creating Trigger CampaignsManaging Trigger CampaignsTable of Contents

Trigger Rules

Condition Based on User Actions

Condition Based on Date or Time

Condition Based on Feed Changes

Requirements



Creating Trigger Campaigns [0]

https://docs.aiqua.appier.com/docs/creating-trigger-campaigns



Trigger campaigns can be sent via push, SMS, email, or messaging app (such as LINE or Kakao) to users on the Android, iOS, and web platforms. Follow the steps below to create a trigger campaign.

From the navigation bar, go to Campaigns > Trigger Campaigns, and then click Create New Campaign.

📘NoteThe campaign type you select determines the available audience, creative, and advanced options.

Under Campaign, enter a campaign name and select your campaign type. 

Push (web push or app push)

SMS 

Email 

Instant Messaging (LINE and Kakao)

👍TipAdding tags is optional. Tags can be used to search for your campaign on the campaign list page.

Choose a trigger rule based on a user event, a date or time parameter, or a change in the product data feed.

📘NotePast events and attributes that occurred before the campaign starts running can also trigger the campaign if the conditions are met. For example, let's say the campaign is set to trigger 2 days after the user registers an account. If you start running the campaign today, the users who registered 2 days ago will trigger the campaign today.

To create a trigger rule based on a user event:

(A) Set a time interval. After the event occurred, this is the amount of time that should pass before the campaign is sent.

(B) Select an event. This is the action the user must perform to trigger the campaign.

(C) Select the user events to exclude if needed. Users who did the events during the time interval (A) are excluded from the trigger campaign. 

Let's see an example of how the trigger rule works. In the screenshot above, the campaign is set to trigger 2 days after the user does product_added_to_cart. AIQUA will exclude users who do checkout_completed within 2 days of completing the trigger event product_added_to_cart. 

In the illustration below, the trigger campaign is only sent to user B, because user A meets the exclude condition by doing a checkout_completed event within 2 days of completing the trigger event.



Creating Trigger Campaigns [1]

https://docs.aiqua.appier.com/docs/creating-trigger-campaigns



A date/time parameter can be a user attribute or an event parameter, such as the upcoming departure date of a flight_booked event. The campaign can only be used for date/time parameters with a future date or time. In other words, if you set the campaign to trigger on a date in the past, such as the user's birthday (e.g. 1980-12-31), the campaign will not be triggered. 

📘NoteTo use a parameter as date/time trigger, make sure the data is sent to AIQUA using one of the formats below and contact Appier Support to complete setup.

YYYY-MM-DD

YYYY-MM-DDTHH:MM:SS

See more details on how to properly format date/time data.

To create a trigger rule based on a date/time parameter:

(A) Set a time interval and choose before or after. This indicates when to send the campaign in relation to the date or time parameter

(B) Select the date/time parameter you want to use as a trigger.

(C) If you selected days in step A, then you need to select the time and time zone to send the campaign on that day. 

To create a trigger rule based on feed changes:

(A) Select one of the following data feed fields and set the feed change conditions:

price (e.g. price reduces by 10%)

condition (e.g. "new", "used", "like new")

availability (e.g. product availability changes to "in stock")

(B) Select the user event to define the scope of the feed change. If you select product_added_to_wishlist in the past 30 days, the campaign is only triggered when the feed change occurred to the products added to the wishlist by the user in the past 30 days.

(C) Select the user events to exclude if needed. Users who did the events during the time period are excluded from the trigger campaign.

If this is a push campaign, select a platform to indicate whether you want to send an Android, iOS, or web push campaign. The available creative and advanced settings will vary based on the platform selected. Define your campaign the audience using the following options:

Include Users of the Segment: The users in this segment should receive this campaign



Creating Trigger Campaigns [2]

https://docs.aiqua.appier.com/docs/creating-trigger-campaigns



Include Users of the Segment: The users in this segment should receive this campaign

Exclude Users of the Segment: The users in this segment shouldn't receive this campaign

For example, to send a campaign to users who didn't open the app in the last 30 days:

Under Include Users of the Segment, select All users

Under Exclude Users of the Segment, select a segment that contains users who have opened the app in the last 30 days

📘NoteiOS trigger campaigns are only supported for apps provisioned with Apple's distribution (production) certificate.

📘NoteThe available creatives vary based on the Campaign Type and Platform you selected.

In the Creative section, select the type of creative you'll send. Make sure to fill up all the required fields, and then click Test Your Creative to receive a test notification.

For web push campaigns, you can optionally select Include a "drip notification" to add a second notification.

A drip notification is a second notification that appears when the user dismisses the first notification you sent. When enabled, a Drip Creative editor is opened, allowing you to design the creative of the second notification.

In the Advanced section, configure optional settings for your campaign. Advanced options may vary based on the campaign type and platform you selected.

SettingSupported campaign type(s)Support platform(s)DescriptionDefine Time To Live (in sec)PushAndroid

iOS

WebSet a lifespan for your Android, iOS, and web push campaign notifications. Setting a time to live (TTL) is useful for time-sensitive campaigns, e.g. limited time sales. If no value is specified, the TTL is set to that maximum length of 28 days.

For example, if a notification is sent at 5PM with a TTL of 7200 seconds (2 hours), only users whose devices are connected to the notification service between 5PM and 7PM will receive the notification. Possible reasons that could prevent a device from connecting to the notification service include:

• The device being powered off

• The device being in power saving mode



Creating Trigger Campaigns [3]

https://docs.aiqua.appier.com/docs/creating-trigger-campaigns



• The device being powered off

• The device being in power saving mode

• The device having no network connection

Note that a blackout window will override the TTL. For example, if you’ve configured a blackout window starting at 10PM and sent a campaign at 9PM with a TTL of three hours, the campaign's TTL would be reduced from three hours to one hour due to the blackout window.Keep the unclicked notification in the Notification Center (Pile up notifications)PushAndroid

WebWhen selected, all notifications from this campaign will remain in the device's Notification Center until the user clicks on them. Unclicked notifications will be removed from Notification Center when the next notification arrives.Sound File

andCustomize Notification SoundPushAndroid

iOSCustomize your campaign notification's sound. For details, see the audio file requirements for Android and iOS.Heads-up message stylePushAndroidHeads-up notifications allow you to send a notification that briefly appears as a floating window in unlocked Android devices.

Requires:

• Appier Android SDK version 5.5.4 or later

• Android 5.0 (Lollipop) or laterCrop the images to fill the containerPush campaigns with carousel and slider creativesiOSAny image that may be larger than the container of a format can be cropped.Wake app in backgroundPushiOSAllows your app to fetch certain operations in the background.Include Key-Value PairsPushAndroid

iOSRequires modification in the Appier SDK. For details, see the docs for Android and iOS.Goal Events /Set goal events as conversionsAll campaign typesAll platformsAllows you to select events that will override the account-level conversion events for this campaign. In this campaign's performance page, conversion-related metrics will be calculated based on goal events instead of the account-level conversion events.

📘NoteFor email campaigns, the Set goal events as conversions option is located under the Campaign Settings section below the Audience section.



Creating Trigger Campaigns [4]

https://docs.aiqua.appier.com/docs/creating-trigger-campaigns



Click Save to save your settings and create the campaign. After being created, your campaign will be visible from the campaign list page.

From the navigation bar, go to Campaigns > Trigger Campaigns. Find the trigger campaign you want to run, then toggle On to go live.

📘NoteTrigger campaigns must be manually toggled on or off.

An exit push campaign triggers a push notification when a user exits your mobile app after launching the app for the first time, giving you the opportunity to encourage first-time users to continue using your app. Push notifications have a customizable title and message.

The following exit push campaigns exist by default after the corresponding mobile SDK is successfully integrated:

Android Exit Push

iOS Exit Push

Updated 7 months ago Table of Contents

Overview

1. Go to the trigger campaigns page

2. Create a campaign name and select your campaign type

3. Select your trigger rule

Based on user action

Based on date/time

Based on feed changes

4. Select your audience

5. Add your creative

6. (Optional) Add a drip creative for a website push notifications

7. (Optional) Add advanced settings

8. Save your campaign

9. Go to the Trigger Campaigns page to go live

Exit push campaigns



Managing Trigger Campaigns [0]

https://docs.aiqua.appier.com/docs/managing-trigger-campaigns



After creating a trigger campaign, you can go to the Trigger Campaigns page to switch on campaigns, view performance, and export campaign reports. 

Go to AIQUA Dashboard > Campaigns > Trigger Campaigns.

In the Campaign List, each row in the list represents a campaign. 

Edit: This lets you edit the campaign. After editing the campaign, click Save to save your edits.

View Performance: See the Campaign Performance page for details.

Duplicate: This allows you to duplicate a campaign. The duplicate is created above the current campaign in the dashboard.

View Activity Logs: This lets you view all activities related to the current campaign. 

Archive: Once archived, the campaign will not show up in the campaign list unless you select the Show archived campaigns checkbox.

User Report: This lets you export a report that includes a list of users who have been sent this campaign or have interacted with this campaign. See Exporting Campaign User Reports via Dashboard for details.

ON/OFF switch: This allows you to turn on or turn off the trigger campaign.

You can access the performance data of your campaigns in the following places:

Campaign list 

Campaign performance page 

Export Campaign Report button

👍Tip:For more details about how event attribution works, see Understanding Event Attribution.

EVENT: Displays the event that triggers the campaign message. 

DURATION: This is the amount of time between when the user fulfills the trigger condition and when the campaign is sent. For example, if the duration is one hour, this means the campaign is sent one hour before or after the user fulfills the trigger condition.

TOTAL SENT: This is the total number of notifications sent by AIQUA during the entire campaign duration.

DELIVERED (EDM/SMS): This shows you how many times this campaign has been delivered via EDM or SMS.

IMP: An impression is counted when a user receives the message on the device. This is based on the number of notification_received events. 

OPENS: This indicates the number of times the campaign was opened.



Managing Trigger Campaigns [1]

https://docs.aiqua.appier.com/docs/managing-trigger-campaigns



OPENS: This indicates the number of times the campaign was opened.

CLICKS: The number of times users click on the campaign. This is based on the number of notification_clicked events.

CTR: The CTR of the campaign. CTR is defined as (clicks/impressions) x 100%.

OPEN RATE: This indicates the open rate percentage for the campaign.

CONV COUNT: This column represents the count of the online conversion events. This is based on the attribution settings and conversion events you selected in the Account Settings.

OFFLINE CONV COUNT: This column represents the count of the offline conversion events uploaded through Offline Event API V2. This is based on the attribution settings you selected in the Account Settings.

CONV VALUE: This represents the value associated with the online conversion events. For example, if the conversion event is checkout_completed, the CONV VALUE will represent the total value associated with all checkout_completed events attributed to the campaign.

OFFLINE CONV. VALUE: The monetary value associated with the offline conversion events that are attributed to the campaign.

Click Export Campaign Report to export a report containing performance data for your trigger campaigns within a specified date range. The campaign report download link is sent via email. For more details, see Exporting Campaign Performance Reports via Dashboard. 

Updated 11 months ago Table of Contents

Navigating the Trigger Campaigns List

Action Buttons

Accessing Campaign Performance

Campaign List

Export Campaign Report



In-Web Campaigns [0]

https://docs.aiqua.appier.com/docs/in-web-campaigns



In-web campaigns allow you to show notifications to users on your website. In-web campaigns can be triggered based on user actions, scroll depth, idle time, or exit intent.

AIQUA provides different options to help you design the creatives for your in-web campaigns: Basic creatives, Creative Studio, and HTML editor.

Basic Creatives

Fixed Banner, Multiple Actions, Multiple Images: These layouts help you display information to your website visitors in the form of pop-up notifications.

Lead Generation: Lead Generation creatives are pop-ups that allow users to submit information. For example, you can encourage users to sign up for email newsletter.

Subscription Boost: Subscription boost is an overlay with customizable text that points to the permission prompts for web push notifications and encourages unsubscribed users to allow web push notifications.

Creative Studio

Creative Studio is a drag-and-drop in-web editor that comes with a variety of pre-built templates. Contact your Customer Success Manager to enable Creative Studio. 

HTML Editor

The HTML editor allows you to write your own HTML codes to create your in-web creative. Some pre-made HTML templates are provided.

Basic creatives and HTML editors:

Supported browsers• Desktop: Chrome, Edge, Firefox

• Mobile: Chrome, Safari, Firefox

Creative Studio:

Supported browsersNot Supported• Chrome

• Firefox• Internet Explorer

• Safari

• Any browsers in incognito mode

Your website must be integrated with Appier Web SDK.

You must enable In-Web Notification on the AIQUA Dashboard > Account Name > Integration > Website page.

📘Note:In order for in-web creatives to display correctly on mobile devices, the following meta tag needs to be added to the element of your website. This allows the browser to recognize the user's device width.





In-Web Campaigns [1]

https://docs.aiqua.appier.com/docs/in-web-campaigns





Audience Segment: For In-Web Campaigns, a user gets included in the segment 24 hours after they meet the segmentation conditions, except for the following default segments.

All Users: Includes all Web users, including users who first visited your website within the last 24 hours.

New Users: Includes Web users who first visited your website within the last 24 hours.

Trigger Rule: first_visited is a virtual event that cannot be used as a trigger rule in in-web campaigns.

Multiple In-Web Campaigns: If a user meets the trigger rules of multiple in-web campaigns at the same time, the campaigns will be displayed based on the Display Type and Campaign Priority settings. 

Browser Cache: If you are accessing your website to view the in-web campaign after switching on or editing a campaign, open a new tab or new window in the browser, instead of refreshing your website on an existing tab. If refreshing an existing tab, the new campaign can be seen 5 minutes after toggling on or editing due to browser cache.

Single Page Application (SPA): If your website is a Single Page Application (SPA), note that once an in-web notification is triggered, it will remain on screen even after the user goes to a different page on the website. This is because the webpage does not reload during page transition in SPA. The user needs to manually close the creative.

Events in 24 hours with multiple domains: Filtering audience based on events within 24 hours does NOT work across multiple domains or subdomains. Let's say your in-web campaign targets users who have product_viewed events in the past 24 hours, and the triggering rule is set to Exit Intent. If a user completes a product_viewed event on subdomain A, and then shows exit intent on subdomain B, the in-web campaign will not be displayed.

See here for details on how to create In-Web Campaigns.



In-Web Campaigns [2]

https://docs.aiqua.appier.com/docs/in-web-campaigns



See here for details on how to create In-Web Campaigns.

See here for details on how to manage In-Web Campaigns and view campaign performance.Updated over 1 year ago Creating In-Web Campaigns[Creative] Fixed Banner, Multiple Actions, Multiple Images[Creative] Lead Generation[Creative] Subscription Boost[Creative] Creative Studio[Creative] HTML EditorTable of Contents

Overview

Browser compatibility

Integration requirements

Guidelines and Limitations

Creating In-Web Campaigns

Managing In-Web Campaigns



Creating In-Web Campaigns [0]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



Create your in-web campaigns using the following steps:

Go to Campaigns, select In-Web Campaigns, and then click the + Create campaign button.

In the CAMPAIGN box, create a campaign name. Providing a description is optional, and you can also add tags to the campaign to allow you to quickly search for and organize campaigns in the campaign list.

📘Note:A campaign name can be used to search for your campaign on the campaign list page.

Under Target Device, you can choose to target users based on specific types of devices.

Next, select the segments you want to include and exclude. 

The following segments are available under Include Users of the Segment by default:

All Users: Includes all Web users, including users who first visited your website within the last 24 hours.

New Users: Includes Web users who first visited your website within the last 24 hours.

For any segments other than the All Users and New Users segments, it may take up to 24 hours for users to be included in the segment after they meet that segment's condition. This is because AIQUA retrieves the audience segments once a day for in-web and in-app campaigns. 

To further filter your audience based on events that happened within 24 hours, see step 4 below.

Since it may take up to 24 hours for users to be included in the segment after meeting the segmentation conditions (except All Users and New Users segments), this option allows you to target audience based on events your users have completed within 24 hours.

📘Note:Filtering audience based on events within 24 hours does not work across multiple domains or subdomains. See here for more details.

👍Tip:Refer to the Use Cases for examples on how to use this feature.

In the AUDIENCE - ADDITIONAL CONDITIONS section:

Select Narrow down audience based on user events within 24 hours.

Add at least one event as criteria to include or exclude users. Up to three events can be added for each.



Creating In-Web Campaigns [1]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



Add at least one event as criteria to include or exclude users. Up to three events can be added for each.

Users must have any/all of the following events: Among the target audience set in step 3, AIQUA will only include the users who have recently completed the selected events. The events selected here further narrow down the audience. You cannot use this option to add users who were not included in step 3 to the audience. 

Users cannot have any/all of the following events: AIQUA will exclude users who have the selected events from the target audience.

Use In the last x minutes/hours to set a time period for the inclusion and exclusion criteria.

Under TRIGGER RULE, select a trigger rule as the timing to send your in-web campaign to users. Audience-related settings allow you to select WHO to send campaigns to, but the campaign will be sent WHEN the trigger criteria are met.

This triggers your in-web campaign based on user events. Some user events have a Filter by Event Parameters option that lets you add more conditions. 

📘Limitations

first_visited is a virtual event that cannot be used as a trigger rule in in-web campaigns.

User events uploaded through API cannot be used as a trigger rule.

This triggers your in-web campaign based on the detected amount of viewable area scrolled on the web page. You can set the scroll percentage between 10% to 100%. You can use the Filter by Event Parameters option to only trigger this campaign on some web pages.

When the trigger rule is based on scroll percentage, the same in-web campaign will only be shown once during a user’s session. Each time the user visits the website from a new tab or a new window, it is counted as a new session.

This triggers your in-web campaign based on the amount of time the user is inactive on the web page. You can set this between 10 seconds to 10 minutes. You can use the Filter by Event Parameters option to only trigger this campaign on some web pages.



Creating In-Web Campaigns [2]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



📘Mobile web browsersIf the user visits your website from the web browser of a mobile device, the following limitations may apply. The actual behavior may differ depending on the web browser and mobile device used. 

After a web page is loaded, the user needs to interact with the page (e.g. swipe, click) for idle timer to start counting. 

The idle timer is stopped if the web browser is moved to the background. After the web browser is switched back to the foreground, the user needs to interact with the page for idle timer to start counting again.

Exit intent is a user's intention to leave a web page. A user is considered to have exit intent when the user's cursor moves towards the top part of the browser, coming from the body of a web page. Once detected, the in-web campaign gets launched. You can use the Filter by Event Parameters option to only trigger this campaign on some web pages.

When the trigger rule is set to exit intent, the same in-web campaign will only be shown once during a user’s session. Each time the user visits the website from a new tab or a new window, it is counted as a new session.

📘Mobile web browsersExit intent campaigns cannot be triggered on mobile web browsers since there are no cursors on mobile devices.

You can choose to not show in-web popups on certain URLs on your site. For example, you might want to block in-web pop-ups on payment-related pages, to avoid distracting users who are in the process of completing a purchase.

Under BLOCKED URL, select Do not show the notification under the following URL.

Select equals to block the exact url you entered, OR select contains to block all urls containing what you have entered. 

Click Add URL to add more urls to block.

📘Note:URL cannot include non-English characters (e.g. Chinese, Japanese characters). Only ASCII characters are allowed.

Set the Start Date and End Date of your in-web campaign. 

Show repeatedly: The in-web notification can be shown to the user repeatedly up to the cap you specified.



Creating In-Web Campaigns [3]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



Show repeatedly: The in-web notification can be shown to the user repeatedly up to the cap you specified.

Show only once in the user's lifetime: The in-web notification can only be displayed to the user once during the campaign duration. 

When multiple in-web campaigns are triggered at the same time, AIQUA will show all Must-Display campaigns, as well as one standard campaign (non-must display campaign) with the highest campaign priority.

Set as Must-Display: 

If selected, this campaign will always be displayed when the conditions of the campaign are met. You may want to select this option for fixed banners that do not block users from interacting with the webpage's main content.

If not selected, only one standard campaign (non-must display campaign) is shown when multiple standard campaigns are triggered at a time. AIQUA will show the standard campaign with the highest campaign priority (lowest priority number). 

Campaign Priority: The campaign priority affects both the display priority and stack order. When multiple in-web campaigns are triggered at the same time:

Display Priority: Among the triggered standard campaigns (non-must display campaigns), only the one with the highest priority is shown.

Stack Order: The campaigns with higher campaign priority (lower priority number) will be shown toward the top when multiple are displayed.

📘Note:

If triggered at the same time, in-web campaigns in journey maps have higher campaign priority than non-journey map in-web campaigns, both in terms of display priority and stack order.

Creatives generated using Creative Studio will not follow the stack order controlled by campaign priority. Under the default setting, creatives generated using Creative Studio have a lower stack order (closer to the bottom) than basic creatives. If you need to adjust this default setting, contact Appier Support.

When multiple campaigns are displayed, each displayed campaign will have 1 impression counted, even if the campaign is covered by another campaign and not visible to the user.



Creating In-Web Campaigns [4]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



The Experiment feature allows you to divide your audience into 1 control group and multiple variants. You can show different variations of a creative to each variant group and test what works best for your audience. 

For more details, see the Experiments page.

In the CREATIVE section, select a creative type. See guides below for setup instructions.

Basic Creatives

Lead Generation

Subscription Boost

Fixed Banner, Multiple Actions, Multiple Images

Creative Studio: This is a premium feature. Contact your Customer Success Manager for more details.

HTML Editor: See this page for some pre-built HTML templates.

On the right side of the CREATIVE section, you can generate a preview link to see what the creative looks like on your website. 

The preview link will only work on websites integrated with Appier Web SDK using your account's APP ID.

The preview link is valid for 7 days after it is generated.

Preview will not be displayed if your website automatically redirects to a different URL and the query parameter ?aiq_preview= is removed in the process.

Preview on Website is not available for Subscription Boost.

For Basic Creatives, titles are truncated with "..." when they exceed a certain length. The number of characters that can be displayed without truncation depends on the size of the user's device screen or browser window, and can be different from what's shown on the preview.

No user events (e.g. page_viewed, qg_inweb_clicked), user attributes, or lead generation form data will be collected when accessing the website using the preview link. 

To preview on website, click Generate Link, enter the URL of your website, and click Generate.

A preview link is generated. Click Open Link to see the preview or click Copy Link if you want to share the link.

Click Save to save all your settings and exit.

Click Campaigns > In-Web Campaigns. Go to the In-Web campaign you want to run and then toggle ON to go live.



Creating In-Web Campaigns [5]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



Click Campaigns > In-Web Campaigns. Go to the In-Web campaign you want to run and then toggle ON to go live.

📘Note:In-web campaigns need to be turned on or off manually. Note that after you have turned on a campaign for the first time, the creative type can no longer be changed.

===================

The marketer wants to send a reminder to users who have recently added items to the shopping cart but are leaving the website without completing the purchase. The campaign can be set up as below.

[AUDIENCE]: Set Include Users of the Segment to All Users.

[AUDIENCE - ADDITIONAL CONDITIONS]:

Set Users must have any/all of the following events to product_added_to_cart 

Set Users cannot have any/all of the following events to checkout_completed 

In the last 24 hours

[TRIGGER RULE]: Select Exit Intent.

The marketer wants to encourage users to log in when they shop on the website in order to capture more user information. Notification about members-only discounts can be shown to users who are not logged in. The campaign can be set up as below.

[AUDIENCE]: Set Include Users of the Segment to All Users.

[AUDIENCE - ADDITIONAL CONDITIONS]:

Set Users must have any/all of the following events to product_viewed event with total count > 5

Set Users cannot have any/all of the following events to login

In the last 2 hours

[TRIGGER RULE]: Select User Action and set the action to page_viewed.

Updated 3 months ago Lead Generation CreativeSubscription Boost CreativeNotify Users CreativesCreative StudioCustom HTML Editor - HTML TemplatesTable of Contents

1. Go to the in-web campaigns page

2. Type a campaign name

3. Select your audience

All Users and New Users Segments

Other segments

4. Filter audience by events within 24 hours (Optional)

5. Select a trigger rule

Based on User Action

Based on Scroll Percentage

Based on Idle Time

Exit Intent

6. Block in-web popups on certain URLs (Optional)

7. Set up campaign delivery

Delivery date range

Frequency Cap

Display Type and Campaign Priority

8. Perform an experiment (Optional)



Creating In-Web Campaigns [6]

https://docs.aiqua.appier.com/docs/creating-in-web-campaigns



Delivery date range

Frequency Cap

Display Type and Campaign Priority

8. Perform an experiment (Optional)

9. Select a creative

Preview on website

10. Click Save

11. Go to the in-web Campaigns page to go live

Use Case 1: Remind users about items in shopping cart

Use Case 2: Encourage users to log in



Managing In-Web Campaigns [0]

https://docs.aiqua.appier.com/docs/managing-in-web-campaigns



After creating an in-web campaign, you can view and manage it in the in-web campaign list (Campaigns > In-web campaigns). In addition to searching and filtering existing campaigns, you can perform operations such as turning on campaigns, viewing the campaign's performance page, and exporting reports.

Search and filter campaigns 

Perform campaign operations

Viewing campaign performance

From the campaign list, you can find campaigns using the search box and apply various filters to display a more focused set of campaigns.

Enter search terms to find campaigns by name or ID.

Use the provided filter options to streamline searches in the in-web campaign list.

Filter optionDescriptionStatusSelect one of the following campaign statuses:

• Draft: The campaign hasn't been sent yet.

• Scheduled: The campaign is scheduled to run in the future.

• Completed: The campaign period has ended.

• Inactive: The campaign was manually turned off before it's campaign delivery window has passed.

• Archived: The campaign has been archived.DeviceSelect one or more device types.TagSelect one or more tags.Trigger ruleSelect one or more campaign trigger rules. 

From the campaign list, you can access the campaign's edit screen and campaign actions by clicking the buttons next to the campaign's name.

To edit the campaign, click the pencil icon.

To see a list of other available operations, click the three vertical dots and select a campaign operation to perform.

To turn on the campaign, click the toggle.

The following table describes the operations available for in-web campaigns.



Managing In-Web Campaigns [1]

https://docs.aiqua.appier.com/docs/managing-in-web-campaigns



To turn on the campaign, click the toggle.

The following table describes the operations available for in-web campaigns.

Campaign operationDescriptionDuplicateDuplicate the campaign. The duplicated campaign's name will be the original campaign's name with "-copy" appended.Modify tagsAdd and remove tags for this campaign.View Activity LogsView logs detailing operations performed on this campaign.Export user reportExport a user report containing data about users who interacted with or received this campaign.Export form dataOnly available for lead generation campaigns. Specify an email to receive a report that contains the information submitted by the users in the lead form.

If you've enabled experiments in a lead generation campaign, the information collected from each variant will be a separate tab in the report. For details on, see Download Form Data (In-Web / In-App).

The submitTime of the lead form is based on the timezone set in your account settings.ArchiveArchive the campaign. Archived campaigns aren't displayed in the campaign list unless the status filter is set to include campaigns with the Archived status.

You can view performance data using:

Campaign list metrics 

The campaign performance page 

Exportable reports 

The following table lists the metrics and campaign details visible from the campaign list.



Managing In-Web Campaigns [2]

https://docs.aiqua.appier.com/docs/managing-in-web-campaigns



Exportable reports 

The following table lists the metrics and campaign details visible from the campaign list.

MetricDescriptionStatusThe current status of the campaign, one of: Draft, Scheduled, Active, Completed, Inactive, or Archived.PriorityThe campaign's display priority.DeviceThe target device types selected for the in-web campaign.SubmissionsThe number of campaign forms submitted in lead generation campaigns. This is based on the number of qg_inweb_lead_gen events.ImpressionsAn impression is counted when a user receives a campaign notification on their device. This is based on the number of qg_inweb_displayed events.ClicksThe total number of clicks and form submissions in the campaign. This is based on the count for qg_inweb_clicked and qg_inweb_lead_gen events which are logged under the following conditions:

• Basic Creative (Lead Generation): When the user submits a lead generation form.

• Basic Creative (Subscription Boost): When the user clicks to allow push notifications.

• Basic Creative (Fixed Banner): When the user clicks on the action button.

• Basic Creative (Multiple Images): When the user clicks on an image or action button.

• Basic Creative (Multiple Actions): When the user clicks on an action Button where the button's "Click Action" is set to Open URL.

• Creative Studio: When the user clicks on a creative element where element's "Action" is set to URL and when the user submits a form by clicking on a creative element where the element's "Action" is set to Submit form.CONV. countThe count of online conversion events until the campaign's end date. This is based on the attribution settings and conversion events you selected in your account settings.CONV. valueThe monetary value associated with online conversion events.



Managing In-Web Campaigns [3]

https://docs.aiqua.appier.com/docs/managing-in-web-campaigns



For example, if the conversion event is checkout_completed, the CONV. value represents the sum of the conversion values of all checkout_completed events attributed to the campaign.Trigger ruleThe campaign trigger.Start dateThe start date of the campaign delivery schedule.End dateThe end date of the campaign delivery schedule.Include segmentsSegments selected to receive this campaign. Hover over this column to view the full list of included segments.Exclude segmentsSegments excluded from receiving this campaign. Hover over this column to view the full list of excluded segments.Last editedThe last time the campaign was edited.

Click on the campaign's name to open its performance page. For more details, see View Performance.

Campaign performance report 

User report 

Campaign performance reports contain campaign details and performance metrics, and can be exported to a CSV file and downloaded via URL sent to your email address. For details about what data the campaign performance report includes, see Export Campaign Performance Reports.

To export a campaign performance report, click Export report.

User reports contain data about users who interacted with or received this campaign, including their user ID, email address, and whether they performed certain actions, such as opens and clicks. The report can be exported to a CSV file and downloaded via URL sent to your email address. For more details about the data contained in user reports, see Export Campaign User Reports.

To export this report, click the three vertical dots to open the list of available campaign actions, then click Export user report.

Updated 3 months ago Table of Contents

Overview

Searching and filtering campaigns

Searching

Filtering

Performing campaign operations

Viewing campaign performance

Campaign list metrics

Campaign performance page

Exportable reports



[Creative] Fixed Banner, Multiple Actions, Multiple Images [0]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-notify-users-creatives



AIQUA offers the following types of popup notifications to help you convey information to your website visitors.

Fixed Banner

Multiple Actions

Multiple Images

📘Note:Dynamic content is currently not supported for the Fixed Banner, Multiple Images and Multiple Actions creative types.

Fixed Banner creative is a text-only horizontal banner that can pop up at the top or the bottom of your webpage. 

On the AIQUA dashboard, navigate to Campaigns > In-Web Campaigns > Create New Campaign, select Basic Creatives in the Creative section, and select Fixed Banner.

Use short, catchy titles and make your message concise.

Type the text for the Action Button and add the destination link of the button.

If you leave the button text field empty, the action button will be hidden. 

If you leave the url field empty, the popup will close when users click on the button. 

The Overlay Mask allows you to gray out the area outside of the banner. Clicking on the grayed out area will close the notification.

Under Location, click the horizontal bars to change the location of the banner.

Multiple Actions creative can include one image and multiple action buttons in a popup. 

On the AIQUA dashboard, navigate to Campaigns > In-Web Campaigns > Create New Campaign, select Basic Creatives in the Creative section, and select Multiple Actions.

Click on one of the nine boxes to set the position of the popup on desktop. Except for the center position, you will need to specify the Distance from the Left/Right/Top/Bottom edge of the browser. 

Next, set the size of the popup by specifying the Width and Height of the popup.

You can include up to 1 image by specifying the Image Ratio, Image URL, and Image Fit. There are three options under Image Fit:

Cover: The image will fill the width of the popup. If the image does not match the image ratio selected, the image will be cropped. 

Contain: The entire image will be shown on the popup. If the image does not match the image ratio selected, the pop up background color will fill the empty space.



[Creative] Fixed Banner, Multiple Actions, Multiple Images [1]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-notify-users-creatives



Keep Original Size: The image is displayed in its original size. The image will be cropped if the image is larger than the space available. If the image is smaller than the space available, the pop up background color will fill the empty space.

There are two types of button, Primary Buttons for your call-to-actions and Secondary Buttons for users to dismiss the popup. For both types of buttons, there are three Click Action options available.

Open URL: The user is directed to the specified URL when the button is clicked. Typically, you'll want to set the primary buttons to Open URL.

Close the pop up: The popup closes when the button is clicked. The user may see the same in-web campaign again if trigger condition is met and if the frequency settings allow.

Never show again (to the user): When clicked, the popup closes and the same user will not be shown this popup again. To let users know that they can opt out of this campaign, you can set the Action Button Text to "Never show again", and set the Click Action to Never show again (to the user).

🚧ImportantClicks on primary and secondary buttons will generate a qg_inweb_clicked event and count toward the "CLICKS" metrics only when the Click Action of the button is set to Open URL.

👍Tip:After running a Multiple Actions campaign, you can create an audience segment to include users who have clicked on an "Open URL" action button. Here's an example of what the segmentation conditions may look like:

qg_inweb_clicked, callToActionText equals "Sign Up Now"

AND

qg_inweb_clicked = notificationId = "123450000"

Note that the callToActionText parameter is the name of the button and is only supported for "Open URL" Action Buttons in Multiple Action creatives.

You can adjust the size and color of the Close Button if needed. Background Size is the size of the circle, while Icon Size is the size of the "X" icon.

You can include multiple images in a popup, along with a message and action button for each image.



[Creative] Fixed Banner, Multiple Actions, Multiple Images [2]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-notify-users-creatives



You can include multiple images in a popup, along with a message and action button for each image.

On the AIQUA dashboard, navigate to Campaigns > In-Web Campaigns > Create New Campaign, select Basic Creatives in the Creative section, and select Multiple Images. 

Select the layout and size of the popup for desktop users. 

If the size exceeds the user's screen, the user can scroll to see the rest of the popup.

For mobile users, layout and size cannot be selected. 

Select an Image Ratio for popup that will be used on both desktop and mobile devices. Images that do not match the selected image ratio will be cropped to fit the ratio.

Add up to 4 images, and configure the message, destination link, and action button for each image. The action button will take the user to the indicated destination link.

Use the recommended image size shown on the AIQUA dashboard to make sure the image resolution is high enough. 

You can choose to remove action buttons by clearing the selection for Use Action Button.

Updated over 1 year ago Table of Contents

Fixed Banner

Title and Message

Action Button

Overlay Mask and Location

Multiple Actions

Position and Size on Desktop View

Image

Action Buttons

Close Button

Multiple Images

Desktop Display

Images and Action Buttons



[Creative] Lead Generation [0]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-lead-generation



Lead Generation creatives are pop-ups that encourage users to submit information, such as submitting email to sign up for newsletter. 

On the AIQUA dashboard, navigate to Campaigns > In-Web Campaigns > Create New Campaign, select Basic Creatives in the Creative section, and select Lead Generation.

Fill in the required fields to design your lead generation form.

Set the behavior of your in-web notification using any of these options:

No longer be seen by the user - Upon submission of the lead form, the in-web notification would no longer appear for that user.

Remain visible to the user - The in-web notification always pops-up whenever the user lands on the campaign page, even after submitting the lead form.

📘Note:If the user clears their application data, their in-web history will be reset.

Using the Advanced Fields Settings, you can include additional fields in your Lead Generation form to collect more information from your users. Under Field Type, you can choose to set the Field Type to Input Box, Dropdown, or Conditional List. 

Input Box - This field enables your users to type the specific information you need. It may be a field that corresponds to an email address, mobile number, or other demographic information. 

Input the required labels under Field Label and Parameter Name.

Click the dropdown arrow under Content Type to set it as Text or Number.

Dropdown - This field allows you to add a dropdown list into your lead generation form. The dropdown list is based on the specified labels and values.

Field Label is the question shown to the users on your lead generation form. 

Parameter Name is the parameter name you can later use to segment audience. 

Under Dropdown Menu Items, "Label" is the option that is shown on the dropdown menu and "Value" is the data that will be collected and stored.



[Creative] Lead Generation [1]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-lead-generation



Conditional List - This field allows you to add multiple dropdown fields where the dropdown options change based on the user's answer for the previous question. You can use this to sequence your dropdown fields. You will need to create a Conditional List, see below section for details. 

To add more advanced fields, click Add Fields.

Make sure you click Save before exiting the screen.

After your users start submitting the lead generation form, you can download the submitted information by clicking the Download form data button in the in-web campaign list. 

The latest data shown is from two days prior to your download date.

If you have enabled the Experiment feature in the lead generation campaign, the information collected from each variant will be a separate tab in the report.

You can use conditional list to create a lead generation form with multiple dependent dropdown fields. In the example below, the lead generation form includes 3 questions:

Q1: Which region do you live in?

Q2: Which country?

Q3: Which shop is closest to you?

Depending on the region selected for Q1, different countries will be available as the dropdown options under Q2. Once the country is selected for Q2, the shops available in that country will be shown under Q3.

Here’s a sample conditional list that adds these three questions to the lead generation form. 

A conditional list must have:

Field Label: In the first row under Field Label, type the question or sentence that will be shown on your lead generation form before an option is selected. For example, "Which region do you live in?"

Value: This is the answer your users can select in the dropdown list. For example, "North Asia". 

Parameter - The parameter is made up of two components: the parameter name and the parameter value. Each parameter name must have a set of parameter values. In the sample above, the parameter name is region_asia, while a parameter value for this is north_asia. 

Follow these steps to create a conditional list:



[Creative] Lead Generation [2]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-lead-generation



Follow these steps to create a conditional list:

Download and edit the sample from this link. You can also refer to the sample above if you want to create from scratch. 

🚧Important:Make sure that your conditional list is in an .xls or .xlsx file format. You can also use a Google spreadsheet.

In your conditional list, input the following items for Row 2:

Under Field Label, input the text your users will see on the field. Type a question or sentence that allows users to understand the purpose of the options.

Under Parameter, input a parameter name for the list of parameter values to be used.

For row 3 and onward, input the Field Label value and Parameter value. 

The Field Label value will show up as dropdown options in the Lead Generation form. 

The Parameter value is the value that will be stored in AIQUA. 

In the example below, if the users select "North Asia" for the first question, the options "Japan" and "South Korea" will be shown under question 2.

Save your conditional list when done. Make sure that it’s in an .xls or .xlsx file format. You can also use a Google spreadsheet.

After creating your conditional list, you can add it to your lead generation form under Advanced Fields Setting. 

Set the Field Type to Conditional List, click the Edit Conditions button, and copy-paste the conditional list you created inside the EDIT CONDITIONAL QUESTIONS input field. 

📘Note:In some operating systems, an extra line break is added when you paste the conditional list from the spreadsheet to the AIQUA dashboard, sending the mouse cursor to the next line. In this case, you'll need to press backspace to remove the extra line break at the end before you can click the Apply button.

Click Apply. The Field Labels and Parameters indicated in your list appears inside the Conditional List box. You can also preview them in the lead generation form on the right panel.Updated over 1 year ago Creating In-Web CampaignsCreating a Conditional ListTable of Contents

Conditional List

Creating a Conditional List



[Creative] Subscription Boost [0]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-subscription-boost



Subscription boost is a message that shows up on your website to encourage users to subscribe to Web push. Using trigger rule based on user's behavior, Subscription Boost can be shown at the contextually relevant moments in a user’s journey.

Subscription boost is shown as an overlay that contains your custom message and an arrow that points to the system prompt (browser's native prompt). 

When the user meets the trigger rule, the subscription boost pops up at the same time as the system prompt.

The system prompt and the subscription boost can only pop up if the user’s Web push notification setting towards your site is set to Ask (Default). They won't pop up when the notification setting is set to Allow or Block.

If the opt-in prompt (fake prompt) is enabled, the trigger rule is applied to opt-in prompt instead. The system prompt and subscription boost are only shown if the user clicks Allow on the opt-in prompt.

If the opt-in tip is enabled, the opt-in tip will also be displayed instead of the blue arrow. The opt-in tip can be configured in Web Pixel Settings.

👍Tip:It is recommended to enable opt-in tip because some browsers have adopted Quieter Permission UI where some users will no longer see the browser's system prompt.

The time delay settings configured in "Web Pixel Settings > General Settings" are not applied to the system prompt (or opt-in prompt, if enabled) triggered by this subscription boost. The time delay settings will only apply to the system prompt (or opt-in prompt, if enabled) that is automatically displayed after the user visits the site.

Refer to the steps below:

On the AIQUA dashboard, navigate to Campaigns > In-Web Campaigns > Create New Campaign, select Basic Creatives in the Creative section, and select Subscription Boost.

Input a title and a message. Use short, catchy titles and make your message concise.

Check the right panel for a preview of your Subscription Boost notification.



[Creative] Subscription Boost [1]

https://docs.aiqua.appier.com/docs/using-in-web-campaigns-subscription-boost



Check the right panel for a preview of your Subscription Boost notification. 

Under Opt-in Tip Status, you can see whether opt-in tip is enabled. The opt-in tip can be configured in Web Pixel Settings. If opt-in tip is enabled: 

The opt-in tip will show up along with the subscription boost title and message entered above. 

The blue arrow will not appear.

Make sure all other required fields are filled, then click Save.

Updated over 1 year ago In-Web CampaignsCreating In-Web CampaignsTable of Contents

How It Works

Setting Up Subscription Boost



Creative Studio [0]

https://docs.aiqua.appier.com/docs/creative-studio



Creative Studio allows you to build interactive in-web and in-app creatives using a simple drag-and-drop interface—no coding required. It's possible to design complex, multistep creatives with Creative Studio. 

For example, you can:

Display personalized product recommendations.

Ask visitors to fill out a survey and display a coupon code as a reward upon completion.

Spin a lucky wheel to win a prize or offer.

Start by building a template from new scratch in Creative Studio or by customizing a prebuilt template. After creating a template, you'll be able to select it in the campaign creation process.

To ensure Creative Studio displays correctly for in-web campaigns, use a supported browser when accessing it on the AIQUA dashboard.

Supported browsersUnsupported• Chrome

• Firefox• Internet Explorer

• Safari

• Any browsers in incognito mode

Creative Studio in-app campaigns are supported by the following Appier SDKs:

Android SDK 7.24.0 or later

iOS SDK 7.31.0 or later

Use Recommendation with Creative Studio in-app campaigns by following these Appier SDK versions:

iOS SDK 7.32.2 or later

Android SDK 7.24.1 or later

For in-app campaigns created with Creative Studio to display correctly, the following WebView versions are required on the user's device.

📘NoteFor Android devices, the corresponding OS versions listed below include the required WebView versions by default. Devices running earlier OS versions may still meet the requirements if users have updated their device's WebView version.

PlatformRequired WebView versionsCorresponding OS versionsAndroidWebView 66.0.3359.158 or laterAndroid 9 or later (OS versions with required WebView built-in)iOSWKWebView 12.0 or lateriOS 12 or later

Background overlay: When using Creative Studio with in-app campaigns, you can choose to enable a gray background overlay. When the overlay is enabled, users must close the campaign to interact with the app again.

On iOS devices, if the campaign content fails to load, the overlay will disappear, which may create a screen flashing effect.



Creative Studio [1]

https://docs.aiqua.appier.com/docs/creative-studio



On iOS devices, if the campaign content fails to load, the overlay will disappear, which may create a screen flashing effect.

Landscape mode: When a mobile device is in landscape mode, the creative content may shrink to fit the limited screen size. 

On-screen keyboard: When entering information in an in-app campaign, for example, when filling out a lead generation form, the on-screen keyboard may overlap the creative depending on the app's configuration.

Screen orientation change: On Android devices, video playback is paused when the screen is rotated and might not automatically resume depending on the app's configuration.

Refer to the following guides to learn how to use Creative Studio to create campaigns:

Exploring Creative Studio

Designing Creatives

Performance and Reports

Updated 5 months ago Table of Contents

Overview

Requirements and compatibility

In-web campaigns

In-app campaigns

Getting started with Creative Studio



[Creative] HTML Editor [0]

https://docs.aiqua.appier.com/docs/using-in-web-html-templates



The in-web campaign creation page includes a Custom HTML Editor where you can build your own HTML-based in-web notification.

On the AIQUA dashboard, navigate to Campaigns > In-Web Campaigns > Create New Campaign and select HTML Editor in the Creative section.

Paste your HTML code inside the HTML Body. A preview of your campaign appears on the right panel. You can also switch on or switch off the Use Overlay feature to add an overlay setting to your creative.

📘Note:For Images

Images are resized automatically based on the layout settings.

Squared images are recommended in the item list type of creatives. If the image is not squared, it'll be resized based on its width, and the height will auto-adjust according to the original image proportions.

For Text

The title field might not line break if the text is too long.

Hover on the template you'd like to use below and then click Copy.

Paste it on AIQUA's In-Web Campaign HTML Editor. 

Search for REPLACE and replace its content accordingly.

Check the creative preview on the right side panel. 

Set up the rest of your In-Web Campaign and click Save before exiting the page. For details, see Creating In-Web Campaigns. 

Example:





REPLACE_title





REPLACE_detailed_text





REPLACE_button_text <REPLACE_button_link>







Welcome





Add text here to describe your product or service in a more detailed way. This could also be an explanation of the details of your offer if you are running a promotion.





GO! <https://www.appier.com/>



In the following HTML templates, search for REPLACE and replace its content accordingly.







[Creative] HTML Editor [1]

https://docs.aiqua.appier.com/docs/using-in-web-html-templates









<REPLACE_link>





Sample Output 

mobile image

PC image



<REPLACE_link>







Sample output

mobile image

PC image









REPLACE_title





   

   - 

   

   

   REPLACE_text1

   

   <REPLACE_link_1>

   

   - 

   

   

   REPLACE_text2

   

   <REPLACE_link_2>

   

   - 

   

   

   REPLACE_text3

   

   <REPLACE_link_3>

   

   





Sample output 

mobile image

PC image









REPLACE_title





   

   - 

   

   

   REPLACE_text1

   

   <REPLACE_link_1>

   

   - 

   

   

   REPLACE_text2

   

   <REPLACE_link_2>

   

   





Sample output

mobile image

PC image









REPLACE_title





   

   - 

   

   

   REPLACE_text1

   

   <REPLACE_link_1>

   

   - 

   

   

   REPLACE_text2

   

   <REPLACE_link_2>

   

   - 

   

   

   REPLACE_text3

   

   <REPLACE_link_3>

   

   





Sample output

mobile image

PC image









REPLACE_title





   

   - 

   

   

   REPLACE_text1

   

   <REPLACE_link_1>

   

   - 

   

   

   REPLACE_text2

   

   <REPLACE_link_2>

   

   





Sample output



[Creative] HTML Editor [6]

https://docs.aiqua.appier.com/docs/using-in-web-html-templates



REPLACE_text2



<REPLACE_link>









Sample output

mobile image

PC image







REPLACE_title



REPLACE_detailed_text





REPLACE_button_text <REPLACE_button_link>









Sample output

mobile image

PC image









REPLACE_title





REPLACE_detailed_text





REPLACE_button_text <REPLACE_button_link>



Sample output

mobile image

PC image











REPLACE_title





REPLACE_detailed_text



REPLACE_button_text



<REPLACE_link>







Sample output

mobile image

PC image









REPLACE_title





REPLACE_detailed_text





REPLACE_button_text <REPLACE_button_link>



Sample output

mobile image

PC image











REPLACE_title





REPLACE_detailed_text



REPLACE_button_text



<REPLACE_link>







Sample output

mobile image

PC image









REPLACE_title





REPLACE_detailed_text



REPLACE_button_text















<REPLACE_link>







   

   

   

   - 

   

   [image: slide_image_description_1]

   

   

   

   [Creative] HTML Editor [11]

   https://docs.aiqua.appier.com/docs/using-in-web-html-templates

   

   

   

   

   

   

   

   

   

   - 

   

   [image: slide_image_description_2]

   

   

   

   

   

   

   

   

   - 

   

   [image: slide_image_description_3]

   

   

   

   

   

   

   













Sample output

mobile image

PC image











REPLACE_message





[Creative] HTML Editor [15]

https://docs.aiqua.appier.com/docs/using-in-web-html-templates





REPLACE_message





REPLACE_title





REPLACE_detailed_description



REPLACE_button_text <REPLACE_button_link>





Sample output

Mobile message

PC message

This HTML template shows a banner at the top of the webpage with a countdown timer.

Use thefinal_date_time variable to set the end time of the countdown timer. 

The user's browser time is used to calculate the remaining time in the countdown timer. 

If the final_date_time passes before the end of the campaign, the countdown timer will disappear from the in-web popup. 

Since you may have users in different time zones, set the final_date_time to be at least 1 day later than the end time of the in-web campaign. 









Title in PC 

Title in Mobile 



Sub Title







Final Countdown:



























Buy It! <https://www.example.com/Index.aspx> " aiq-close>Button









The following attributes let you customize the behavior of the close button, add deep links, and log some user events when building your own creative using the Popup In-App Campaign HTML Editor.

This attribute dismisses the HTML popup creative and turns it into a floating icon.

Dismiss

🚧Known issueIn Android SDK versions 7.17.0 to 7.20.0, aiq-close-kill would close the in-app campaign, but wouldn't fully kill it. As a result, relaunching the app would allow the campaign to display again.To avoid this issue, please use Android SDK 7.21.0 or later.

This attribute dismisses both the HTML pop-up creative and its floating icon. This campaign will never be displayed again unless the app is reinstalled by the user. Modifying the campaign doesn't take effect after the in-app is shown.

Dismiss

📘Note:

The href tag is not supported. Refer to aiq-deeplink instead.

In the HTML code, the tag without an href doesn’t appear with an underline.

This attribute logs a user event and its corresponding label or event name. 

Log a checkout_completed event

🚧Important:

Use aiq-deeplink to embed links. 

onclick function is disabled as well as all click events are prevented by default unless Aiqua tags are used.

If you need to embed a universal link, deep link, specific web, or app pages, for example: https://mybusiness/product.com, use the following format.

link

For other actions, this is the accepted deep link format: scheme://resource. A sample of this would be: aiquademo://profile?user=JohnSu



In-App Custom HTML Editor [2]

https://docs.aiqua.appier.com/docs/using-the-in-app-campaign-html-editor



link

Use the following format to open a link from an image button.



Use notification persistence options in the HTML Editor to control how your campaign behaves when users interact with deep links or click different areas. 

Click areaPersistPersist until the notification is clickedDon't persistHTML attribute aiq-deeplinkOpens deep link and collapses into a floating icon.Opens deep link and disappears.Opens deep link and disappears.HTML attribute aiq-closeCollapses into a floating icon.Collapses into a floating icon.Disappears when clicked.HTML attribute aiq-close-killCreative and floating icon disappear. The campaign won't be displayed again unless the app is reinstalled.Creative and floating icon disappear. The campaign won't be displayed again unless the app is reinstalled.Creative and floating icon disappear. The campaign won't be displayed again unless the app is reinstalled.Close button (system)Collapses into a floating icon.Collapses into a floating icon.Disappears when clicked.Overlay backgroundCollapses into a floating icon.Collapses into a floating icon.Disappears when clicked.Floating iconExpands creative when clicked.Expands creative when clicked.Expands creative when clicked.Updated 4 months ago Creating In-App CampaignsIn-App CampaignsIn-App Popup CreativesTable of Contents

HTML template

AIQUA attributes

Buttons

Logging events

Deep link or universal link embedding

Notification persistence



Journey Maps (Legacy)

https://docs.aiqua.appier.com/docs/customer-journey-maps



📘Legacy featureThe legacy journey maps feature will be deprecated in the future. We recommend using the latest journey maps for a more intuitive journey builder and better cross-channel integration. Contact your customer success manager for more details.

You can design a journey map that takes your users through a series of marketing messages based on their behavior at each step of the journey. Using the drag-and-drop function, journey maps are created in flowchart-like diagrams to help you visualize the process. 

There are five main components to a journey map: Audience, Entry Action, Conditions, Notifications, and Exit. 

A journey map starts with an audience. If an entry action is selected, users from the targeted audience segment need to complete the entry action (e.g. user visited website) to proceed to the next step.

Users are targeted by different notifications based on the conditions they meet (e.g. users who viewed product A received a push about product A). You can add as many notifications and conditions as needed.

Users exit the journey when they reach an exit on the map or when they fulfill the exit criteria (e.g. user fulfilled the marketing goal by making a purchase).

Updated 7 months ago Creating Journey MapsTable of Contents

Overview



Creating Journey Maps (Legacy) [0]

https://docs.aiqua.appier.com/docs/creating-customer-journey-maps



📘Legacy featureThe legacy journey maps feature will be deprecated in the future. We recommend using the latest journey maps for a more intuitive journey builder and better cross-channel integration. Contact your customer success manager for more details.

Below are the steps to create a journey map. There is a sample use case at the end. 

Go to Campaigns, select Journey Maps, and then click the Create New Map button. Type a map name.

Select the user segment you want to include and exclude. 

📘Note:AIQUA updates the campaign audience once per hour, so it may take up to one hour for users to be included in the segment after they meet that segment's conditions.

Click Create.

Select an audience segment to Include. 

Select an audience segment to Exclude (optional).

Click Create.

If you set an event as the entry action, users from your target audience need to complete the entry action to proceed to the next step.

Click the + icon, select Entry Action and click Create. 

Click Add Events and select an event. For example, product_viewed.

If needed, click Add Filter and set the associated parameters. For example, category_name of the product viewed needs to contain "shoes". 

Click Update.

You can select an event as the condition, where users will only go to the next step if they complete the event. Multiple events can be set with each event leading to a different notification or condition. 

📘Note:The following events cannot be used as a trigger condition in Journey Maps: first_app_launched, first_visited, and app_uninstalled.

There are two types of condition:

Wait for events to happen: AIQUA waits for users to complete the event before going to the next step.

Based on past events: AIQUA examines users' events from the past X days and users who have completed the events will proceed to the next step. Only events that happen after the entry action are considered.

Click the add icon, select Add Conditions and select Wait for events to happen or Based on past events.

Click Create.



Creating Journey Maps (Legacy) [1]

https://docs.aiqua.appier.com/docs/creating-customer-journey-maps



Click the add icon, select Add Conditions and select Wait for events to happen or Based on past events.

Click Create. 

Click Add Events to select an event and optionally click Add Filter to add associated event parameters. 

If you want to set multiple scenarios, click Add New Scenario and repeat the step above. 

Specify the time duration.

If you have selected Based on past events, you can adjust the time of in the last X days to look for event completion in the past X days.

If you have selected Wait for events to happen, specify the Time duration to wait for events to happen.

Click Update when done. 

Set the notification you want to send. 

Click the add icon to select a message type.

Click Create. 

Type a campaign name and set the creatives. Different types of creative are available based on the type of notification selected. Refer to Creatives for more details.

Between boxes, you can click the Timer icon to postpone proceeding to the next step. 

There are three options available:

Immediately - Proceed to the next step immediately. 

Delay - Wait X days before proceeding to the next step. For example, if the user enters this phase on July 1 at 9 pm and you are delaying the push for 1 day, the user will receive the push on July 2nd at 9 pm.

Delay and send at certain time - Wait X calendar days and proceed to the next step at the indicated time. For example, if the user enters this phase on July 1 at 9 pm, and the timer setting is 11 am after one day, the user will move to the next step on July 2 at 11 am. 

If you need to make changes to the journey map, you can delete a box or delete a link between boxes, and then link unconnected boxes using one of these methods:

Click the add icon and drag the Drag and Connect option.

Click and hold the add icon to drag to another box. 

It is required to specify how the users will exit the journey.

Each route in the journey map must end with an Exit box. Click the add icon and select Exit the Users. 

You need to set an overall Exit Criteria.



Creating Journey Maps (Legacy) [2]

https://docs.aiqua.appier.com/docs/creating-customer-journey-maps



You need to set an overall Exit Criteria.

Exit Criteria override all conditions in the map. For example, if the goal of the journey is to encourage purchase, you can exit the users when they make a purchase. Another common practice is to set a maximum number of notifications received to be the exit criteria to prevent users from receiving too many notifications.

To set exit criteria:

Click the Edit button next to Exit Criteria at the bottom.

Click Add Events to select an event as the exit criteria and optionally click Add Filter to add associated event parameters. 

You can click Add New Condition to have more than one criteria. Users exit the journey if they fulfill any one of the exit criteria.

If needed, select Allow user to re-enter the journey up to X times and set a limit for how many times the users can enter the journey if they complete the entry action again. 

Click Save. 

When you are done with setting up the journey map, click Save. You will see the created campaign in the Journey Maps List.

If you want to manually start running the journey map, set the switch to ON when you are ready to activate it. 

If you want to set a schedule to activate the journey map, select Schedule to set the Start Time and End Time. Next, set the switch to ON and the journey map will start running based on your scheduled time.

Let's say you run an English learning website that offers online lessons for paid members. Your goal is to encourage users to sign up for membership. Using Web Push, you offer a free lesson to interested users. If the user takes the free lesson, membership discount is offered to encourage signup. If the user didn't accept the lesson, you offer another free lesson.

This use case can be set up as shown below:

For this use case, the Exit Criteria can be set to membership signup. If the user subscribes to membership at any point, they will be exited from the journey.Updated 7 months ago Managing Customer Journey MapsTable of Contents

1. Create a New Journey Map

2. Select Target Audience



Creating Journey Maps (Legacy) [3]

https://docs.aiqua.appier.com/docs/creating-customer-journey-maps



1. Create a New Journey Map

2. Select Target Audience

3. Set an Entry Action (Optional)

4. Add Conditions

Setting Up Conditions

5. Add Notifications

6. Utilize Other Features

Adjust Timing Between Boxes

Drag and Connect

7. Exit the Users

Exit Criteria

8. Activate the Journey

Sample Use Case



Managing Journey Maps (Legacy) [0]

https://docs.aiqua.appier.com/docs/managing-customer-journey-maps



📘Legacy featureThe legacy journey maps feature will be deprecated in the future. We recommend using the latest journey maps for a more intuitive journey builder and better cross-channel integration. Contact your customer success manager for more details.

After a journey map is created, it will be listed in the Journey Maps list. Here you can edit the journey maps, start running the journey, and view the performance.

Go to AIQUA Dashboard > Campaigns > Journey Maps. 

In the Journey Map List, each row represents a journey map. 

Edit: You can revise the journey map if it hasn't started running.

View Performance: See the section below.

Schedule: Use Manual Start and No End Time if you want to manually activate and stop the journey map using the ON/OFF switch. Alternatively, you can set a schedule to start or stop the journey map. After you set a scheduled start time, be sure to switch the journey map to ON.

Duplicate: Create a copy of the journey map to edit.

View Activity Logs: Show the actions that have been done to this journey map (e.g. Edited, activation...etc) 

Archive: Hide the journey map from the list. 

If you archive a running journey, the journey will be stopped first before it is archived. 

You can click Show archived maps in the top-right corner when you want the list of journey maps to include archived items.

ON/OFF switch: Start running the journey map. The journey map settings need to be completed before you can use the switch. Once you switch off a running journey map, it is permanently terminated. You will not be able to resume a stopped journey map.

👍How Do I Complete a Journey Map?If you see (Not Completed) under the ON/OFF switch, make sure:

You have added an overall exit criteria.

You exit the user at the end of each route.

All notification messages and conditions have been configured.

An audience segment has been selected.

You can find the following columns for each journey map:

Status: The status of the journey map.



Managing Journey Maps (Legacy) [1]

https://docs.aiqua.appier.com/docs/managing-customer-journey-maps



You can find the following columns for each journey map:

Status: The status of the journey map.

Inactive: An inactive journey map with a white circle indicates that settings have been completed and the journey map can be switched ON. An inactive journey map with a red circle indicates that the journey map settings have not been completed. See the green tip above.

Scheduled: The journey map is scheduled to start at a later time. If you need to edit the journey map, set the switch to OFF and click the Edit button.

Running: Once the journey map has started running, it can no longer be edited or paused. You can only duplicate it to create a similar one.

Done: Once the journey map has been stopped or has finished running, it can no longer be restarted.

Entry Users: 

If the journey map doesn't have an entry action, this is the number of users in the targeted audience segments.

If the journey map has an entry action, this is the number of users who completed an event after the journey map started running.

Start Time: This is when the journey map started running or is scheduled to start running.

End Time: This is when the journey map stopped running or is scheduled to stop running.

For each journey map, you can view its performance by clicking the View Performance icon.

Inside each box, you can find the number of users who meet the condition of the previous box. 

📘NoteThe number of users shown includes users from all channels and platforms. Since not all users are eligible to receive notification from the campaign you set up, the performance numbers of the campaign may be significantly lower.For example, let's say you start the journey map with a web push campaign. You may see 10,000 users listed in the web push campaign box, but out of the 10,000 users, only 500 users are web users who are subscribed to your push notifications. As a result, the impression and click numbers will be significantly lower than the user count shown.

Inside the campaign boxes, you can click See Details to see the performance of that campaign.



Managing Journey Maps (Legacy) [2]

https://docs.aiqua.appier.com/docs/managing-customer-journey-maps



Inside the campaign boxes, you can click See Details to see the performance of that campaign.

Impressions and Clicks: Go to Campaign Performance to see the definition of Impressions and Clicks in different types of campaign. 

CTR: The click-through rate of the campaign is shown in the parentheses next to the Clicks number. 

Push, in-web, and in-app campaigns: CTR is defined as (Clicks / Impressions) x 100%.

Email campaigns: When Total Event is selected, CTR is defined as (Clicks / Opens) x 100%. When Unique Event is selected, CTR is defined as unique (Clicks / Impressions) x 100%.

LINE and SMS campaigns: CTR is not available.

Attributed Events: An event is attributed to the campaign that is last clicked or last viewed by the user before completing the event.

The Last-View + Last-Click attribution model is used in Journey Maps. 

The event must happen within the attribution window. The default attribution window is 24 hours for click-through attribution and 1 hour for view-through attribution.

Events that are also set as account-level conversion events are bolded under Attributed Events and Attributed Event Values.

Campaign-related default events such as notification_clicked will not count toward attributed events.

Attributed Event Values: Value acquired through attributed events.

In the top-right corner, a drop-down list allows you to select Total Event where each event is counted once, and Unique Event where multiple events from a unique user are only counted once.Updated 7 months ago Table of Contents

Navigating the Journey Map List

Action Buttons

Journey Details

Accessing Campaign Performance



Experiments

https://docs.aiqua.appier.com/docs/experiment



Experiments allow you to create different variations of a creative and test what works best for your audience. For example, you can use a different image in each variant to see which creative performs the best.

This feature is supported in the following campaign types.

Supported campaign typesDocsNotesIn-web campaigns:

All except subscription boostSee here-In-app campaigns: Pop-upSee hereControl group are supported in the following Appier SDK versions:

• iOS SDK 7.6.0 or later

• Android SDK 6.8.0 or laterRegular campaignsSee hereControl groups are not supported.

Test one variable at a time to pinpoint what's affecting the outcome. 

To make sure the results are statistically significant, include enough users in each group and allow enough performance data to accumulate.

For in-app and in-web campaigns, do not run more than one experiment with the same trigger rule at the same time.

After creating an experiment campaign, you can use that campaign's notification IDs to create segmentation conditions, allowing you to target specific users based on their interaction with the campaign. To learn more, see How do I segment by notification ID.

Updated 8 months ago Table of Contents

Overview

Supported campaign types

Best Practices



Experiments: In-Web and In-App Campaigns [0]

https://docs.aiqua.appier.com/docs/experiments-in-web-in-app-campaigns



📘Note:The following Appier SDK versions are required if you want to include a control group in the Experiment of your in-app campaigns. 

iOS SDK 7.6.0 or later

Android SDK 6.8.0 or later

Experiments allow you to create different variations of a creative and test what works best for your audience. In in-web and in-app campaigns, the target audience of each campaign can be divided into 1 control group and up to 6 variants. 

The control group will only include users from the segment who have met the trigger rule. Since the campaign notification will not be shown to users in the control group, you can compare the effects of running the campaign against not showing the campaign at all. 

In each variant, you can create variations of a creative to test your users' preferences. You can use different creative types in each variant. You can also use the same creative type across all variants and tweak the individual creative elements. For example, use a different call-to-action message in each variant to see which one drives more conversions. 

Repeated impressions during idle time: For campaigns triggered based on Idle Time, users in the control group will continue to trigger the campaign after meeting the trigger rule, leading to repeated impression counts for the same user. To avoid this issue, set the frequency cap to Only once in the user's lifetime when using Idle Time as trigger rule. 

Cannot edit: After an Experiment campaign starts running, the campaign can no longer be edited. In the Edit Campaign page, you can click on the tab of each variant, but you will not be able to scroll within the Creative section to see the creative details.

Cannot restart: An Experiment campaign cannot be restarted once you have stopped it.

For overall instructions on how to create campaigns, refer to Creating In-Web Campaigns or Creating In-App Campaigns.

Inside the campaign creation page, enable Perform Experiment.

If you want to include a control group, select Include Control Group.



Experiments: In-Web and In-App Campaigns [1]

https://docs.aiqua.appier.com/docs/experiments-in-web-in-app-campaigns



If you want to include a control group, select Include Control Group. 

You can click the Add Variants button to create more variants. 

Manually enter a percentage for the control group and variants, or click Divide Equally. The percentage must add up to 100%.

Under the Creative section, design the creative for each variant. You can click Copy Content From to copy the creative of another variant. 

Click Save when done.

To see the campaign performance of the experiment, click View Performance in the campaign list. 

Under Performance Overview, the impression count only includes the total impressions of all variants. The impression count of the control group is not included. 

Campaign Performance page > Performance Overview

Under Experiment Report, an IMP count is available for the control group even though users in the control group are not exposed to the notifications. The impression count is the number of times users in the control group meet the trigger rule of the campaign. 

Campaign Performance page > Experiment Report

The following data is not available for the control group.

Clicks

CTR

CVR (defined by (Conversions / Clicks) x 100%)

Submissions

Submission Rate

In the Campaign Performance page, impression-based CVR and CVR lift are available for some campaign types.

MetricsDefinitionSupported CampaignsIMP. CVRThis is defined by (Conversions / Impressions) x 100%. Since the control group does not have any clicks data, having impression-based CVR allows us to compare the conversion rate between the control group and variant groups.In-web: All campaigns

In-app: Experiments with control groupCVR LIFTThis is the percentage increase in the average impression-based CVR of all variants compared to the impression-based CVR of the control group.In-web and in-app: Experiments with control group

👍Tip:

For more details on performance data, see Campaign Performance.

If you want to create an audience segment to include users who received a certain variant of Experiment campaigns, see How do I segment by notification ID?



Experiments: In-Web and In-App Campaigns [2]

https://docs.aiqua.appier.com/docs/experiments-in-web-in-app-campaigns



📘Note:In the Campaign List, the numbers only include the performance of all variants. The performance of the control group is not included.Updated over 1 year ago Table of Contents

Overview

Limitations

Setting Up Experiments

Campaign Performance

Impressions

Clicks

Impression-based CVR and CVR LIFT



Experiments: Regular Campaigns

https://docs.aiqua.appier.com/docs/experiments-regular-campaigns



Experiments allow you to create multiple variations of a creative to determine what works best for your audience. For example, you can use a different image in each variant to see which creative performs the best.

This feature is supported in the following campaign types.

Campaign typeGuideNotesIn-web campaigns:

All except subscription boostSee here-In-app campaigns: Pop-upSee hereControl groups are supported for apps using the following Appier SDK versions:

• iOS SDK 7.6.0 or later

• Android SDK 6.8.0 or laterRegular campaigns: Email, Push (web and app)• Email

• Push Control groups are not supported for email campaigns.

Test one variable at a time to pinpoint what's affecting the outcome. 

To make sure the results are statistically significant, include enough users in each group and allow enough performance data to accumulate.

For in-app and in-web campaigns, do not run more than one experiment with the same trigger rule at the same time.

Updated 9 months ago Table of Contents

Overview

Supported campaign types

Best practices



Experiments: Email [0]

https://docs.aiqua.appier.com/docs/experiments-regular-campaign-email



Experiments allow you to create different variations of a creative and test what works best for your audience. For example, use a different call-to-action button in each variant to see which one drives more conversions. 

There are two ways to run an experiment in email campaigns: Manual Distribution and Automatic Winner Distribution.

Manual Distribution: You can set a percentage for each variant and the variant will be distributed to that proportion of the users in the segment. For example, you can have three different variants and distribute the variants to 50%, 30%, and 20% of the users respectively.

Automatic Winner Distribution: You can distribute the variants to a certain percentage of the audience for sampling and then send the winning variant to the remaining users. For example, you can randomly distribute the variants to 10% of your users as sampling. The variant with the best performance after 6 hours will be sent to the remaining 90% of the users. 

Cannot edit: After an experiment campaign starts running, the campaign can no longer be edited. In the Edit Campaign page, you can click on the tab of each variant, but you will not be able to scroll within the Creative section to see the creative details.

Cannot restart: An experiment campaign cannot be restarted once you have stopped it.

No recurring schedule: An experiment campaign cannot be set on a recurring schedule. 

No control group: Currently, having a control group is not supported when running experiments in regular email campaigns.

For overall instructions on how to create regular campaigns, refer to Creating Regular Campaigns.

Inside the campaign creation page, select Perform Experiment and select Manual Distribution. 

To add more variants, click the Add Variants button. 

Manually enter a percentage for each variant. The percentage must add up to 100%. You can also click Divide Equally to equally distribute the variants to your users. 

Add a creative for each variant. 

Click Save when done.



Experiments: Email [1]

https://docs.aiqua.appier.com/docs/experiments-regular-campaign-email



Add a creative for each variant. 

Click Save when done.

Inside the campaign creation page, select Perform Experiment and select Automatic Winner Distribution. 

Set up how you want to conduct sampling.

i. Enter the percentage of users you want to use as sampling.

ii. Set the amount of time to wait before determining the winning variant.

iii. To add more variants, click the Add Variants button. 

In the screenshot below, the three variants are randomly and equally distributed to 15% of the users for sampling. After three hours, the variant with the best performance becomes the winning variant. 

Under Winner Criteria, select the performance metrics you want to use to decide which variant is the winner. Use the Total / Unique drop-down list to change how events are counted. 

Total: Each event is counted once.

Unique: If a user completes the same event multiple times, the event is only counted once. The number of unique events is an approximation with a <1% margin of error.

Add a creative for each variant. 

Click Save when done.

To see the campaign performance of the experiment, click View Performance in the campaign list.

In the Campaign Performance page, you can find the performance of the variants listed under Experiment Report. 

In the Campaign Performance page, you can find these two sections: Experiment Report - Total Performance and View the performance in the sampling time.

This section shows the performance accumulated during the date range selected. 

In the table, the performance of each sample variant is shown, followed by the performance of the Winning Group. 

Each sample variant is shown as a row in the table. This is the performance of the variants that were sent to the sample users during the sampling time. 

The Winning Group row appears after sampling time ends. This is the performance of the winning variant that was sent to the remaining users after the sampling time is over.



Experiments: Email [2]

https://docs.aiqua.appier.com/docs/experiments-regular-campaign-email



The variant that had the best performance during sampling time is marked with a winner icon. Since users may continue to open and click on the email after the sampling time is over, it may be possible to see a non-winning variant with better performance than the winning variant.

This section appears after the sampling time has ended. 

In this section, you can find the settings that were used during sampling to see how the winning variant was determined. In the screenshot below, the winner variant was determined under the following settings.

50% of the users in the segment were used for sampling.

AIQUA waited 15 minutes for results to accumulate before determining the winning variant. 

The variant that had the most total clicks is the winning variant. 

Conversions were counted based on the conversion events set in the account settings.

The attribution model was set to Last-View and Last-Click.

Events are counted based on Total Event, where each event is counted once.

The performance table shows the performance of the variants accumulated during the sampling time. If a variant is sent out during sampling time and a user clicks on the email after sampling time has ended, this click is not included here. 

The date range selected on this page does not affect the results here.

👍Tip:

For more details on performance data, see Campaign Performance.

If you want to create an audience segment to include users who received a certain variant of Experiment campaigns, see How do I segment by notification ID?

📘Note:For email campaigns with the experiment feature enabled, the Download icon to download details about users who clicked on the campaign is not available in the campaign list.Updated 9 months ago Table of Contents

Overview

Limitations

Creating experiments for email campaigns

Manual Distribution

Automatic Winner Distribution

Campaign Performance

Manual Distribution

Automatic Winner Distribution



Experiments: Push [0]

https://docs.aiqua.appier.com/docs/experiments-regular-campaign-push



Experiments allow you to create different variations of a creative and test what works best for your audience, for example, by experimenting with two variants with different call-to-action buttons to see which one drives more conversions.

Recurring schedules are not supported.

Once an experiment campaign starts running, it can no longer be edited. 

Once an experiment campaign is stopped, it can't be restarted.

Experiments can be added during the regular push campaign creation process. The available configurations differ depending on what type of experiment you're creating:

Static distribution: Set a percentage for each variant and the variant will be distributed to that proportion of the users in the segment. For example, you can create three variants and distribute 50%, 30%, and 20% of your users to each variants, respectively.

Winner distribution: Distribute the variants to a certain percentage of the audience for sampling and then send the winning variant to the remaining users. For example, you can randomly distribute the variants to 10% of your users for sampling. The variant with the best performance after 6 hours will be sent to the remaining 90% of the users.

📘NoteAn experiment campaign can't be edited once it has started running, so remember to verify your configuration before publishing the campaign.

In the campaign creation page under Distribution method, select Winner distribution.

Set up how you want to conduct sampling. Enter the percentage of users you want to use for sampling. To add more variants, click + Add variant.

Set the amount of time to wait before determining the winning variant.

Under Winning metric select the performance metrics you want to use to decide which variant is the winner.

Use the total/unique dropdown to change how events are counted.

Total: Each event is counted once.

Unique: If a user completes the same event multiple times, the event is only counted once. The number of unique events is an approximation with a <1% margin of error.



Experiments: Push [1]

https://docs.aiqua.appier.com/docs/experiments-regular-campaign-push



Use the goal event dropdown to select one of the winning metrics: clicks, CTR, conversion events, or CVR.

Under Test duration, configure how long you'd like the test to continue before a winning variant is selected.

Add a creative for each variant.

Click Next after you finish setting up the experiment.

In the following example, three variants are randomly and equally distributed for a total 15% of users for sampling. After 30 minutes, the variant with the best performance becomes the winning variant.

Winning variant doesn’t include the control group. Control group won’t receive any notification from any variants in the experiment campaign.

In the performance report, Marketers can view the following additional metrics if the control group is applied and VTA attribution model is selected.

Targeted: The number of notification_targeted.

Targeted Conversion: The number of conversion events (attributed using notification_targeted).

Targeted CVR: Calculated using Targeted Conversion/ Targeted.

Targeted Conversion Value: The sum of the value to sum of conversion events (attributed using notification_targeted).

Average Targeted Conversion Value: Calculated using Targeted Conversion Value / Targeted.

CVR uplift: The percentage change of Targeted CVR between the control group and variant groups.

Incremental Value: Evaluate how many Targeted Conversion Value of the variant group are from the campaign by assuming the Average Targeted Conversion Value of the variant group without sending notification is the same as the control group.

To see the campaign performance of the experiment, click View Performance in the campaign list. The metrics in the listing page will include variants aggregated numbers. Control group related metrics won’t be included here.

Export campaign report: The metrics in the export report will include each variant’s numbers. Control group related metrics won’t be included here.

For all experiment campaigns: You can see performance of each variant and the total variant aggregated performance.



Experiments: Push [2]

https://docs.aiqua.appier.com/docs/experiments-regular-campaign-push



For all experiment campaigns: You can see performance of each variant and the total variant aggregated performance.

In this section, only variant groups will be included (excluding the control group).

The metrics and aggregated result should be exactly the same as the metrics in the general performance tab.

The default attribution model will follow your account settings.

Updated 7 months ago Table of Contents

Overview

Limitations

Creating experiments

Static distribution

Winner distribution

Control group

Campaign performance



Getting Started with Journey Maps [0]

https://docs.enterprise.appier.com/docs/getting-started-with-journey-maps



Appier's journey maps use an omni-channel customer journey builder that allows you to quickly launch personalized, comprehensive campaigns across Appier's supported marketing channels. Journey maps are designed for:

Cross-channel connection: Connect user data across channels to create a holistic user profile and amplify your reach with a wide range of supported platforms including websites and mobile apps, conventional marketing channels such as email and SMS, and messaging channels like LINE and WebChat.

User-based marketing: Orchestrate user-based campaigns and track performance metrics for each touchpoint, allowing you to quickly identify steps in the journey that can be optimized to maximize conversions.

Efficient journey map building: With an intuitive interface, dozens of prebuilt templates, and our AI-powered Journey Copilot, you can build customer journeys with minimum effort.

A journey map takes your users through a series of messages based on different conditions at each step of the journey. Users across different devices and channels are unified based on the unique identifier user_id to create a personalized and seamless experience.

Below are the main components of a journey map: Trigger, Message, Split, Wait, and Exit.

A journey map starts with an entry trigger, which can be based on past conditions, real-time events, or a date-format user attribute. Users who meet the trigger criteria (e.g. signed up for membership) enter the journey.

Users are targeted with different messages based on the split path they are in (e.g. users who viewed tutorial videos vs users who didn't) and based on the wait time you set.

Users exit the journey when they reach an exit on the map or when they fulfill the exit criteria (e.g. users fulfilled the marketing goal by making a purchase).

📘NoteContact your customer success manager to activate this feature.

User data requirements

Channel integration

Some features in journey maps have specific user data tracking requirements. Refer to the sections below.



Getting Started with Journey Maps [1]

https://docs.enterprise.appier.com/docs/getting-started-with-journey-maps



Channel integration

Some features in journey maps have specific user data tracking requirements. Refer to the sections below.

Offline events and segments

Offline users

Date format data

In journey maps, you can use offline events when setting up trigger events and conditions. Offline events are identifiable by an Offline tag in journey analytics and can be selected as conversion goals alongside online events.

To use offline events or segments in journey maps:

The offline events must be uploaded through the Offline Event API v2 with user_id as the unique identifier.

The offline segments must be created on AIQUA. The offline events must include user_id as the unique identifier. See segment by offline events.

For details and best practices on using offline events and segments in journey maps, see merging online and offline users.

📘Limitations

New offline users uploaded within one day may not be processed in time to be considered in the past conditions.

Offline events cannot be used as real-time trigger events in in-web and in-app campaigns.

If you upload offline users using the Bulk Upload Offline Users API or Add / Update User Profiles feature, be sure to include a user_id in each user record. Offline users need to have an user_id in order to enter a journey.

Your user attributes and events may include date-related data such as birthdays and departure dates. Journey maps will automatically convert event or attribute parameters that meet the following requirements to date-type data.

The value must follow this format: YYYY-MM-DD

The parameter name must satisfy one of the following requirements:

The parameter name is birthday.

The parameter name includes _date, for example, departure_date and register_date_website.

After the user data is converted to date format:

The following operators will be available when setting up conditions in journey maps: in the past, in the next, before, after, on or before, on or after, during, and in the month of.



Getting Started with Journey Maps [2]

https://docs.enterprise.appier.com/docs/getting-started-with-journey-maps



Date-format user attributes can be used as a date-based trigger for users to enter the journey.

📘Limitations

New offline users uploaded within one day may not be processed in time to be considered in the past conditions.

Offline events cannot be used as real-time trigger events in in-web and in-app campaigns

Below are the AIQUA and BotBonnie channels you can use in journey maps. Some channels require additional integrations.

ChannelsAppier servicesIntegration requiredWeb push

App push

Email

SMS

In-web

In-appAIQUANo additional integration is required if you are already using these channels on AIQUA.LINEAIQUA BotBonnieAIQUA: Additional integration is required. See LINE Integration.

BotBonnie: No additional integration is required.Facebook Messenger

WebChat

WhatsApp

Zalo

ViberBotBonnieNo additional integration is required if you are already using these channels on BotBonnie.

To use LINE campaigns in journey maps:

If you are already using LINE on BotBonnie, no additional integration is required.

If you have not set up LINE integration before or if you have previously set up LINE integration through AIQUA, you must integrate your LINE Official Account through the Appier Enterprise Console.

To integrate, log into Appier Enterprise Console (https://console.appier.com/) and follow the LINE integration guide.

Existing LINE users and any associated user data from the AIQUA LINE integration will be synced in journey maps.

Updated 20 days ago



Dynamic Content [0]

https://docs.aiqua.appier.com/docs/dynamic-content-for-personalizing-creatives



Dynamic content is a variable used in creatives that changes based on each user's behaviors and attributes. Having contents relevant and personalized for individual users is crucial for engaging your users. 

A typical example is to send a message that includes the name and image of the products the user has added to cart.

Dynamic content can be based on the following:

Based on attributes and events collected about a user (e.g. product viewed by the user)

Based on recommended products generated for a user using Recommendation 2.0

Based on changes in product feed for the product associated with a user event (e.g. 10% price drop for a product added to cart by the user)

You can add dynamic content to different elements of the creatives, such as text (e.g. titles, messages), URLs (e.g. deep links, destination URLs), images (e.g. notification images, icons). 

👍TipTo use dynamic content in Email campaigns, see this section.

Attributes & eventsRecommendationFeed triggerRegularPush: Yes

SMS: Yes

Email: Yes

LINE: Yes

Kakao: YesPush: Yes

SMS: Yes

Email: Yes

LINE: Yes

Kakao: NoNoTriggerPush: Yes

SMS: Yes

Email: Yes

LINE: Yes

Kakao: NoPush: Yes

SMS: Yes

Email: Yes

LINE: Yes

Kakao: NoPush: Yes

SMS: Yes

Email: Yes

LINE: Yes

Kakao: NoIn-web and In-appNoNoNoJourney mapsPush: Yes

SMS: Yes

Email: Yes

In-web: No

In-app: NoPush: Yes

SMS: Yes

Email: Yes

In-web: No

In-app: NoNo

📘NoteWhen using Recommendation 2.0 as dynamic content in Regular Campaigns, note the following delivery rate:

Push and SMS: AIQUA can deliver up to 50 notifications per second.

Email and LINE: AIQUA can deliver up to 10 - 15 notifications per second.

You can use user attributes and events collected from SDK as dynamic content.

On the AIQUA dashboard, click Campaign, select a campaign type, and click Create New Campaign.

Go to the Creative section.

To personalize your title, message, link, or image, type two curly brackets to see the list of available user attributes and events that you can use as variables. Select the user attribute or event you'd like to use.



Dynamic Content [1]

https://docs.aiqua.appier.com/docs/dynamic-content-for-personalizing-creatives



📘NoteDynamic content is not supported for some creative types and elements. If typing two curly brackets does not bring up the events and attributes drop-down list, this means that dynamic content is not supported for this input field.

Set a default title, message, link, or image. The default content will be displayed in case the data doesn't exist for the variable you selected. For example, if the notification title includes the user's first name, you can set a default value to address users without first name data.

👍TipIn some creative types, the default field is not provided, and you will need to manually type the default value by adding |default('default_value') after the event or attribute. For example, {{first_name|default('there')}}.

Instead of saying, "Hi, are you interested in this item?", you can insert the user's first name and the product category viewed by the user. Using these variables, the users might see: "Amy, interested in Brand Z shoes?"

If you want to insert the image of the last product viewed by the user, you can select the following parameters in the list that appears.

If you want the user to click on the notification and land on the product page of "Brand Y Smartwatch", you need to insert the deep link of the page of the last viewed product. 

After inserting two curly brackets, you might select product_viewed > product_deeplink > of the latest event.

Here's a sample of inserting the last 4 products viewed by the users in the 4 carousel cards for carousel app push.

For Carousel Cards, you will need to manually type the default value for fallback by adding |default('default_value'). For example, {{product_viewed.0.product_name|default('Tennis Shoes')}}.

If Recommendation 2.0 has been enabled for your account, you can include dynamic content based on recommendation 2.0 in your creatives. 

📘Limitations

Currently, Recommendation 2.0 can be used in the creatives of Regular Campaigns and Trigger Campaigns.



Dynamic Content [2]

https://docs.aiqua.appier.com/docs/dynamic-content-for-personalizing-creatives



📘Limitations

Currently, Recommendation 2.0 can be used in the creatives of Regular Campaigns and Trigger Campaigns. 

In the recommendation scenario list, performance analytics is not available for recommendation scenarios placed in campaign creatives.

Make sure the required integrations for Recommendation 2.0 are completed.

Create a recommendation scenario for campaign creative. See Creating Scenario for details.

Use this tool to generate dynamic syntax for recommendation 2.0. Make a copy of the Google Spreadsheet, and follow the instructions on the spreadsheet.

Update Sheet Setting: After you click the Update Sheet Setting button, a script will run to retrieve the available scenarios.

You will need to grant access the first time you run the script.

Scenarios in your account that are set to "Campaign Creative" placement and under "Ready" status will be shown in the spreadsheet.

Category Filter: If you want to use category filter, click the category tab in the spreadsheet and enter the category names you would like to use as filter. 

The value for category name is case-sensitive and must be exact match with the category name specified during product data feed onboarding.

If you have a hierarchy structure for categories, use > between categories of different levels. For example: "clothes > shirts" means that "shirts" is a sub-category under the "clothes" category. This hierarchy also needs to match the category structure specified in product data feed.

Default Value: If the creative element already has a default field available on the Dashboard (e.g. Default Title), uncheck the "Do you want to specify the default value...." checkbox in row 17 of the tool. You will need to enter the default value in the default field.

After clicking the Show the Syntax button in the spreadsheet, paste the generated dynamic syntax in the creative elements. 

In the example above:

xyz12345 is the scenario ID generated in part I.



Dynamic Content [3]

https://docs.aiqua.appier.com/docs/dynamic-content-for-personalizing-creatives



In the example above:

xyz12345 is the scenario ID generated in part I. 

Two category filters are set to only show recommended results that belong to both "Clearance" and "Jackets" categories.

An index of 0 indicates that this is the first item in the recommendation list generated for this user.

The product title is the parameter that will be shown in the creative. 

A default product title "Fleece Jacket" is used as fallback. 

If a default field is provided, do not include the default value inside the curly brackets. Instead, manually type a fallback value in the default field.

Dynamic content can be based on trigger by feed changes. For example, you have set up a Trigger Campaign that will be sent when there is a 10% price drop in the products added to cart by the user. In the creative of this Trigger Campaign, you can dynamically show the product added to cart by the user that had a 10% price drop.

To use dynamic content based on feed trigger, add:

{{feed_trigger.event.index.parameter_name}}

{{feed_trigger.product_added_to_cart.0.product_name}}

📘NoteDefault value is not supported in dynamic content based on feed trigger.

For dynamic content based on user events or feed trigger, you can also use product information from the data feed for the parameter you want to display. This is useful if the product information you want to display for dynamic content is in a data feed, but not collected by Appier SDK.

To use product information from data feed with user events, add:

{{event.index.feed.parameter_name|default('default_value')}}

To use product information from data feed with feed trigger, add:

{{feed_trigger.event.index.feed.parameter_name}}

🚧Important

The parameter_name must match the column name or field name in the product datafeed. Make sure you do not change the fields of the datafeed after you provide the datafeed to Appier.



Dynamic Content [4]

https://docs.aiqua.appier.com/docs/dynamic-content-for-personalizing-creatives



When using product information from data feed with user events, the user event must include a product_id parameter. AIQUA uses this product_id to map the product logged in the event with the product in the data feed.

In the example below:

The product_viewed is an event collected via SDK.

The index 0 indicates the latest product_viewed event the user completed.

The retail_price is a field in the product data feed, but not collected by SDK.

The product_viewed and retailed_price are linked by the same product ID. The retail price of the product last viewed by the user will be shown in the message.

In the example below:

The retail_price is a field in the product data feed.

The message shows the retail price of the product last viewed by the user that has a feed trigger.

For email campaigns, you can use dynamic content in the following places.

Subject line of the email

Drag & Drop Editor: Text

Drag & Drop Editor: Image

Drag & Drop Editor: Link

Drag & Drop Editor: HTML block

HTML Editor

In the Subject field, type two curly brackets and select the user attribute or event you'd like to use. 

Manually type the default value by adding |default('default_value') after the event or attribute. For example, {{first_name|default('there')}}.

To add a dynamic text:

Inside Drag & Drop Editor, click on a text box to call out the text menu. 

📘NoteTo add a dynamic text based on Recommendation 2.0 or feed trigger, paste the dynamic syntax in the text box. To add a dynamic text based on attributes or events, proceed to step 2.

Click Insert dynamic content.

Select a user attribute or user event from the Value drop-down menu. 

Type the default value in case the dynamic parameter is not available for some users. The Default value is optional, but it's highly recommended to have a fallback.

When you're done setting up your dynamic text, click Confirm.

To add a dynamic image:

Inside Drag & Drop Editor, click on an Image box to access the Content Properties on the right.



Dynamic Content [5]

https://docs.aiqua.appier.com/docs/dynamic-content-for-personalizing-creatives



To add a dynamic image:

Inside Drag & Drop Editor, click on an Image box to access the Content Properties on the right.

Click the switch next to Dynamic Image to enable it and type the dynamic syntax inside Dynamic URL. For example:

{{product_added_to_wishlist.0.product_image_url|default("https://www.example.com/jacket.png"}}

🚧ImportantThe link inside the URL field below the Dynamic URL is NOT the fallback image if there is no dynamic content matched with the user. It is the URL link for adding static image.

You can add a dynamic link to text, videos, and buttons.

To add a dynamic link:

Inside the Drag & Drop Editor, go to the URL field. 

Text URL: Click on a text box to call out the text menu, click the Insert Link icon to find the Url field.

👍TipYou can also add dynamic syntax to the Text to display field if needed.

Video URL: Click on a video and find the Video url field in the Content Properties on the right. 

Button URL: Click on a button and find the Url field in the Content Properties on the right. 

In the Url or Video url field, type the dynamic syntax. For example:

{{product_viewed.0.product_url|default("https://www.example.com/jacket02/")}}

Updated 5 months ago Table of Contents

What is dynamic content?

Supported campaign types

Based on attributes and events

Based on Recommendation 2.0

Based on Feed Trigger

Using product information from your data feed

Dynamic content in email campaigns

Subject Line of the Email

Drag & Drop Editor: Text

Drag & Drop Editor: Image

Drag & Drop Editor: Link



Creatives

https://docs.aiqua.appier.com/docs/creatives



In AIQUA, a creative refers to the appearance of the actual notification sent to your users in a campaign. Different campaign types offer different types of creative. Each creative type can consist of different components, such as images, text, and call-to-action buttons.

AIQUA's creatives can be personalized using variables that change based on each user's behaviors and attributes. For more details, see Dynamic Content.

Refer to Image Specifications to see the recommended size and aspect ratio of the creative images.

Each campaign type supports a different set of creative types. Refer to the sections below for a list of available creatives by campaign type:

Regular campaigns and triggers campaigns

In-app campaigns 

In-web campaigns 

Regular and trigger campaigns support the same creative types.

Android and iOS in-app campaigns support the same creative types.

Listed below are the OS and browser compatibility of creatives when sent to a mobile or PC device. See the Specifications column for some specific requirements. 

CreativeOS and BrowserSpecificationsSubscriptionAndroid OS:

• Chrome

• FirefoxStandard web pushAndroid OS:

• Chrome

• Firefox• Icon Image

• Big Image

AIQUA supports using emojis in a web push sent via iOS, Android, Mac, or Windows platforms. 

The following table lists some important requirements to ensure that emojis in your web push appear in a Chrome browser. 

PlatformSupported VersionsWindows- Windows 7 and Windows 8 need the KB2729094 patch. See this guide. - Windows 10 and aboveAndroidAndroid 4.1 (Jelly Bean) and abovemacOSmacOS 10.10 (Yosemite) and aboveiOSiOS 6 and aboveUpdated 9 months ago Table of Contents

Overview

Creative images

Creative types

Regular campaigns and trigger campaigns

In-app campaigns

In-web campaigns

OS and browser compatibility

Mobile

PC

Using emojis



Image Specifications [0]

https://docs.aiqua.appier.com/docs/image-types



Images are one of the most crucial components of a creative. To make sure the creative images appear correctly on your user's device, refer to the recommended sizes and aspect ratios listed below.

📘NoteDepending on the screen’s resolution, Android crops the image to fit it into the container. We recommend avoiding any text within 10% of the margin space in a big image, carousel, and in-app full screen image.

👍Tip: GIF image sizeSmaller files sizes improve display speed and performance.

Image typeCreativeRecommended size (px)Aspect ratioSupport image formatsFloating IconIn-App Creatives192 x 192 or larger1:1• All SDK versions: JPG, PNG

• Android SDK 7.25.0 or later: JPG, PNG, GIF (standard gif87a and gif89a)Full ScreenIn-App Full Screen720 x 12809:16

For more details about full screen image aspect ratios, see In-app pop-up full screen images.• All SDK versions: JPG, PNG

• Android SDK 7.24.4 or later: JPG, PNG, GIF (standard gif87a and gif89a)MediumIn-App Medium512 x 5121:1• All SDK versions: JPG, PNG

• Android SDK 7.24.4 or later: JPG, PNG, GIF (standard gif87a and gif89a)

📘NoteIn collapsed mode, the push image is displayed as a square, and will be cropped if the image ratio is not 1:1.

Image typeCreativeRecommended size (px)Aspect ratioStandard ImagePush: Standard512 x 512 or larger

1024 x 512 or larger1:1

2:1Slider ImagePush: Slider1024 x 512 or larger2:1Carousel ImagePush: Carousel512 x 5121:1

For iOS Push Standard Creative, you can also choose to attach video or audio files to the notifications. See the maximum file size and supported file formats:

iOS - StandardMaximum file sizeSupported file formatsImage or GIF10 MBJPEG, GIF, PNGAudio5 MBMP3, MPEG-4 AudioVideo50 MBMPEG-4

👍Tip: GIF and APNG image sizeSmaller file sizes improve display speed and performance.

Note that for floating icons using a GIF/APNG file, if displayed on a device running iOS 13 or earlier, the first frame of the GIF/APNG file will be used for the image.



Image Specifications [1]

https://docs.aiqua.appier.com/docs/image-types



Image typeCreativeRecommended size (px)Aspect ratioSupported image formatsFloating IconIn-App Creatives192 x 192 or larger1:1• All SDK versions: JPG, PNG

• iOS SDK 7.33.0 or later: JPG, PNG, GIF, APNGFull Screen ImageIn-App Full Screen720 x 12809:16

For more details about full screen image aspect ratios, see In-app pop-up full screen images.• All SDK versions: JPG, PNG

• iOS SDK 7.32.4 or later: JPG, PNG, GIF, APNGMedium ImageIn-App Medium512 x 512

512 x 256 (supported until iOS SDK 7.26.0)1:1

2:1 (supported until iOS SDK 7.26.0)• All SDK versions: JPG, PNG

• iOS SDK 7.32.4 or later: JPG, PNG, GIF, APNG

The full screen creative size is based on the screen size. While we recommend using an image with an aspect ratio of 9:16, as this ratio works the best for most devices, you may need to adjust the aspect ratio depending on the types of devices you plan to target. Specifically:

A 9:16 image aspect ratio is ideal for devices with a 9:19.5 screen aspect ratio, but may be horizontally cropped (top and bottom of image) on devices with shorter aspect ratio, e.g. 9:18, 9:16.

A 2:3 image aspect ratio is ideal for devices with a 9:16 screen aspect ratio, but may be cropped vertically (sides of image) on devices with an taller aspect ratio, e.g. 9:18, 9:19, 9:19.5.

Due to the height of full screen images, displaying in-app pop-up campaigns containing full screen images while the device is in landscape mode will cause the creative to be cropped on the top and bottom.

To avoid image cropping when displaying campaigns in landscape mode, you can use a medium image instead of a full screen image.Updated 9 months ago Table of Contents

Web push

Android push

Android in-app pop-up

iOS push

iOS in-app pop-up

In-app pop-up full screen images

Image size and image ratio

Landscape mode considerations



App Push: Standard [0]

https://docs.aiqua.appier.com/docs/standard



A standard creative can be used in app push notifications for Android and iOS, as well as web push notifications. 

The standard creative for Android push appears in two notification states: collapsed and expanded. By default, a notification appears in the collapsed state and can be expanded by swiping down. 

Android Standard Sample: Collapsed and Expanded

These are the available options:

This is the title of the notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or dynamic. The Default Title field appears if you use dynamic content in the title. The default title will be displayed for users who do not have data for the variable you selected.

This is an optional text-based component of the notification. Note that whether and where the subtitle appears in the notification depend on the Android version of the user's device.

📘NoteThe Subtitle setting is supported in Android SDK v6.0.0 and later

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit but keeping it within 30-40 characters is recommended.

The text can be either be static or personalized. 

When the user clicks on the notification, they'll be taken to the deep link specified in this field.

If not set, the user will be taken to the home page of your default website.

You can customize the text and background color of a notification in its collapsed state.

Appier SDK versionNotesAndroid SDK 7.13.0 and earlierThe collapsed notification background will be set to white when:

• A custom notification text color is set without a custom background color being set, and vice versa



App Push: Standard [1]

https://docs.aiqua.appier.com/docs/standard



• A custom notification text color is set without a custom background color being set, and vice versa

• Big Image URL > Show image preview when notification is collapsed is selected and no custom colors are setAndroid SDK 7.14.0 and later• If you set the background color but don't set the text color, the notification will use your app's default text color

• If you customize the text color without customizing the background color, the background will be transparent

The large icon image is displayed in both the expanded state and collapsed state of the notification. If the large Icon image URL is left empty, the app icon will be shown. 

See Image Specifications to upload the correct specifications. 

Host your icon image on the web to enable adding its image URL in the field. 

The image can also be personalized based on user activities.

This image is only displayed in the expanded state of the notification. 

See the Image Specifications.

Host your big image on the web to enable adding its image URL in the field. 

This image can also be personalized based on user activities.

Select Show image preview when notification is collapsed if you want to display the big image in collapsed mode of the notification. If not selected, the big image stays hidden in the collapsed mode. 

📘LimitationThe collapsed notification's background is always white for apps using Android SDK 7.13.0 and earlier when Show image preview when notification is collapsed is selected and either of the following is true:• A custom notification text color is set without a custom background color being set and vice versa

• No custom colors are set

There are three types of action buttons that can be added in a standard push:

Standard: You can add up to three standard buttons to the notification. Add the text of your action button in the Action button text field. If you add a deep link in the Deep link field, the user will be taken to the URL specified. If an URL is not added, the button functions like a close button.



App Push: Standard [2]

https://docs.aiqua.appier.com/docs/standard



Use as poll: You can add a poll in your notification with up to three poll options.

Use as coupon code: You can add a coupon code in your notification. The Button text to Copy Code field is the text shown on the action button and its default text is "Copy Coupon Code". This is what your users can click or tap to copy the coupon code to their clipboard. Add the coupon code in the Coupon Code field. 

If you want to view the notification before sending it out to your users, click this button

to send a notification to all the test devices in your Test Segment. 

By default, a notification appears in the collapsed state and can be expanded by swiping down. 

iOS Standard Sample

These are the available options:

This is title of the notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or personalized. The Default Title field appears if you create a personalized title. You can only input a text in this field.

This is an optional text-based component of the notification, similar to the title.

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit but keeping it within 30-40 characters is recommended.

The text can be either be static or personalized. 

When the user clicks on the notification, they'll be taken to the deep link specified in this field.

If not set, the user will be taken to the default website.

You can attach an image, GIF, video, or audio clip to your notification. Host your media on the web to enable adding its media URL in the field. It can also be personalized based on user activities.

🚧ImportantUse HTTPS URLs when hosting any of the following media attachments.

The icon image must adhere to the image specifications for iOS.

This gives a label to your group of action buttons. Leave this blank when sending a standard creative.



App Push: Standard [3]

https://docs.aiqua.appier.com/docs/standard



This gives a label to your group of action buttons. Leave this blank when sending a standard creative.

If you want to view the notification before sending it out to your users, click this button to send a notification to all the test devices in your Test Segment. 

Updated 9 months ago Table of Contents

Android push

Title

Subtitle

Message

Deep Link

Notification text color and Notification background color

Large icon URL

Big image URL

Include action buttons

Test creative

iOS push

Title

Subtitle

Message

Deep link

Media Attachment URL

Action Category

Test creative



App Push: Banner [0]

https://docs.aiqua.appier.com/docs/banner-image



You can send an Android push notification consisting of one or multiple banner images. If you add multiple images, the notification will become an animated banner.

The notification layout—including the title, subtitle, message, and destination URL.

Title: (Required) Enter a concise title for the notification. The title will be trimmed based on the device's screen size.

Subtitle: (Optional) The subtitle is an optional component. Its appearance depends on the Android version. Subtitles are supported on Android SDK version 6.0.0 and later.

Message: (Required) Enter the main message for the notification. The message is also trimmed based on screen size.

Destination URL: (Optional) Specify the URL that users will be directed to when they click the notification. You can set different URLs for iOS, Android, and Web by selecting the corresponding checkbox. If no URL is set, the user will be directed to the homepage of your default website.

📘NoteIn cases where the notifications are piled up in the Notification Center or if the banner image fails to load, only the title and message will appear.

Add up to 10 images for the notification. If multiple images are added, the notification becomes animated, cycling through the images.

To create an animated banner:

Host your image online and enter its URL to the Banner image URL field.

Click + Add image to upload additional images.

In the Time interval field, specify the duration (in milliseconds) between each image transition.

For more details, refer to the Android push image specifications.

The total animation time is capped at 15,000 milliseconds (15 seconds).

The cycle duration is calculated as Time Interval × Number of Banner Images.

If the total cycle time is ≤ 15,000 milliseconds (15 seconds), the banner will animate and complete as many cycles as possible within the 15-second limit. For example:

If a cycle takes 6,000 milliseconds (6 seconds), the animation will complete two cycles.

If a cycle takes 9,000 milliseconds (9 seconds), the animation will complete one cycle.



App Push: Banner [1]

https://docs.aiqua.appier.com/docs/banner-image



If a cycle takes 9,000 milliseconds (9 seconds), the animation will complete one cycle.

If the total cycle time exceeds 15,000 milliseconds (15 seconds), only the first image will be displayed.

Once the animation finishes, the banner stops on the last image.

Choose how notifications behave in the Notification Center:

Pile up: Keeps unclicked notifications in the Notification Center. Note that this option is disabled when multiple banner images are added.

Replace: Replaces this notification with incoming notifications in the Notification Center.

Push notifications are designed to expand and display the title, message, and banner image simultaneously.

In most cases, notifications will expand consistently across Android devices. However, notification behavior differs based on the different devices and SDK version in use. In earlier SDK versions, notifications may not be expandable, while newer versions ensure a fully expandable experience. 

The table below outlines how notifications behave in different SDK versions:

VersionNotification behaviorSDK v7.26.0 and earlierNotifications may not be expandable, and expanded notifications may only display either the banner image or title and message.SDK v8.0.0 and laterNotifications are fully expandable, showing the title, message, and banner image simultaneously when expanded.

To preview the notification before sending it to users, click Test creative. This will send the notification to all devices in your Test segment.

Updated 5 months ago Table of Contents

Overview

Basic settings

Advanced settings

Banner images and time interval

Banner animation cycle

Notification Center settings

Expandable notification behavior

Test creative



App Push: Carousel [0]

https://docs.aiqua.appier.com/docs/carousel



A carousel can be used to display multiple images in a single notification. Images are displayed via carousel cards. A carousel can be used as an Android or iOS push that appears in two notification states: collapsed and expanded. 

By default, the carousel appears in a collapsed state and can be expanded by swiping it down.

Android Carousel Sample: Collapsed

Android Carousel Sample: Expanded

These are the available options:

This is the title of the notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or dynamic. The Default Title field appears if you use dynamic content in the title. The default title will be displayed for users who do not have data for the variable you selected.

This is an optional text-based component of the notification. Note that whether and where the Subtitle appears in the notification depend on the Android version of the user's device.

📘Note:Subtitle is supported in Android SDK versions 6.0.0 and above.

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or personalized.

When the user clicks on the notification, they'll be taken to the URL specified in this field.

If not set, the user will be taken to the home page of your default website.

You can customize the text and background color of a notification in its collapsed state.

Appier SDK versionNotesAndroid SDK 7.13.0 and earlierThe collapsed notification background will be set to white when:

• A custom notification text color is set without a custom background color being set, and vice versa



App Push: Carousel [1]

https://docs.aiqua.appier.com/docs/carousel



• A custom notification text color is set without a custom background color being set, and vice versa

• Big Image URL > Show image preview when notification is collapsed is selected and no custom colors are setAndroid SDK 7.14.0 and later• If you set the background color but don't set the text color, the notification will use your app's default text color

• If you customize the text color without customizing the background color, the background will be transparent

The large icon image is displayed in both the expanded state and collapsed state of the notification. 

See the Image Specifications.

Host your Large Icon image on the web to enable adding its image URL in the field. 

Select Show image preview when notification is collapsed if you want to display the image in collapsed mode of the notification. If not selected, the image stays hidden in the collapsed mode.

📘LimitationThe collapsed notification's background is always white for apps using Android SDK 7.13.0 and earlier when Show image preview when notification is collapsed is selected and either of the following is true:• A custom notification text color is set without a custom background color being set and vice versa

• No custom colors are set

Add at least 3 and up to 10 carousel cards in a carousel notification. See Carousel Image for details on image specifications.

📘Note:In Android carousel push, the Headlines and Descriptions of the carousel images will only be displayed if they are added for all carousel images. If not added for all carousel images, the Title and Message of the push will be displayed in the expanded mode instead.

Check this option to enable key-value pairs in your carousel cards. A key-value pair is a set of identifiable keys and associated values. In a pair, a specific key is mapped to a certain value.

Input the key in the Key field and its designated value in the Value field. Click Add key-value pair to add multiple key-value pairs in your carousel notification.



App Push: Carousel [2]

https://docs.aiqua.appier.com/docs/carousel



If selected, the notification is dismissed from the device’s Notification Center after the user taps on a carousel image. IF not selected, the notification remains in Notification Center until the user swipes to remove it.

If you want to view the notification before sending it out to your users, click this button to send a notification to all the test devices in your Test Segment.

By default, the carousel appears in a collapsed state and can be expanded by swiping it down.

iOS Carousel Sample

This is the title of the notification and can be entered as a text or emojis by clicking on the emoji icon. There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or personalized. The Default Title field appears if you use dynamic content in the title. The default title will be displayed for users who do not have data for the variable you selected.

This is an optional text-based component of the notification, similar to the title.

This is where you can input the main message of your notification and can be entered as a text or emojis by clicking on the emoji icon. There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can be either be static or personalized. 

When the user clicks on the notification, they'll be taken to the URL specified in this field.

If not set, the user will be taken to the default website.

Click the drop-down arrow to select how your carousel push will be displayed as a notification.

Add at least 3 and up to 10 carousel cards in a carousel notification. See Carousel Image to know the image specification.

Check this option to enable key-value pairs in your carousel cards. A key-value pair is a set of identifiable keys and associated values. In a pair, a specific key is mapped to a certain value.

Input the key in the Key field and its designated value in the Value field. Click Add key-value pair to add multiple key-value pairs in your carousel notification.



App Push: Carousel [3]

https://docs.aiqua.appier.com/docs/carousel



If you want to view the notification before sending it out to your users, click this button to send a notification to all the test devices in your Test Segment.

Updated 9 months ago Table of Contents

Overview

Android push

Title

Subtitle

Message

Destination URL

Notification text color and Notification background color

Large Icon URL

Carousel Images

Include key-value pairs

Remove push from notification center after user clicks on one of the images

Test creative

iOS push

Title

Subtitle

Message

Destination URL

Carousel push style

Carousel images

Include key-value pairs

Test creative



App Push: Slider [0]

https://docs.aiqua.appier.com/docs/slider



A slider can display multiple big images in a single notification. Just like the carousel, the slider appears in two notification states: collapsed and expanded.

By default, the slider appears in the collapsed state and can be expanded by swiping it down.

Android Slider Sample: Collapsed

Android Slider Sample: Expanded

These are the available options:

This is the title of the notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or dynamic. The Default Title field appears if you use dynamic content in the title. The default title will be displayed for users who do not have data for the variable you selected.

This is an optional text-based component of the notification. Note that whether and where the Subtitle appears in the notification depend on the Android version of the user's device.

📘Note:Subtitle is supported in Android SDK versions 6.0.0 and above.

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit, but keeping it short is recommended.

The text can be either be static or personalized.

When the user clicks on the notification, they'll be taken to the URL specified in this field.

If not set, the user will be taken to the home page of your default website.

You can customize the text and background color of a notification in its collapsed state.

Appier SDK versionNotesAndroid SDK 7.13.0 and earlierThe collapsed notification background will be set to white when:

• A custom notification text color is set without a custom background color being set, and vice versa

• Show image preview when notification is collapsed is selected and no custom colors are setAndroid SDK 7.14.0 and later• If you set the background color but don't set the text color, the notification will use your app's default text color



App Push: Slider [1]

https://docs.aiqua.appier.com/docs/slider



• If you customize the text color without customizing the background color, the background will be transparent

If you’ve included slider images in the notification, it usually stays hidden unless someone expands the notification. You can display the slider images, even in a collapsed state, by ticking this box.

📘LimitationThe collapsed notification's background is always white for apps using Android SDK 7.13.0 and earlier when Show image preview when notification is collapsed is selected and either of the following is true:• A custom notification text color is set without a custom background color being set and vice versa

• No custom colors are set

Add at least 2 and up to 10 slider images in a notification. Click + Add Image to add more slider images.

A slider image uses the same image specifications as Big Images.

Host your big image on the web to enable adding its image URL in the field. 

This can also be personalized based on user activities.

Check this option to enable key-value pairs in your slider. A key-value pair is a set of identifiable keys and associated values. In a pair, a specific key is mapped to a certain value.

Input the key in the Key field and its designated value in the Value field. Click Add key-value pair to add multiple key-value pairs.

If selected, the notification is dismissed from the device’s Notification Center after the user taps on a slider image. If not selected, the notification remains in Notification Center until the user swipes to remove it.

If you want to view the notification before sending it out to your users, click this button to send a notification to all the test devices in your Test Segment.

By default, the slider appears in the collapsed state and can be expanded by swiping it down.

iOS Slider Sample

This is the title of the notification and can be entered as a text or emojis by clicking on the emoji icon. There is no character limit for the title, but keeping it within 30-40 characters is recommended.



App Push: Slider [2]

https://docs.aiqua.appier.com/docs/slider



The text can either be static or personalized. The Default Title field appears if you create a personalized title. The default title will be displayed for users who do not have data for the variable you selected.

This is an optional text-based component of the notification, similar to the title.

This is where you can input the main message of your notification and can be entered as a text or emojis by clicking on the emoji icon. There is no character limit, but keeping it short is recommended.

The text can be either be static or personalized. 

When the user clicks on the notification, they'll be taken to the URL specified in this field.

If not set, the user will be taken to the default website.

Add at least 2 and up to 10 slider images in a notification. Click + Add image to add more slider images.

See the image specifications of the Slider Image. 

Host your image on the web to enable adding its image URL in the field. 

This can also be personalized based on user activities.

Check this option to enable key-value pairs in your slider. A key-value pair is a set of identifiable keys and associated values. In a pair, a specific key is mapped to a certain value.

Input the key in the Key field and its designated value in the Value field. Click Add key-value pair to add multiple key-value pairs.

If you want to view the notification before sending it out to your users, click this button to send a notification to all the test devices in your Test Segment.

Updated 9 months ago Table of Contents

Overview

Android push

Title

Subtitle

Message

Destination URL

Notification text color and Notification background color

Show image preview when notification is collapsed

Slider Images

Include key-value pairs

Remove push from notification center after user clicks on one of the images

Test creative

iOS push

Title

Subtitle

Message

Destination URL

Slider Images

Include key-value pairs

Test creative



App Push: Subscription

https://docs.aiqua.appier.com/docs/subscription



A subscription can be used to nudge users to share their phone number or email ID using rewards. Using a subscription creative, a user can share their phone number or email from within the notification.

Subscription Sample: Notification

Subscription Sample: Form

This is the title of the notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

The text can either be static or dynamic. The Default Title field appears if you use dynamic content in the title. The default title will be displayed for users who do not have data for the variable you selected.

This is an optional text-based component of the notification. Note that whether and where the Subtitle appears in the notification depend on the Android version of the user's device.

📘Note:Subtitle is supported in Android SDK versions 6.0.0 and above.

This option allows you to select whether to prompt users to give their phone number or email ID when they tap the notification.

This is where you can input the main message of your notification and can be entered as a text or emoji (click on the emoji icon). There is no character limit for the title, but keeping it within 30-40 characters is recommended.

Enter the text you'd like to display in the action button.

If you want to view the notification before sending it out to your users, click this button to send a notification to all the test devices in your Test Segment.

Updated 9 months ago Table of Contents

Overview

Settings

Title

Subtitle

Collect user profile by

Message

Action button text

Test creative



Kakao Creatives

https://docs.aiqua.appier.com/docs/kakao-creatives



Kakao creatives can include an image, a notification message, and action buttons. For details on how to set up Kakao campaigns and creatives, see Kakao Campaign Quick Start.

Updated over 1 year ago What’s NextKakao Campaign Quick StartDid this page help you?



My Templates

https://docs.aiqua.appier.com/docs/creative-templates



Using My Templates, you can build creative templates and reuse these templates in different campaigns. A variety of premade default templates are provided to help you quickly get started. You can also choose to build creative templates from scratch.

Currently, this feature is supported in the following campaign types:

In-web campaigns built using Creative Studio: See Creative Studio.

Email campaigns: See Email Templates.

📘NoteThis feature is not supported in email campaigns inside legacy journey maps.

Updated 11 months ago



Email Templates [0]

https://docs.aiqua.appier.com/docs/email-templates



📘NoteEmail templates are only supported in regular campaigns and trigger campaigns. This feature is not supported in email campaigns inside the legacy journey maps.

To create an email template, click My Templates, and select Email Templates.

Click Create New Template.

Select one of the three methods to create an email template.

Default Templates: Modify from a default template provided by Appier.

My Templates: Modify from an existing template you have previously created.

Create Your Own: Create a template from scratch.

Design your email template. For more details on how to use the email editors, see Drag & Drop Editor or HTML Editor.

When you are done, click Save and name the template. If you add a tag, you will be able to search for templates by tags.

In the email template list, you can use the following functions to find your template.

Search Template: Search by the template name.

Type: Select Drag & Drop Editor or HTML Editor to filter based on the email editor used to create the template.

Tag: Filter based on the tags added to the templates.

Sort By: Select Last Edit to sort by last edited time or select Template Name to see the templates in alphabetical order.

You can use the menu icon under each template to edit, duplicate, or delete the template. You can also create a campaign with this template.

You can apply a template to email campaigns either from the email template list or by selecting the template from the Create Campaign page.

Option 1: In the email template list, click the menu icon of the template and select Create regular campaign or Create trigger campaign.

Option 2: When creating campaigns, click Add Email Creative under the CREATIVE section and select My Templates to find the template.

After you have selected a template, you can make further adjustments if needed and save the modified template to this campaign. If you want to save this modified template as a new template for future use, click Save as new template.

Updated over 1 year ago Table of Contents

Creating Email Templates



Email Templates [1]

https://docs.aiqua.appier.com/docs/email-templates



Updated over 1 year ago Table of Contents

Creating Email Templates

Managing Email Templates

Using Templates in Email Campaigns



Exploring Creative Studio [0]

https://docs.aiqua.appier.com/docs/exploring-creative-studio



Navigating Creative Studio is simple and user-friendly. Whether you're designing creatives from scratch or using prebuilt templates, you can easily find your way around with a few clicks. 

You can enter Creative Studio through two different methods: 

From the navigation sidebar

From campaign creation

To access Creative Studio from AIQUA's navigation sidebar, click My templates > Creative Studio.

To use Creative Studio templates when creating in-web or in-app campaigns, go to the Creative Editor section and select Creative Studio, click Add Creative, and choose a Creative Studio template to design your campaign.

There are two ways to start designing a template in Creative Studio:

Select an existing template 

Create a new template

Once you enter Creative Studio, select an existing template from the template list or search for a specific template by name or ID.

Each template supports the following actions:

Edit: Modify the selected template.

Duplicate: Create a copy of the selected template.

Copy template ID: Copy the unique template ID for reference.

Delete: Remove the template from your list.

Click + Create New Template to design your own template.

You can choose from three options to get started:

Default templates: Prebuilt templates provided by Appier for immediate use.

My templates: Your saved and customized templates.

Create your own: Start from scratch and design your own template.

Go to the Default templates tab to browse prebuilt templates. You can quickly find the right template by:

Searching by template name or ID.

Filtering by Goal, Format, or Device.

Sorting by Last edit or Template name.

Go to the My templates tab to choose from your previously saved and customized templates.

Go to the Create your own tab and click + Create from scratch to start designing a whole new template. 

Next, proceed to Designing Creatives to learn how to work with elements, manage views, and optimize your creatives for all devices.Updated about 2 months ago Table of Contents

Accessing Creative Studio



Exploring Creative Studio [1]

https://docs.aiqua.appier.com/docs/exploring-creative-studio



Accessing Creative Studio

From the navigation sidebar

From campaign creation

Start designing a template

Select an existing template

Create a new template



Designing Creatives [0]

https://docs.aiqua.appier.com/docs/designing-creatives



Creative Studio provides a powerful interface for designing engaging creatives. Follow the instructions below to learn how to use various elements, manage views, and optimize your designs for different devices with Creative Studio:

Name your template

Add elements

Customize the elements

Preview creatives across devices

Manage creatives with views 

Modify animations and manage elements 

Save the template

In addition, refer to the best practices to optimize your designs and ensure effective use of Creative Studio's features. 

📘NoteYou can also start with our prebuilt templates and customize them for your specific use case to save your time while still achieving a personalized design.

Enter a unique and descriptive name for your template at the top of the interface to quickly identify and manage your work in Creative Studio.

The left toolbar offers various types of elements to facilitate interactions with your end users. Drag and drop elements to the creative canvas to add and customize your creatives.

Button: Add clickable buttons that trigger actions in your creative.

Checkbox: Use checkboxes to select multiple options or indicate true/false choices.

Input field: Allow users to input text or other types of data.

Radio: Use radio buttons to let users select a single option from a list.

Drop-down list: Allow users to select from a predefined set of options.

Text element: Display written content to inform or guide users within your creative.

Image: Add static images to enhance visuals in your creative.

Video: Embed video content to engage your audience within your creative.

Custom content: Embed external content or custom code for flexible or unique additions.

Wheel of fortune: Create interactive spinning elements for gamified experiences.

Use the right sidebar's four tabs to customize elements within each view:

Settings: Change element names, adjust accessibility features, define placements, and set animations. Available options may vary depending on the selected element.



Designing Creatives [1]

https://docs.aiqua.appier.com/docs/designing-creatives



Styles: Customize the appearance of elements by adjusting text styles, background colors, borders, and more. Available options may vary depending on the selected element.

Actions: Define what happens when users interact with an element (for example, button clicks). Use the Check and Action sections to define conditions and their corresponding actions. To avoid unexpected behavior, avoid adding actions after the Exit action.

👍TipsSee Creative Elements to learn more about the customizable options for each element.

Preview how your creative will look on different devices. The central preview area shows how your creative will appear on desktop, mobile, and other devices, ensuring a consistent user experience across all platforms.

For in-web campaigns, preview your creatives directly on your website by entering the URL and clicking Preview.

In Creative Studio, a creative can consist of multiple views, allowing you to build interactive and multistep web content for your users.

To manage creatives with multiple views, use the view management panel at the bottom of the interface. View 1 is added by default. To add more views, click the + icon in the rightmost thumbnail and repeat the add elements step to create additional views.

Switch between views to edit different parts of your creative. Each view represents a step, and all steps are shown as miniature previews in the panel.

The right sidebar provides two key areas for enhancing your creative's functionality and organization:

Animation: Control how views transition and animate.

Elements: Organize and manage elements within each view.

This tab lets you control how views appear and disappear. You can enable animation effects, select the style, and set the duration.

Entrance animation: Apply effects when the first view appears.

Between views: Add animation effects for transitions between steps.

Exit animation: Set the effect when a view closes.



Designing Creatives [2]

https://docs.aiqua.appier.com/docs/designing-creatives



Between views: Add animation effects for transitions between steps.

Exit animation: Set the effect when a view closes.

In the Elements tab, you can manage and reorder elements within a view. The structured tree format helps you navigate through elements, adjust their order, and toggle their visibility.

📘NoteIf any settings are incomplete, an alert icon will appear. Click the icon to go directly to the incomplete settings.

Once you're satisfied with your design, click Save.

If you're creating a new template, you'll be redirected to the Creative Studio template list.

If you're designing from the in-web or in-app campaign creation interface, you'll be redirected back to the campaign creation screen.

To preview your creative on your website, click Generate link to create a preview campaign.

Preview in-app creatives directly in the AIQUA dashboard to see how they will display in your app or website.

Use these best practices to ensure a smooth user experience across all campaigns:

Design and user experience

Form handling

Interactive elements

Follow these best practices to design effective campaigns and enhance the user experience:

Include a close button 

Optimize image sizes 

Ensure mobile responsiveness

Highlight required input fields

For in-app campaigns, always add a close button to allow users to exit the campaign.

Use smaller images to improve load times and enhance user experience.

Consider mobile users when designing your creatives to provide a seamless experience across all devices.

Use mobile-optimized templates: Creative templates with (Mobile) in the template names are pre-adjusted to fit mobile devices.

Modify other templates to make them mobile-friendly:

Use the mobile icon to preview how the creative looks on mobile devices.

Make necessary adjustments to ensure proper display on smaller screens.

Under the Settings tab, check Input required to highlight elements when users attempt to proceed without entering input or making a selection.



Designing Creatives [3]

https://docs.aiqua.appier.com/docs/designing-creatives



For example, when a radio button element is set to Input required, ensure the "Next" button is set up correctly:

Select the "Next" button and go to the Actions tab.

Under ...check if..., ensure there's a condition set to View inputs are valid. If no condition is set yet, select + Check to add one.

Enable the Highlight check failures option.

Learn how to manage form submissions and input validation:

Preventing duplicate submissions

Validating form inputs

To avoid multiple submissions of the same form:

Select the "Submit" button and navigate to the Actions tab.

Click + Action and choose Submit form.

Add another action: Change view to redirect users to a "Thank You" page.

To ensure all required fields are filled correctly:

For each required field (for example, email input):

Set the Input type appropriately (for example, Email field).

Check Input required in the Settings tab.

For the "Submit" button:

In the Actions tab, set a Check condition to View inputs are valid.

Set the Action to Submit form.

Discover how to set up engaging interactive features in your campaigns:

Discount banner example

Limit the number of spins

For a discount banner with a "Shop Now" button:

No Check conditions are needed.

Set the Action to URL to redirect users to the product page when they select the "Shop Now" button.

When creating interactive creatives with the wheel of fortune, follow these steps to limit the number of spins each user can have:

Select the wheel of fortune element, navigate to the Settings tab, and set the number of spins allowed to limit how many spins each user can have.

Navigate to the Actions tab.

Select + Check, then choose Spins count to verify if the user has reached the spin limit.

Select + Action, and set the first drop-down to Change view to display a message like "You've reached your spin limit. Thank you for playing!"

Updated 2 months ago Table of Contents

Overview

1. Name your template

2. Add elements

3. Customize the elements

4. Preview creatives across devices

5. Manage creatives with views



Designing Creatives [4]

https://docs.aiqua.appier.com/docs/designing-creatives



2. Add elements

3. Customize the elements

4. Preview creatives across devices

5. Manage creatives with views

6. Modify animations and manage elements

7. Save the template

Best practices

Design and user experience

Form handling

Interactive elements
