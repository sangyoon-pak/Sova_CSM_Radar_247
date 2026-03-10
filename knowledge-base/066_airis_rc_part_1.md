---
source: notebooklm_export
file_id: "066"
filename: "066_airis_rc_part_1.txt.txt"
doc_type: "reference_card"
product: "AIRIS"
content_type: "txt"
language: "en"
guide_summary: "The source material serves as comprehensive documentation for AIRIS, an advanced customer analytics cloud service designed to track and analyze the complex, **non-linear customer journey**. A key theme is the platform's ability to be **channel and platform agnostic**, collecting granular, individual-level behavioral data across all touchpoints, from websites and social media to product engagement itself. This unified tracking breaks down traditional data silos, enabling users to create **detaile"
guide_keywords: "Customer analytics, Tracking user behavior, Journey reporting, Data segmentation, System integrations"
---

# 066 airis rc part 1

Introduction to AIRIS

https://docs.airis.appier.com/docs/introduction



The modern customer journey is non-linear, omnichannel, and cyclical. AIRIS was created out of the need to understand the customer experience by being truly channel and platform agnostic. AIRIS pioneered individual-level customer analytics even before businesses identified the challenges with nonlinear customer journeys and fragmented product engagement.

The platform tracks user behaviors across websites, through email, social media, paid media, sales, technical support, help desk, video, and most importantly, the engagement on the product/service itself.

AIRIS's journey analytics breaks down the data silos of mobile, app, product, or web analytics, and combines them with other essential touchpoints to help you see the world as your customers do.Updated 23 days ago



Introduction to AIRIS

https://docs.airis.appier.com/docs



The modern customer journey is non-linear, omnichannel, and cyclical. AIRIS was created out of the need to understand the customer experience by being truly channel and platform agnostic. AIRIS pioneered individual-level customer analytics even before businesses identified the challenges with nonlinear customer journeys and fragmented product engagement.

The platform tracks user behaviors across websites, through email, social media, paid media, sales, technical support, help desk, video, and most importantly, the engagement on the product/service itself.

AIRIS's journey analytics breaks down the data silos of mobile, app, product, or web analytics, and combines them with other essential touchpoints to help you see the world as your customers do.Updated 23 days ago



Getting Started with the Data Query API

https://docs.airis.appier.com/reference



The AIRIS APIs use the HTTP Basic Authorization Scheme, so to make any requests, you'll need an app ID and API key. An example request might look like this:

curl --request GET \

--url 'https://www.woopra.com/rest/3.10/trends?project=&report_id=' \

--user :

Follow the instructions below to retrieve your app ID and API key.

Click your name in the top right corner and click My Profile and open the Developer tab.

If you haven't created an API key yet, click Generate a new API key. After completing the following settings, click Create.

App ID: You can choose to enter a custom app ID. If you don't provide an app ID, AIRIS will automatically populate this field.

Expires: Set the expiry time for the API secret.

Click an app ID in the list to view and copy its API secret.

👍Tip: Testing the APIYou can send requests directly from the API documentation by entering your app ID in the username field and the API secret for the password field in the request's authorization section.

The global per-project limit on API calls is:

300 per minute

600 per hour

3000 per day

Rate-limited requests will receive a status code of 429.



What is AIRIS: Product Capabilities [0]

https://docs.airis.appier.com/docs/what-is-airis-product-capabilities



AIRIS is an advanced customer analytics cloud service built with proprietary tracking technology that automatically builds detailed profiles of each customer in real time. These profiles enable you to view the behavioral data of each customer based on touch points throughout their digital journey and build behavioral segments, leveraging AIRIS’s segmentation filters.

The AIRIS platform offers several core functionalities that allow you collect, analyze, and gain insights from your data:

Tracking: Track the events and attributes of both anonymous and identified users, and display it in a timeline on the AIRIS console.

Reports: View what kind of customer relationships are driving revenue and growth for your organization using highly-customizable reporting.

Triggers and automations: Automatically trigger operations such as automated batch tasks or syncs with third-party integrations based on users actions and changes in profile properties.

Integrations: Connect to third-party services to centralize data and trigger automated operations.

Differing from some platforms that track website traffic by device types, AIRIS creates individual profiles for each of your website visitors. AIRIS tracks the behaviors, event-based activity, demographics, and social touch points of both anonymous and identified users and displays these data in the form of a timeline. AIRIS’s smart tracking technology also enables complete journey tracking across multiple devices for identified users.

AIRIS's schema defines what type of user data is tracked, how you want it to be displayed, and how it can be aggregated. Schemas can be based on both user data and event data. A basic schema is automatically generated from any custom event or user property, making it possible for you to aggregate data for smart filtering and powerful analytics reports quickly.



What is AIRIS: Product Capabilities [1]

https://docs.airis.appier.com/docs/what-is-airis-product-capabilities



With AIRIS, you can create and track an unlimited number of custom actions. Custom actions are tracked by the built-in events installed automatically when you install an Integrations app, or tracked by adding code that sends AIRIS data about specific behaviors that a user might take while on your website or app, such as signing up, playing a video, or adding a product to their cart.

Using built-in, highly customizable reporting, you can easily view what kind of customer relationships are driving revenue and growth for your organization. Without going through the hassle of writing code, AIRIS allows you to build powerful behavioral reports in a few steps to instantly build a picture of how prospects are engaging with the product or service. By getting a unified view of a wide range of custom events, you can quickly build customer segments. For example, customers who are engaging with similar content can be bundled to offer suggestions about related items they may be interested in.

AIRIS offers reports such as:

Journey reports that allow you to understand the customer journey and help you avoid misplaced spending on optimization and personalization.

Trend reports that that you to monitor how your key metrics perform over time and what behavioral properties drive the organization's key metrics’ performance.

Retention reports that measure and analyze how long visitors and customers continue to perform an action over the course of time with AIRIS's retention reports.

AIRIS’s customer analytics is built so that you can stop going from one department to another to collect relevant customer information. Instead, you can focus on generating data-driven reports that show what the customer is actually experiencing, allowing you to ask questions that were never thought of before.



What is AIRIS: Product Capabilities [2]

https://docs.airis.appier.com/docs/what-is-airis-product-capabilities



AIRIS gives you the ability to build custom profile reports, leveraging AIRIS’s segmentation filters. Profile reports show which customers matter most to the business based on a vast number of behavioral, demographic, or application-specific criteria. Profile reports can be modified even further by adding custom columns that include user properties (e.g. e-mail, city, or country), segments, and dynamic fields.

AIRIS’s Customer Journey, one of AIRIS's most powerful features, is designed to effectively break down cross-departmental data silos and combine any set of actions for a complete view of the customer’s journey. From product engagement and website behaviors to support requests and campaign sentiments, journey reports map customer journeys step by step, showing you how customers move across different touch points all within one report.

Journey reports are 3-dimensional because of the Optional Steps feature. Optional steps allow you to study the attribution of those goals towards success, even though customers are not required to take them. With optional steps, you can track alternative paths customers might take in order to complete their journey and have these represented within the original funnel as well.

For instance, you can determine if customers likely to convert if:

They use the API

They read the product setup guide

They invite a colleague

They come back from a retargeting campaign

The customer journeys mentioned above can be measured in a single journey report, giving you a complete picture of the customer journey and aggregated product sales revenue.



What is AIRIS: Product Capabilities [3]

https://docs.airis.appier.com/docs/what-is-airis-product-capabilities



With trends reports, you will never be in the dark again about how key metrics are performing over time. For example, you can dig deeper and find out how seasonality affects your business revenue, or discover how customers from Europe behave differently compared to users from North America. Trend reports allows you to analyze any events tracked in AIRIS during a fully customizable timeframe. It’s also super easy to share them with teammates so everyone in an organization is on top of their KPIs performance.

Retention reports help you see what actions customers take over time by illustrating how long customers continue to get value out of the product or service. For example, what actions do customers take to remain a customer, or what series of actions resulted in them dropping off the engagement funnel, and at what point of the funnel? Retention reports are completely shareable with other teammates, making it possible to democratize customer data throughout the organization.

For a cloud service that automates innumerable actions in a matter of a few seconds, AIRIS is incredibly user-friendly and nimble. In AIRIS, you can use triggers to define and set off actions based on a series of events and visitor properties.

You can build dynamic triggers based on multiple variables derived from behavioral data within AIRIS. For example, you can add or update user properties when a user performs a specified action such as downloading a white paper on your website. You can also run custom scripts in order to trigger actions such as displaying discount messages or newsletter opt-ins.

AIRIS allows you to set up triggers to automatically perform actions in third-party applications. With over 60 different third-party integrations, you can set up a wide range of triggers such as creating a lead in Salesforce when a customer signs up for your product demo or adding a user to a Hubspot workflow to send a promotional email.



What is AIRIS: Product Capabilities [4]

https://docs.airis.appier.com/docs/what-is-airis-product-capabilities



With AIRIS, you can schedule automated recurring tasks based on user events or attributes. Scheduled tasks allow you to perform powerful actions such as data syncing, exporting email lists, adding/updating subscription groups based on user behavior, sending reports to teammates, and exporting email lists so that you can focus on other important tasks. With integrations such as Dropbox, Box, and Mailchimp, AIRIS empowers you to share critical business insights and updates in your organization.

To get a full picture of customer engagement across different tools, teams usually need to spend a lot of time looking at siloed data snapshots and piecing them together.

AIRIS solves this industry-wide problem by providing pre-built plug-ins that allow you to connect your other tools in a few steps. With AIRIS’s Integrations technology, you can gather data across CRM, payment, mobile, marketing automation, social, support, and many other tools. This greatly enriches the user data tracked by the Appier SDK in your website or app.

AIRIS offers integrations with over 60 different applications across e-commerce, mobile, email marketing, website tracking, CRM, advertising, social, storage, personalization, and productivity platforms. These integrations allow you to take control of your organization’s data and centralize it in one single platform.Updated 23 days ago



Types of Tracked Data [0]

https://docs.airis.appier.com/docs/types-of-tracked-data



Understanding how AIRIS ingests and categorizes data is an important step to ensuring you gain the most value possible out of the platform. AIRIS uses three types of data:

Event data

User properties

Visit properties

We recommend planning and organizing what types of data are important to you with developers to implement custom tracking.

Event data consists of user events and associated event details, such as:

Page views

Payments

Sign-ups

Logins

Purchases

By default, the Appier SDK tracks page views, scroll depth, button clicks, and download events. In addition, you can customize your tracking to record other important events that you wish to track on your site, e.g. sign-ups, and payments.

You can send event data from your website to AIRIS using appier('event', ...).

👍TipNot sure how to begin tracking event data in AIRIS? Check out our Getting Started guide or consult with your developers to determine which custom events make the most sense for your business.

While tracking events is useful, adding context to describe the events allows you to truly understand your users' behavior. Event properties are specific attributes that provide additional details for the event you’re tracking.

For example, to track every time a customer makes a payment, you can send a “payment” event to AIRIS, along with associated properties such as:

Payment amount

User plan or package

Payment option (e.g. credit card, Paypal, ACH)

There are two types of event properties:

System event properties: These are the event properties that AIRIS tracks by default for every tracked event. See the System Properties page in the AIRIS console for a list of automatically-collected event properties.

Custom event properties: These are the custom properties you've chosen to track with your event. For example, if you’re tracking a payment event, you might include event properties such as payment amount and payment type. You can edit the event schema to control how custom event properties should be read and processed by AIRIS.



Types of Tracked Data [1]

https://docs.airis.appier.com/docs/types-of-tracked-data



User properties consist of any information about the person that's visiting your site or app. User data includes details like:

Name

Email

Company

Phone number

User properties can be leveraged in AIRIS’s segmentation filters to define a behavioral audience you want to analyze, answering questions like:

How many people from "Company A" have engaged with my product in the last 30 days?

How many people older than 30 years old have made a purchase on my website within the last year?

Are users with a job title containing "marketing" more likely to convert than those whose title contains "sales"?

Are users who originally came to my website from Google Adwords more engaged with my product than those who came from Facebook ads?

Tracking user properties requires using the Appier SDK, and you'll need help from your developer to implement it. You can send user data from your website to AIRIS using appier('identify', ...).

Visit properties reflect the state of a session, and are automatically tracked at the start of a session and when user events occur. This data includes automatically-generated System Properties such as:

Browser type

Operating system

Timestamp

IP address

Location

Similar to custom event properties, visit properties can help you to be more specific in defining an event you want to analyze. For example, using visit properties, you can see all the customers who have made a payment from the US by setting the visit property constraint to “Country is USA.”Updated 23 days ago



