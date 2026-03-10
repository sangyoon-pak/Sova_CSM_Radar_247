---
source: notebooklm_export
file_id: "071"
filename: "071_bb_rc_part_3.txt.txt"
doc_type: "reference_card"
product: "BotBonnie"
content_type: "txt"
language: "en"
guide_summary: "This documentation outlines the comprehensive features of BotBonnie, focusing on **journey maps** for automated user engagement and **growth tools** for acquiring and managing users across various messaging platforms like LINE, Facebook, and Instagram. Key themes include the structured **creation and analysis of user journeys**, which involve triggers like date-based attributes and sequential nodes for messages, splits, waits, and updates. The platform also details **advanced functionality**, su"
guide_keywords: "Journey Maps, Growth Tools, Auto Reply, Live Chat, Broadcast Messages"
---

# 071 bb rc part 3

Getting Started with Journey Maps [2]

https://docs.botbonnie.appier.com/docs/getting-started-with-journey-maps



Date-format user attributes can be used as a date-based trigger for users to enter the journey.

Below are the channels you can use in journey maps. No additional integration is required if you are already using these channels on BotBonnie.

LINE

Facebook

WebChat

WhatsApp

Zalo

Viber

To use LINE campaigns in journey maps:

If you are already using LINE on BotBonnie, no additional integration is required.

If you have not set up LINE integration before or if you have previously set up LINE integration through AIQUA, you must integrate your LINE Official Account through the Appier Enterprise Console.