Challenges the AIRIS Platform Solves [0]

https://docs.airis.appier.com/docs/challenges-the-woopra-platform-solves



The modern customer journey is highly complex and non-linear in nature. To understand the customer experience across channels, teams and tools, you must expand beyond the silos of strictly marketing or product-related touchpoints.

Today’s businesses need to derive insights from across the organization, leveraging marketing, paid and unpaid advertising, customer success, product, support, sales and other groups within the company.

Most businesses find it challenging to democratize data across the organization and obtain a 360-degree view of their customers to drive end-to-end business objectives.

It’s crucial to know how prospective users engage with your product or service in order to identify leads at the right time and on the right channel. This is especially true for SaaS companies that offer a ‘freemium’ model when acquiring new customers. Often, they spend an unreasonable amount of time and resources on lead acquisition by sending repeated communications to prospects on an action such as a free trial sign up form.

Unfortunately, given the vast array of options available out there, such actions are no more telling of the lead’s propensity to purchase. What’s worse is that unwanted emails or calls can do more harm than good by deterring them from your product or service altogether.

For a company focused on the customer experience, actions such as repeated use of certain features, downloading how-to tutorials, and viewing software setup videos are much more indicative of interested prospects. However, there are few tools that track behavior across a product or service while enabling teams to engage with their users in real-time.

With an estimated 66 different SaaS applications that are in use per enterprise – primarily for web and social traffic based analytics activity – companies are unable to properly leverage the data flowing in their organization to generate meaningful and timely insights.



Challenges the AIRIS Platform Solves [1]

https://docs.airis.appier.com/docs/challenges-the-woopra-platform-solves



Moreover, the market is crowded with solutions promising results such as higher conversion rates that are generating further confusion about what solution to implement, at what cost, and at what time. Such a conundrum gives rise to data siloes that often fail to render timely insights to business users. Most importantly, companies often fail to realize how difficult it is to bring all the customer-centric data together in order to find a single source of truth.

Given the fragmentation of investments in tools across all sizes of enterprises, a unifying customer journey analytics solution integrates with all the relevant applications to provide a singular view of each customer and better analyze their interaction and needs across all channels. Companies need to anticipate their customers’ behaviors and shift how they think about and engage throughout the decision journey.

Although every organization is now aware that data is their gold mine, few have managed to establish a sound data strategy that will allow them to consistently monetize from it. Most companies have trouble simplifying their data architectures to build a single layer that augments all the relevant customer-related information in one central location. Connecting with leads and channelizing efforts to truly convert engagement to revenue is that piece of the puzzle that unfortunately many are still trying to solve.Updated 23 days ago



Getting Started with AIRIS [0]

https://docs.airis.appier.com/docs/getting-started-guide-the-woopra-essentials-mix



10-Steps to Get Familiar with the AIRIS Platform and Unleash Your Inner Data Scientist!

Begin exploring all of AIRIS's features with these ten steps:

Install the Web SDK to see your first user profile

Identify users on your website

Track custom events to tailor AIRIS to your business

Use schemas to define your data

Integrate AIRIS with third-party services

Build a journey report to understand your customers' journeys

Build a trends report to analyze the growth of key metrics over time

Build a retention report to increase customer lifetime value

Create a segment to begin analyzing groups of users

Create a trigger to automate tasks outside of AIRIS

AIRIS tracks user behavior across your website, product, and mobile app. To get started, simply insert the Appier Web SDK code snippet to the section of your website.

There are several other ways you can start tracking data instantly in AIRIS. If you’re using an integration like Segment, you can stream any actions already housed in Segment into your AIRIS project.

Once you've finished integrating the SDK, navigate to the Profiles section in AIRIS and watch as your AIRIS user profiles populate. To begin identifying your users, move on to step two!

You can log any custom visitor data to AIRIS by using the appier('identify', ...) function anywhere a user is identified for the first time. Be sure to include a unique identifier like an email address or user ID, along with any other relevant properties you'd like to collect, such as company name or location.

For example, you can log a user's ID or email address when they log in to your website or sign up for a service.

Interested in tracking when your visitors sign up? When customers make a payment? When leads watch a video on your website? Track your first custom action to see how AIRIS can be completely customized to track the metrics that matter most to your business.



Getting Started with AIRIS [1]

https://docs.airis.appier.com/docs/getting-started-guide-the-woopra-essentials-mix



AIRIS allows you to track any combination of custom actions such as payments, logins, or product engagement. Use the appier('event', ...) function to send the event and its associated details to AIRIS. For example, you can send a product_purchased event containing parameters such as product_id, product_name, and category.

Once you begin identifying users and tracking custom actions, they will automatically be added to user profiles and be visible in real time.

👍Defining your eventsBefore you start tracking custom events, it's important to define the which events to track and what parameters to include for each one.Not sure what to track? Check out our SaaS and eCommerce What to Track Guides

Consider the AIRIS schema as your personal data dictionary, where you can define different data types (user properties, events, and event properties) with descriptions that everyone on your team can understand.

Once you track your first custom event, you can edit your data schemas by navigating to the Configure section, then going to Manage > User Schema or Manage > Event Schema. In a schema, you can specify details such as:

The event or property key, template description (for events), and icon

Whether the event is a result of a direct user action

Data type (for user properties)

In addition, you can define how an event is displayed in user profiles by creating a template description. Template descriptions can include tags that are dynamically populated for each user, allowing all your team members to quickly see the relevant data for that user directly in the profile view.

👍Learn more about schemasFor more details about managing your schemas, see Schema.



Getting Started with AIRIS [2]

https://docs.airis.appier.com/docs/getting-started-guide-the-woopra-essentials-mix



👍Learn more about schemasFor more details about managing your schemas, see Schema.

The greatest challenge to improving the customer experience is unifying it. In just a few clicks, you can integrate AIRIS with your favorite email, text, push notification, product, support, live chat tools, or any other supported services. Leverage your data across platforms to analyze the end-to-end experience users have with your brand — from tweets to clicks to conversions and back again.

The majority of integrations include built-in triggers and automations, allowing you to take real time action on your data in the connected service, and without requiring any additional setup. Simply add a connection, and you'll instantly be able to use that service's built-in triggers and automations.

For example:

The Salesforce integration includes a trigger allowing you to automatically updated a lead or contact status based on a user’s behavior, attributes, and engagement.

The Zendesk integration allows you to embed AIRIS user profiles embedded directly within Zendesk, allowing support teams to see every action taken by that user prior to submitting a support ticket and providing a foundation for resolving support inquiries with increased efficiency and greater personalization.

👍Learn more about integrationsFor more details about how to use integrations, see Integrations.

Combine any set of actions, events, or goals to understand how users move across campaigns, through your website, within your application, and beyond!

Journey reports allow you to answer questions such as:

Which of my marketing campaigns drove the most conversions last year?

Where am I losing potential users during onboarding?

What are my highest performing customer segments?

How many users read documentation or submit a support ticket before becoming a customer?

👍Learn more about journey reportsSee Journeys for detailed instructions on creating journey reports.



Getting Started with AIRIS [3]

https://docs.airis.appier.com/docs/getting-started-guide-the-woopra-essentials-mix



👍Learn more about journey reportsSee Journeys for detailed instructions on creating journey reports.

Monitor and analyze the growth of key metrics over time with trends reports. Trends reports help you understand how the most relevant metrics to your business change over time and the underlying forces behind these changes.

Create your first trends report to answer questions like:

How are subscriptions trending over time by package or plan type?

Which product features are used most and by whom?

Are mobile users more engaged as compared to those who use the web app? For mobile users, how active are iOS users compared to Android users?

How is signup growth trending month over month and in what regions?

👍Learn more about trends reportsSee Trends for detailed instructions on creating trends reports.

Retention reports tell you whether users continue to complete significant actions, such as making purchases, using your product, or opening your emails, helping you understand if users are engaged enough with your offerings to keep coming back.

Retention reports allow you to answer questions such as:

Do users continue to take important actions, such as making purchases, using your product, or opening your emails?

How long do customers continue to take a specific action after signing up?

Are users more likely to convert after downloading my mobile application?

👍Learn more about retention reportsSee Retention for detailed instructions on creating retention report.

Creating a segment allows you to begin analyzing users according to who they are and what they do. For example, you can create a “Submitted support ticket” segment containing users who have submitted a support request, or an “At-risk” segment containing users who are at risk of churning.

There are two ways to create a segment in AIRIS:

Create a predefined segment: Navigate to the Configure section, then go to Manage > Segments. Click + New Segment, then specify segment conditions using events and properties.



Getting Started with AIRIS [4]

https://docs.airis.appier.com/docs/getting-started-guide-the-woopra-essentials-mix



Create segments in reports: In any report, specify the segmentation conditions in the Performed by section. The report will only show data for users that satisfy the segmentation conditions you specify.

👍Learn more about segmentationFor more details about segmentation and how to create a segment, see How to Create Segments.

Triggers can be used to complete actions outside of AIRIS, directly in the third-party services you've connected to your project. After installing any of AIRIS’s one-click integrations, you’ll instantly see their associated trigger actions appear in the Automate section.

For example:

The Zendesk integration allows you to automatically update ticket priority based on a user’s behavior or attributes.

The Google Ads integration allows you to sync any custom segments from AIRIS into AdWords to fuel more personalized retargeting campaigns.

The HubSpot integration allows you to automatically enroll users in a drip campaign when they meet certain engagement criteria.

👍Learn more about triggersFor more details about how to create and configure triggers, see Triggers.

Congratulations! You’ve covered the fundamentals of the AIRIS platform. Now that you’re an AIRIS champ, it’s time to invite your colleagues to join. Invite your teammates to AIRIS and start harnessing the power of unified customer data.Updated 23 days ago



Users and Groups [0]

https://docs.airis.appier.com/docs/users-and-group



AIRIS is designed to be accessible by multiple groups of users, each with levels of access to project settings and data.

Each user can customize their own setup that includes their personal dashboard as well as fully customizable trends, journeys, retention, and profile reports.

Each group shares permissions that can be adjusted to limit or allow access to the features for its users.

To add team members to your AIRIS project:

Click Configure in the top navigation bar, then in the left menu, go to User > Users,

Click Invite User.

In the modal that appears:

Under Email address, enter the user's email address. The project invitation will be sent to this email address.

Under Roles, select the user's account type from the dropdown menu.

Under Groups, choose which groups the user should be a part of. Multiple groups can be selected, and each group can be configured with different group permissions.

An email with an invitation to join your AIRIS project will be automatically sent to the user. If the user already has an AIRIS account, the project will be automatically shared with their account.

Users invited to AIRIS can be added as either Admin or Users. Each project can have multiple Admin, but only one Owner.

RoleDescriptionOwnerAn Owner is an Admin. The Owner will have a lock key next to their name in the user list. Each project can only have one Owner.AdminAdmins can add, remove, or update other users’ group settings. They can also update the global project settings like the timezone and schema.Only Admins can see the website’s settings view.UserUsers can set up their own configuration but they cannot add or remove other users or change global website settings.

Admins can control which parts of their data are shared with each user group. To view all user groups associated with your project, and see details such as group permissions, go to User > Groups in the left menu.

Create groups to assign permissions to multiple team members at the same time. To create a group:



Users and Groups [1]

https://docs.airis.appier.com/docs/users-and-group



Create groups to assign permissions to multiple team members at the same time. To create a group:

Navigate the Configure section, go to Users > Groups, then click + New Group.

Enable or disable the features the group should have access to.

To grant or revoke permissions for a user group:

Click on the group you'd like to edit permissions for.

Enable or disable the features the group should have access to.

Updated 23 days ago



Data Onboarding

https://docs.airis.appier.com/docs/airis-data-onboarding



There are several ways to collect the data required to build comprehensive user profiles and power capabilities such as segmentation, analytics, and triggers. Data can be sent to AIRIS using the following methods:

Appier SDK

Data loader

API

👍Data retentionAIRIS supports a minimum data retention period of 2 years. To increase your organization's data retention period, contact your customer success manager.

Integrate the Appier SDK with your website or mobile app and use the SDK methods to collect default user and event data and log custom user and event data. Default data (generated properties) are automatically collected by the SDK, while custom data requires code modifications to your website or mobile app. For details, see Tracking Overview.

Import data from a CSV file or third-party connection directly on the AIRIS console. With the data loader, you can create mappings between the external data source's columns and your AIRIS columns. For details, see Data Loader Overview.

Import data directly from your server via API. For details, refer to the following API references:

Offline Event API v2

Bulk Upload Offline Users API

Updated 23 days ago



What to Track - SaaS and eCommerce

https://docs.airis.appier.com/docs/what-to-track-saas-and-ecommerse



Knowing what to track in AIRIS is an important step. Depending on your business, certain metrics and tracking events can be crucial to understanding your customer's journey. Refer to the following guides to help you determine what to track for SaaS and eCommerce business:

SaaS Tracking

eCommerce Tracking

📘Organize your tracking!Before you start tracking your custom events, it's important to write down all the events you want to track to stay organized.Updated 23 days ago Data OnboardingeCommerce Tracking



eCommerce Tracking [0]

https://docs.airis.appier.com/docs/ecommerce-tracking



We realize that every industry and vertical is unique, for example, an eCommerce company will usually track different events than a mobile gaming or travel company. To help guide you through this process, we’ve compiled tips and best practices by industry to provide the Ultimate Tracking Setup Guide: eCommerce Edition.

Unlike traditional retail stores, eCommerce establishments possess a unique advantage—the capability to track and customer actions. By precisely determining which events to track and specifying the details to accompany each event, you can gather the necessary information to generate valuable insights into your users.

If you’re using WooCommerce or Shopify, you can streamline this process by installing the integration with a few clicks. This will automatically begin tracking relevant eCommerce platform events right out of the box! But what if you’re not using one of these integrations?

We’ve combed through the most successful eCommerce companies using AIRIS and identified trends in what they’re tracking to provide you with a foundation for getting started. Once user property and event logging is set up, the information will display on the user’s AIRIS profile and you can begin to segment, build customer journeys, and leverage the data in your reporting!

📘NoteKeep in mind that the help of a developer will be required to code the custom events you’d like to track. By using this guide, you’ll be able to outline the key events first to significantly cut down on implementation and development time!

AIRIS is designed to track unique, unidentified website and mobile app users from their first touch. The user is assigned a unique ID and all of their anonymous activity is tracked in the customer profile. You’ll also have data regarding the user’s location, system, platform, referrer, and more!



eCommerce Tracking [1]

https://docs.airis.appier.com/docs/ecommerce-tracking



Once the user is identified — by logging their details during a sign up or subscription, for example — all previous anonymous activity will be merged into the same profile. This provides a complete picture of the full lifecycle for every user, starting with the first touch.

To start tracking anonymous website traffic, complete the Appier Web SDK integration (see Tracking Overview) and ensure that the SDK code is pasted into every page of your site that you’d like to track.

👍TipIf you’re hosting your website on WordPress, you don’t need to install the Javascript snippet to track website activity. Simply, install the Woopra WordPress integration and the tracking code will automatically be added!

Most of the activity on your site likely happens pre-sale. That’s when customers are exploring your site, looking through your products, and managing their carts. All of this activity needs to be tracked. Remember that, along with the events, you'll also want to send properties, which are pieces of information that describe the event. Here are some of the key events and properties you should be sent outside of basic page views.

You’ll want to track when website users are viewing specific products, product categories, and product pages on your site. Along with the page view event, we suggest tracking:

product_name

product_id

product_category

product_url

📘NoteThis event should only replace the default page view event in product pages.

Here’s an example of the tracking code that you could customize to track product view events:

const event_parameters = {

'product_id': 'E0238',

'product_name': 'Brand A Computer',

'product_category': 'electronics',

'product_url': 'https://example.com/products/brand-a-computer'

}

appier('event', 'product_viewed', event_parameters);

👍TipAdding the product URL to a product viewed event will generate a link to the product in the AIRIS user profile. This is an easy way to quickly reference the exact product the user viewed.



eCommerce Tracking [2]

https://docs.airis.appier.com/docs/ecommerce-tracking



Tracking when a user plays product videos helps identify the importance of content on conversions. The properties to send with this event might include:

product_name

product_id

product_category

product_url

video_url

When you customize the code, it should look similar to this:

const event_parameters = {

'product_id': 'E0238',

'product_name': 'Brand A Computer',

'category': 'electronics',

'product_url': 'https://mystore.com/products/brand-a-computer',

'video_url': 'https://mystore.com/products/brand-a-computer#play-video'

}

appier('event', 'video_viewed', event_parameters);

How do you know what types of content perform better than others? Are users who read a blog post more likely to convert to paying customers?

Track your blog activity to measure blog attribution, inform future blog post topics, and measure engagement. You can leverage this data in reporting and funnels to optimize engagement.

For example, the following "Blog Attribution" funnel shows how many people read a blog post and then continue to take other actions on the website. You can see how many users read a post and subsequently subscribed, added an item to their cart, added a credit card, and made a purchase.

To track your blog activity, provide the following example to your developer.

appier('event', 'article_viewed', {

'title': 'Blog post title',

'url': 'https://wwww.blog.example.com/',

'author': 'Leon Kimura',

'category': 'News,

'published_on': 125234234234 // Timestamp indicating when the post was published

});

// You can also log an event when a user leaves a comment

appier('event', 'article_commented', {

'comment': 'Great article!'

});

👍TipCheck out this article to learn how to leverage customer insight to fuel content decisions!

It’s important to track when users identify themselves and engage with other content on your site. For eCommerce, this might include contact forms for:

Providing feedback

Submitting a complaint

Order status inquiries



eCommerce Tracking [3]

https://docs.airis.appier.com/docs/ecommerce-tracking



Providing feedback

Submitting a complaint

Order status inquiries

For customer success teams, this information can help you measure the effectiveness of your efforts and allow you to optimize areas for improvement. You can also tie these efforts directly back to ROI by measuring how many users submit support inquiries or provide feedback and make (or don’t make) a purchase.

To track contact form submissions, ask your developer to customize the code snippet below for each of your contact forms:

// Log the user's properties

const user_properties = {

'email': 'appier@example.com',

'first_name': 'Foo',

'last_name': 'Bar'

}

appier('identify', user_properties);

// Log the feedback event

appier('event', 'feedback_form', {

'subject': 'Support feedback',

'message': 'The live chat support was very helpful',

});

If you have a promotional video on your homepage or landing pages throughout your site, you’ll want to track when users play your video content. This is separate from product video views as they do not directly relate to a specific product. Customize the following code sample to begin sending and measuring video engagement data in AIRIS:

const event_parameters = {

'title': 'Video title',

'videoId': '1SF3sx',

'url': 'https://www.example.com/promo-video'

}

appier('event', 'video_played', event_parameters);

Tracking when users add items to their shopping cart allows for greater personalization and insights in your AIRIS reports. For example, if you send the product_id along with the add to cart event, you could trigger an email campaign to everyone who added that specific item to their cart. The properties you could include with the product_added_to_cart event could include:

product_name

product_price

product_category

product_url

quantity (if the user is removing an item from the cart, the quantity will be negative)



eCommerce Tracking [4]

https://docs.airis.appier.com/docs/ecommerce-tracking



product_category

product_url

quantity (if the user is removing an item from the cart, the quantity will be negative)

In addition, the final positional parameter specifies the monetary value associated with the event—in this case, it represents the product's price. After deciding which properties to send along with the product_added_to_cart event, your code could look like this:

const event_parameters = {

'product_id': 'A5343S',

'product_name': 'Brand A Phone',

'product_category': 'Mobile devices & accessories',

'product_url': 'https://www.example.com/brand-a-phone',

'quantity': 1

}

appier('event', 'product_added_to_cart', event_parameters, 799.99);

After customers add items to their cart, you’ll probably want to provide them with an estimate of their shipping costs. Tracking this event can show if the displayed shipping price impacts conversion rates. Properties to send along with shipping estimate events include:

zip_code

shipping_price

Your code snippet will look similar to the following example:

const event_parameters = {

'zip_code': 94104,

'shipping_price': 12.95

}

appier('event', 'estimate_shipping', event_parameters)

If customers leave reviews for the products that you’re selling, it’s helpful to know who reads the reviews. This will allow you to measure if the product reviews negatively or positively impact conversion rates. Some important properties to track along with this event include the:

product_name

product_id

product_category

product_url

You also could track:

total_reviews: This can help you to understand if people are seeing enough reviews for the product they wish to purchase.

rating: This can help show how ratings contribute to conversions.

In addition, the final positional parameter specifies the monetary value associated with the event—in this case, it represents the product's price. Here’s an example of what your custom code snippet could look like when including the above properties:

const event_parameters = {

'product_name': 'Brand A Phone',

'product_id': 'A5343S',



eCommerce Tracking [5]

https://docs.airis.appier.com/docs/ecommerce-tracking



const event_parameters = {

'product_name': 'Brand A Phone',

'product_id': 'A5343S',

'product_url': 'https://www.example.com/brand-a-phone',

'product_category': 'Mobile devices & accessories',

'total_reviews': 412,

'review_rating': 4.9

}

appier('event', 'read_product_review', event_parameters, 799.99)

Online reviews are essential. 92 percent of consumers now rely on product reviews to help inform purchasing decisions. If you offer reviews on your products, you’ll want to track when customers submit reviews to analyze how they impact product purchases. Properties to pass with this event include:

product_name

product_id

product_url

product_category

review_number

review_url

review_rating

In addition, the final positional parameter specifies the monetary value associated with the event—in this case, it represents the product's price. Once you’ve decided which properties matter most to you, customize the code snippet like the example below:

const event_parameters = {

'product_name': 'Brand A Phone',

'product_id': 'A5343S',

'product_url': 'https://www.example.com/brand-a-phone',

'product_category': 'Mobile devices & accessories',

'review_url': 'https://mystore.com/products/iphone-7-plus/reviews/412',

'review_number': 413,

'review_rating': 5

}

appier('event', 'product_reviewed', event_parameters, 799.99)

If you spend a significant amount of time posting to social media, running AdWords campaigns or sharing content – you’re driving traffic from hundreds of different URLs a day. But, how do you know which social media posts drove the most traffic? Can you quickly see which campaigns drove the most conversions over time?

Using UTM parameters, you can compare the performance of campaigns from different mediums and channels and measure over time. A UTM tag will answer questions such as:

Where are my users coming from?

How are they finding me?

What happens after they engage with my campaign?



eCommerce Tracking [6]

https://docs.airis.appier.com/docs/ecommerce-tracking



Where are my users coming from?

How are they finding me?

What happens after they engage with my campaign?

Once you've integrated with the Appier SDK, AIRIS will automatically begin tracking UTM tags for you. You can then set up journeys and trends reports to monitor and measure campaign effectiveness by factors such as campaign name, source, content.

For example, the following journey report shows how many users came to AIRIS through a campaign, sorted by campaign name, and the subsequent actions they took.

Users searching on your website can offer insight into popular products, product categories, and frequently asked questions. Leveraging this data will allow you to personalize their experience and provide the most relevant experience possible. Customize the below tracking snippet to send product search events from your website to AIRIS and include properties such as:

keyword

total_results

The total number of search results allows you to find gaps in product offerings and understand if users are unable to find products they’d like to purchase.

const event_parameters = {

'keyword': 'phone',

'total_results': 12

}

appier('event', 'product_search', event_parameters)

👍TipIncluding the number of search results will allow you to segment searches where users didn’t find any results. This tells you where there might be gaps in your content. It’s also an opportunity to reach out directly and provide an answer or automate an email campaign to provide additional assistance.

One of your main objectives is to get the user to identify themselves on your marketing website. A common strategy is to provide a frictionless, live chat feature.

If you’re using one of AIRIS’s integrations partners for chat, simply navigate to Integrations in your AIRIS instance and install the integration. If not, see the below code snippet as an example of how to track live chat events.

// Log the user properties

const user_properties = {

'first_name': 'First name',

'email': 'user@example.com',

'phone': '123456789' 

}



eCommerce Tracking [7]

https://docs.airis.appier.com/docs/ecommerce-tracking



const user_properties = {

'first_name': 'First name',

'email': 'user@example.com',

'phone': '123456789' 

}

appier('identify', user_properties);

// Log the event

appier('event', 'start_chat');

Every eCommerce company should track customer and user sign-ups. They’re a crucial indicator of traction and allow you to nurture customer relationships over time. For example, you should measure how many people sign up to make a purchase on your website vs. how many continue to checkout as a guest. Properties that you can send along with a sign-up event might include:

email

name

user_id

address (the shipping address)

As well as any other fields relevant to your business that you’re collecting during sign-ups. For example, a clothing store might also want to include a user’s size details and any personal preferences.

The most important property to send with the signup event is the user’s email address. This is what allows you to identify the user and track them across multiple devices (e.g. laptop, phone, work computer).

To track these signup events, you can define the event name string and the properties associated with that event object, as shown below. The following code will track a custom signup event with additional information about the new account.

const event_parameters = {

'name': 'Isabella Kim',

'user_id': 'isabella_kim',

'email': 'isabella_kim@example.com',

'address': 'XYZ Street',

}

appier('event', 'signup', event_parameters);

Passing these events into AIRIS will automatically show the information being sent in real-time on the user profiles and you can start to run custom reporting and funnels. For example, you could measure the number of sign ups by location to understand if your brand is gaining more traction in one area of the world than another.



eCommerce Tracking [8]

https://docs.airis.appier.com/docs/ecommerce-tracking



How often do users login to your application? Who is logging on and what actions do they take next? Tracking login events will answer these questions and help you understand factors, such as the rate at which users successfully log in and the authentication methods used.

Having this data gives you the ability to calculate conversions and identify your most engaged customers. Work with your developer to have log in events sent to AIRIS. Here’s an example of what the code will look like:

// Send at least the email address to AIRIS. This will allow the user

// to be identified even if they're logging in from a different device.

appier('identify', {'email': 'user@example.com'})

appier('event', 'login');

When a user updates their profile information on your website, you’ll want to track this information in AIRIS. Send it as a profile_update event, and include any other parameters that are relevant to your user profiles, e.g. mailing address, email, or when they update their preferred payment method.

const user_properties = {

'first_name': 'First name',

'last_name': 'Last name'

}

appier('identify', user_properties);

appier('event', 'profile_update', user_properties);

See how many users add a payment method before checkout by tracking an "add payment method" event. Be sure to include the payment type as a property to understand which payment methods are the most popular!

appier('event', 'add_payment_method',{'payment_type': 'Visa'});

Understand which promotions are used the most frequently to optimize promotional campaigns and measure their success! Include the below properties with your event:

coupon_code

valid (true or false)

const event_parameters = {

'coupon_code': 'SUMMER24',

'valid': true,

}

appier('event', 'apply_coupon', event_parameters);

Whenever a user checks out, you’ll want to send properties such as payment amount and the product being checked out. Properties to include along with this event include:

total_items

discount_amount

tax_amount

shipping_amount

order_id



eCommerce Tracking [9]

https://docs.airis.appier.com/docs/ecommerce-tracking



total_items

discount_amount

tax_amount

shipping_amount

order_id

In addition, the final positional parameter specifies the monetary value associated with the event—in this case, it represents the product's price.

const event_parameters = {

'total_items': 3,

'discount_amount': 0,

'tax_amount': 154.23,

'shipping_amount': 12.95,

'order_id': '22bksmkdz4m9ds',

}

appier('event', 'checkout_completed', event_parameters, 1430.43);

When tracking customer checkouts, you should also track the itemized checkout to understand the actual sales for every product. For example, if the checkout includes one phone and two phone cases, you’ll want to track each of those items separately so that you can study sales by product item and category. Include event properties such as:

product_name

product_id

product_category

product_url

quantity

In addition, the final positional parameter specifies the monetary value associated with the event—in this case, it represents the product's price.

// Log an event for first product

let event_parameters = {

'product_id': 'A5343S',

'product_name': 'Brand A Phone',

'product_category': 'Mobile devices & accessories',

'product_url': 'https://www.example.com/brand-a-phone',

'quantity': 1

}

appier('event', 'product_purchased', event_parameters, 799.99);

// Log an event for the second product

event_parameters = {

'product_id': 'B4723CV',

'product_name': 'Phone case',

'product_category': 'Mobile devices & accessories',

'product_url': 'https://www.example.com/phone-case',

'quantity': 2

}

appier('event', 'product_purchased', event_parameters, 49.95);

👍TipDo you use Stripe for payment processing? Even better! We’ve built a custom integration with Stripe to make payment tracking seamless. Simply install the integration and let AIRIS do the work!



eCommerce Tracking [10]

https://docs.airis.appier.com/docs/ecommerce-tracking



If you’re an eCommerce company with a subscription model, it’s important to measure new subscriptions, and it’s equally important to measure subscription changes over time to keep a pulse on the health of your customer base. You can drill down based on any available metrics such as geolocation, campaigns, lead sources, and platforms. Tracking subscription events in AIRIS will allow you to answer essential questions such as:

What are my highest and lowest performing customer segments?

At what point are customers likely to churn?

How often do people engage with my product (or take any action) after becoming a customer?

Every time a customer subscription is created, modified, or canceled, you can send a subscription_update event to AIRIS with the following properties:

old_acv: The previous ACV value of the subscription.

new_acv: The new ACV value of the subscription.

delta: The difference between previous ACV and new ACV.

For example, if a customer upgrades from a $99/month (ACV $1,188) package to a $199/month (ACV $2,388) package, the resulting increase in your ARR (Annual Recurring Revenue) is your ACV delta, would be $1,200.

To begin tracking subscription events, follow the same steps to define your event name string and the properties associated with the event object. Adding the above-mentioned properties, your code will look like this:

appier('event', 'subscription_update', {

'old_acv': 1188.0,

'new_acv': 2388.0,

'delta': 1200.0

});

If the customer is creating the subscription for the first time, the old ACV is 0

If the customer is downgrading the subscription, the old ACV is higher than new ACV and the delta is negative

If the customer is canceling their subscription, the new ACV is 0 and the delta is negative

Whether we like it or not, issues and problems occur! By tracking the errors that users encounter, you can arm your customer success team with data to help them provide better service and support. For example, you can send the following events for the various form errors a user may encounter:



eCommerce Tracking [11]

https://docs.airis.appier.com/docs/ecommerce-tracking



appier('event', 'form_error', {

'form': 'signup form',

'error': 'Email already registered'

});

appier('event', 'form_error', {

'form': 'login form',

'error': 'Wrong username or password'

});

appier('event', 'form_error', {

'app_version': '1.2',

'error_code': 500,

'error': 'Failed to download resource'

});

Server-side events can be useful especially when those events are performed on behalf of the user. Here are some events that you should consider tracking.

It’s important to track when a customer's order has successfully shipped, as you can leverage this data to automate email campaigns when the item has arrived and to assist customers experiencing issues. Include properties such as:

order_id

shipping_method

days (days until delivered)

const event_parameters = {

'order_id': '22bksmkdz4m9ds',

'shipping_method': 'FedEx',

'days': 5

}

appier('event', 'product_shipped', event_parameters);

Track when an item is refunded, returned, or exchanged. Be sure to include the refund_amount event parameter as shown in the following example:

appier('event', 'issue_refund', {'refund_amount': 344.95});

It’s important for marketers, sales and customer support teams to track when users open, receive and click on emails. AIRIS integrates with most of the popular email marketing platforms to make email tracking a breeze. Track email events and update lead lists automatically!

For example, the Marketo app will track Marketo events such as an email is sent, or when a user opens and clicks on it. These events are tracked, sent to AIRIS, and included in the AIRIS profile.

In addition, you’ll have trend reports reflecting these events. For example, you may want to analyze which emails had the most opens among customers in California. Or, you may want to build a journey report report showing where people drop off on the path to conversion after they come from an email campaign – and ultimately what impact their email marketing is having on conversion.



eCommerce Tracking [12]

https://docs.airis.appier.com/docs/ecommerce-tracking



You can also set up automations to automatically send new leads to your email marketing software or update existing lead records. For example, if someone signs up on your website, you can set up a trigger to automatically send the lead’s information to Hubspot and a new Hubspot Lead will be created. If they change their company information, later on, those fields will be updated in their Hubspot Lead record.

Want to use all this data in AIRIS to update your email marketing lists based on user behavior? This functionality is also built into our integrations. For example, you could update your MailChimp List for “Ready to Buy” users whenever a user adds an item to their cart, enters their shipping information and adds a credit card to their profile!

Pick your email platform below to learn more about each integration:

Marketo

Hubspot

MailChimp

SendGrid

Campaign Monitor

Customer.io

Are users who submit support requests more likely or less to convert? What impact do certain product features have on support tickets? Do well-answered support tickets drive conversions? Find all of this out and more by integrating with one of our customer support tools!

Track when users submit tickets and track when they get resolved. This is helpful to study the attribution of your customer success team to the retention of your customers.

Are you collecting valuable NPS data from your customers? Track this data in AIRIS to build audiences of promoters and detractors. Integrating with Delighted will allow you to automatically see NPS survey results on profiles on AIRIS. You can trigger personalized emails to re-engage detractors or send a special offer to your promoters!Updated 23 days ago



SaaS Tracking [0]

https://docs.airis.appier.com/docs/saas-tracking



We realize that every industry and vertical is unique, for example, an eCommerce company will usually track different events than a mobile gaming or travel company. To help guide you through this process, we’ve compiled tips and best practices by industry to provide The Ultimate Tracking Setup Guide: SaaS Edition.

Each SaaS application you use, from your marketing automation software to your CRM, houses unique engagements and actions taken by users. When these scattered data sources are pieced together, they reveal the total customer experience and enable you to optimize and engage with customers like never before.

Many SaaS companies are heavily reliant on key moments in the customer lifecycle that fuel their success and growth. These include marketing website actions, sign-ups, subscriptions, free trials, onboarding, usage, retention, and upsells. In this guide, we’ll walk through how to track and measure each of these moments in AIRIS. Once property and event logging is set up, the information will be displayed on user’s AIRIS profile and you can begin to segment, build customer journeys, and leverage the data in your reporting!

📘NoteKeep in mind that the help of a developer will be required to code the custom events you’d like to track. But, by using this guide, you’ll be able to outline the key actions first to significantly cut down on implementation and development time!

AIRIS is designed to track unique, unidentified website and mobile app users from their first touch. The user is assigned a unique ID and all of their anonymous activity is tracked in the customer profile. You’ll also have data regarding the user’s location, system, platform, referrer, and more!

Once the user is identified — by logging their details during a sign-up or subscription, for example — all previous anonymous activity will be merged into the same profile, providing a complete picture of the full lifecycle for every user.



SaaS Tracking [1]

https://docs.airis.appier.com/docs/saas-tracking



To start tracking anonymous website traffic, complete the Appier Web SDK integration (see Tracking Overview) and ensure that the SDK code is added into every page of your website that you’d like to track.

How can you determine which types of content perform better than others? Are users who read a blog post more likely to convert to paying customers?

Track your blog activity to measure blog attribution, inform future blog post topics, and measure engagement. You can leverage this data in reporting to optimize engagement.

For example, the below ‘Blog Attribution’ customer journey shows how many people read a blog post and then went on to take other events in my product and on my website.

To track your blog activity, provide the following code sample to your developer.

const event_parameters = {

'title': 'Blog post title',

'url': 'https://blog.companya.com/we-are-awesome',

'author': 'John Smith',

'category': 'News',

'published_on': 125234234234 // Timestamp indicating when the post was published

}

appier('event', 'article_viewed', event_parameters)

appier('event', 'article_commented', {'comment': 'Great article!'})

👍TipCheck out this article to learn how to leverage customer insight to fuel content decisions!

It’s important to track when users identify themselves and reach out regarding experiences with your site, your support or transactions. This could include:

Downloading a white paper

Downloading an eBook

Submitting a demo request form

Registering for a webinar

Submitting a contact request form

For a marketer, this information can help you measure the effectiveness of your efforts and allow you to optimize areas for improvement. You can also tie these marketing efforts directly back to ROI by measuring how many users sign up for your product or become a customer after engaging with your content.

To track contact form submissions, customize the following code snippet for each of your contact forms:

// Log the user's properties

const user_properties = {

'email': 'appier@example.com',

'name': 'Full name',



SaaS Tracking [2]

https://docs.airis.appier.com/docs/saas-tracking



// Log the user's properties

const user_properties = {

'email': 'appier@example.com',

'name': 'Full name',

'company': 'Appier'

}

appier('identify', user_properties);

// Log the demo request event

const event_parameters = {

'subject': 'Technical demo',

'message': 'We would love to schedule a demo this week',

}

appier('event', 'demo_request', event_parameters)

If you have a promotional video on your homepage or instructional videos throughout your site, you’ll want to track when users play your video content. Customize the following code sample to begin sending and measuring video engagement data in AIRIS:

const event_parameters = {

'title': "Video title",

'videoId': "1SF3sx",

'url': "https://example.com/promo_video/"

}

appier('event', 'play_video', event_parameters)

If you spend a significant amount of time posting to social media, running AdWords campaigns or sharing content – you’re driving traffic from hundreds of different URLs a day. But, how do you know which social media posts drove the most traffic? Can you quickly see which campaigns drove the most conversions over time?

Using UTM parameters, you can compare the performance of campaigns from different mediums and channels and measure over time. A UTM tag will answer questions such as:

Where are my visitors coming from?

How are they finding me?

What happens after they engage with my campaign?

Once you've integrated the SDK with your website, AIRIS will automatically begin tracking UTM tags for you. You can then set up journeys and trend reports to monitor and measure campaign effectiveness using properties such as campaign name, source, and content.

For example, the following journey report shows how many users came to AIRIS through a campaign, sorted by campaign name, as well as the subsequent actions they took.



SaaS Tracking [3]

https://docs.airis.appier.com/docs/saas-tracking



User searches can provide insights into popular content and frequently asked questions. Leveraging this data will allow you to personalize their experience and provide the most relevant content possible. Customize the following code sample to send internal search events to AIRIS:

const event_parameters = {

'query': 'campaign tracking',

'url': 'https://www.appier.com',

'results': 14

}

appier('event', 'search', event_parameters)

👍TipIncluding the number of search results will allow you to segment searches where users didn’t find any results. This tells you where there might be gaps in your content. It’s also an opportunity to reach out directly and provide an answer or automate an email campaign to provide additional assistance.

One of your main objectives is to get users to identify themselves on your marketing website. A common strategy is to provide a frictionless, live chat feature.

If you’re using one of AIRIS’s integrations partners for chat, you install the integration directly from the AIRIS console. Alternatively, refer to the following code sample to learn how to track live chat actions.

const event_parameters = {

'name': 'Name',

'email': 'user@example.com',

'company': 'Example Company'

}

appier('event', 'start_chat', event_parameters)

👍TipRead “How to Generate Leads with Data and Live Chat” for additional guidance and tips!

Every SaaS company should track application sign-ups. They are one of the most crucial indicators of traction and must be optimized over time. Properties that you can send along with a sign-up action might include:

Email address

Name

Username

Plan/account level

Company name

As well as any other fields relevant to your business that you’re collecting during sign-up. The most important property to send with the sign-up event is the user’s email address. This is what allows you to identify the user and track them across multiple devices (e.g. laptop, phone, work computer).

The following code tracks a custom sign_up event along with additional account details:



SaaS Tracking [4]

https://docs.airis.appier.com/docs/saas-tracking



The following code tracks a custom sign_up event along with additional account details:

const event_parameters = {

'company': 'Example Business',

'name': 'Full name',

'username': 'username',

'email': 'user@example.com',

'plan': 'Free Trial'

}

appier('event', 'sign_up', event_parameters)

Passing these events into AIRIS will automatically show the information being sent in real-time on the user profiles and you can start to build custom trends and journeys reports. For example, you could measure the number of sign-ups by company to understand if your product is expanding across an organization.

How often do users log in to your application? Who is logging on and what actions do they take next? Tracking login events will answer these questions and help you understand other factors, such as the rate at which users successfully log in and the authentication methods used.

appier('event', 'login', {'email': 'user@example.com'})

When a user updates their profile information within your application or on your website, you’ll want to track this information in AIRIS by sending a profile_update event. Include any of the fields that are relevant to your user profiles, such as their name or company.

const event_parameters = {

'first_name': 'First name',

'last_name': 'Last name',

'company': 'Company',

}

appier('event', 'profile_update', event_parameters)

Whenever a user makes a payment, you’ll want to send properties such as payment amount and what service the payment was for. For recurring payments, you may need to track server-side events, since the user won't be on the website during renewal.

In the following code sample, the final positional parameter specifies the monetary value associated with the event—in this case, it represents the product's price.

appier('event', 'payment', {'product': 'premium'}, 500);

👍TipUse Stripe for payment processing? Even better! We’ve built a custom integration with Stripe to make payment tracking seamless. Simply install the integration and let AIRIS do the work!



SaaS Tracking [5]

https://docs.airis.appier.com/docs/saas-tracking



SaaS companies live and die by their ARR (Annual Recurring Revenue), MRR (Monthly Recurring Revenue), ACV (Annual Contract Value), and LTV (Lifetime Value). While it’s important to measure new subscriptions, it’s equally important to measure subscription changes over time to keep a pulse on the health of your customer base.

You can drill down based on any available metrics such as geolocation, campaigns, lead sources, and platforms. Tracking subscription events in AIRIS will allow you to answer essential questions such as:

What are my highest and lowest performing customer segments?

At what point are customers likely to churn?

How often do people engage with my product (or take any action) after becoming a customer?

Every time a customer subscription is created, modified, or canceled, you can send a subscription update event to AIRIS with the following properties:

old_acv: The previous ACV value of the subscription.

new acv: The new ACV value of the subscription.

delta: The difference between previous ACV and new ACV.

For example, if a customer upgrades from a $99/month (ACV $1,188) package to a $199/month (ACV $2,388) package. The resulting increase in your ARR (Annual Recurring Revenue) is your ACV delta, which is $1,200 in this example. The following code sample demonstrates how to track this subscription update:

appier('event', 'subscription_update', {

'old_acv': 1188.0,

'new_acv': 2388.0,

'delta': 1200.0

});

If the customer is creating the subscription for the first time, the old ACV is 0

If the customer is downgrading the subscription, the old ACV is higher than new ACV and the delta is negative

If the customer is canceling their subscription, the new ACV is 0 and the delta is negative

Every SaaS company will have its own onboarding process with key milestones, all of which should be tracked to monitor and analyze product adoption and usage. This is where you should give a lot of thought to answering the following question: What actions must a user take to get value out of my product?



SaaS Tracking [6]

https://docs.airis.appier.com/docs/saas-tracking



To begin tracking your onboarding events in AIRIS, outline the milestones that matter most to your organization. These could include actions that users take within your product or other events such as opening an email or communicating with your sales team.

It helps to pretend to be a new user and go through the sign-up, implementation, and onboarding process yourself, documenting every critical event along the way. For example, you might want to create a journey that includes the following steps:

Arrived on the landing page

Signed up

Added a credit card

Installed the mobile app

Became a customer

👍TipLearn more about how to build and optimize an onboarding journey!

It’s great to track when new users sign up for your product, but what’s even more important is what happens after they sign up.

What features are they engaging with?

Where are they getting stuck?

What does a healthy customer look like in your product?

How do you identify users who qualify for an upsell?

Tracking the behavior that users take once they’re in your application will allow you to answer all of these questions, and more! Before deciding the product events to send to AIRIS, you’ll want to start by asking: What are the key actions a user takes to get value from my product?

In addition to your “core” events, you should also track the events you would expect to see advanced users doing, such as using your more complex features. This will enable you to analyze the behavior of power users and give you clues as to how you can help move your less advanced users along this path.

A single-page application (SPA) is a website or web app that loads all of the resources required to navigate throughout the application on the first page. It’s important to track the application's load_time property for basic monitoring and to see if application load times are impacting conversions or churn.

appier('event', 'app_load', {'load_time': 1231})



SaaS Tracking [7]

https://docs.airis.appier.com/docs/saas-tracking



appier('event', 'app_load', {'load_time': 1231})

Track any CRUD operations that users may execute. The way to think about this is to identify all of the main entities in your project (e.g. report, dashboard, widget, song, board, project) and all the verbs that apply to them (e.g. create, view, update, delete, archive, share), then track all the required combinations of entities and verbs.

For example, a recruiting company would probably want to track when users create a job listing, so they could track events for when a user creates a job listing, updates a job listing, and archives a job listing:

appier('event', 'create_widget', {'title': 'Widget Title', 'type': 'chart', 'project': '143'});

appier('event', 'create_job_listing', {'title': 'Marketing Intern', 'department': 'marketing'});

appier('event', 'update_job_listing', {'title': 'Marketing Associate', 'department': 'marketing'});

appier('event', 'delete_widget', {'project': '142'});

Does your application have sharing or collaboration capabilities? You’ll want to track when users invite other users to join projects, when they join or when they share specific entities.

appier('event', 'user_invite', {'user': 'user@example.com'});

appier('event', 'share_widget', {'user': 'user@example.com','widget': '123'});

Whether we like it or not, issues and problems occur! Be prepared by tracking the errors that users experience. This will help you build a better product and will arm your customer success team with data to help them provide better service and support. For example, if a user receives a form error, you could send the event to AIRIS using the following code:

appier('event', 'form_error', {

'form': 'signup form',

'error': 'Email already registered'

});

appier('event', 'form_error', {

'form': 'login form',

'error': 'Wrong username or password'

});

appier('event', 'form_error', {

'app_version': '1.2',

'error_code': 500,

'error': 'Failed to download resource'

});



SaaS Tracking [8]

https://docs.airis.appier.com/docs/saas-tracking



});