To integrate, log into Appier Enterprise Console (https://console.appier.com/) and follow the LINE integration guide.

Existing LINE users and any associated user data from the AIQUA LINE integration will be synced in journey maps.

Updated 9 days ago



Creating a Journey Map

https://docs.botbonnie.appier.com/docs/creating-a-journey-map



The journey map creation process consists of the following steps:

Choose a journey creation method

Add journey nodes

Configure schedule and re-entry settings

Test and publish the journey

Updated 9 days ago Getting Started with Journey MapsChoose a Journey Creation MethodDid this page help you?



Choose a Journey Creation Method

https://docs.botbonnie.appier.com/docs/choose-a-journey-creation-method



From the left menu, go to Journey map, then click + Create journey map. Next, choose a journey creation method.

After adding a new journey map from scratch or from a template, you can use journey copilot, your AI-powered assistant, to automatically generate a journey map based on a text description of the desired user journey.

To learn more, see Journey Copilot.

Start from scratch: Start with a blank canvas and manually add nodes to construct a user journey.

Choose a template: Start with a prebuilt template based on a specific use case, such as "New User Registration" or "First Purchase incentive", then modify the specifics to suit your needs.

To start with a blank canvas, click + Start from scratch.

The journey maps feature comes with a list of prebuilt templates based on specific use cases.

Hover over a template to read a description of the journey and preview it by clicking the eye icon. If you're ready to start editing with the template, click Use this template.

Fill out the basic settings of the journey and click Continue.

Journey map name: Enter a name for the journey map.

Conversion event: Add up to six conversion events to track how often users take specific actions after entering the journey.

Offline events are labeled with an Offline tag for easy identification, helping you quickly distinguish offline actions from online actions for more accurate tracking and reporting.

Exit rule: Select one exit event. Users are exited from the journey after completing the exit event.

You can also use an offline event with Offline tag as an exit rule.

📘Exit the journeyThere are three ways for users to exit the journey:

They reached an exit node on the map.

They have completed the exit event.

They are dropped because they are not reachable.

Next, proceed to add nodes to your journey.Updated 9 days ago



Journey Copilot

https://docs.botbonnie.appier.com/docs/journey-copilot



After adding a new journey map from scratch, you can use journey copilot, your AI-powered assistant, to automatically generate a journey map based on a text description of the desired user journey, for example:

"Drive newsletter sign-ups for exclusive product launch notifications."

"Increase user engagement by promoting participation in a seasonal winter sales event with limited-time discounts."

"Boost customer retention by encouraging recent purchasers to join the loyalty program, offering points for every purchase, and promoting upcoming exclusive member events and sales."

After copilot generates a journey, you can review the nodes and settings before applying the changes to your journey map.

Open the journey map you'd like to edit and click the copilot icon at the top right corner of the canvas.

In the copilot window, enter a description of the desired user journey.

If you're not sure how to write a description, click Try example for a list of suggestions. You can click on any example to generate a journey based on that description.

Next, click Generate to see what the copilot-generated journey looks like.

If the resulting journey settings are suitable for your marketing scenario, click Apply to add the journey to the canvas.

📘NoteThe journey generated by journey copilot won't be applied to the canvas until you click Apply.

The copilot-generated journey is now saved, and you can continue to add and edit journey nodes or directly proceed to configure the journey's schedule and re-entry settings.Updated 9 days ago



Add Journey Nodes [0]

https://docs.botbonnie.appier.com/docs/add-journey-nodes



Each node in the journey map is a step in the user journey, and each node contains settings related to its specific purpose. For example, a message node contains campaign creative settings, while a split node contains logic for splitting users into different paths.

The first step in creating your journey is to add an entry trigger node, which specifies how users enter the journey. Next, continue customizing your journey by:

Adding nodes

Edit nodes

Copying nodes

Deleting nodes

Undoing and redoing changes

To add a node, click on the + that appears in the journey map. After clicking the add button, you'll be able to select one of the following node types:

Entry trigger node: Specify how users will enter the journey. Only available as the first node in the journey. For details, see Entry Trigger Node.

Message: Reach out to users across different channels. In a message node, you can set up the creative you want to send. For details, see Message Node.

Split: Specify a condition that splits users into different paths. For details, see Split Node.

Wait: Wait for a certain amount of time before continuing to the next node. For details, see Wait Node.

Update users: Update user-related information. For details, see Update Users Node.

To edit a node, simply click on it, and its settings panel will open on the right. Then, you can modify its settings and click Save to apply the changes.

To delete a node, hover over it and click the trash can.

Next, choose how to handle the path after the node you're deleting, then click Confirm.

The available deletion options will differ depending on the node type. For example, if you're deleting a message node, you can choose whether to delete the path for reachable users, the path for non-reachable users, or both.

To copy a node and its subsequent branches, hover over the node and click on the copy button. After clicking the copy button, you can copy the node into any of the available positions shown in the journey.



Add Journey Nodes [1]

https://docs.botbonnie.appier.com/docs/add-journey-nodes



In the bottom right corner of the canvas, you'll find undo and redo buttons, which allow you to revert or reapply the following operations:

Adding a node

Deleting a node

Copying and pasting a node

Updated 9 days ago



Entry Trigger Node [0]

https://docs.botbonnie.appier.com/docs/entry-trigger-node



The entry trigger node allows you to specify how users should enter the journey. Click Add a trigger and select a trigger type:

Past condition

Real-time event

Date-based

You can use existing segments to be the past conditions, or manually define the conditions using events and attributes. After the journey becomes active, the system will import users who meet the conditions into the journey. After the initial import, the system will check for qualified users every 6 hours and add them to the journey.

Use segments: Select segments you want to include or exclude. You need to include at least one segment.

Define conditions: Select the events and attributes you want to include or exclude.

The Users to include section allows you to include users who have the specified user attributes or have performed the specified user events. The Users to exclude section allows you to exclude users who have the specified user attributes or events.

You can add one or multiple conditions. If you select All, users need to match all conditions to be considered a match. If you select ​Any, users who match any of the conditions will be considered a match.

Enter a number for Only consider events in the last x days. Only events that occurred within that time period will be used to calculate qualified users. This setting does not apply to user attributes that are set as conditions.

📘LimitationNew offline users uploaded within one day may not be processed in time to be considered in the past conditions.

You can select one event to be the trigger. Users will only enter the journey if the event happened after the journey becomes active. If the event is an offline event, the event timestamp must be later than the journey activation time, and the users will enter the journey after the offline events are uploaded.

To set an audience filter, select Only include users in the selected segment and select up to 5 segments. The system will check for qualified users in segments every 6 hours.



Entry Trigger Node [1]

https://docs.botbonnie.appier.com/docs/entry-trigger-node



You can let users enter the journey based on a date that is associated with that user. Here are some common ways to use a date-based trigger.

Birthday: Send a coupon to users during the month of their birthday

Membership expiration date: Send a renewal reminder to users 5 days before their membership expires

📘NoteSee Tracking date format data for requirements to use user attributes as date-based triggers. Currently, event parameters cannot be used as date-based trigger.

Select the user attribute you want to use as the trigger, and set up the timing of the trigger. If you want to use a date in the past, such as the user's birthday, select Ignore the year in the date.

In the screenshot below, users will enter the journey on the first day of the month of their birthday. For example, a user with a birthday on 1980-04-10 will enter the journey on April 1 every year during the journey schedule. If Ignore the year in the date is not selected, the journey will not be triggered because the user's birthday is in 1980 when the year is considered.

Updated 9 days ago



Message Node

https://docs.botbonnie.appier.com/docs/message-node



Message nodes allow you to reach out to users across all your integrated channels. Depending on the channel you select, you can either add a creative or a chatbot flow module.

Adding a message node

Set the split criteria

Click on any + icon that appears between and after nodes, then click Channels, and select the channel you'd like to use to send the message.

Next, enter a node name and set up the creatives or flow modules, depending on whether you selected a message node for an AIQUA channel or BotBonnie channel.

If you add a message node for an AIQUA channel, you'll see a button to add a creative.

👍To learn more about each creative and its settings, refer to the table of creative types.

For app push channels (Android and iOS), you also have the option to use advanced templates. To view the available advanced templates, select Use advanced Android template or Use advanced iOS template.

If you add a message node for a BotBonnie channel, you'll see a button to add a flow module.

👍To learn more about creating modules, see Modules and Messages.

Dynamic content in message nodes enables you to create personalized interactions by customizing messages based on available user data. To insert personalized content, click the {⋯} icon in supported creative fields.

BotBonnie channels support user attributes and events for dynamic content personalization. Note that only data collected through BotBonnie can be used.

LINE

Facebook Messenger

WhatsApp

WebChat

Viber

Zalo

📘NoteKakao Talk currently does not support dynamic content.

User demographics collected through BotBonnie.

Custom parameters created in BotBonnie.

User events, including:

Cart items (from product_added_to_cart events)

Browsed items (from product_viewed events)

Purchased items (from product_purchased events)

Users who receive the message will be split into two paths depending on whether the message was sent, or clicked. You can click the dropdown menu to change the split criteria.

Updated 9 days ago



Split Node

https://docs.botbonnie.appier.com/docs/split-node



Split nodes allow you to split users into different paths. To add a split node, click the circle in between nodes, and select one of the following:

Check condition

Check reachability (Note: Only available for BotBonnie channels)

AB testing

You can create scenarios that are based on user events and attributes in the past and then split users into different paths on the journey map if they meet the conditions of the scenario. If no scenarios are matched, the users will enter the "Not matched" path.

👍"Check condition" vs "Wait for condition"Use Check condition when you want to split users based on conditions in the past, which can be user attributes that already exist or events that already happened. If you want to wait for users to complete an event in the future, use Wait for condition instead.

📘LimitationEvents that happened within 1 hour may not be processed in time to be considered in the Check condition node.

If you create multiple scenarios, the ones closer to the top of the list have higher priority. Users who meet the conditions of multiple scenarios will enter the path of the scenario closer to the top. You can adjust the order of the scenarios by clicking the arrow buttons.

You can split users based on their reachability in different channels.

Select the channel next to Check if the users are reachable on and select the LINE Official Account. If needed, click Add Channel to add more paths for other channels.

📘NoteCurrently, only the reachability of LINE, Facebook Messenger, WebChat, and WhatsApp are supported.

You can split users randomly to conduct AB testing. Under User distribution, you can name and specify the percentage of users who should be assigned to each path.

Manually enter a percentage for each path (the percentage must add up to 100%) or click Divide equally to equally distribute users to each path.

You can add up to five test paths.

Updated 9 days ago



Wait Node

https://docs.botbonnie.appier.com/docs/wait-node



Wait nodes allow you to control when users should move to the next node. To add a wait node, click the circle in between nodes and select one of the following types:

Time delay

Wait for condition

You can keep the users at the current node for a period of time or until a time slot.

Wait for a period of time: Users are moved to the next node in the journey map after a certain period of time has passed. You can set a duration under How long should people wait for.

Wait until a time slot: Users are moved to the next node in the journey map when they reach a specified timeslot during the day or during the week.

Select Daily if you want to set timeslots during certain hours of the day.

Select Weekly if you want to set timeslots during certain days of the week.

Users are moved to the next node in the journey map when they perform certain events. You can select up to 3 events to be the condition. Users meet the criteria when they complete any one of the events.

If the user does not complete the event for a period of time, they will be moved to the Timeout path. Under Timeout, you can click the edit icon to adjust the timeout period.

Updated 9 days ago



Update Users Node

https://docs.botbonnie.appier.com/docs/update-users-node



Use the update users node allows you to modify a user's details when they enter the node.

📘NoteThis node type is only supported for users on BotBonnie channels. It has no effect for users on AIQUA channels.

Click on the node to open its settings.

To configure tags to add to the user, click the input box under Add the following tags to users.

To configure tags to remove from the user, click the input box under Remove the following tags to users

To add an existing tag, select from the list of tags that appear, then click Ok.

To add a new tag, type the tag name directly into the input box, then click Create tag.

Updated 9 days ago



Advanced Node [0]

https://docs.botbonnie.appier.com/docs/journey-maps-advanced-node



## Overview

Use advanced nodes to implement more complex functionalities in your journey, such as integrating with external APIs and services.

* [Webhook node](#webhook-node) 



***

## Webhook node

A webhook is an automated HTTP request sent by from one service to another when a specific event occurs. You can use webhooks to enhance your journey by integrating external APIs and services, enabling you to personalize the next steps in the journey. 

When a user reaches the webhook node, an HTTP request is triggered to an external service to retrieve data which can be used to tailor the campaign in real time, supporting use cases such as:

* Fetching location-based data such as weather.

* Retrieving customer profile details.

* Checking inventory status.

To create a webhook node, click on any **+** icon that appears between and after nodes, then click **Advanced > Webook**.



Clicking the newly added node opens the settings panel with the following fields:









Name





Required





Description





Example













**Node name**





Yes





Enter a name for this node.





"Send coupon"









**Target URL**





Yes





Enter the API's endpoint URL.





`https://www.example.com/coupon_endpoint`









**HTTP method**





Yes





Select an HTTP method from the dropdown.





`GET`









**QPS**





No





Enter the maximum number of queries to send.





`10`









**Batch requests enabled**



Advanced Node [1]

https://docs.botbonnie.appier.com/docs/journey-maps-advanced-node





Enter the maximum number of queries to send.





`10`









**Batch requests enabled** 

**Batch size** 

**Batch – Minimum interval**





No





Batch multiple API calls into a single request. 

* **Batch requests enabled**: To enable batching, enter "true" into the input field. 

* **Batch size**: Enter the maximum number of requests to batch together. 

* **Batch – Minimum interval**: Specify the interval (in milliseconds) at which the batch request will be sent, regardless if the batch size has been met.















**HTTP header**





No





Enter any required HTTP headers.





`{"Authorization": "Bearer TOKEN"}`









**Content type**





No





Specify the request's content type.





`application/json`









**Request body**





No





Enter the request body content. 

To dynamically insert user attributes in the request body, use `{{ }}`. For example, to insert the value of the user's `email` attribute, use `{{email}}`.





`{"membership_email":"{{email}}"}`









**Response field mapping**





No





Create a mapping between webhook response field names and the name you'd like to use when [creating conditions](#creating-conditions-based-on-webhook-responses) or for use in [dynamic content](#using-webhook-fields-to-populate-dynamic-content). 

Tip: Use dot notation to map nested fields.





`{"coupon.code": "coupon_code", "coupon.discount_pct": "discount"}`









After completing the webhook settings, you can:

* [Create conditions based on webhook responses](#creating-conditions-based-on-webhook-responses) which determine the path users should take next in the journey.



Advanced Node [2]

https://docs.botbonnie.appier.com/docs/journey-maps-advanced-node



* [Use webhook fields to populate dynamic content](#using-webhook-fields-to-populate-dynamic-content) in the journey's subsequent campaigns.

### Creating conditions based on webhook responses

Select **Check response** to start creating scenarios to split users by. In a scenario, you can add one or more conditions based on the webhook's responses.



In each scenario, next to **Match**, determine whether users need to satisfy all conditions or any conditions in the scenario to split into the scenario.



Next, for each condition in the scenario, configure the following:

1. Field name: Enter the name of the field in the webhook response.

2. Data type: Select the field's data type.

3. Operator: Select the operator used to evaluate the field's value. The data type you selected determines what operators are available.

4. Value: Enter the value to compare the field's value against.

After adding the desired scenarios and conditions, click **Save**.



### Using webhook fields to populate dynamic content

Use the syntax provided in the following table to insert dynamic content in your campaign. Note that the syntax will differ depending on the campaign channel.









Campaign channel





Dynamic content syntax













• Web push

• App push

• Email

• SMS

• In-app

• In-web





`{{ctx_}}` 

Replace `` with one of the values you specified in the response field mapping.



Advanced Node [3]

https://docs.botbonnie.appier.com/docs/journey-maps-advanced-node



Replace `` with one of the values you specified in the response field mapping. 

















• WebChat\

• WhatsApp\

• Zalo\

• Viber





`{{extra_params_}}` 

Replace `` with one of the values you specified in the response field mapping. 















Updated 9 days ago



Journey Schedule and Re-entry Settings

https://docs.botbonnie.appier.com/docs/journey-schedule-and-re-entry-settings



After you finish designing the journey map by adding journey nodes, click Next to complete the journey settings.

Under Journey schedule, set the start time and the end time of the journey.

Under Journey re-entry, select a re-entry rule.

Users can enter this journey only once: Once exited, users will not re-enter this journey.

Users can re-enter this journey up to X times after exiting: Enter the maximum number of times users can enter this journey and set a minimum interval between entries.

Users can re-enter this journey any number of times after exiting: Users can re-enter this journey an unlimited number of times during the journey schedule. Set a minimum interval between entries.

📘Note

If you allow users to re-enter the journey, be sure to set an appropriate minimum interval to avoid sending too many messages to users. After the minimum interval has passed, users will re-enter the journey if the past conditions are met or when they complete the real-time event.

If you edit the re-entry rule after a journey becomes active, users who are already in the journey but have exceeded the maximum number of re-entries will continue to finish the journey.

Push notifications in journey map are also capped by the daily limit set in account settings. The minimum intervals in account settings do not affect journey map messages.

Updated 9 days ago



Test and Publish the Journey

https://docs.botbonnie.appier.com/docs/test-and-publish-the-journey



After you've finished creating your journey, you can test the journey to visualize how a user traverses the journey before publishing it. From the top bar, click Test journey.

To add a test user, click Select user and search for the test user. Next, select a user, and click Select.

Search by entering the complete email, phone number, or user_id. The search results only include users who exactly match the data you entered. Searches are case-sensitive.

You can only add one test user.

Under Wait time settings, you can shorten the wait nodes to speed up the test process. Select Set all wait times (time delay nodes, time-out settings) to and set a new wait time. The wait time will be applied to the following nodes.

Time delay nodes

Wait for conditions nodes: Time-out settings

Message nodes: Time-out settings

Under Trigger node settings, if you select Bypass the trigger node, the test user will automatically enter the journey even if they do not meet the trigger condition.

Finally, click Start test journey to begin testing. In test mode, you can see the test user's position in the journey.

📘NoteYou may be subject to messaging fees when you send email and SMS messages during the test.

When you have completed the settings, click Publish.

Once the journey starts running, its status will change to Active.

To make edits after publishing, you need to pause the journey first. To pause a journey, click the three dots next to the journey's name, then click Pause journey map.

Please note that making certain types of edits on a journey after publishing it may affect performance data.

Changing the journey structure (e.g. moving a node to another position) will clear the performance data of each affected node.

Modifying a creative in a message node has no effect on that node's performance data.

Updated 9 days ago



Journey Performance and Analytics [0]

https://docs.botbonnie.appier.com/docs/journey-performance-and-analytics



After a journey has started running, you can see the performance and analytics of the journey map. Refer to the sections below.

How users flow through the journey

Journey overview

Node details: Node stats

Campaign performance of the message node

Node details: Performance

Overall performance of the journey map

Journey analytics

Journey map list

📘NoteMetrics related to Offline conversions appear only if your journey includes offline events. By default, these columns remain hidden until you publish a journey with offline events enabled.

You can click the journey to see how the users move through the journey under the Journey Overview tab.

Under the nodes, the following metrics are available:

Entered: The number of users who met the trigger condition and started the journey by entering the entry node. Re-entered users are counted each time they enter.

Arrived: The number of users who arrived at this node. In message nodes, this is the number of users the system has tried to send the message to. To see the actual sent, views, delivered, and clicked metrics, open the message node and see the Performance tab instead.

Moved forward to: The number of users who have moved on to the next node. If there are multiple paths after this node, you can click the expand arrow to see the user counts for each path. In message nodes, if the user interaction (e.g. a click) happens after the timeout period has passed, the user will still remain in the no interaction path (e.g. not clicked path).

On hold: The number of users who are on hold at this node for a fixed duration or until a time slot.

Wait for response: The number of users who are kept at the message node until they interact with the message or until timeout.

Exited journey: The number of users who exited the journey at this node. Click the expand arrow to see the following numbers:

Exit rule met: The number of users who exited the journey by completing the exit event specified in the exit rule.



Journey Performance and Analytics [1]

https://docs.botbonnie.appier.com/docs/journey-performance-and-analytics



Exit rule met: The number of users who exited the journey by completing the exit event specified in the exit rule.

Dropped: The number of users who exited the journey because they were not reachable in the channel. For example, users who entered the email message path in the journey but do not have a valid email address.

Complete: The number of users who completed and exited the journey because they reached an exit node in the flow.

Open each node to see the following tabs.

Node overview: Shows the summary of the node conditions or message content.

Node stats: Shows the number of users who arrived at the node, moved forward to the next node, are currently being held at the node, and exited the journey while they are at the node.

Performance: Available only for message nodes, this tab displays delivery status, campaign performance data, and a detailed breakdown of conversion metrics.

Message metrics: Shows views, clicks, and conversions.

Funnel: Provides a visual representation of key metrics such as views, clicks, and conversions over time.

Timeline: Allows you to view metrics by day, week, or month for a more targeted analysis.

Open the journey and click the Journey analytics tab to view key performance metrics and visualized trends for conversions, conversions value, total exits, and total clicks of your journey.

Using the date range selector and interval drop down menu to analyze data across different time periods.

In the journey map list, you can see the following performance metrics of the journeys.

Entered: The number of users who met the trigger condition and started the journey. Re-entered users are counted each time they enter.

Conversion: The total number of conversion events completed by users who entered the journey.

Conversion rate: Calculated using (Goal conversions / Entered) x 100%.

Conversion value: The total value of online conversions from all channels in the journey.

Offline conversions: The total number of offline conversion events completed by users who entered the journey.



Journey Performance and Analytics [2]

https://docs.botbonnie.appier.com/docs/journey-performance-and-analytics



Offline conversions: The total number of offline conversion events completed by users who entered the journey.

Offline conversion rate: Calculated using (Offline conversion events / Entered) x 100%.

Offline conversion value: The total value of offline conversions from all channels in the journey.

Exit rule met: The number of users who exited the journey by completing the exit event specified in the exit rule.

Completed: The number of users who finished the journey after reaching the last node of a path, excluding the not-reachable paths.

Dropped: The number of users who exited the journey because they were not reachable in the channel. For example, users who entered the email message path in the journey but do not have a valid email address.

See FAQs related to analytics and performance here.Updated 9 days ago



Journey Map FAQs

https://docs.botbonnie.appier.com/docs/journey-map-faqs



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

To see the actual sent, views, delivered, and clicks metrics, open the message node and see the Performance tab instead.Updated 9 days ago



Merging Offline and Online User Data [0]

https://docs.botbonnie.appier.com/docs/merging-offline-and-online-user-data



Journey maps allow you to connect online and offline user data to create a seamless experience for your customers. You can upload offline events that occurred in your physical stores, such as purchases and membership registrations, and use these events in journey maps.

See Use case: encourage offline purchase for an example.

In journey maps, users across different channels are unified based on user_id. To learn more about the requirements and limitations of using offline events in journey maps, see the requirements for offline events and segments.

Follow the best practices below to ensure offline events are effectively uploaded and used in journey maps.

Upload events frequently

Add an upload time interval

Unlike online events tracked via Appier SDK, offline events need to be uploaded to AIQUA via APIs. As a result, there will always be a time gap between when the event actually occurred and when the event is uploaded.

We recommend uploading offline events at least once a day if you want to use offline events or segments in journey maps.

In some nodes, you can extend the time periods to allow more time for offline events to be uploaded.

Past condition: Add the upload time interval to the time period you want to set in Only consider events in the last x days. For example, if your event upload interval is one day and you want to consider events in the last 3 days, set the Only consider events in the last x days settings to four days.

Real-time event: The event timestamp must be later than the journey activation time, and the users will enter the journey after the offline events are uploaded.

Wait for conditions: Extend the timeout period by adding the event upload interval. For example, if your event upload interval is one day, and you want to wait seven days for users to complete the conditions, set the timeout period to eight days.



Merging Offline and Online User Data [1]

https://docs.botbonnie.appier.com/docs/merging-offline-and-online-user-data



Check condition: Insert a time delay node before the check condition node to make sure offline events are already uploaded before users proceed to the check condition node. For example, if you upload offline events once a day, you can add a time delay node to put users on hold for a day.

Goal event: Goal events are calculated based on the actual timestamp of the offline events. The event count will be added after the event upload, but the end results are not affected.

Exit rule: Users who meet the exit rule will exit the journey after the exit events are uploaded.

Let's say you want to send marketing campaigns to the VIP members to encourage offline purchases in your physical stores.

First, make sure offline purchase events are uploaded to AIQUA daily.

Next, set up the journey map as below.

In the entry trigger node, select Past condition and set the condition to include VIP members.

Add a Wait for condition node and add the offline purchase event as the condition.

In the Matched path, add a thank-you email to users who have completed offline purchases.

In the Timeout path, email encourage offline purchases.

If the email is opened, send another email to follow up. If the email is not opened, send a message through SMS instead.

Set the offline purchase event as the goal event and exit rule.

Updated 9 days ago



AI Rules

https://docs.botbonnie.appier.com/docs/ai-rules



Add AI rules to respond to user messages based on designated keywords. No matter where a user is in the flow, if their message contains a designated keyword, your bot will respond with the dialogue module you specify.

The bot tries to respond based on the current module's user input settings.

If there is no configured response for user input, the bot tries to respond using AI rules.

If there are no configured responses for user input or AI rules, the auto reply is sent.

Go to Content > AI rules, then click + Add AI Rule. The new rule will be added to the top of the rule list.

Click on the newly added AI rule to expand its settings. First, provide the keywords in the user's message that should trigger the rule. Next, specify how the keywords should be matched:

Contains any keywords: The user's message can contain any of the specified keywords.

Contains all keywords: The user's message must contain all the specified keywords.

Exact match: The user's message must match the specified keyword exactly, without any additional text.

📘Note

AI rule keywords are not case-sensitive.

AI rule keywords are width-sensitive (full-width and half-width characters are not the same).

Under Bot reply, open the dropdown and select the module that should be sent to the user when this rule is triggered.

To see the module details, click its name.

Click Set up triggered actions to configure additional triggered actions.

After completing all the settings, click the Deploy bot at the top right of the page to deploy your changes.

You can search for your AI rules by name or the keywords they use.

To disable or re-enable an AI rule, click the toggle under Status.

Updated 9 days ago



LINE Beacon [0]

https://docs.botbonnie.appier.com/docs/line-beacon



LINE Beacon enables your bot to detect when users enter a beacon region and interact with them using personalized messages. By integrating LINE Beacon with BotBonnie, you can deliver timely and relevant communications tailored to your business needs.

For example, you can use LINE Beacon in:

Retail stores: Greet customers with a welcome message, share promotions, provide store navigation assistance upon entry.

Events or exhibitions: Facilitate faster check-ins, deliver schedules or materials, guide participants to specific locations.

Before you begin, you must have:

Connect your LINE Official Account to BotBonnie.

A LINE Beacon service configured for API integration.

Received your LINE Beacon hardware IDs from the service application.

For hardware specifications and setup instructions, see the LINE Beacon documentation.

📘Important

Sending LINE Beacon notifications is limited to once per hour per user to ensure a better user experience and reduce message fatigue.

LINE platform messaging fees will apply to messages sent from LINE Beacon.

Follow these steps to create a LINE Beacon scenario in the BotBonnie console:

Navigate to Content > LINE Beacon, then click Add scenario.

Configure the following settings:

SettingDescriptionScenarioRequired. Enter a recognizable title for the scenario.ActivationToggle the scenario on or off.Triggered moduleRequired. Select a module to define the trigger when a device is near the LINE Beacon devices.Triggered actionsAdd up to five actions to take place when the scenario is triggered. To learn more, see the Triggered actions.Beacon IDRequired. Add unique identifiers for your beacon devices. Each beacon ID can only be used in one scenario.• Manual entry: Enter IDs in the input field, separated by commas, semicolons, or spaces.

• Bulk upload: Click Import LINE Beacon ID by CSV to upload IDs.

Click Save to create the scenario.

Navigate to Content > LINE Beacon to view all scenarios. The page displays the following details for each scenario:



LINE Beacon [1]

https://docs.botbonnie.appier.com/docs/line-beacon



Navigate to Content > LINE Beacon to view all scenarios. The page displays the following details for each scenario:

ColumnDescriptionScenarioClick the title to view the scenario. Use the icons next to the title to duplicate or delete it.StatusToggle the scenario to activate or deactivate it.Number of IDsDisplays the number of Beacon IDs associated with the scenario.ModuleDisplays the triggered module applied to the scenario.ActionsDisplays the number of triggered actions linked to the scenario.

Updated 9 days ago



Auto Replies

https://docs.botbonnie.appier.com/docs/auto-replies



The auto reply module is sent when your bot encounters a message that it doesn't know how to respond to using an any user input settings or AI rules.

The bot tries to respond based on the current module's user input settings.

If there is no configured response for user input, the bot tries to respond using AI rules.

If there are no configured responses for user input or AI rules, the auto reply is sent.

From the menu, go to Content > Auto replies.

From the dropdown, select which module should be used for the fallback response. After selecting the module, the module's name will appear below the dropdown, and you can click it to view the message content.

Updated 9 days ago



Menus [0]

https://docs.botbonnie.appier.com/docs/menus



Enhance your chatbot's user experience with BotBonnie's advanced menu creation tools. Design and deploy Messenger persistent menus and LINE rich menus directly from the BotBonnie console to improve your bot's user experience by providing:

Interactive elements: Incorporate interactive buttons that lead to different chatbot responses, URLs, or other actions within the messaging app.

Streamlined navigation: Create always-accessible menus that offer users quick access to your chatbot's key features and content.

Personalized functionality: Create customized menus that can be automatically assigned to different users based on certain conditions. For example, you can display a member-exclusive menu group to users who have successfully linked their social account with your brand account, providing access to features such as order tracking and viewing account details.

There are two types of menus you can create.

Default menu group: All users see this menu by default.

User-level menu groups: Use a triggered action in your flow to assign a user to a specific menu group. Users who aren't assigned to a user-level menu group will see the default menu group instead.

The required settings differ for different messaging platforms. For setup instructions, refer to the sections below:

Messenger menu

LINE menu

Go to Content > Menus.

Click the tab for Messenger menu, then under the section for the menu type you'd like to create (either Default menu groups or User-level menu groups), and click + Add menu.

Complete the following settings:

Menu name: This is only visible from the BotBonnie console.

Menu type: Choose whether this menu should always be available (Persistent menu) or only available for a specified period of time (Limited-time menu).

Operation Menu Period: If you set the menu type to Limited-time menu, specify the start and end dates and times. A menu timeline will be displayed under this setting, allowing you view the schedules of all your menus.



Menus [1]

https://docs.botbonnie.appier.com/docs/menus



Under Persistent Menu Item Settings, click + Add an item, then configure a button or triggered actions.

After you've completed all the settings, go to the top of the page and click Deploy.

Go to Content > Menus.

Click the tab for LINE menu, then under the section for the menu type you'd like to create (either Default menu groups or User-level menu groups), and click + Add menu.

Enter a menu name, choose a default display mode, and choose a menu type.

Menu name: This is only visible from the BotBonnie console.

Default display mode: Choose whether the menu should be displayed or hidden by default.

Menu type: Choose whether this menu should be always be available (Persistent menu) or only available for a specified period of time (Limited-time menu).

If you set the menu type to Limited-time menu, specify the start and end dates and times under Operation menu period. A menu timeline will be displayed under this setting, allowing you to view the schedules of all your menus.

Under Image upload and layout settings, choose the menu layout size. Next, you'll be able to upload a base menu image, select a menu layout, and configure the desired menu interactions.

After you've completed all the settings, click Deploy at the bottom of the page.

The LINE menu offers two layout sizes for different design needs. Select a layout that best fits your images and improves user interaction.

Layout sizeCompactLargeDescriptionOptimized for simpler menu designs.A larger layout for more detailed visuals.Menu tabsSupports only a single menu.Supports up to four menu tabs.Supported dimensions• 2500 × 843

• 1200 × 405

• 800 × 270• 2500 × 1686

• 1200 × 810

• 800 × 540File formats• JPG

• JPEG

• PNG• JPG

• JPEG

• PNGFile sizeUp to 1 MB.Up to 1 MB.

📘NoteWhen using the Large layout with multiple tabs, account for the height of the menu tabs by including padding at the top of your base images. This ensures a sufficient tappable area, allowing users to switch tabs smoothly.The required padding for menu tabs in each layout size is as follow:



Menus [2]

https://docs.botbonnie.appier.com/docs/menus



2500 × 1686 px: 200 px

1200 × 810 px: 96 px

800 × 540 px: 64 px

The example below shows the 1200 × 810 px layout. Leave enough space at the top so users can switch between tabs.See the layout size reference for details on other layout sizes.

Go to Content > Menus to view all of your menu groups. The menus page displays the following details for each menu group:

Menu name: The name you set for the menu group.

Operational status: The current status of the menu group, indicating whether users can see the menu group or not.

Operation period: The duration which the menu group is valid for. If the menu group isn't on a limited schedule, this column will display Permanent.

Last edited: The last time the menu group's settings were edited.

To see a schedule of all your menu groups, click the three dots next to the menu group type, then click View menu timeline.

Updated 9 days ago



Greetings

https://docs.botbonnie.appier.com/docs/greetings



👍Supported channels

Facebook

Greetings appears when users interact with a Facebook fan page bot via Messenger for the first time. Customize greetings to introduce your brand, describe available services, or guide users in interacting with the chatbot.

From the menu, go to Content > Greetings.

Enter a greeting message in the text input box. A preview will be displayed on the right.

📘NoteClick {...} or the emoji icon at the bottom right to add dynamic content or emojis to create personalize messages.

(Optional) Configure the Get Started button action:

Select a module from the dropdown to guide users with a welcome message, introduce your brand, direct users to your website, or enable chatbot interactions.

Select None if no further action is needed.

Click Deploy bot to save the greeting message.

Updated 9 days ago



Live Chat [0]

https://docs.botbonnie.appier.com/docs/live-chat



Your chatbot's live chat menu allows you to view the chatbot's ongoing conversations from all channels in a single, unified view. Monitor real-time interactions and provide support when users require assistance from a live customer service agent.

The live chat page consists of three panels for easy access to all the chat-related information, allowing you to:

View and search the conversation list: Sort and search your chatbot's ongoing conversations. After selecting a conversation, the next two panels will be populated.

Send messages in the chatroom: Send messages, manage conversations, and use the AI assistant for reply suggestions.

View and edit user details: View and edit the demographic attributes, tags, and parameters. In addition, you can add notes about the user for more personalized customer service.

👍Access live chat on your mobile deviceYou can access the mobile version of the live chat menu by logging in to https://console.appier.com on your device's web browser.

LINE messaging fees: Sending messages in the Main chatroom will count towards your LINE message quota and may be subject to LINE messaging fees. To avoid messaging fees, use a live agent chatroom.

Conversation retention: Conversations are stored for six months. Messages older than six months will no longer appear in the live chat.

Paused chatbot: When the customer service agent sends a message to the chat, the chatbot will be automatically paused for 30 minutes by default.

To search conversations, click the search icon above the message list.

To filter conversations, use the dropdown menus at the top:

Category: Main, Done, Unread, Spam. You can change a chat's category at any time.

Platform: LINE, Facebook, or WebChat.

Assigned customer service agent

When you select a conversation, you can:

Send messages

Use AI assistant for reply suggestions

Assign the chat to a customer service agent

Set the chat's category

In addition, the chat menu consists of two chatrooms which you can freely toggle between: Main chatroom and Live agent chatroom.



Live Chat [1]

https://docs.botbonnie.appier.com/docs/live-chat



Main chatroomLive agent chatroomPlatformAll connected channelsLINE onlyMessaging feesConversations on the LINE platform may incur messaging feesNo LINE messaging feesInterfaceNative channel interfaceWeb view in LIFF appSetup requiredAvailable by defaultRequires enabling and button setup

To open a conversation, click a user in the conversation list. To send a message, you can either:

Enter a message directly from the chat menu.

Send an emoji, attachment, image file, video file, audio file, or an existing module.

Use the AI assistant for reply suggestions.

📘NoteWhen adding a module to a live chat session, only individual modules are available in the dropdown. Modules grouped under a kit cannot be selected.

The AI assistant helps customer service agent to generate reply suggestions based on the conversation context. You can:

Select a suggested response and send it directly.

Edit the response before sending.

Enter a prompt to adjust the response before generating suggestions.

Adjust the AI assistant settings for tone, length, and language.

📘LimitationsEach click on the AI assistant generates a new response based on the conversation context. The AI assistant can generate up to 120 responses per bot per day. Contact your customer success manager for details.

To access the AI assistant:

Click the AI assistant or Check suggestion in the message input area.

Review the generated response. If needed, you can click of the following:

Enter prompt to provide input or instructions to generate a new response.

Edit response to modify the AI-generated response before sending.

Then, click Send.

To customize AI assistant suggestions, click the settings icon next to the AI assistant, adjust the following settings to match your brand voice or customer expectations, and click Apply to save changes:

Tone: Define a tone for your reply:

Professional

Friendly

Casual

Emphatic

Confident

Length: Define your reply length:

Short

Long.

Language: Select the preferred language:

English

Traditional Chinese

Japanese

Korean



Live Chat [2]

https://docs.botbonnie.appier.com/docs/live-chat



Short

Long.

Language: Select the preferred language:

English

Traditional Chinese

Japanese

Korean

After assigning a chat to a specific customer service agent, you'll be able to filter the message list to view conversations by assignee.

You can organize conversations by assigning them to different categories. This helps streamline chat management and allows customer service agents to filter in the conversation list. To categorize a conversation, use the icons at the top of the chat window:

Main: All conversations are moved to this category by default when a user triggers the Notify agent action. In addition, the chatbot will be paused for 30 minutes. To modify the duration, go to Settings > Pause bot (Notify agent).

Done: Making a conversation Done will re-enable the chatbot.

Follow Up: Messages that customer service agents have manually marked as Follow Up will be moved to this category.

Unread: Messages sent by users after the notify agent action is triggered or while the bot is deactivated will be placed in this category. Conversations can also be manually marked unread.

Spam: Messages that customer service agents have manually marked as Spam will be moved to this category.

In the user details panel of the live chat menu, you can manually edit user details, such as:

Adding and removing tags.

Adding and removing parameters.

Modifying demographic attributes.

Customer service agents can also leave notes under each user's profile for personalized service in future interactions.

To edit a user's demographic attributes, open their profile by clicking View.

👍Supported channel

LINE

The live agent chatroom allows users to interact seamlessly with your live customer service agents in a LIFF web view within LINE app.

Once users enter this web view chatroom, customer service agents can access their conversations by selecting the Live Agent Chatroom tab. This ensures that messages are sent within this designated chatroom without incurring additional LINE messaging fees.



Live Chat [3]

https://docs.botbonnie.appier.com/docs/live-chat



📘NoteThe Live agent chatroom tab doesn't appear by default in the live chat interface. It becomes visible only when triggered by user interaction.Updated 5 days ago



Getting Started with Growth Tools

https://docs.botbonnie.appier.com/docs/getting-started-with-growth-tools



👍Supported channels

LINE

Messenger

Instagram

Growth tools enable your brand to increase its friends and followers through interactions such as post replies, link clicks, or QR code scans. Growth tools are:

Conversation-starting entry points for users who can continue interacting with your brand and continue on to become friends or followers of your social channels.

Used to initiate conversations at various touchpoints, such as official websites, posts, offline event boards, and more, making it easier for users to join the channel.

Performance reports are available for growth tools to allowing you to understand their effectiveness.

After creating a growth tool, you'll be able to see the following basic information for each tool on the growth list page:

Title

Type

Channel

Operational status

Operation period

Each growth tool will have icons next to it for copying its link, viewing its performance, editing, and deleting. To enable or disable a growth tool, toggle the Operational status switch.

In addition, you can utilize the search function at the top of the page to directly search for a growth tool by its name.

Updated 9 days ago



Start Chats [0]

https://docs.botbonnie.appier.com/docs/start-chats



Use BotBonnie's URL and QR code generator to increase your brand account's friends and followers by providing an easy entry point for users to engage with your brand.

👍Supported channels

LINE

Facebook

Instagram

Go to Growth tools, then click + Add growth tool.

Select the channel you're creating this growth tool for, then click Start chat with short URL or Start chat with QR Code.

In the setup page, complete the following settings:

Campaign name: This name won't be visible to users, so choose a name that's easy for your brand to manage.

Operation period: Choose between continuous operation or operation within a limited time period.

Started conversation module: The module that opens when the link is clicked. For a module to be available for selection, it needs to be created and published in the flow beforehand.

Triggered actions: Select a triggered action to execute when the user clicks the link.

Channel: Select a channel from the list of channels connected to your account.

📘NoteDon't modify the LIFF ID Setting.

After completing all the settings, click Generate.

After the creation process successfully completes, the URL and QR code will appear in the top right corner. Click the Save button to save your settings.

Now you can start sharing the URL and QR code with your customers!

👍Editing the growth toolYou can edit the growth tool and regenerate a URL and QR code. The previous URL and QR code will continue to function as long as the channel hasn't been changed.

Once you've made the URL or QR code publicly accessible, you can begin to monitor their effectiveness by viewing the performance page. Go to the growth tool list and click the eye icon on the right side to open the report where you'll see a report containing:

The total number of unique users who clicked/scanned

The total number of clicks/scans

Line charts are displaying for both metrics, allowing you to track their performance.



Start Chats [1]

https://docs.botbonnie.appier.com/docs/start-chats



The total number of clicks/scans

Line charts are displaying for both metrics, allowing you to track their performance.

When you access the page, you can customize the time interval for viewing data using a date selector. This allows you to analyze the engagement across different periods effectively.

📘NoteUser data in the report includes URL clicks/QR code scans from both new and existing friends.Updated 9 days ago



Facebook Auto Reply

https://docs.botbonnie.appier.com/docs/facebook-auto-reply



Growth tools help brands engage with users on Facebook through automated interactions on Facebook posts and Messenger conversations. These tools enable brands to:

Auto reply for Facebook posts: Automatically reply to comments on Facebook posts.

Auto reply for Messenger Ads JSON: Send an automated message using Messenger Ads JSON to trigger chatbot flows set up in BotBonnie with a JSON code.

Updated 3 days ago Start ChatsAuto Reply for Facebook PostsDid this page help you?



Auto Reply for Facebook Posts [0]

https://docs.botbonnie.appier.com/docs/auto-reply-for-facebook-posts



You can use BotBonnie's auto-reply feature to automatically respond to users who comment on your posts with comment replies or private messages. You can set the conditions that need to be met for auto-replies to be triggered.

For example, you can use auto replies to encourage users to tag their friends in the comment by providing a discount code by:

Creating an auto reply that sends a message containing a discount code.

Adding a condition to send an auto reply to users who tag their friends in a comment on your post.

After setting up the auto reply, users who fulfill this condition will receive an auto reply from your page containing the discount code.

Go Growth tools, then click + Add growth tool.

Select Facebook and choose one of the following options:

Facebook Auto reply for post comments: Create an auto reply for one post on your connected page.

Facebook Multiple Auto Reply: Create an auto reply for multiple posts on your connected page by providing post URLs.

👍TipUse Facebook Multiple Auto Reply if you'd like to use the same auto reply for multiple posts.

Enter a name to help you identify the auto reply.

Set an operation period for the auto reply. There are two options:

Permanent: This auto reply will be active immediately and continue to run without an end date.

Limited-time: This auto reply will only be active during the time period you specified.

Depending on whether you chose Facebook Auto reply for post comments or Facebook Multiple Auto Reply when creating the growth tool, the way you associate an auto reply with a post or multiple posts will differ.

Facebook auto reply for post comments: Select a post from a connected account to associate with the auto reply.

Facebook multiple auto reply: Provide multiple post URLs to associate with the auto reply.

Under Facebook Posts, select the connected page from the dropdown, then click + Select post.

From the list of available posts, select the one you'd like to associate with the auto reply, then click Confirm.



Auto Reply for Facebook Posts [1]

https://docs.botbonnie.appier.com/docs/auto-reply-for-facebook-posts



From the list of available posts, select the one you'd like to associate with the auto reply, then click Confirm.

📘Scheduled postsNote that scheduled posts won't appear in the selection screen until after they're published.

Under Facebook post link, enter the URLs of the posts you'd like to associate with the growth tool. For URLs to be valid, the post must be from a connected Facebook page.

Click + Add default reply or + Add conditional reply.

Default reply: Auto replies will be triggered by all comments made under this post.

Conditional reply: Auto replies will only be triggered by comments that meet the conditions you set. You can create multiple conditional replies if needed.

A condition reply allows you to set conditions based on the number of friends tagged or based on whether the user's comment includes the keywords you specified.

Number of friends tagged: Select a number to indicate the number of people the user needs to tag in the comment. If you set the number to 2, the user needs to tag two or more friends in the comment to meet the condition.

Comment: Enter one or more keywords, then select a matching option from the dropdown. Depending on the matching option you select, the user's comment will need to include one or all keywords you entered.

Contains any keywords: The user's comment needs to include at least one keyword and can include other text.

Contains all keywords: The user's comment needs to include all keywords and can include other text.

Exact match: The user's comment needs to be an exact match with one of the keywords and cannot include other text.

The following table provides examples of what types of user input would match for two keywords, I want and free sample, based on different settings.

Matching optionExamplesContains any keywordsIf the user's comment is:

• I want → Match

• free sample → Match

• I want to get a free sample→ Match

• sample → Not a matchContains all keywordsIf the user's comment is:

• I want free sample → Match

• I want to get free sample → Match



Auto Reply for Facebook Posts [2]

https://docs.botbonnie.appier.com/docs/auto-reply-for-facebook-posts



• I want free sample → Match

• I want to get free sample → Match

• free sample → Not a matchExact matchIf the user's comment is:

• I want → Match

• free sample → Match

• I want free sample → Not a match

• I want to get free sample → Not a match

You can add two different types of reply modules:

Select Add public reply to reply to users in public comments.

Select Add private reply to reply in private messages.

You can also add both public and private replies if needed. For example:

In the public reply, notify users who commented users know that a private message has been sent to them.

In the private reply, you send the actual discount code.

If you add more than one reply module under a reply type, BotBonnie will randomly send one reply module to the user.

If you have multiple reply modules under both public and private replies, you can decide if you want to lock the public and private replies in pairs.

If you enable Send public and private replies in pairs, the first public reply will always be sent together with the first private reply, and the second row of replies will always be sent together, etc. You will need to have the same number of reply modules under public and private replies.

Updated 3 days ago



Auto Reply for Messenger Ads (JSON)

https://docs.botbonnie.appier.com/docs/auto-reply-for-messenger-ads-json



Messenger Ads JSON helps you attract new users and engage existing ones by integrating BotBonnie’s chatbot flows with your Messenger ads. This growth tool that JSON code allows you to use pre-built modules and responses from BotBonnie when setting up ads in Meta Ads Manager. When users click the ad’s call-to-action button, they receive an opt-in message and are directed to Messenger to start a conversation with your chatbot.

To use a BotBonnie module in a Messenger Ad, you need to obtain its JSON string. For detailed instructions, see Meta's guide to creating Messenger Ads with your existing BotBonnie message flow.

👍RecommendationFor best results, set your campaign objective to Engagement when using Messenger Ads with BotBonnie.

Navigate to Growth tools and click + Add growth tool.

Select Facebook > Messenger Ads JSON.

From the dropdown, select a module for the first message to send in the Messenger.

Click the copy icon next to the JSON string box.

In Meta Ads Manager, paste the JSON string into the Enter JSON code field to link your BotBonnie flow to the ad.

📘NoteIf you need help completing the setup, see Meta’s guide to setting up Messenger Ads with JSON.

📘NoteRemove all backslashes () from the copied JSON string before using it.Updated 3 days ago



Auto Reply for Story Mentions [0]

https://docs.botbonnie.appier.com/docs/auto-reply-for-story-mentions



You can use BotBonnie's auto reply feature to automatically send a private message to users who mention your Instagram business account in their Stories. This feature is commonly used to automate campaigns that encourage users to promote a brand, and rewards can be automatically provided to users using the auto reply.

📘Note

Make sure your Instagram business account is linked to your BotBonnie bot.

Auto reply for story mention will only be triggered if the user's Instagram account is set to public. You can remind users to set their Instagram account to public.

In the left menu, click Growth tools, then click + Add growth tool.

Select Instagram and click Auto reply for Story mentions.

Enter a name to help you identify the auto reply (e.g. the name of the campaign) and select your Instagram business account.

Set an operation period for the auto-reply. There are two options:

Permanent: This auto-reply will be applied immediately and continue to run without an end date.

Limited-time: This auto-reply will only be applied during the time period you specified.

The reply will be automatically sent to users as private messages when users mention your Instagram business account in their Stories.

📘NoteIf you add more than one default reply, BotBonnie will randomly display one reply message to each user.

Click + Add default reply.

Name the default reply and click + Add reply.

Each default reply can include up to 5 messages. A message can be text, image, carousel, delay, or JSON.

Click Confirm. You can use the preview on the right to check the results.

The auto reply will be switched on by default and will be applied according to the operation period you set. You can use the toggle to switch off this auto reply if needed.

You can encourage users to mention your brand by offering a chance to play lucky wheel or scratch-off if they mention your Instagram business account in their Stories. Users will be able to play the games and receive rewards directly in the Instagram message box.



Auto Reply for Story Mentions [1]

https://docs.botbonnie.appier.com/docs/auto-reply-for-story-mentions



To do this, simply add a button to the default reply, set the On click behavior to Postback module, and select a lucky wheel kit or scratch-off kit.

For details on how to set up the lucky wheel or scratch-off kit, refer to Lucky Wheel Kit and Scratch-Off Kit.Updated 9 days ago



Auto Reply for Live Comments [0]

https://docs.botbonnie.appier.com/docs/auto-reply-for-live-comments



You can use BotBonnie's auto reply for live comments to automatically send a private message to users who comment during your live broadcast. Using conditional replies, a different auto reply can be sent to users based on what the users write in their comments.

This allows you to make the live broadcast more interactive without having to manually reply to each user.

📘Note

Make sure your Instagram business account is linked to your BotBonnie bot.

Auto replies can only be sent as private messages to users who commented during the live stream.

If a user repeatedly makes the exact same comment during the live broadcast, Instagram might filter out the comment. The user might not receive the auto reply when this happens.

In the left menu, click Growth tools, then click + Add growth tool.

Select Instagram and click Auto reply for live comments.

Enter a name to help you identify the auto reply (e.g. the name of the campaign).

Select your Instagram business account, click Select live, select the ongoing live broadcast, and click Confirm.

Click Add default reply or Add conditional reply.

Default reply: Auto-replies will be triggered by all comments made during this live stream.

Conditional reply: Auto-replies will only be triggered by comments that meet the conditions you set. You can set up multiple conditional replies if needed.

If you have selected Add conditional reply, you can set the conditions based on the number of friends tagged or based on whether the user's comment includes the keywords you specified.

Number of friends tagged: Select a number to indicate the number of people the user needs to tag in the comment. If you set the number to 3, the user needs to tag three or more friends in the comment to meet the condition.

Comments: Enter one or multiple keywords, and select a matching option. Depending on the matching option you select, the user's comment will need to include one or all keywords you entered.

Contains any keywords: The user's comment needs to include at least one keyword and can include other text.



Auto Reply for Live Comments [1]

https://docs.botbonnie.appier.com/docs/auto-reply-for-live-comments



Contains any keywords: The user's comment needs to include at least one keyword and can include other text.

Contains all keywords: The user's comment needs to include all keywords and can include other text.

Exact match: The user's comment needs to be an exact match with one of the keywords and cannot include other text.

Let's say you entered 2 keywords, I want and free sample. Refer to the table below to see examples of what would be considered a match under the different matching options.

Matching optionExamplesContains any keywordsIf the user's comment is:

• I want → match

• free sample → match

• I want to get a free sample→ match

• sample → not a matchContains all keywordsIf the user's comment is:

• I want free sample → match

• I want to get free sample → match

• free sample → not a matchExact matchIf the user's comment is:

• I want → match

• free sample → match

• I want free sample → not a match

• I want to get free sample → not a match

Click Add private reply and create the reply module.

📘NoteIf you add more than one reply module under the default or conditional reply, BotBonnie will randomly send one reply module to the user.Updated 9 days ago



Auto Reply for Post Comments [0]

https://docs.botbonnie.appier.com/docs/auto-reply-for-post-comments



You can use BotBonnie's auto-reply feature for post comments to automatically send public and private messages to users who comment on your posts. You can set the conditions that need to be met for auto-replies to be triggered.

For example, you can encourage users to tag their friends in the comment by providing a reward. When the users meet the requirement by tagging their friends, BotBonnie automatically leaves a public reply asking users to check their inbox for the discount code, and a private reply is sent to the users to provide the actual discount code.

📘NoteMake sure your Instagram business account is linked to your BotBonnie bot.

In the left menu, click Growth tools, then click + Add growth tool.

Select Instagram and click Auto reply for post comments.

Enter a name to help you identify the auto-reply (e.g. the name of the campaign).

Set an operation period for the auto-reply. There are two options:

Permanent: This auto-reply will be applied immediately and continue to run without an end date.

Limited-time: This auto-reply will only be applied during the time period you specified.

Select the Instagram business account, click Select post, select the post you want to add the auto-reply to, and click Confirm.

Click Add default reply or Add conditional reply.

Default reply: Auto-replies will be triggered by all comments made under this post.

Conditional reply: Auto-replies will only be triggered by comments that meet the conditions you set. You can set up multiple conditional replies if needed.

If you have selected Add conditional reply, you can set the conditions based on the number of friends tagged or based on whether the user's comment includes the keywords you specified.

Number of friends tagged: Select a number to indicate the number of people the user needs to tag in the comment. If you set the number to 2, the user needs to tag two or more friends in the comment to meet the condition.



Auto Reply for Post Comments [1]

https://docs.botbonnie.appier.com/docs/auto-reply-for-post-comments



Comments: Enter one or multiple keywords, and select a matching option. Depending on the matching option you select, the user's comment will need to include one or all keywords you entered.

Contains any keywords: The user's comment needs to include at least one keyword and can include other text.

Contains all keywords: The user's comment needs to include all keywords and can include other text.

Exact match: The user's comment needs to be an exact match with one of the keywords and cannot include other text.

Let's say you entered 2 keywords, I want and free sample. Refer to the table below to see examples of what would be considered a match under the different matching options.

Matching optionExamplesContains any keywordsIf the user's comment is:

• I want → match

• free sample → match

• I want to get a free sample→ match

• sample → not a matchContains all keywordsIf the user's comment is:

• I want free sample → match

• I want to get free sample → match

• free sample → not a matchExact matchIf the user's comment is:

• I want → match

• free sample → match

• I want free sample → not a match

• I want to get free sample → not a match

You can select Add public reply to reply to users in public comments, or select Add private reply to reply in private messages.

You can set up both public and private replies if needed. For example, in the public reply, you can let the commented users know that a private message has been sent to them. In the private reply, you can then include the actual discount code.

Here's what the public and private replies look like to users.

If you add more than one reply module under a reply type, BotBonnie will randomly send one reply module to the user.

If you have multiple reply modules under both public and private replies, you can decide if you want to lock the public and private replies in pairs.



Auto Reply for Post Comments [2]

https://docs.botbonnie.appier.com/docs/auto-reply-for-post-comments



By selecting Send public and private replies in pairs, the first public reply will always be sent together with the first private reply, and the second row of replies will always be sent together, etc. You will need to have the same number of reply modules under public and private replies.

Updated 9 days ago



Auto Reply for Reels Comment [0]

https://docs.botbonnie.appier.com/docs/auto-reply-for-instagram-reels-comment



With BotBonnie's Reels comment auto-reply feature, you can automatically respond to comments on your Instagram Reels. Easily send both public replies and personal messages to your followers based on conditions you set.

Encourage your followers to tag friends or leave a comment by offering special rewards. When they meet your conditions, you can send them a public reply directing them to check their inbox, while also sending them a private message containing their exclusive discount code.

Connect your Instagram business account to your BotBonnie bot.

In the left menu, click Growth tools, then click + Add growth tool. Next, go to Instagram tab and select Reels comment reply.

Enter a name to help you identify the auto-reply, such as the name of the campaign.

Set an operation period for the auto-reply. There are two options:

Permanent: This auto-reply will be applied immediately and continue to run without an end date.

Limited-time: This auto-reply will only be applied during the specified time period.

Select the Instagram business account from the dropdown, then click + Select Reel to choose the reel you want to configure for auto-replies. Click Confirm to save your selection.

Click +Add default reply or +Add conditional reply.

Default reply: Auto-replies will be triggered by all comments under this reel.

Conditional reply: Auto-replies will only be triggered by comments that meet the conditions you set. You can set up multiple conditional replies if needed.

If you selected Add conditional reply, you can set the conditions based on the number of friends tagged or whether the user's comment includes specified keywords.

Comments: Enter one or multiple keywords and select a matching option:

Contains any keywords: The comment must include at least one keyword.

Contains all keywords: The comment must include all specified keywords.

Exact match: The comment must exactly match one of the keywords.

Number of friends tagged: Select a number to indicate how many people the user needs to tag in the comment.



Auto Reply for Reels Comment [1]

https://docs.botbonnie.appier.com/docs/auto-reply-for-instagram-reels-comment



Number of friends tagged: Select a number to indicate how many people the user needs to tag in the comment.

You can select + Add public reply to respond to users in public comments or + Add private reply to send a direct message.

If you create multiple reply modules under the same reply type (public or private), a random reply module will be sent when the condition is met.

To ensure each public reply is paired with a specific private reply, enable Send public and private replies in pairs.

Updated 9 days ago



LINE Smart Link [0]

https://docs.botbonnie.appier.com/docs/line-smart-link



Use LINE smart links to execute a triggered action (e.g. updating parameters, tags, and demographic attributes) for a user when they click the URL. LINE smart links can be embedded, just like a standard URL, and can also be shared via QR code. After a user clicks a LINE smart link:

The user will be briefly redirected to your LINE Official Account in the LINE app.

Immediately after opening their conversation with your LINE Official Account, they will be automatically redirected to the destination URL you specify.

You can also place a LINE smart link outside the Official Account, e.g. a standard web page. When users who are friends of the LINE Official Account click on the link, their clicks will also be recorded.

Before creating a LINE smart link, you'll need to create a LIFF app on the LINE Developers Console under the same provider as your Official Account. Please note the following LIFF app requirements:

The LIFF app's Size setting must be set to Compact.

Endpoint URL must be set to: https://rd.botbonnie.com/liff/, where is the ID of the linked Official Account.

The following Scopes must be selected: profile, openID.

Go to Growth tools, click + Add growth tool, then select LINE > LINE Smart Link.

Enter a name for the LINE smart link campaign.

Under Operation period, set the validity period of the link.

Permanent: The link will immediately be active and will continue to function until it is deleted.

Limited-time: The link is only valid during the specified time period.

Under Redirect URL, enter the final destination URL. Note that users who click on the LINE smart link will be briefly redirected to your LINE Official Account before being automatically redirected to the final destination URL.

(Optional) Under Triggered actions, add the triggered actions you'd like to execute when the user clicks on the link. For example, you can update the user's parameters or tags.

Under Channel, select the connected LINE Official Channel that should be opened when the smart link is clicked.



LINE Smart Link [1]

https://docs.botbonnie.appier.com/docs/line-smart-link



Under Channel, select the connected LINE Official Channel that should be opened when the smart link is clicked.

Under LIFF ID Setting - Compact, the ID of your LIFF app will automatically be populated. If you encounter any issues, please contact your customer success manager for assistance.

After completing all the required settings, click Generate, then copy the short URL or download the QR code to use the LINE smart link.

After publishing the smart link, you can open its performance report by clicking the eye icon in the growth tool list. The report includes:

The total number of unique users who clicked a URL or scanned a QR code.

The total number of URL clicks and QR code scans.

Line charts showing the trends of clicks and scans.

📘NoteThe report includes clicks and QR scans from both new and existing friends.

Yes, you can update the URL without changing the channel, and it won't affect URLs and QR codes that have already been published.

When users click on a link, they can still be redirected to the redirect page even if they don’t become friends of the official account or grant permission for the LINE LIFF app to access their personal information. However, BotBonnie can't tag them or record the click count under these circumstances.

Updated 9 days ago



Broadcasts [0]

https://docs.botbonnie.appier.com/docs/broadcasts



You can send broadcast messages to your users through Facebook Messenger, LINE Official Account, and KakaoTalk. Using BotBonnie, you can target the right audience based on different conditions, such as tags, last interaction time, and account linking status.

BotBonnie also offers an AI Click Optimization feature that predicts users who are more likely to click on your broadcasts, allowing you to target the right users and increase click-through rate (CTR). By excluding users who are not likely to click, you can potentially save broadcast costs and avoid disturbing users who are not interested.

📘AI Click Optimization

AI Click Optimization is a premium feature. Contact your customer success manager for more details.

You will need to have past broadcast data in order to use this feature. The AI model analyzes user behaviors based on the performance of recent broadcasts that include a clickable URL.

For more details on the requirements and the setup steps, see Set up AI Click Optimization.

Below are the different ways to filter broadcast audience and the AI features supported by each channel.

FeaturesLINE OAFacebook MessengerKakaoTalkWays to filter audienceFilter by conditions

Filter by segmentFilter by conditionsFilter by conditionsAI Click OptimizationSupportedN/AN/A

Go to Broadcasting > Broadcasts, then click + Create broadcast.

Select the channels you want to broadcast to.

You can select multiple Facebook Pages, LINE Official Accounts, or KakaoTalk channels, but the channels selected need to be of the same messaging platform.

📘Expected receivers

Facebook: if you see a reload symbol 🔄 and the expected receiver count is not displayed, make sure you have admin access to the Facebook Page.

KakaoTalk: KakaoTalk broadcasts are sent through the user's phone number. Only users with a phone number are included in the expected receiver count. This number may not match the user count in the user list.

Below are the filtering methods and the corresponding message types supported by each platform.



Broadcasts [1]

https://docs.botbonnie.appier.com/docs/broadcasts



Below are the filtering methods and the corresponding message types supported by each platform.

📘ViberNote that Viber broadcasts can only be sent to users with a saved phone number.

Filter methodLINEFacebookKakaoTalkViberFilter by condition: no condition setTargeted broadcast

Mass broadcastAll message typesAll message typesAll message typesFilter by condition: conditions setTargeted broadcastAll message typesAll message typesAll message typesFilter by segmentNarrowcastN/AN/AN/A

There are two ways to filter your broadcast audience.

Filter by condition: You can set up one or multiple filter conditions, or no conditions at all.

If you do not select a filter condition, the broadcast message will be sent to all users who have interacted with the channel.

If you want to set multiple filter conditions, click Add condition. You can select Match all to target users who meet all conditions or select Match any to target users who meet any of the conditions.

Filter by segment: You can select an existing segment. To create a segment, go to Audience > Segments.

Below are the different filter conditions.

Tags: You can target users based on the tags. Below is an example of how the different operators work if you select two tags, A and B.

Tag confidence level: You can target users based on the confidence index of a tag by entering an index between 1 to 10.

The confidence level of a tag is calculated based on the last tagged date and the tag count. A higher confidence index is given to users with a higher tag count and a more recent tagged date.

Tag count: You can target users based on the number of times the user has been tagged with this tag. For example, you can offer a discount to users who have been tagged with the same tag more than twice.

Tagged date: You can target users based on the date that the user was tagged with this tag. For example, you can target users who recently contacted customer service after a certain date.



Broadcasts [2]

https://docs.botbonnie.appier.com/docs/broadcasts



Another user case is if you use the same tag for multiple campaigns with different and non-overlapping campaign periods, you can also use this condition to distinguish users who participated in different campaigns.

First interaction: You can target users based on the date of their first interaction with your bot. For example, you can target new users by filtering users whose first interaction time is after a certain date.

Last interaction: You can target users based on the time of their last interaction with your bot.

Account linking status: You can target users based on their account linking status by selecting Linked or Not linked.

Menu group: You can target users based on the LINE or Messenger menu group that they belong to.

One-time notifications / recurring notifications: You can target users who have clicked on the Notify me button in a one-time notification request or a recurring notification request.

If you have set the triggered action of the Notify me button to Add tag, you can add a second condition to filter based on that tag.

Not been sent broadcast recently: You can target users who have not been sent a broadcast in the past 1 to 60 days to avoid sending broadcasts to users too frequently.

Birthday: You can target users who have a birthday during a certain month. For example, you can broadcast birthday special offers to users who have a birthday in October.

Set a broadcast time and click Next.

Broadcast now: The broadcast will be sent after you complete all the broadcast settings. Note that it may take up to a few minutes for users to receive the broadcast depending on the size of your receivers.

Schedule broadcast: You can set a broadcast time that is at least 30 minutes and up to 6 months from now.

📘NoteAvoid modifying the broadcast content within 30 minutes of the scheduled time.

For LINE and Facebook, select a message tag. For Kakao, proceed to step 6.

If you are broadcasting through LINE Official Account, select one of the following messaging types based on how you filter the target audience.



Broadcasts [3]

https://docs.botbonnie.appier.com/docs/broadcasts



Targeted broadcast: This option is only supported if you have selected Filter by Condition. The broadcast will be sent to users who meet the filter conditions selected and have interacted with the chatbot before.

Mass broadcast: This option is only supported if you did not set any filter conditions. The broadcast will be sent to all users who are friends with your LINE Official Account, including users who have not interacted with you before. Those who blocked your LINE Official Account are excluded.

Narrowcast: This option is only supported if you have selected Filter by segment. The broadcast will be sent to users in the segment who have interacted with the chatbot before.

If you are broadcasting through Facebook Messenger, select one of the following messaging tags based on the content and purpose of your broadcast.

Confirmed event update: Send users confirmations, reminders or updates for an event they have registered for, such as purchased tickets. This tag can be used for upcoming events and events in progress. Promotional content is not allowed.

Post-purchase update: Send users updates on recent purchases, such as transaction details and shipment status notifications. Promotional content is not allowed.

Account update: Send users notifications about their application or account, such as credit card application or suspicious activity notifications. Promotional content is not allowed.

Non-promotional subscription update: Subscription messaging is only available for news organizations that successfully register their Pages with Facebook's News Page Index (NPI). Promotional content is not allowed.

Standard messages: The content can be promotional. The broadcast will only be sent to users who have interacted with your Messenger within the last 24 hours. See Facebook's policy on what counts as an interaction.

🚧ImportantCarefully choose your message type based on the content of your broadcast. Facebook may suspend you if it finds that you have abused them.



Broadcasts [4]

https://docs.botbonnie.appier.com/docs/broadcasts



Promotional content can only be sent through Standard messages.

See Facebook's guide on the allowed usages of different message tags.

Select an existing broadcast module or click Add module to create a new one. The available message types will differ depend on the messaging platform you're broadcasting on.

ChannelSupported message typesLINE• Text

• Image

• Carousel

• Image carousel

• Video

• Audio

• Imagemap

• Video imagemap

• One-time notification request

• JSONMessenger• Text

• Image

• Carousel

• Video

• Audio

• Delay

• One-time notification request

• Recurring notifications request

• JSONKakaoTalk• Basic text

• Wide image

• Wide list

• Carousel Commerce

• Carousel feedViber• Text (Viber)

• Image (Viber)

📘Kakao Moment: Advertising messageThis option must be enabled if the broadcast message contains any promotional content (for example, special discounts, promotions, or product-related events) even if the message includes both promotional and non-promotional content. Enabling this option is legally required in some countries.

📘Requirements

AI Click Optimization is a premium feature. Contact your customer success manager for more details.

To use AI Click Optimization, the following requirements must be met:

AI Click Optimization can only be used on a single LINE Official Account.

The message type must be Targeted broadcast or Narrowcast.

The broadcast module must include an URL.

The broadcast needs to be scheduled at least 1 hour from now.

The expected receivers need to exceed 1000 users.

To use this feature, click Start prediction. It'll take a few minutes for the prediction to complete.

After the prediction is completed, you will see a slide bar that indicates the number of estimated receivers and the estimated CTR. The Optimal point is the sweet spot calculated by AI that boosts CTR but still includes enough users, striking a balance between precision and coverage.



Broadcasts [5]

https://docs.botbonnie.appier.com/docs/broadcasts



You can drag the slide bar or enter a user size to adjust the number of receivers to include. If you move the slide bar to the right, more users will be included, but the estimated CTR will also drop because the target audience now includes more users who are less likely to click. The opposite is true if you move the slide bar to the left.

📘NoteThe Estimated CTR is based on the prediction generated by the AI model. The actual CTR may differ from the prediction. The message content you used will also affect the actual CTR.

Click Next. Review the broadcast settings and click Schedule or Send.

You'll find the broadcast under either Scheduled broadcasts or Sent broadcasts.

To view the performance report of the broadcast, click the View icon of the broadcast. After the broadcast is sent, it may take several minutes for the View icon to become available.

If you are using LINE mass broadcast or narrowcast, you can export a detailed report.

To export the report, click Export report in the top-right corner.

Type the email address where you'd like the CSV file to be sent to. Click Confirm.

Sent users: The estimated number of users who were sent broadcast messages. Broadcast messages may not be sent successfully due to reasons such as being blocked by users or reaching LINE message limit.

Delivered users: The number of users who received the messages.

Read users: The number of users who opened the messages. This number is not available for LINE targeted broadcasts.

Clicked users: The number of users who clicked any of the buttons or quick replies in the broadcast.

📘NoteFor LINE mass broadcast and narrowcast messages, the numbers are provided by LINE. To protect users' privacy, LINE does not provide some metrics (for example, read users and clicks users) when the number of users is too low.

For LINE targeted broadcasts, you can click View total button clicks to see the number of times each button has been clicked by users.

Updated 9 days ago



Team Members

https://docs.botbonnie.appier.com/docs/manage-team-members



You can invite your colleagues to access projects in the Personalization Cloud console. There are six types of roles:

Admin: Admins have full access to all features.

Editor: Editors can access all features except team management and integrations.

Analyst: Analysts can view bot flows and reports, and access audience-related features.

Tester: Testers can view and test bot flows.

Customer Manager: Customer managers can access customer service messages and assign agents.

Customer Agent: Customer agents can view and respond to customer service messages.

To see the detailed permissions granted to each role, refer to the Access Control List below.

To invite team members, you need to have admin access to the project.

Follow the steps below to invite.

From the left menu, go to Settings, then select the Team members tab, and click + Invite.

Enter the email addresses, select a role, and click Send invite.

You can add multiple email addresses at a time with the same role.

If you have multiple projects, you have to send invitations from each project to provide access to each.

The invited team members will receive an invitation email with an activation link.

See the following table for the access rights of each type of role.

PermissionsAdminEditorAnalystTesterCustomer ManagerCustomer AgentView flows✅✅✅✅✅✅Edit flows✅✅❌❌❌❌Test bot✅✅✅✅✅✅Deploy bot✅✅❌❌❌❌View analytics reports✅✅✅❌✅❌View and edit broadcasts✅✅✅❌❌❌

📘NoteFlows includes bot flows, contents, and growth tools.

PermissionsAdminEditorAnalystTesterCustomer ManagerCustomer AgentView user information✅✅✅❌✅✅Edit user bot status✅✅❌❌✅✅Assign customer agent✅✅❌❌✅❌View and reply to customer services✅✅❌❌✅✅

PermissionsAdminEditorAnalystTesterCustomer ManagerCustomer AgentManage team members✅❌❌❌❌❌View and edit billing information✅❌❌❌❌❌View, connect, and disconnect channels✅❌❌❌❌❌View and edit agent notification settings✅✅❌❌❌❌View channel status check✅✅❌❌❌❌View API token✅✅❌❌❌❌View basic settings✅✅✅✅✅✅Edit basic settings✅❌❌❌❌❌Updated 9 days ago



Notify Agent [0]

https://docs.botbonnie.appier.com/docs/notify-agent



Customize how your chatbot transfers conversations to human agents with the Notify agent settings:

Agent off-hours settings: Set an automatic reply when messages are sent to your chatbot outside business hours.

Pause bot (Notify agent): Temporarily pause automated chatbot responses when a user is talking to a live customer service agent.

Notification: Notify customer service agents via LINE notification or email.

📘NoteEnable Agent off-hours settings by first setting up your business hours.

When this setting is enabled:

Customers receive an automated reply if they message outside off-hours.

LINE notifications are paused during off-hours, but agents still receive email notifications.

Conversations are categorized under Follow up, so agents can respond on the next business day.

To handle customer messages outside business hours:

Expand the Agent off-hours settings section and turn on the switch.

Click + Reply to configure messages and user input for the autoreply, then click Save.

Select a destination folder for off-hours chat inquiries from the dropdown.

Pause bot responses while a live agent is assisting a user.

When the Notify agent action is triggered, you can configure how long to pause bot automated responses:

Until the close of business (resumes at the end of business hours or when an agent moves the message to Done).

For a specified duration in minutes (default is 30 minutes).

📘NoteTo learn more about pausing a chatbot for a live chat Pause bot (Live chat).

Set up LINE or email notification to alert customer service agents when the Notify agent action is triggered.

Select Via LINE Notification to send alerts through LINE.

Use Via Email to keep customer service agents informed of new inquiries through email notifications.

Set up LINE notifications to alert customer service agents when the Notify agent action is triggered. This ensures agents receive real-time updates about customer inquiries, even when they're not actively monitoring the conversation.

📘Note



Notify Agent [1]

https://docs.botbonnie.appier.com/docs/notify-agent



📘Note

Each bot can connect to only one LINE OA, which cannot be shared with chatbot services.

Before proceeding, make sure:

The LINE OA is added to the target group.

Your LINE OA has enough message quota to cover notifications (for example, sending to a group of 20 members consumes 20 message credits).

Click + Connect LINE OA and follow the instructions in LINE Channel Settings to link your LINE OA with a Messaging API channel.

After you connect a LINE OA, click + LINE Notification on the right. Sign in to your LINE account and select a group or an individual account. A message will be sent once your LINE OA has successfully joined the group.

📘NoteThe connected LINE OA sends notifications. Make sure the LINE OA is included in the group; otherwise, you won’t receive the "Linking completed" message, and it won’t appear in the notification recipients list.

Under Agent, click the dropdown and select and assign an agent to receive notifications.

Add triggered action at chatbot flows by selecting Notify agent and customer service agent groups/name from the dropdown.

Click + LINE Notification to add another recipient.

To use a different LINE OA, click Update LINE OA, then delete the existing one and link a new account.

Click the trash bin icon on the right side to remove a LINE notification recipient. Ensure the chatbot flow remains linked to a valid group or individual to maintain a valid connection.

🚧CautionWhen deleting or changing the LINE OA:

Existing recipients may be affected, and notifications may not be delivered until they are reassigned.

Check for attention icons on the affected recipients and update the chatbot flow as needed. Make sure the new LINE OA is linked to the same group or individual as before to maintain a valid flow.

Set up email notifications to alert customer service agents when the Notify agent action is triggered. This ensures agents receive updates even when they're not actively monitoring the conversation.



Notify Agent [2]

https://docs.botbonnie.appier.com/docs/notify-agent



Click + Email notification to create a notification group and assign customer service agents to receive emails.

Then, add triggered action at chatbot flows by selecting Notify agent and customer service agent groups/name from the dropdown.

To manage email notifications:

Click the pencil icon to modify the notification recipient.

Click the trash bin icon to remove the notification recipient.

Updated 9 days ago



Status Check

https://docs.botbonnie.appier.com/docs/status-check



The status check page allows you to view:

Bot usage (by feature): View quotas and quota usage for your bot.

The status of your connected channels: See if your messaging channels are connected properly, and fix connection settings if they aren't.

To open the status page, go to Settings, then click the Status check tab.

Click the arrow to expand the Bot usage section. Each feature will have a colored dot representing its current status, and if there is a quota, it will be displayed on the right side.

Status colorDescriptionGreenThere is remaining quota or there is no usage limit for this feature.YellowThere is no remaining quota for this feature.RedThis feature was previously active, but is currently inactive.GrayThis feature has never been used or is not enabled.

Click the arrow on the right to expand the Channel status section. Each channel will have a colored dot representing its current status.

Status colorDescriptionGreenNo connection issues detected.YellowIssues detected in the connected platform (e.g. LINE, Instagram) that may affect some functions of your bot.RedConnection issues detected.

If a channel has connection issues, a button will appear on the right side, allowing you to initiate the connection repairing process.

Updated 9 days ago



Business Hours [0]

https://docs.botbonnie.appier.com/docs/business-hours



In the Settings, go to Business hours tab to configure the following settings:

Business hours for your WebChat widget.

Bot pause settings for live chat.

Use Business Hours to manage customer service agent availability and customer interactions based on defined working hours.

During business hours, an Online icon will be displayed in the WebChat. Outside of business hours, an Offline icon will be displayed, helping users understand agent availability.

Follow these steps to configure your business hours:

Toggle the Business hours switch to enable the feature.

Select the days of operation, then choose a start and end time from the dropdown menus.

Click + Add business hours to configure multiple time slots if needed.

📘NoteThe default timezone is Asia/Taipei. If you have any concerns, contact your customer success manager.

After configuring business hours, you may want to customize settings in the Notify agent tab to optimize how your chatbot transfers conversations to human agents and handles auto-reply outside business hours.

Configure the bot's pause duration after live agents take actions during a live chat session. Set the pause duration for the following scenarios:

When an agent sends a message in the chatroom.

When a chat moves to the Main category.

The bot will automatically resume when the chat is moved to the Done category.

Follow these steps to configure the bot pause duration:

Toggle the Pause bot (Live chat) switch to enable this feature.

Specify the number of minutes the bot should remain paused.

Changes take effect immediately after saving.

To better understand the differences between Pause bot (Live chat) and Pause bot (Notify agent), here’s a comparison table that highlights the key distinctions:



Business Hours [1]

https://docs.botbonnie.appier.com/docs/business-hours



FeaturePause Bot (Live chat)Pause Bot (Notify agent)PurposePauses the bot after a live agent takes actionPauses the bot while the live agent is assisting the userTriggerAfter a live agent sends a message or moves the chat to Main category.Triggered when the Notify agent action is initiated.ResumesResumes when moved to Done category.Resumes at the end of business hours or after a specified duration.ConfigurationPause duration• Until close of business

• Pause duration (default 30 minutes)Updated 9 days ago