appier('event', 'form_error', {

'app_version': '1.2',

'error_code': 500,

'error': 'Failed to download resource'

});

It’s important for marketers, sales and customer support teams to track when users open, receive and click on emails. Use AIRIS's email service integrations to track email events and update lead lists automatically!

For example, the Marketo app will track Marketo events such as when an email is sent or when a user opens and clicks on it. These events are tracked, sent to AIRIS, and included in AIRIS profiles.

In addition, you’ll have trends reports reflecting these events. For example, you may want to analyze which emails had the most opens among customers in California. Or, you may want to build a journey report report showing where people drop off on the path to conversion after they come from an email campaign — and ultimately what impact their email marketing is having on conversion.

You can also set up automations to automatically send new leads to your email marketing software or update existing lead records. For example, if someone signs up on your website, you can set up a trigger to automatically send the lead’s information to Hubspot and a new Hubspot Lead will be created. If they change their company information, later on, those fields will be updated in their Hubspot Lead record.

Want to use all this data in AIRIS to update your email marketing lists based on user behavior? This functionality is also built into our integrations. For example, you could update your Marketo List for “Ready to Buy” users whenever a user completes a free trial, uses the app at least 20 times, and has no unresolved help desk tickets!

Are users who submit support requests more or less likely to convert? What impact do certain product features have on support tickets? Do well-answered support tickets drive conversions? Find all of this out and more by integrating with one of our customer support tools!



SaaS Tracking [9]

https://docs.airis.appier.com/docs/saas-tracking



Track when users submit tickets and track when they get resolved. This is helpful to study the attribution of your customer success team to the retention of your customers.

Leverage behavioral data from AIRIS in Salesforce to get a pulse on customer health without ever leaving your CRM!

The AIRIS + Salesforce integration allows you to automatically create leads within Salesforce and convert them to Salesforce “opportunities” when they meet specified criteria, such as engaging with your website in a certain way or opening your emails. The app also synchronizes your Salesforce fields with AIRIS user data to automatically create or update user properties.

For example, if someone signs up on your website, the integration could automatically add the user as a lead in Salesforce and populate the lead record with the user’s information such as name, email address, company, and more. Conversely, lead data in Salesforce can be sent to AIRIS to automatically update the profile with the lead information. This integration can also automatically convert leads to opportunities when the lead has performed specific actions, such as:

Using your SaaS product ten times

Submitting at least one support ticket

Starting a live chat with a sales rep

Not using Salesforce? Check out our other CRM integrations such as PipeDrive.

👍TipLearn how to build a product qualified lead engine uniting product engagement and CRM data!

Are you collecting valuable NPS data from your customers? Track this data in AIRIS to build audiences of promoters and detractors. Integrating with Delighted will allow you to automatically see NPS survey results on profiles on AIRIS. You can trigger personalized emails to re-engage detractors or send a special offer to your promoters!Updated 23 days ago



Manage

https://docs.airis.appier.com/docs/configure-manage



The following configurations are available under the Manage section:

Segments

Annotations

ID Hierarchy

Schema

System Properties

Archive

Updated 23 days ago SaaS TrackingSegmentsDid this page help you?



Segments

https://docs.airis.appier.com/docs/segments



You may have many questions about your users. For example:

Of the people who came to the website via search engines, how many purchased items?

What behavioral attributes do my customers have in common?

What actions have my customers taken while engaging with my marketing website or product?

Segmentation is the process of grouping users based on certain behaviors, demographics, or other user data. Once a segment is created, you can quickly apply it to other AIRIS features such as reports and triggers.

By focusing on only the users you want to analyze, you can better understand your users, probe deeper to make data-driven decisions, and take action based on these valuable insights.

You can find AIRIS segments under the Configure section of your AIRIS Dashboard. See how to create segments.

Updated 23 days ago



How to Create Segments [0]

https://docs.airis.appier.com/docs/how-to-create-segments



You can build segments based on user properties, events, and visit properties. You can also use a combination of these criteria to fulfill more complicated scenarios.

For example, you may want to create a segment of customers who’ve submitted at least two support tickets and visited at least four documentation pages within the last 30 days to monitor customers who’ve sought out help. This would allow your customer success team to act faster in resolving issues. Or, you may want to create a segment of customers who’ve signed up for your product after downloading a white paper to monitor their engagement and conversion and better understand the ROI of your content marketing.

There are two ways to create segments in AIRIS.

You can create segments in the Configure section.

You can segment users inside reports and triggers, and save the segmentation filters as a new segment.

Go to Configure > Segments in the navigation bar, and click New Segment.

Name your segment, give it a description, and select a color. These settings will determine how the segment will appear throughout AIRIS.

Click the + sign next to Filter by and define the segmentation filters. For details on how to use filters, see Segmentation Filters.

You can add multiple filters if needed.

Complete the following settings.

Profile: You can choose whether or not to display the segment in the profiles of users who belong to this segment.

Track events: You can choose whether or not to track segment join and segment leave events when the user does an action that includes or excludes them from the segment. For more details about these events, see Segment join and segment leave.

Click Save.

You can also create segments in reports and triggers.

In reports or triggers, click the + sign next to Performed by and define the segmentation filters. For details on how to use filters, see Segmentation Filters.

You can add multiple filters if needed.

👍TipIn the drop-down list, you can also select segments you’ve previously created in AIRIS before.



How to Create Segments [1]

https://docs.airis.appier.com/docs/how-to-create-segments



👍TipIn the drop-down list, you can also select segments you’ve previously created in AIRIS before.

If you want to save these segmentation filters as a new segment, click Save next to Custom and name the segment.

Finish setting up the report or trigger you want to create.

If you choose not to save the custom segment, the segmentation filters created within the report or trigger are still applied the next time you access the report or trigger. You can always make changes to your segmentation filters within the report or trigger, and save your changes.

Here are some examples of how to use segments in reports, triggers, and schedule batches.

Profile reports: You can select a segment of users you want to see in the profile report, build a customizable table with the segment data, and save or export it later. For example, you can create a segment of users who’ve submitted at least five support tickets within the last 30 days and create a table of these customers showing their first name, last name, company, and email address. You can then share this list with your customer success team so they can proactively follow up with these customers.

Journeys reports – In journeys, you can segment users and see if they complete the journey you’ve designed for them. A good example of leveraging segments in journeys would be setting up your onboarding funnel and analyzing if the segment of users who’ve clicked on your onboarding emails are more likely to convert than those who haven’t. This would help you understand the impact your onboarding emails have had on conversions.

Retention report: In retention reports, you can build a behavioral segment of customers to see if they keep coming back to engage with your offering. For example, you can create a segment of your enterprise customers to see if they log in to their accounts and continue using your core product features.



How to Create Segments [2]

https://docs.airis.appier.com/docs/how-to-create-segments



Trends reports: In trends reports, segments can help you analyze how a particular group of people behaves over time. For instance, you can create a segment of customers who came from your Google Ads campaigns and see how they convert into paying customers over time.

Triggers: With triggers, you can define a segment and trigger an automatic action when certain criteria are met. For example, you can set up a segment of users who’ve recently downgraded. You can set up a trigger in AIRIS so that every time they log in to their accounts, you can notify your account executive team via Slack or Email to initiate a conversation and see what went wrong.

Scheduled Batches: With scheduled batches, you can take automated action on a profile report based on a set time interval. For instance, you can create a profile report based on a segment of users who haven’t engaged with your newly-built product feature in the past 7 days. You can then target these customers with a highly-contextual automated email on a weekly basis.

Updated 23 days ago



Segmentation Filters [0]

https://docs.airis.appier.com/docs/segmentation-filters



AIRIS segmentation filters are extremely flexible as you can leverage multiple types of data, filter based on event count, and organize filters into multiple nested levels.

When creating a segment, report, or trigger, you can set up segmentation filters by clicking the + sign next to Filter by or Performed by.

Inside each segmentation filter, there are three main settings:

Filter

Aggregation

Timeframe

You can use the following types of data to filter users:

Events

User properties

Visit properties

More information about each type of data can be found in Types of tracked data.

These are the actions users perform while on your website or app. In the Filter drop-down list, select or type in the event you’d like to filter by. This could be a payment, signup, login, or any other events you’re tracking within AIRIS.

After selecting an event, click Add constraint to select your event properties if you want to be more specific.

📘Note

You don’t need to select an event property if you want to analyze just only that event.

If you add multiple constraints, all event properties specified must be met.

Here's an example. You could select "product purchase” as an event to see all customers who’ve purchased a product. You can also add event properties to only include purchase events where the product category is "sportswear" and the product price is greater than $20. AIRIS would include all users who have purchased products that are over $20 and belong to the "sportswear" category.

Visit properties are the data AIRIS automatically tracks about a user's visit session, such as the browser type used by the users or visit duration.

In the Filter drop-down list, select or type in the visit property you’d like to filter by. For example, you could filter by the visit property “Country” where the country is “Canada.” See the system visit properties that AIRIS tracks by default.



Segmentation Filters [1]

https://docs.airis.appier.com/docs/segmentation-filters



After selecting a visit property, you’ll notice that the event section will be set to Any Event. This means that AIRIS will build a segment of users who have performed any event and who match the visit property you’ve defined.

You can always change Any Event to an event you want to focus on. For example, you can choose “Payment” as an event, and if the user property country is set to Canada, AIRIS will create a segment of users who’ve made a payment while being in Canada.

User properties are information or attributes about the users who are visiting your site or app, such as name, email, company, and membership status.

In the Filter drop-down list, select or type in the user property you’d like to filter by. For instance, if you’re tracking “Company” as a user property, you can filter by “Company” and set the company name to "Appier". AIRIS will then create a segment of users at the company "Appier".

The Aggregation option allows you to filter based on how many times a customer has performed a certain action, the total duration of the event, or the sum of the properties.

Here are the default aggregation types you’ll find in the Segmentation filter:

Count Events: You can define the number of times a customer has performed the action you’re analyzing. An example would be customers who’ve made a payment at least three times. Alternatively, you could set the count to “0” to see customers who have not performed a certain action. For example, you could create a segment for customers who have never visited your website.

Count Visits: You can define the number of visits where the user has performed a certain action. If the user performs the action multiple times during a visit, it's only counted once.

Sum of Event Duration: The sum of the values of the Event Duration system properties.

For event or user properties that can be added up, such as a number, you can also add the sum of the property as a custom aggregation type. You'll need to set this up in the event schema or user schema first.



Segmentation Filters [2]

https://docs.airis.appier.com/docs/segmentation-filters



When defining event properties and user properties in a schema, if you have set the Aggregate setting to Amount, the property will also show up in the Aggregation drop-down of the segmentation filter. This allows you to filter based on the sum of the property.

For example, let's say you have an event purchase_product with product_price as one of its event properties. You can set the Aggregate setting to Amount.

In the segmentation filter, you can now see Sum of product_price as one of the Aggregation options. For example, if you set the Sum of product_price to $200, AIRIS would only include users with purchases that added up to over $200 during the time frame.

Under Timeframe, you can define a date range for the event you’re analyzing. You can click the calendar icon to select from one of the preset options. Or click the start time or end time to customize the date range.

There are three timeframe options when customizing a date range.

Absolute: Select a static date, such as “March 4, 2024”.

Relative: Select a time that is relative to the present day, such as "90 days ago" or "Today". This timeframe is dynamic and updates in real time.

Annotations: If you have set up annotations to tag a significant date, you can select an annotation.

You can create multiple segmentation filters in AIRIS and combine the filters using the AND/OR operators. Click AND/OR to change the operators between all filters.

AND: The “AND” parameter will retrieve users who match all of the filters.

OR: The “OR” parameter will retrieve users who match any of the filters.

For example, if you want to create a segment of customers who’ve submitted at least five support tickets within the last 90 days and who have an ARR greater than $10,000, you could create the two following filters:

Event is set to “Ticket Submitted”, count events is “at least 5 times”, and the timeframe is last 90 days

AND

User Property is set to “ARR”, and user property constraint is “ARR>$10,000.”



Segmentation Filters [3]

https://docs.airis.appier.com/docs/segmentation-filters



AND

User Property is set to “ARR”, and user property constraint is “ARR>$10,000.”

Alternatively, if you want to create a segment of all “United States” customers who’ve started a chat conversation with you or opened a promotional email, you’ll set up segmentation filters as follows:

Visit Property is country, visit property constraint is USA, event is “Chat Initiated”

OR

Visit Property is country, visit property constraint is USA, event is “Email Opened”

If you have more than two filters and want to use both AND and OR operators, you can group the filters into nested levels. To do this, you can hover over the filter and click the + icon. You can also drag a filter and drop it onto another filter.

Let’s take an example. Say you want to identify all customers who visited your website or mobile app at least once in the last 30 days but did not purchase so that you can determine how to engage with them. Simply add the segmentation filters as shown below:

Did page view at least once in the last 30 days OR did app launch at least once in the last 30 days, AND

Did product purchase event exactly 0 times in the last 30 days

Updated 23 days ago



Predictions [0]

https://docs.airis.appier.com/docs/predictions



📘Contact your customer success manager to enable this feature.

Use AIRIS prediction scores to enhance campaign effectiveness by identifying users based on their behavior and likelihood of engagement. By leveraging these scores to create targeted segments, you can drive higher conversions, increase click-through rates (CTR), and optimize the return on investment (ROI) of their campaigns.

The following table describes the available prediction types.

Prediction typeDescriptionExample campaign use casesTarget campaign audienceConversion ScoreUse Conversion Score to predict a user's intent to convert during their session.This prediction type enables precise targeting of high-potential customers, increasing overall conversion rates and customer lifetime value.• General marketing campaigns, including storewide discounts or clearance sales.• Targeting high-value customers to maximize conversions.Users who are likely to convert.Campaign Engagement ScoreUse Campaign Engagement Score to predict the likelihood of a user interacting with a campaign.This prediction type is particularly useful for re-engaging inactive users or driving CTR in promotional campaigns.• Re-engaging users who haven't visited recently but showed high engagement before.• Promotional campaigns featuring deeper discounts or special sales.Inactive users who are likely to interact with a campaign.

Go to Configure, then from the left menu, go to Manage > Predictions.

Click the prediction you'd like to start using, then click Activate.

After activating the prediction, choose a template under Segment templates and click Create Segment.

Next, adjust the segmentation criteria and criteria values to fit your specific requirements.

The number of Estimated users displays the estimated segment size—if the segment size doesn't meet your expectations, you can continue adjusting the segmentation criteria and reviewing the estimated user count.



Predictions [1]

https://docs.airis.appier.com/docs/predictions



Once you're satisfied with the segmentation criteria, save the segment. The newly-created segment will appear in the segment list, and you'll be able to start using it in your campaigns.

The following table describes each segmentation criteria.

CriteriaUsageDescriptionLikelihood levelSegment users based on how many standard deviations they are from the average (mean) prediction score.There are five likelihood levels:• Very Low: Scores less than or equal to -2 standard deviations from the mean.• Low: Scores between -2 and -1 standard deviations from the mean.• Medium: Scores within ±1 standard deviation from the mean.• High: Scores between +1 and +2 standard deviations from the mean.• Very High: Scores greater than or equal to +2 standard deviations from the mean.PercentileSegment users based on their percentile, or relative prediction score.Users are split into 100 equally-sized groups based on their prediction score so that each group represents one percent of the total population.ScoreSegment users based on their raw prediction score.The user's raw score.

👍Tip: Likelihood level vs Percentile

Likelihood level: Ideal for optimizing resource allocation, such as assigning different incentive levels based on user engagement intensity. This criterion can help to identify behavioral outliers.

Percentile: Ideal for campaigns where ranking is the primary goal, such as rewarding the top 10% of users. This criterion ranks based on equally-sized groups, making it easier to control audience size.

Updated 23 days ago



Annotations

https://docs.airis.appier.com/docs/annotations



Use Annotations to tag important milestones and events to understand which initiatives are driving the most growth.Annotations allow you to tag a significant date to clearly see what impact it had on conversions, growth, and engagement. You create annotations for important events such as a new feature launch, the start of a campaign, the beginning and end of financial quarters, and much more!

Once you create an annotation, you'll be able to see it marked in trend reports, and annotations can also be used in report Timeframe settings.

Go to Configure > Annotations. Click + New Annotation, then set the title, description, and event date.

You can optionally put the annotation in an annotation group. For example, you can create annotation groups like "Marketing Campaign" or "Feature Release".

To create a new group, click on the Annotation Group dropdown and select Manage Annotation Groups.

When you're satisfied with your settings, click Create to finish creating the annotation.

In trend reports, you can show or hide annotations by clicking on the annotation icon.

When you show the annotations, you'll see them marked on the trend report graph.

Hover over the annotation dots to see more information.

You can also use annotations to set the Timeframe setting in reports. To do so, select the timeframe start or end point, then select to the Annotations tab and select an annotation. After selecting one, the timeframe setting will use the date from the annotation.

Updated 23 days ago



AIRIS's Profile ID System [0]

https://docs.airis.appier.com/docs/profile-id-system



AIRIS has an advanced ID mapping system that allows it to use many different fields to uniquely identify an individual profile. The basic concepts section introduces some conventional database concepts and AIRIS's challenges—then we'll dive into how AIRIS's ID system works and how to make the best use of it.

There is some necessary but unfortunate equivocation in the terminology we use here: ID. There is the concept of:

An identifier, which could be a database ID field or other identifying fields like an email address or even a cookie.

The value of one of these identifiers, which might be referred to as a person's or profile's ID, email ID, device ID (i.e. cookie), etc.

The highest-order identifier in the AIRIS ID hierarchy.

AIRIS needs to be able to tell which person's profile performed an incoming tracked action (or property update). The problem is that people in AIRIS can exist at a number of different levels of being identified. They could be a first-time anonymous visitor to a website or a long-time paying customer.

Sometimes a person will make a few visits to your site anonymously over a year before they decide to sign up for your newsletter, giving you their email. Sometimes this means that what was previously considered to be two different people in AIRIS is now known to be a single person, perhaps originally from two devices, requiring a merge of the two profiles.

In the traditional database world, merging two rows with different identifiers is a messy business.

Which primary unique identifier is kept?

What if a database user asks for the row with an ID that was removed?



AIRIS's Profile ID System [1]

https://docs.airis.appier.com/docs/profile-id-system



Which primary unique identifier is kept?

What if a database user asks for the row with an ID that was removed?

Additionally, since every row must have an ID, you can't wait until you know that all of a single person's actions and traits are in the one database row that represents them. Another issue is that if you want to track anonymous behavior and even attribute it to known people in the future as they identify themselves to you, then using a single ID value per person becomes more complex. Similarly, if you want to track behavior across channels, then it's basically impossible to maintain the database ID for the profile between your website and, say, your email marketing automation service.

These and other more nuanced issues make this problem of identifiers significant in the AIRIS system. AIRIS solves this problem by dedicating an entire sub-system to managing identifiers.

AIRIS needs to be able to take whatever information is available about a person performing the action in an incoming track request and use it to determine, with the highest accuracy possible, which other actions this person has performed and thus, to which profile the incoming events belong.

If a user visits your website anonymously, all you have is a cookie, which is conceptually a device ID pointing to that browser on that machine. The cookie will be the same if the person uses the same machine and browser during their next visit. But if they visit from a different browser or device, such as their phone, you will have a new cookie. When that person eventually signs in, AIRIS needs to be able to associate these devices and know that these cookies all refer to one person.



AIRIS's Profile ID System [2]

https://docs.airis.appier.com/docs/profile-id-system



Similarly, you may have an incoming "Email Sent" event from your email marketing tool that is not from a browser and has no cookie. This event has an email address—another major identifier. When the person eventually signs in with that email address on their browser with that cookie they had in the past, AIRIS needs to be able to associate that the events performed by cookie 1, cookie 2, and email 1 all belong to the same profile.

AIRIS's profile ID system supports multiple profile identifier fields. The ID fields exist in a hierarchy and are stored in their own database that associates or maps profiles to the values of various identifiers in the ID hierarchy that have been given to a person.

When an individual first visits your site, they will be an anonymous visitor. A unique user profile is created and AIRIS will track them via Appier ID. Once they are identified, their profile will be updated with their visitor properties. If there are multiple profiles for the same user, AIRIS will automatically merge these profiles based on a unique ID and based on the ID hierarchy.

By default, all AIRIS projects are preset with Appier ID as a profile identifier. An Appier ID is automatically generated for all web and app users tracked by Appier SDK.

AIRIS also allows you to add multiple custom profile IDs, such as users' email addresses, phone numbers, or the customer ID used by your business. You can also hash the email and pass it as a custom profile ID.

Appier ID: The default profile ID for new AIRIS projects.

Custom profile IDs: Additional profile IDs that are added to your project (e.g. email, user_id).

With multiple identifiers, you need to define the ID hierarchy, which determines which identifier takes precedence when mapping new user data to profiles. For example, you might have your customer user ID (user_id) as the highest priority, email as the second priority, and cookie (appier_id) as the third priority.



AIRIS's Profile ID System [3]

https://docs.airis.appier.com/docs/profile-id-system



Every track request, whether it's a user event or property, needs to include at least one user identifier; otherwise, the user data will be dropped since AIRIS doesn't know which profile this newly tracked data belongs to.

When a user event or property is sent to AIRIS, the identifier is submitted to the ID system. If mapped, the ID system returns the mapped profile, and the new user data is now merged with that profile. If there are multiple identifiers on a track record, AIRIS will start with the highest-order identifier and go to the next identifier in the list if not mapped. If none of the identifiers are mapped, a new profile is created.

Here's how AIRIS maps and merges incoming user data to existing profiles using ID hierarchy. See each section for details and examples.

Highest-order identifier takes precedence

Newer user property overwrites older property

New data merges with the most recent profile

Previously overwritten identifiers can be used for profile mapping

👍ID hierarchy in examplesIn the examples below, we will use the following ID hierarchy:Customer user ID >> Email >> Appier ID (Cookie in web users)

When there are multiple identifiers, AIRIS maps profiles using the identifier with the highest priority that exists in both the incoming data and the existing profile.

In example A, the new data will merge with profile 1 because they share the same cookie (Appier ID). Cookie is the highest-priority identifier that exists in both the incoming data and the existing profile.

Example A

In example B, since the user_ids do not match, the new data will not merge with profile 1 and will become a new profile. Even though they share the same email, in this example, email has a lower priority in the ID hierarchy compared to user_id.

Example B

When the new user data is successfully mapped with an existing profile, if the value for a user property is different, AIRIS will take the value of the newer data, which is the newly tracked user property.



AIRIS's Profile ID System [4]

https://docs.airis.appier.com/docs/profile-id-system



In example C, the new data merges with profile 1, because user_id matches. Since the incoming data is more recent compared to the existing profile,jane@email.com will override zoe@example.com. Events will not be overwritten. All events will be retained in the merged profile.

Example C

👍User events will not be overwrittenUnlike user properties, user events will not be overwritten during profile merging. Events will be attached to the merged profile.

If the newly tracked data maps with multiple profiles in the database, it will only merge with the most recent profile in the database. AIRIS will look at the last tracked user data in each profile, and the profile with the most recent track record will be considered the most recent profile.

In example D, the new data is only merged with profile 2. Although both profile 1 and profile 2 share the same email with the new data, AIRIS only merges it with the most recent profile.

Example D

👍TipIf most of your events are tracked with email, email should have higher priority in the ID hierarchy to avoid the scenario in example D.

If an identifier was overwritten during a profile merge, AIRIS can still use this overwritten identifier to map incoming new user data that uses this overwritten identifier.

In the example below, even though the email zoe@email.com was already overwritten by new data 1, AIRIS can still map new data 2 to profile 1 based on this overwritten email. And since new data 2 is more recent, the email zoe@email.com will overwrite jane@email.com.

Example EUpdated 23 days ago



Schema [0]

https://docs.airis.appier.com/docs/configuring-your-schema



Schemas are the skeleton of an AIRIS project. Schemas are declarations of event and user property metadata, defining how tracked data should be read and processed. The schema configuration tells AIRIS:

What type of data it is

How the data should be displayed

How the data can be aggregated

In addition, note that:

Editing a schema doesn't affect the actual tracking of the data, it only changes how AIRIS reads and displays tracked data.

Deleting a schema won't delete any existing data that has already been collected.

🚧ImportantPlease exercise caution when updating the Key value in a schema. Doing so can result in duplicate events in your schemas.

Whenever AIRIS receives a new event or user property without an existing schema, a basic schema is automatically created so that the event or user property will be visible in reports and searches. For a schema to be automatically generated for an event or user property:

The data must only contain letters, numbers, underscores, dashes, and spaces.

You must not have more than 500 existing schemas. For example, if your account has 500 user property schemas and 0 event schemas, AIRIS won't automatically generate a schema for new property data, but will continue to automatically generate schemas for event data.

You can edit the schema to customize the schemas and modify fields that can't be auto-generated, such as the display name or template. If the schema already exists, AIRIS will not modify it when you start sending other properties. This means:

New properties won't be automatically added to the existing schema.

To update the schema, you'll need to either delete it and wait for the event to be tracked again, or manually make the property modifications yourself.

Basic schemas are automatically created from custom events and user properties that are tracked, or from events generated by integrated apps. After the basic schema is generated, you should customize the configuration to suit your needs.

📘NoteTo edit a schema, you must be an Admin user.



Schema [1]

https://docs.airis.appier.com/docs/configuring-your-schema



📘NoteTo edit a schema, you must be an Admin user.

Navigate to the Configure section, go to Manage, and select Event Schema or User Schema.

There are two types of schemas in AIRIS: user schemas and event schemas. Refer to the following section, Schema types for details.

User schema

Event schema

The user schema defines the custom user properties that are being tracked. The name, email, and company name are added to the user schema by default, but AIRIS will also add a schema for custom user data that is tracked.

📘Note: FormattingSchemas are character-sensitive. Accepted characters are: upper and lower case letters, numbers, underscores, dashes, and spaces.

In each user schema, you can set the following:

Schema propertyDescriptionTitleThe property name displayed in the AIRIS console, for example, in reports. This helps users understand the event being tracked, even if they did not participate in the tracking code setup.DescriptionThe description is an important reference for the entire team to understand the meaning of the user property, especially those who did not participate in the tracking code setup. It’s always a good practice to add a description to fields to make it easy for other users to take action on this data.KeyThe key name as tracked on the website. This comes directly from the tracking code. We don't recommend changing this value unless you understand how the events are being sent. If you're unsure, change the Title value instead.Property TypeThe property type can be a standard field, a preset formula, or a custom formula. Refer to Schema Formulas for details.Data TypeThe data type. One of:

• Text: For any string value.

• Number: For numbers/decimals.

• Timestamp: For dates. Note that these should be sent in milliseconds rather than seconds.AggregationSpecify whether the property is a unique value, amount, or group. Refer to Aggregations for details.BucketsRefer to Buckets for details.Sensitive InformationRefer to Hide Sensitive Data for details.



Schema [2]

https://docs.airis.appier.com/docs/configuring-your-schema



The event schema is different from the user schema because it defines the events from the installed integrations or user events tracked on your website or mobile app.

Editing the event schema configuration allows you customize how information is displayed in user profiles. For example, instead of “User did event payment”, you could customize the schema to say “Jim purchased the Yearly Small Business package for $1,999.50“).

In each event schema, you can set the following:

NameDescriptionTitleThe event name displayed in the AIRIS console, for example, in reports. This helps users understand the event being tracked, even if they did not participate in the tracking code setup. Administrators can associate an icon with the event that is being tracked.DescriptionThe description is an important reference for the entire team to understand the meaning of this event, especially those who did not participate in the SDK integration process. It’s always a good practice to add a description to fields to make it easy for other agents to act on this data.KeyThe key name as tracked on the website. This comes directly from the tracking code. We don't recommend changing this value unless you understand how the events are being sent. If you're unsure, change the Title value instead.Event TypeIn user profiles, you can choose whether to show only Active events, only Passive events, or both.

• Active: This event is sent as a result of direct user event.

• Passive: This event is sent as part of a background process or tracked on a user's behalf.

Each property will have the following fields:

NameDescriptionKeyThe name of the property as it’s tracked e.g. amount.TitleThe event property name displayed in the AIRIS console, for example, in reports.DescriptionA description of the event property.Data TypeThe data type of the event property:• Text: For any string value.

• Number: For numbers/decimals.

• Boolean: For two possible values. Accepted input is True or False.



Schema [3]

https://docs.airis.appier.com/docs/configuring-your-schema



• Number: For numbers/decimals.

• Boolean: For two possible values. Accepted input is True or False.

• Short Boolean: For two possible values. Acceptable input is 0 for False, 1 for True.

• Timestamp: For dates, e.g. indicating when an event occurred.

• Duration: Specifies a duration in seconds or milliseconds.Only number and timestamp types support the Format option, which allows you to specify how the value should be displayed, for example: "$1000.00" or "1000" for numbers, "MM/dd/yyyy" or "dd/MM/yyyy" for timestamps.AggregateSpecify whether the property is a unique value, amount, or group. Refer to Aggregations for details.BucketsRefer to Buckets for details.FormulaDefine a custom formula to calculate the value of this event property. Refer to Schema Formulas for details.Sensitive InformationRefer to Hide Sensitive Data for details.Event Unique IDIf enabled, this property is included in the composite ID used for tracking upserts.

NameDescriptionGroupUsed for properties that can be applied to multiple events or users, such as company, product, or credit card type.UniqueUsed for properties that are a unique identifier for a specific event, such as a receipt ID or a transaction ID. For users, a username or email address would be a unique identifier, while company would be a “group” as it can be applied to more than one user.AmountUsed for properties that can be added up or summed. When you designate a property as “amount”, you will be able to sum it in your segmentation filters and analytics reports.For example, in the “payment” event schema, we can set the “amount” property's Aggregate setting to Amount. Now when we are using segmentation filters, we can segment for “all customers who have made payments that totaled more than $200”. Similarly, our report for the “payment” event will include a column that sums the total payment amounts by day, week, or month.



Schema [4]

https://docs.airis.appier.com/docs/configuring-your-schema



Buckets can be used to group number types for use in trend reports. Press the Enter key to add the next bucket. For example, if a user can purchase different quantities of items from your store, you can use buckets to define each quantity range for use in trend reports.

Now when you run the report, the quantities will be bucketed:

The template is how the event is displayed when it occurs in a timeline or event history. It allows you to insert variables in a sentence that are dynamically populated when viewing an individual user's profile. For example, given a template of "Joined segment Name", the Name variable would be replaced with the actual segment name when the event is displayed in a user profile.

👍TipSee Templates to learn more about creating your own templates.

Given the event template shown above, here's how the report entry would look:

Updated 23 days ago



System Event Schema [0]

https://docs.airis.appier.com/docs/system-action-schema



AIRIS automatically comes with the system event schema listed below. You can find them in Configure > Event Schema.

Field KeyField NameDescriptionbutton clickButton ClickThis event is generated when the user clicks on a button.outgoingOutgoing linkThis event is generated when the userclicks on an external link.property updateProperty updateThis event is generated when a property in a user schema is updated to a new value. See Property update for more details.label leaveSegment leaveThis event is generated when a user leaves a segment. See Segment leave and segment join for more details.downloadDownloadThis event is generated when the user downloads a file.label joinSegment JoinThis event is generated when a user joins a segment. See Segment leave and segment join for more details.

This event is generated when a property in a user schema is updated to a new value (e.g. a user's email is updated from “null” to “jane@example.com"). This event is tracked for property updates that occurred through Appier SDK, data loader, CSV loader, and server-side events. If the property is updated manually in AIRIS or by using a formula, a property update event will not be tracked.

Segment Join and Segment Leave events are recorded if you enable the Track events toggle in segment settings.

The Segment Join event is only triggered when the user does an action that qualifies them for the segment. Similarly, the Segment Leave event is only triggered when the user does an action that excludes them from the segment. AIRIS does not record Segment Join or Segment Leave events when a user joins or leaves a segment based on a passive condition without doing an action.

Let's look at some examples.

You have a segment that includes users who did exactly 10 product_purchased events. When the user makes the 10th purchase, a Segment Join event will be recorded. On the 11th purchase, the user no longer meets the segment conditions, so a Segment Leave event will be recorded.



System Event Schema [1]

https://docs.airis.appier.com/docs/system-action-schema



You have a segment that includes users who did at least one product_added_to_cart event within 30 days. When the user joins the segment after adding a product to cart, AIRIS records a Segment Join event.

If the user in the segment does not do any product_added_to_cart event within 30 days, the user will be removed from the segment. In this case, AIRIS will not record a segment leave event because the user leaves the segment due to a passive condition, instead of an action.Updated 23 days ago



System User Schema

https://docs.airis.appier.com/docs/system-visitor-schema



AIRIS automatically comes with the system user schema listed below. You can find them in Configure > User Schema.

Field KeyField NameDescriptionrecent_regionMost Recent RegionThe user's most recent region.actions_90_dActions Last 90 daysThe number of events in the last 90 days.visits_90_dVisits Last 90 DaysThe number of visits in the last 90 days.nameNameThe user's name.companyCompanyThe user's company name.timespent_90_dTime Spent Last 90 DaysThe user's time spent in the last 90 days.unique_ipsUnique IP AddressesThe number of unique IP addresses used by the user.recent_countryMost Recent CountryThe user's most recent country.recent_cityMost Recent CityThe user's most recent city.last_seenLast SeenThe user's last seen time.onlineOnlineThe user's online status.avg_session_screensAvg Screens per SessionThe average number of screens the user scrolls through during a session.avg_session_lengthAvg Session LengthThe average time the user spends on your app in one session.stickinessStickinessThe percentage of days the user used your app that month. A stickiness ratio of 50% means that the user is using your app 15 out of 30 days that month.Updated 23 days ago



User Schema - Profile Metrics

https://docs.airis.appier.com/docs/visitor-schema-profile-metrics



User Schema Profile Metrics

Profile metrics allow you to create custom user schemas based on aggregate operations of custom events. For example, you can calculate the Count or Sum of specific events the user has completed.

To create a custom profile metric, navigate to the Configure section, then go to Manage > User Schema and click + New User Schema.

Name the new property and select a profile metric operation from the Property Type dropdown. Refer to the table below for details on each operation.

Select the event and event properties you'd like to use to calculate this profile metric.

Finally, click Create to save the schema.

OperationUseExampleCountCounts the total number of times the selected event occurs.Count the total number of songs a user played on your site.SumSums the total of a numerical event property.Sum the total revenue from a payment made event.Count UniqueCounts the unique number of times a selected event occurs.Count the unique songs a user played on your site.Last TouchDisplays the last event property of a specific event.Show the last article a user viewed on your site.First TouchDisplays the first event property of a specific event within a specified timeframe.Show the first product a user purchased in the past 2 years.TopDisplays the top occurrence of a specific event.Show what feature the user was using the most.MeanDisplays the average out of a set of numbers.Show the average payment amount a user spends out of their purchase history.MinDisplays the smallest value in a set of numbers.Show the smallest order amount the user spent.MaxDisplays the highest value in a set of numbers.Show the highest amount a user has loaded into their account.Updated 23 days ago



Schema Formulas [0]

https://docs.airis.appier.com/docs/schema-formulas



You can build formulas using existing properties to create new custom schema properties, which can then be used in reports. Formulas are supported for user schemas and event properties in event schemas.

Navigate to the Configure section.

For user schemas: Go to Manage > User Schema and click + New User Schema.

For event schemas: Go to Manage > Event Schema and click + New Event Schema.

Select the property type.

For user schemas: From the Property Type dropdown, select Formula.

For event schemas: Click Add Property to add a new event property. From the new event property's Property Type dropdown, select Formula.

Enter the formula for your new property. For a list of available operations, see the Formula overview.

Let's use a formula to create a new user property called Name that combines two other properties: First Name and Last Name.

📘NoteThe user property Name is built into AIRIS by default. AIRIS's user profiles display the Name property on the top of the profiles, so we recommend sending the full name to this property.

First, go to the User Schema page and click + New User Schema.

Next, in the Property Type dropdown, select Formula.

Create a formula using the CAT (string concatenate) operator and add the following parameters:

first_name

A space

last_name

Click Save.

Finally, add the property into your report (by editing the Columns setting) and click Run to refresh your report.

Let's say we have an event called Played Song with an event property genres. We want to group and unify similar music genres to make it easier to run reports on the data.

Our goal is to convert the "Genres Original" column in the table below to the "Genres Converted" column. To do this, we need to create a new property in the event Played Song using a formula that will group similar music genres.

Genres OriginalGenres ConvertedpopPopPOPPoprocRockrockRockhip hopHip-Hophip-hopHip-HophiphopHip-Hop

Click Add Property under the Played Song event while viewing that event in the event schema.



Schema Formulas [1]

https://docs.airis.appier.com/docs/schema-formulas



Click Add Property under the Played Song event while viewing that event in the event schema.

Select the formula box and start selecting and entering the formula. For this example, we can use IF_THEN_ELSE and select the condition, true result, and false result.

Click Save. You can now use this new property in your reports.

📘NOTEFormulas will only work on properties within the same event. You cannot create a formula that has parameters from another event or event property. In other words, if you have a Played Song event, you cannot make a new formula property under Played Song that uses event properties from another event (e.g. Played Video).

In the reports, if you add the two columns in the Compare by, you'll see that the names have been changed for the genres edited.

Now you can use the new property in the reports.

Updated 23 days ago



Hide Sensitive Data

https://docs.airis.appier.com/docs/hide-sensitive-data



Based on your company's security policies, it may be necessary to hide PII information or other sensitive data from certain users or all users within your organization.

You can either send encoded data to AIRIS, or you can follow the steps below to hide the data in post-processing.

To hide sensitive data, you can navigate to a user schema or event schema, and select a property you want to hide. For example, if we want to hide email addresses from reports and downloads, we can select the email property in the Schema, and toggle on the Sensitive Information switch.

After marking a property as sensitive, we need to configure the Users and Group settings.

Navigate to the Configure tab at the top, then click Users > Groups on the left. Select an existing group or create a new group. Next, you can switch off the Sensitive Information toggle to hide sensitive information from users in that group.

Finally, navigate to the Users page and select a user. You can then add them to the group you created or edited to hide sensitive information.

Now, sensitive data will be hidden in all reports, exports, and API calls for that user.

Updated 23 days ago



System Properties

https://docs.airis.appier.com/docs/built-in-fields



The AIRIS tracking system is designed to be completely customizable, where we track whatever you send us. You can define what is sent after the fact using Schema.

However, the AIRIS tracking system does some things automatically when it comes to your data. When sending a tracking event for instance, even if you don't explicitly include the user's IP address in the custom event properties, the AIRIS system will record the IP from the HTTP request itself. Then, in the case of IP addresses, more data enrichment may occur, such as adding location data (region, etc.), company data (owner of the IP address), and more.

This section explains all of the automatic data recording and enrichment that happens in AIRIS in all three of the data scopes: user data, visit data, and event data.Updated 23 days ago



System Visit Properties [0]

https://docs.airis.appier.com/docs/generated-visit-properties



System-Generated Visit PropertiesThese are the Built-in Fields or Properties of Visits (aka. Sessions). This data is associated with a visit, which is a set of events considered to have occurred in the same session, i.e.: more or less continuously, without a large time gap in between. For more information on visit properties, see the table below:

Field KeyField NamecityCity of IP addressregionRegion/State/Province of IP addresscountryCountry of IP AddresscontinentContinent of IP AddresstimezoneTimezone of the estimated locationoffsetTimezone Offset (ex: +08:00)lngEstimated LongitudelatEstimated LatitudeipIP addressscreenScreen Size/ResolutionlanguageLanguage set in operating system/browser preferences on the device.os Operating System of DevicedomainThe domain of the websitebrowserThe browser if any, used by the client.timeTime that visit began in UNIX Millisecond Time FormathourHour of the day of the visitdayDay of the month of visit.monthMonth of VisitquarterQuarter (3-month period) of VisityearYear of VisitdurationDuration of Visit in MillisecondsreferrertypeVisit Referrer TypereferrerqueryVisit Referrer Query (for search referrals)referrerurlVisit Referrer URL

All of these visit fields are generated by the AIRIS tracking engines when logging a visit. They cannot be overridden when sending real-time events. They can be sent, however, when running bulk visit imports using the Import API.

(city, region, country, continent, timezone, offset, lng, lat)

AIRIS uses an IP geolocation service to estimate the location of the device doing the actions that make up a given visit. Geolocation can be very precise in some cases, and very imprecise in others. Sometimes a visit is coming from a serverside tracking event, and the original client device's IP has not been passed along to AIRIS. AIRIS will then use the IP of whatever device sent us the track request, and that IP will belong to a server in a data center in Dallas, Texas while the user is sitting in a coffee shop in Milwaukee.
